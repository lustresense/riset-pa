# API Specification — Simulasi Interaktif Literasi AI untuk Siswa SMP

> **Version:** 1.0.0  
> **Base URL:** `http://localhost:3000/api`  
> **Architecture:** Browser-based TF.js inference + Node.js/Express REST API + SQLite  
> **Auth Model:** Simple NIS/Name-based login (wajib login — see §0)  
> **Last Updated:** 2025-07-09

---

## §0 — Kenapa WAJIB LOGIN? (Keputusan Bu Hesti)

Tanpa login, setiap sesi browser membuat record anonim baru. Tidak ada cara untuk:

1. **Melacak progress siswa dari waktu ke waktu** — Setiap buka browser = siswa baru. Tidak bisa tahu apakah siswa A sudah menyelesaikan Level 3 atau belum.
2. **Mengukur perubahan perilaku** — Apakah siswa belajar meng-override AI yang salah? Tanpa identitas, kita tidak bisa membandingkan round 1 vs round 10 untuk individu yang sama.
3. **K-Means clustering per-siswa** — Clustering butuh vektor fitur per siswa (override rate, accuracy, confidence gap, dll). Data per-sesi anonim tidak bisa diagregasi ke satu individu.
4. **Dashboard historis** — Guru perlu melihat pola siswa: siapa yang selalu accept, siapa yang sudah kritis, siapa yang perlu intervensi.

**Dengan login**, setiap decision_log terikat ke `user_id`. Session masih dicatat (`session_id`), tapi history menyeberang sesi. Ini memungkinkan analisis longitudinal.

**Mekanisme login:** Sederhana — siswa memasukkan **NIS** (Nomor Induk Siswa) dan **nama**. Tidak perlu password (konteks SMP, riset internal). NIS menjadi primary identifier; nama untuk display. Jika NIS belum terdaftar, akun dibuat otomatis (auto-register).

---

## §1 — Database Schema (SQLite)

### 1.1 Table: `users`

```sql
CREATE TABLE IF NOT EXISTS users (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    nis           TEXT    NOT NULL UNIQUE,       -- Nomor Induk Siswa (login key)
    name          TEXT    NOT NULL,              -- Display name
    class_id      TEXT    DEFAULT NULL,          -- e.g. "7A", "8B" (opsional, untuk filter dashboard)
    created_at    TEXT    NOT NULL DEFAULT (datetime('now')),
    last_login_at TEXT    NOT NULL DEFAULT (datetime('now'))
);

CREATE INDEX idx_users_nis ON users(nis);
CREATE INDEX idx_users_class ON users(class_id);
```

### 1.2 Table: `sessions`

```sql
CREATE TABLE IF NOT EXISTS sessions (
    id            TEXT    PRIMARY KEY,            -- UUID v4, generated client-side
    user_id       INTEGER NOT NULL,
    level         INTEGER NOT NULL,               -- Level 1–6
    started_at    TEXT    NOT NULL DEFAULT (datetime('now')),
    ended_at      TEXT    DEFAULT NULL,           -- NULL if session still active
    total_rounds  INTEGER DEFAULT 0,              -- Updated on session end
    final_score   REAL    DEFAULT 0,              -- Accuracy % across all rounds
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE INDEX idx_sessions_user ON sessions(user_id);
CREATE INDEX idx_sessions_level ON sessions(level);
CREATE INDEX idx_sessions_user_level ON sessions(user_id, level);
```

### 1.3 Table: `decision_logs`

```sql
CREATE TABLE IF NOT EXISTS decision_logs (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id      TEXT    NOT NULL,
    user_id         INTEGER NOT NULL,
    level           INTEGER NOT NULL,
    round_number    INTEGER NOT NULL,
    top1_label      TEXT    NOT NULL,             -- e.g. "kucing", "anjing"
    top1_conf       REAL    NOT NULL,             -- 0.0–1.0
    top2_label      TEXT    DEFAULT NULL,
    top2_conf       REAL    DEFAULT NULL,
    top3_label      TEXT    DEFAULT NULL,
    top3_conf       REAL    DEFAULT NULL,
    decision        TEXT    NOT NULL CHECK(decision IN ('accept','override','correct')),
    override_label  TEXT    DEFAULT NULL,         -- Filled only when decision='override'
    is_correct      INTEGER DEFAULT NULL,         -- 1=correct, 0=incorrect, NULL=pending
    latency_ms      INTEGER NOT NULL,             -- Time from prediction display to decision
    created_at      TEXT    NOT NULL DEFAULT (datetime('now')),

    FOREIGN KEY (session_id) REFERENCES sessions(id) ON DELETE CASCADE,
    FOREIGN KEY (user_id)   REFERENCES users(id) ON DELETE CASCADE
);

CREATE INDEX idx_dlog_session ON decision_logs(session_id);
CREATE INDEX idx_dlog_user    ON decision_logs(user_id);
CREATE INDEX idx_dlog_user_level ON decision_logs(user_id, level);
CREATE INDEX idx_dlog_decision ON decision_logs(decision);
CREATE INDEX idx_dlog_created  ON decision_logs(created_at);
```

### 1.4 Entity-Relationship Summary

```
users (1) ──── (N) sessions
users (1) ──── (N) decision_logs
sessions (1) ── (N) decision_logs
```

A `decision_log` row belongs to both a `session` and a `user` directly. The `user_id` is denormalized into `decision_logs` for fast per-user queries without JOINing through sessions.

---

## §2 — API Endpoints

### 2.1 `POST /api/auth/login`

Authenticate or auto-register a student by NIS + name.

**Request Headers:**
```json
{
  "Content-Type": "application/json"
}
```

**Request Body:**
```json
{
  "nis": "20250101",
  "name": "Aisyah Putri",
  "class_id": "7A"
}
```

| Field       | Type   | Required | Description                                  |
|-------------|--------|----------|----------------------------------------------|
| `nis`       | string | **Yes**  | Nomor Induk Siswa — unique login identifier  |
| `name`      | string | **Yes**  | Display name (ignored if NIS already exists) |
| `class_id`  | string | No       | Class grouping, e.g. "7A", "8B"             |

**Success Response — `200 OK`** (existing user):
```json
{
  "ok": true,
  "user": {
    "id": 1,
    "nis": "20250101",
    "name": "Aisyah Putri",
    "class_id": "7A",
    "last_login_at": "2025-07-09T10:30:00.000Z"
  },
  "token": "eyJhbGciOiJIUzI1NiJ9..."
}
```

**Success Response — `201 Created`** (new user, auto-registered):
```json
{
  "ok": true,
  "user": {
    "id": 42,
    "nis": "20250109",
    "name": "Budi Santoso",
    "class_id": "7B",
    "last_login_at": "2025-07-09T10:30:00.000Z"
  },
  "token": "eyJhbGciOiJIUzI1NiJ9..."
}
```

> **Token:** JWT signed with server secret. Payload: `{ user_id, nis, class_id }`. Used as `Authorization: Bearer <token>` in subsequent requests. Token expires in 8 hours (school day).

**Error Responses:**

| Status | Condition                        | Body                                                      |
|--------|----------------------------------|-----------------------------------------------------------|
| 400    | Missing `nis` or `name`          | `{"ok":false,"error":"nis and name are required"}`        |
| 400    | `nis` too short (< 4 chars)      | `{"ok":false,"error":"nis must be at least 4 characters"}`|
| 409    | NIS exists but name mismatch     | `{"ok":false,"error":"nis already registered with different name","registered_name":"Aisyah Putri"}` |
| 500    | Database error                   | `{"ok":false,"error":"internal server error"}`            |

**Notes on Implementation:**
- **No password** — This is by design. The system runs inside a school lab; NIS is the identifier, not a secret. If Bu Hesti later wants passwords, the schema can be extended with a `password_hash` column.
- **Name mismatch (409):** If a different student types someone else's NIS, we return the registered name so they realize the mistake. We do NOT auto-login with a different name.
- **`class_id` update:** If an existing user logs in with a different `class_id`, the field is updated (students may change classes).
- **Rate limiting:** Max 5 login attempts per IP per minute to prevent enumeration.

---

### 2.2 `POST /api/log`

Core HITL decision logging endpoint. Called by the client every time a student makes a decision (accept/override/correct) on an AI prediction.

**Request Headers:**
```json
{
  "Content-Type": "application/json",
  "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9..."
}
```

**Request Body:**
```json
{
  "session_id": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
  "level": 3,
  "round_number": 7,
  "top1_label": "kucing",
  "top1_conf": 0.82,
  "top2_label": "anjing",
  "top2_conf": 0.11,
  "top3_label": "kelinci",
  "top3_conf": 0.04,
  "decision": "override",
  "override_label": "harimau",
  "latency_ms": 3420
}
```

| Field            | Type    | Required | Description                                           |
|------------------|---------|----------|-------------------------------------------------------|
| `session_id`     | string  | **Yes**  | UUID v4, client-generated per play session            |
| `level`          | integer | **Yes**  | Game level (1–6)                                      |
| `round_number`   | integer | **Yes**  | Round within the level (1-based)                      |
| `top1_label`     | string  | **Yes**  | Highest-confidence prediction label                   |
| `top1_conf`      | float   | **Yes**  | Confidence of top1 (0.0–1.0)                          |
| `top2_label`     | string  | No       | Second prediction label                               |
| `top2_conf`      | float   | No       | Confidence of top2                                   |
| `top3_label`     | string  | No       | Third prediction label                                |
| `top3_conf`      | float   | No       | Confidence of top3                                   |
| `decision`       | string  | **Yes**  | `"accept"` \| `"override"` \| `"correct"`            |
| `override_label` | string  | No       | Required when `decision="override"`. Student's label. |
| `latency_ms`     | integer | **Yes**  | Milliseconds from prediction display to decision      |

**`decision` values explained:**

| Value       | Meaning                                                        |
|-------------|----------------------------------------------------------------|
| `accept`    | Student accepted the AI's top-1 prediction                     |
| `override`  | Student overrode the AI's prediction with their own label      |
| `correct`   | Student confirmed the prediction as correct (post-verification)|

**Success Response — `201 Created`:**
```json
{
  "ok": true,
  "log_id": 1307,
  "message": "decision logged"
}
```

**Error Responses:**

| Status | Condition                                   | Body                                                      |
|--------|---------------------------------------------|-----------------------------------------------------------|
| 401    | Missing or invalid Authorization header     | `{"ok":false,"error":"unauthorized"}`                     |
| 400    | Missing required fields                     | `{"ok":false,"error":"session_id, level, round_number, top1_label, top1_conf, decision, latency_ms are required"}` |
| 400    | Invalid `decision` value                    | `{"ok":false,"error":"decision must be accept, override, or correct"}` |
| 400    | `override` without `override_label`         | `{"ok":false,"error":"override_label is required when decision is override"}` |
| 400    | Confidence out of range                     | `{"ok":false,"error":"confidence values must be between 0.0 and 1.0"}` |
| 400    | Level out of range                          | `{"ok":false,"error":"level must be between 1 and 6"}`    |
| 404    | `session_id` not found for this user        | `{"ok":false,"error":"session not found for this user"}`  |
| 500    | Database error                              | `{"ok":false,"error":"internal server error"}`            |

**Notes on Implementation:**
- **Auto-create session:** If `session_id` doesn't exist in `sessions` table, auto-insert a new session row with `user_id` from JWT, `level` from payload, and `started_at = now()`. This avoids requiring a separate "start session" endpoint.
- **Denormalized `user_id`:** Extracted from JWT, not from request body. Prevents impersonation.
- **`is_correct` is NULL at log time:** The client doesn't know ground truth at decision time. It's filled later via a batch update or during the level-completion phase when ground truth is revealed.
- **Batch logging:** Client may batch multiple decisions and send them together in the future. For now, one decision per request keeps it simple.
- **Idempotency:** Not required — each decision is unique by `(session_id, round_number)`. If a duplicate arrives, it's INSERT-ed again (log is append-only). De-duplication can be added with a UNIQUE constraint if needed.

---

### 2.3 `GET /api/sessions`

Retrieve session history for a user. Used by the student's profile/history view and by the dashboard.

**Request Headers:**
```json
{
  "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9..."
}
```

**Query Parameters:**

| Param    | Type    | Required | Description                              |
|----------|---------|----------|------------------------------------------|
| `user_id`| integer | No*      | User ID to query. Defaults to JWT user.  |
| `level`  | integer | No       | Filter by level (1–6)                    |
| `limit`  | integer | No       | Max sessions to return (default: 50)     |
| `offset` | integer | No       | Pagination offset (default: 0)           |

> *\*Teachers/admins can query any `user_id`. Students can only query their own (enforced by JWT).*

**Example Request:**
```
GET /api/sessions?level=3&limit=10&offset=0
```

**Success Response — `200 OK`:**
```json
{
  "ok": true,
  "count": 3,
  "total": 12,
  "offset": 0,
  "limit": 10,
  "sessions": [
    {
      "id": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
      "user_id": 1,
      "level": 3,
      "started_at": "2025-07-09T10:35:00.000Z",
      "ended_at": "2025-07-09T11:02:00.000Z",
      "total_rounds": 15,
      "final_score": 73.3,
      "decisions": [
        {
          "round_number": 1,
          "top1_label": "kucing",
          "top1_conf": 0.91,
          "decision": "accept",
          "override_label": null,
          "latency_ms": 1200,
          "is_correct": 1
        },
        {
          "round_number": 2,
          "top1_label": "anjing",
          "top1_conf": 0.65,
          "decision": "override",
          "override_label": "serigala",
          "latency_ms": 5200,
          "is_correct": 1
        }
      ]
    },
    {
      "id": "a1b2c3d4-5678-9012-abcd-ef0123456789",
      "user_id": 1,
      "level": 3,
      "started_at": "2025-07-08T09:10:00.000Z",
      "ended_at": "2025-07-08T09:40:00.000Z",
      "total_rounds": 15,
      "final_score": 60.0,
      "decisions": []
    }
  ]
}
```

> **Note:** `decisions` array is included by default but can be excluded with `?include_decisions=false` for lightweight listing. When `decisions` is empty `[]`, it means the detailed log was not requested or the session data is summary-only.

**Error Responses:**

| Status | Condition                               | Body                                                |
|--------|-----------------------------------------|-----------------------------------------------------|
| 401    | Missing or invalid token                | `{"ok":false,"error":"unauthorized"}`               |
| 403    | Student querying another user_id        | `{"ok":false,"error":"forbidden: can only view your own sessions"}` |
| 400    | Invalid level filter                    | `{"ok":false,"error":"level must be between 1 and 6"}` |
| 500    | Database error                          | `{"ok":false,"error":"internal server error"}`      |

**Notes on Implementation:**
- **Pagination:** `total` reflects the count after filters, before `limit`/`offset`. Client uses `total` + `limit` to know if more pages exist.
- **Decision detail:** Including `decisions` inline avoids N+1 queries on the client. If performance becomes an issue with large datasets, use `?include_decisions=false` and fetch decisions per session via a dedicated endpoint.
- **Sorting:** Sessions returned in reverse chronological order (`started_at DESC`).

---

### 2.4 `POST /api/analyze`

Trigger K-Means clustering analysis on collected decision data. Returns cluster assignments, centroids, and suggested labels.

**Request Headers:**
```json
{
  "Content-Type": "application/json",
  "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9..."
}
```

> **Authorization:** Only teacher/admin accounts can trigger analysis. Students receive 403.

**Request Body:**
```json
{
  "n_clusters": 3,
  "features": [
    "override_rate",
    "accept_rate",
    "accuracy",
    "avg_confidence_gap",
    "avg_latency_ms",
    "override_accuracy"
  ],
  "level": null,
  "min_decisions": 5
}
```

| Field            | Type     | Required | Description                                          |
|------------------|----------|----------|------------------------------------------------------|
| `n_clusters`     | integer  | No       | Number of K-Means clusters (default: 3)              |
| `features`       | string[] | No       | Feature vector components (default: all 6 listed)    |
| `level`          | integer  | No       | Analyze only data from this level (null = all levels)|
| `min_decisions`  | integer  | No       | Minimum decisions per user to include (default: 5)    |

**Available Features:**

| Feature               | Calculation                                                   |
|-----------------------|---------------------------------------------------------------|
| `override_rate`       | COUNT(override) / COUNT(all decisions)                        |
| `accept_rate`         | COUNT(accept) / COUNT(all decisions)                          |
| `accuracy`            | SUM(is_correct=1) / COUNT(all decisions where is_correct ≠ NULL) |
| `avg_confidence_gap`  | AVG(top1_conf - top2_conf) — how "certain" the AI appears    |
| `avg_latency_ms`      | AVG(latency_ms) — how long student takes to decide            |
| `override_accuracy`   | SUM(override AND is_correct=1) / COUNT(override) — are overrides correct? |

**Success Response — `200 OK`:**
```json
{
  "ok": true,
  "meta": {
    "n_clusters": 3,
    "features_used": ["override_rate", "accept_rate", "accuracy", "avg_confidence_gap", "avg_latency_ms", "override_accuracy"],
    "level_filter": null,
    "min_decisions": 5,
    "total_users_analyzed": 28,
    "total_users_excluded": 3,
    "iterations": 12,
    "inertia": 142.7
  },
  "clusters": [
    {
      "cluster_id": 0,
      "label": "AI Dependent",
      "description": "Siswa cenderung menerima prediksi AI tanpa mempertimbangkan. Override rate rendah, akurasi menurun saat AI salah.",
      "size": 11,
      "centroid": {
        "override_rate": 0.08,
        "accept_rate": 0.88,
        "accuracy": 0.62,
        "avg_confidence_gap": 0.41,
        "avg_latency_ms": 1800,
        "override_accuracy": 0.33
      }
    },
    {
      "cluster_id": 1,
      "label": "Developing Critical Thinker",
      "description": "Siswa mulai meng-override saat AI kurang yakin. Akurasi meningkat, latency lebih tinggi (berpikir lebih lama).",
      "size": 10,
      "centroid": {
        "override_rate": 0.35,
        "accept_rate": 0.55,
        "accuracy": 0.78,
        "avg_confidence_gap": 0.28,
        "avg_latency_ms": 3400,
        "override_accuracy": 0.71
      }
    },
    {
      "cluster_id": 2,
      "label": "Critical Thinker",
      "description": "Siswa secara aktif meng-override prediksi AI yang salah. Override accuracy tinggi, menunjukkan pemahaman baik.",
      "size": 7,
      "centroid": {
        "override_rate": 0.52,
        "accept_rate": 0.35,
        "accuracy": 0.89,
        "avg_confidence_gap": 0.19,
        "avg_latency_ms": 4100,
        "override_accuracy": 0.83
      }
    }
  ],
  "assignments": [
    { "user_id": 1,  "nis": "20250101", "name": "Aisyah Putri",  "cluster_id": 2 },
    { "user_id": 2,  "nis": "20250102", "name": "Budi Santoso",  "cluster_id": 0 },
    { "user_id": 3,  "nis": "20250103", "name": "Cahya Dewi",    "cluster_id": 1 }
  ]
}
```

**Error Responses:**

| Status | Condition                                   | Body                                                      |
|--------|---------------------------------------------|-----------------------------------------------------------|
| 401    | Missing or invalid token                    | `{"ok":false,"error":"unauthorized"}`                     |
| 403    | Non-teacher account                         | `{"ok":false,"error":"forbidden: analysis requires teacher role"}` |
| 400    | `n_clusters` < 2 or > 10                    | `{"ok":false,"error":"n_clusters must be between 2 and 10"}` |
| 400    | Unknown feature name                        | `{"ok":false,"error":"unknown feature: foo_bar"}`         |
| 422    | Insufficient data (< 2 users qualify)       | `{"ok":false,"error":"insufficient data: only 1 user meets min_decisions threshold"}` |
| 500    | Analysis computation error                  | `{"ok":false,"error":"clustering failed: [reason]"}`      |

**Notes on Implementation:**
- **K-Means library:** Use [`ml-kmeans`](https://github.com/mljs/kmeans) (pure JS) or call Python's `sklearn.cluster.KMeans` via a child process for larger datasets.
- **Feature scaling:** All features MUST be standardized (z-score) before clustering. Raw values have different scales (latency in ms vs rates 0–1).
- **Cluster labels:** Auto-generated based on centroid characteristics. The labeling logic:
  - High `accept_rate` + low `accuracy` → "AI Dependent"
  - Moderate `override_rate` + moderate `accuracy` → "Developing Critical Thinker"
  - High `override_rate` + high `override_accuracy` → "Critical Thinker"
- **Caching:** Results are NOT cached. Each request runs a fresh analysis. If the dataset grows large, add a `?cached=true` option that returns the last-computed result with a timestamp.
- **Performance:** With ≤100 students and ≤50 decisions each, the computation finishes in <200ms. No async queue needed yet.
- **Why this is POST, not GET:** The request body contains analysis parameters that are too complex for query strings, and triggering computation is a state-changing action (even if the DB isn't written to).

---

### 2.5 `GET /api/dashboard`

Aggregated statistics for the teacher/admin dashboard. No heavy computation — just SQL aggregation.

**Request Headers:**
```json
{
  "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9..."
}
```

> **Authorization:** Teacher/admin only. Students receive 403.

**Query Parameters:**

| Param       | Type   | Required | Description                                  |
|-------------|--------|----------|----------------------------------------------|
| `class_id`  | string | No       | Filter by class, e.g. "7A" (default: all)    |
| `date_from` | string | No       | Start date ISO 8601 (default: 7 days ago)    |
| `date_to`   | string | No       | End date ISO 8601 (default: today)           |

**Example Request:**
```
GET /api/dashboard?class_id=7A&date_from=2025-07-01&date_to=2025-07-09
```

**Success Response — `200 OK`:**
```json
{
  "ok": true,
  "filters": {
    "class_id": "7A",
    "date_from": "2025-07-01",
    "date_to": "2025-07-09"
  },
  "summary": {
    "total_students": 28,
    "total_sessions": 87,
    "total_decisions": 1305,
    "avg_accuracy": 0.71,
    "avg_override_rate": 0.27,
    "avg_latency_ms": 2950
  },
  "level_completion": {
    "1": { "attempted": 28, "completed": 25, "avg_score": 82.1 },
    "2": { "attempted": 24, "completed": 20, "avg_score": 75.4 },
    "3": { "attempted": 18, "completed": 12, "avg_score": 68.9 },
    "4": { "attempted": 10, "completed": 6,  "avg_score": 61.2 },
    "5": { "attempted": 4,  "completed": 2,  "avg_score": 55.0 },
    "6": { "attempted": 1,  "completed": 0,  "avg_score": 0 }
  },
  "cluster_distribution": {
    "AI Dependent": 11,
    "Developing Critical Thinker": 10,
    "Critical Thinker": 7
  },
  "daily_activity": [
    { "date": "2025-07-01", "sessions": 8,  "decisions": 120, "avg_accuracy": 0.65 },
    { "date": "2025-07-02", "sessions": 12, "decisions": 180, "avg_accuracy": 0.68 },
    { "date": "2025-07-03", "sessions": 10, "decisions": 150, "avg_accuracy": 0.70 },
    { "date": "2025-07-04", "sessions": 15, "decisions": 225, "avg_accuracy": 0.72 },
    { "date": "2025-07-07", "sessions": 18, "decisions": 270, "avg_accuracy": 0.74 },
    { "date": "2025-07-08", "sessions": 14, "decisions": 210, "avg_accuracy": 0.73 },
    { "date": "2025-07-09", "sessions": 10, "decisions": 150, "avg_accuracy": 0.75 }
  ],
  "top_overriders": [
    { "user_id": 1,  "name": "Aisyah Putri",  "override_rate": 0.58, "override_accuracy": 0.86 },
    { "user_id": 7,  "name": "Dewi Lestari",  "override_rate": 0.52, "override_accuracy": 0.80 },
    { "user_id": 15, "name": "Fajar Rahman",  "override_rate": 0.49, "override_accuracy": 0.77 }
  ],
  "needs_attention": [
    { "user_id": 22, "name": "Gilang Pratama", "accept_rate": 0.95, "accuracy": 0.48, "reason": "always accepts, even when AI is wrong" },
    { "user_id": 19, "name": "Hana Safitri",   "accept_rate": 0.92, "accuracy": 0.52, "reason": "never overrides, low accuracy" }
  ]
}
```

**Error Responses:**

| Status | Condition                               | Body                                                |
|--------|-----------------------------------------|-----------------------------------------------------|
| 401    | Missing or invalid token                | `{"ok":false,"error":"unauthorized"}`               |
| 403    | Non-teacher account                     | `{"ok":false,"error":"forbidden: dashboard requires teacher role"}` |
| 400    | Invalid date format                     | `{"ok":false,"error":"date_from must be ISO 8601 (YYYY-MM-DD)"}` |
| 400    | `date_from` after `date_to`             | `{"ok":false,"error":"date_from must be before date_to"}` |
| 500    | Database error                          | `{"ok":false,"error":"internal server error"}`      |

**Notes on Implementation:**
- **All SQL aggregation:** No K-Means here. The `cluster_distribution` is a snapshot from the last `/api/analyze` result (cached server-side in memory or a `analysis_cache` table). If no analysis has been run, this field returns `null`.
- **`top_overriders`:** Students with highest override rate AND highest override accuracy. These are the "critical thinkers" — good examples for the class.
- **`needs_attention`:** Students with `accept_rate > 0.85` AND `accuracy < 0.60`. These students trust the AI blindly and get wrong answers. Bu Hesti can give them extra guidance.
- **`daily_activity`:** Aggregated per calendar day. Useful for spotting trends (e.g., accuracy improving over the week).
- **Performance:** With ≤100 students, all queries finish in <50ms. No need for materialized views yet.

---

## §3 — Common Patterns

### 3.1 Authentication Flow

```
┌──────────┐          ┌──────────┐          ┌──────────┐
│  Client  │          │  Server  │          │  SQLite  │
└────┬─────┘          └────┬─────┘          └────┬─────┘
     │  POST /api/auth/login   │                   │
     │  { nis, name }         │                   │
     │ ──────────────────────>│                   │
     │                        │  SELECT from users│
     │                        │  WHERE nis = ?    │
     │                        │ ─────────────────>│
     │                        │                   │
     │                        │  row / empty      │
     │                        │ <─────────────────│
     │                        │                   │
     │                        │  (if not found)   │
     │                        │  INSERT into users│
     │                        │ ─────────────────>│
     │                        │                   │
     │  200/201 + JWT token   │                   │
     │ <──────────────────────│                   │
     │                        │                   │
     │  Subsequent requests:  │                   │
     │  Authorization: Bearer │                   │
     │ ──────────────────────>│                   │
```

### 3.2 Logging Flow

```
Student makes decision on sketch
        │
        ▼
Client builds payload (session_id, predictions, decision, latency)
        │
        ▼
POST /api/log  ──────>  Server validates JWT
                              │
                              ▼
                        Extract user_id from JWT
                        (NOT from body — prevents impersonation)
                              │
                              ▼
                        Auto-create session if needed
                              │
                              ▼
                        INSERT into decision_logs
                              │
                              ▼
                        201 { ok: true, log_id }
```

### 3.3 Error Response Format

All errors follow a consistent format:

```json
{
  "ok": false,
  "error": "human-readable message",
  "details": {}          // optional, for validation errors
}
```

### 3.4 Rate Limiting

| Endpoint           | Limit                          |
|--------------------|--------------------------------|
| `POST /api/auth/login` | 5 requests / minute / IP  |
| `POST /api/log`        | 60 requests / minute / user |
| `GET /api/sessions`    | 30 requests / minute / user |
| `POST /api/analyze`    | 5 requests / minute / user  |
| `GET /api/dashboard`   | 30 requests / minute / user |

### 3.5 CORS Configuration

```javascript
// server.js
app.use(cors({
  origin: ['http://localhost:5500', 'http://127.0.0.1:5500'],
  methods: ['GET', 'POST'],
  allowedHeaders: ['Content-Type', 'Authorization'],
  credentials: true
}));
```

The TF.js client runs on a different port (e.g., Live Server on 5500) than the Express API (port 3000), so CORS is required.

---

## §4 — Future Extensions (Out of Scope for v1.0)

| Feature                          | Why Not Now                            | Endpoint Sketch              |
|----------------------------------|----------------------------------------|------------------------------|
| Password authentication          | Not needed for internal school lab     | `POST /api/auth/register`    |
| Session start/end endpoints      | Auto-creation in `/api/log` is simpler | `POST /api/sessions/start`   |
| Per-decision detail endpoint     | Included inline in `GET /api/sessions` | `GET /api/log/:log_id`       |
| Export CSV                       | Bu Hesti can use dashboard for now     | `GET /api/export?format=csv` |
| Real-time WebSocket notifications| Dashboard is pull-based for v1         | `WS /ws/dashboard`           |
| Multi-teacher admin roles        | Single teacher (Bu Hesti) for research | Add `role` to `users` table  |
| Analysis result persistence      | Fresh analysis each time is fine       | `analysis_results` table     |

---

## §5 — Implementation Checklist

- [ ] Create SQLite schema (users, sessions, decision_logs)
- [ ] Implement JWT token generation/validation middleware
- [ ] Implement `POST /api/auth/login` with auto-register
- [ ] Implement `POST /api/log` with session auto-creation
- [ ] Implement `GET /api/sessions` with pagination
- [ ] Implement `POST /api/analyze` with ml-kmeans
- [ ] Implement `GET /api/dashboard` with SQL aggregation
- [ ] Add rate limiting middleware
- [ ] Add CORS configuration
- [ ] Add request validation middleware (Joi/Zod)
- [ ] Write integration tests for each endpoint
- [ ] Seed script for demo data (28 students × ~50 decisions each)
