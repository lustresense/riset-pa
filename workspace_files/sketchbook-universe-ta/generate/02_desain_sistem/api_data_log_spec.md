# API & Data Log Specification — Sketchbook Universe

> **Project:** Sketchbook Universe — Simulasi Interaktif Literasi AI untuk Siswa SMP Kelas 7-9  
> **Version:** 1.0.0  
> **Base URL:** `http://localhost:3000/api/v1`  
> **Architecture:** Browser-based TF.js inference + Node.js/Express REST API + SQLite  
> **Auth Model:** NIS + Name (wajib login — see §0)  
> **Last Updated:** 2025-07-09

---

## §0 — Kenapa WAJIB LOGIN? (Keputusan Bu Hesti)

Tanpa login, setiap sesi browser membuat record anonim baru. Tidak ada cara untuk:

1. **Melacak progress siswa dari waktu ke waktu** — Setiap buka browser = siswa baru. Tidak bisa tahu apakah siswa A sudah menyelesaikan Level 3 atau belum.
2. **Mengukur perubahan perilaku** — Apakah siswa belajar meng-override AI yang salah? Tanpa identitas, kita tidak bisa membandingkan round 1 vs round 10 untuk individu yang sama.
3. **K-Means clustering per-siswa** — Clustering butuh vektor fitur per siswa (override rate, accuracy, confidence gap, dll). Data per-sesi anonim tidak bisa diagregasi ke satu individu.
4. **Dashboard historis** — Guru perlu melihat pola siswa: siapa yang selalu accept, siapa yang sudah kritis, siapa yang perlu intervensi.

**Dengan login**, setiap `action_log` terikat ke `user_id`. Session masih dicatat (`session_id`), tapi history menyeberang sesi. Ini memungkinkan analisis longitudinal.

**Mekanisme login:** Sederhana — siswa memasukkan **NIS** (Nomor Induk Siswa) dan **nama**. Tidak perlu password (konteks SMP, riset internal). NIS menjadi primary identifier; nama untuk display. Jika NIS belum terdaftar, akun dibuat otomatis (auto-register).

> *"Login bukan hambatan — login adalah fondasi data. Tanpa identitas, simulasi ini hanya permainan. Dengan identitas, ini menjadi penelitian."* — Bu Hesti

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

### 1.3 Table: `action_logs`

```sql
CREATE TABLE IF NOT EXISTS action_logs (
    log_id           INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id       TEXT    NOT NULL,
    timestamp        TEXT    NOT NULL DEFAULT (datetime('now')),
    action_type      TEXT    NOT NULL CHECK(action_type IN ('gesture','click','system')),
    raw_data         TEXT    DEFAULT NULL,         -- JSON blob: full prediction details, coordinates, etc.
    context_level    INTEGER NOT NULL,             -- Level 1–6 when this action occurred
    cnn_prediction   REAL    DEFAULT NULL,         -- Top-1 confidence from CNN (0.0–1.0)
    decision         TEXT    NOT NULL CHECK(decision IN ('accept','override','correct')),
    override_label   TEXT    DEFAULT NULL,         -- Filled only when decision='override'
    is_correct       INTEGER DEFAULT NULL,         -- 1=correct, 0=incorrect, NULL=pending grading
    latency_ms       INTEGER NOT NULL,             -- Time from prediction display to decision

    FOREIGN KEY (session_id) REFERENCES sessions(id) ON DELETE CASCADE
);

CREATE INDEX idx_alog_session ON action_logs(session_id);
CREATE INDEX idx_alog_level   ON action_logs(context_level);
CREATE INDEX idx_alog_decision ON action_logs(decision);
CREATE INDEX idx_alog_action  ON action_logs(action_type);
CREATE INDEX idx_alog_ts      ON action_logs(timestamp);
```

**`action_type` values explained:**

| Value      | Meaning                                                              |
|------------|----------------------------------------------------------------------|
| `gesture`  | Canvas sketch input — drawing stroke coordinates stored in `raw_data` |
| `click`    | UI interaction — accept/override/correct button tap                  |
| `system`   | Auto-generated event — session start, level transition, timeout      |

**`raw_data` JSON structure examples:**

```json
// gesture event
{
  "stroke_points": [[120, 45], [122, 47], [125, 50]],
  "stroke_count": 3,
  "canvas_size": [480, 360]
}

// click event (decision)
{
  "top1_label": "kucing",
  "top1_conf": 0.82,
  "top2_label": "anjing",
  "top2_conf": 0.11,
  "top3_label": "kelinci",
  "top3_conf": 0.04,
  "round_number": 7
}

// system event
{
  "event": "level_complete",
  "score": 73.3
}
```

### 1.4 View: `analytics_summary`

Auto-generated aggregation view with **kesimpulan kalimat** (conclusion sentence) — as specifically requested by Bu Hesti. Every data log must have an interpretable conclusion alongside the metrics.

```sql
CREATE VIEW IF NOT EXISTS analytics_summary AS
SELECT
    s.id                          AS session_id,
    s.user_id,
    u.nis,
    u.name,
    u.class_id,
    s.level,
    s.started_at,
    s.ended_at,
    s.total_rounds,
    s.final_score,

    -- Decision breakdown
    COUNT(al.log_id)                                                          AS total_actions,
    SUM(CASE WHEN al.decision = 'accept'   THEN 1 ELSE 0 END)               AS accept_count,
    SUM(CASE WHEN al.decision = 'override' THEN 1 ELSE 0 END)               AS override_count,
    SUM(CASE WHEN al.decision = 'correct'  THEN 1 ELSE 0 END)               AS correct_count,

    -- Rates
    ROUND(
        1.0 * SUM(CASE WHEN al.decision = 'override' THEN 1 ELSE 0 END)
        / NULLIF(COUNT(al.log_id), 0), 3
    )                                                                          AS override_rate,
    ROUND(
        1.0 * SUM(CASE WHEN al.decision = 'accept' THEN 1 ELSE 0 END)
        / NULLIF(COUNT(al.log_id), 0), 3
    )                                                                          AS accept_rate,

    -- Accuracy
    ROUND(
        1.0 * SUM(CASE WHEN al.is_correct = 1 THEN 1 ELSE 0 END)
        / NULLIF(SUM(CASE WHEN al.is_correct IS NOT NULL THEN 1 ELSE 0 END), 0), 3
    )                                                                          AS accuracy,
    ROUND(
        1.0 * SUM(CASE WHEN al.decision = 'override' AND al.is_correct = 1 THEN 1 ELSE 0 END)
        / NULLIF(SUM(CASE WHEN al.decision = 'override' THEN 1 ELSE 0 END), 0), 3
    )                                                                          AS override_accuracy,

    -- Confidence & latency
    ROUND(AVG(al.cnn_prediction), 3)                                          AS avg_cnn_confidence,
    ROUND(AVG(CAST(al.latency_ms AS REAL)), 0)                                AS avg_latency_ms,

    -- =====================================================
    -- KESIMPULAN KALIMAT (auto-generated via CASE WHEN)
    -- Bu Hesti: "data log harus punya kesimpulan kalimat"
    -- =====================================================
    CASE
        -- Critical Thinker: high override + high accuracy
        WHEN 1.0 * SUM(CASE WHEN al.decision = 'override' THEN 1 ELSE 0 END)
             / NULLIF(COUNT(al.log_id), 0) >= 0.40
             AND 1.0 * SUM(CASE WHEN al.decision = 'override' AND al.is_correct = 1 THEN 1 ELSE 0 END)
             / NULLIF(SUM(CASE WHEN al.decision = 'override' THEN 1 ELSE 0 END), 0) >= 0.70
        THEN 'Siswa menunjukkan pemikiran kritis: aktif meng-override prediksi AI yang salah dengan akurasi tinggi.'

        -- Developing Thinker: moderate override, improving
        WHEN 1.0 * SUM(CASE WHEN al.decision = 'override' THEN 1 ELSE 0 END)
             / NULLIF(COUNT(al.log_id), 0) >= 0.20
             AND 1.0 * SUM(CASE WHEN al.decision = 'override' AND al.is_correct = 1 THEN 1 ELSE 0 END)
             / NULLIF(SUM(CASE WHEN al.decision = 'override' THEN 1 ELSE 0 END), 0) >= 0.50
        THEN 'Siswa mulai mengembangkan pemikiran kritis: mulai meng-override saat AI kurang yakin, akurasi override masih berkembang.'

        -- AI Dependent: low override, accuracy suffers
        WHEN 1.0 * SUM(CASE WHEN al.decision = 'accept' THEN 1 ELSE 0 END)
             / NULLIF(COUNT(al.log_id), 0) >= 0.80
             AND 1.0 * SUM(CASE WHEN al.is_correct = 1 THEN 1 ELSE 0 END)
             / NULLIF(SUM(CASE WHEN al.is_correct IS NOT NULL THEN 1 ELSE 0 END), 0) < 0.65
        THEN 'Siswa bergantung pada AI: hampir selalu menerima prediksi, akurasi rendah saat AI salah. Perlu bimbingan.'

        -- Fast Acceptor: high accept but still decent accuracy (easy levels)
        WHEN 1.0 * SUM(CASE WHEN al.decision = 'accept' THEN 1 ELSE 0 END)
             / NULLIF(COUNT(al.log_id), 0) >= 0.80
        THEN 'Siswa cenderung menerima prediksi AI tanpa evaluasi mendalam, namun akurasi masih cukup baik.'

        -- Default: mixed behavior
        ELSE 'Siswa menunjukkan perilaku campuran: kadang menerima, kadang meng-override AI. Perlu lebih banyak data untuk kesimpulan yang lebih spesifik.'
    END                                                                          AS conclusion

FROM sessions s
JOIN users u ON s.user_id = u.id
LEFT JOIN action_logs al ON al.session_id = s.id
GROUP BY s.id;
```

### 1.5 Entity-Relationship Summary

```
users (1) ──── (N) sessions
users (1) ──── (N) action_logs  (via sessions)
sessions (1) ── (N) action_logs

analytics_summary (VIEW) ── reads from users + sessions + action_logs
```

An `action_log` row belongs to a `session`. The `user_id` is accessible via the `sessions` join (not denormalized into `action_logs`, unlike the earlier design). The `analytics_summary` VIEW aggregates all three tables and auto-generates the `conclusion` field.

---

## §2 — API Endpoints

### 2.1 `POST /api/v1/auth/login`

Authenticate or auto-register a student by NIS + name. Returns JWT for subsequent requests.

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
  "token": "eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJuaXMiOiIyMDI1MDEwMSIsImNsYXNzX2lkIjoiN0EifQ.abc123"
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
    "last_login_at": "2025-07-09T10:31:00.000Z"
  },
  "token": "eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo0MiwibmlzIjoiMjAyNTAxMDkiLCJjbGFzc19pZCI6IjdCIn0.def456"
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

**Implementation Notes:**
- **No password** — This is by design. The system runs inside a school lab; NIS is the identifier, not a secret.
- **Name mismatch (409):** If a different student types someone else's NIS, we return the registered name so they realize the mistake. We do NOT auto-login with a different name.
- **`class_id` update:** If an existing user logs in with a different `class_id`, the field is updated (students may change classes).
- **Rate limiting:** Max 5 login attempts per IP per minute to prevent enumeration.

---

### 2.2 `POST /api/v1/logs`

Core HITL decision logging endpoint. Called by the client every time a student makes a decision (accept/override/correct) on an AI prediction, or when a gesture/system event occurs.

**Request Headers:**
```json
{
  "Content-Type": "application/json",
  "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9..."
}
```

**Request Body — Decision log (click action):**
```json
{
  "session_id": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
  "action_type": "click",
  "raw_data": {
    "top1_label": "kucing",
    "top1_conf": 0.82,
    "top2_label": "anjing",
    "top2_conf": 0.11,
    "top3_label": "kelinci",
    "top3_conf": 0.04,
    "round_number": 7
  },
  "context_level": 3,
  "cnn_prediction": 0.82,
  "decision": "override",
  "override_label": "harimau",
  "latency_ms": 3420
}
```

**Request Body — Gesture log:**
```json
{
  "session_id": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
  "action_type": "gesture",
  "raw_data": {
    "stroke_points": [[120, 45], [122, 47], [125, 50]],
    "stroke_count": 3,
    "canvas_size": [480, 360]
  },
  "context_level": 3,
  "cnn_prediction": null,
  "decision": "accept",
  "override_label": null,
  "latency_ms": 0
}
```

**Request Body — System event:**
```json
{
  "session_id": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
  "action_type": "system",
  "raw_data": {
    "event": "level_complete",
    "score": 73.3
  },
  "context_level": 3,
  "cnn_prediction": null,
  "decision": "correct",
  "override_label": null,
  "latency_ms": 0
}
```

| Field             | Type    | Required | Description                                                |
|-------------------|---------|----------|------------------------------------------------------------|
| `session_id`      | string  | **Yes**  | UUID v4, client-generated per play session                 |
| `action_type`     | string  | **Yes**  | `"gesture"` \| `"click"` \| `"system"`                    |
| `raw_data`        | object  | No       | JSON blob with full details (predictions, strokes, events) |
| `context_level`   | integer | **Yes**  | Level 1–6 when this action occurred                        |
| `cnn_prediction`  | float   | No       | Top-1 confidence from CNN (0.0–1.0). Null for gestures.    |
| `decision`        | string  | **Yes**  | `"accept"` \| `"override"` \| `"correct"`                 |
| `override_label`  | string  | No       | Required when `decision="override"`. Student's label.      |
| `latency_ms`      | integer | **Yes**  | Milliseconds from prediction display to decision            |

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
  "message": "action logged"
}
```

**Error Responses:**

| Status | Condition                                   | Body                                                      |
|--------|---------------------------------------------|-----------------------------------------------------------|
| 401    | Missing or invalid Authorization header     | `{"ok":false,"error":"unauthorized"}`                     |
| 400    | Missing required fields                     | `{"ok":false,"error":"session_id, action_type, context_level, decision, latency_ms are required"}` |
| 400    | Invalid `action_type` value                 | `{"ok":false,"error":"action_type must be gesture, click, or system"}` |
| 400    | Invalid `decision` value                    | `{"ok":false,"error":"decision must be accept, override, or correct"}` |
| 400    | `override` without `override_label`         | `{"ok":false,"error":"override_label is required when decision is override"}` |
| 400    | `cnn_prediction` out of range               | `{"ok":false,"error":"cnn_prediction must be between 0.0 and 1.0"}` |
| 400    | `context_level` out of range                | `{"ok":false,"error":"context_level must be between 1 and 6"}` |
| 404    | `session_id` not found for this user        | `{"ok":false,"error":"session not found for this user"}`  |
| 500    | Database error                              | `{"ok":false,"error":"internal server error"}`            |

**Implementation Notes:**
- **Auto-create session:** If `session_id` doesn't exist in `sessions` table, auto-insert a new session row with `user_id` from JWT, `level` from `context_level`, and `started_at = now()`. This avoids requiring a separate "start session" endpoint.
- **`user_id` from JWT:** The user_id is extracted from the JWT token, never from the request body. This prevents impersonation.
- **`raw_data` stored as JSON string:** SQLite doesn't have a native JSON type, so `raw_data` is serialized with `JSON.stringify()` on insert and parsed with `JSON.parse()` on read.
- **`is_correct` is NULL at log time:** The client doesn't know ground truth at decision time. It's filled later via a batch update or during the level-completion phase when ground truth is revealed.
- **Idempotency:** Each action is unique by `(session_id, timestamp)`. The log is append-only. De-duplication can be added with a UNIQUE constraint if needed.

---

### 2.3 `GET /api/v1/analytics/{session_id}`

Get session analytics summary, including the auto-generated `conclusion` from the `analytics_summary` VIEW.

**Request Headers:**
```json
{
  "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9..."
}
```

**URL Parameters:**

| Param        | Type   | Required | Description               |
|--------------|--------|----------|---------------------------|
| `session_id` | string | **Yes**  | UUID of the session       |

**Example Request:**
```
GET /api/v1/analytics/f47ac10b-58cc-4372-a567-0e02b2c3d479
```

**Success Response — `200 OK`:**
```json
{
  "ok": true,
  "session_id": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
  "user": {
    "user_id": 1,
    "nis": "20250101",
    "name": "Aisyah Putri",
    "class_id": "7A"
  },
  "session": {
    "level": 3,
    "started_at": "2025-07-09T10:35:00.000Z",
    "ended_at": "2025-07-09T11:02:00.000Z",
    "total_rounds": 15,
    "final_score": 73.3
  },
  "metrics": {
    "total_actions": 18,
    "accept_count": 8,
    "override_count": 7,
    "correct_count": 3,
    "override_rate": 0.389,
    "accept_rate": 0.444,
    "accuracy": 0.733,
    "override_accuracy": 0.714,
    "avg_cnn_confidence": 0.682,
    "avg_latency_ms": 3100
  },
  "conclusion": "Siswa mulai mengembangkan pemikiran kritis: mulai meng-override saat AI kurang yakin, akurasi override masih berkembang."
}
```

> **Note:** The `conclusion` field is auto-generated by the `analytics_summary` VIEW using `CASE WHEN` logic. This satisfies Bu Hesti's requirement that every data log must have a "kesimpulan kalimat" (conclusion sentence) alongside the raw metrics.

**Error Responses:**

| Status | Condition                               | Body                                                |
|--------|-----------------------------------------|-----------------------------------------------------|
| 401    | Missing or invalid token                | `{"ok":false,"error":"unauthorized"}`               |
| 403    | Student querying another user's session | `{"ok":false,"error":"forbidden: can only view your own analytics"}` |
| 404    | Session not found                       | `{"ok":false,"error":"session not found"}`          |
| 500    | Database error                          | `{"ok":false,"error":"internal server error"}`      |

**Implementation Notes:**
- **VIEW query:** The endpoint executes `SELECT * FROM analytics_summary WHERE session_id = ?` and maps the result to the response format above.
- **Authorization:** Students can only view analytics for their own sessions. Teachers/admins can view any session.
- **Empty sessions:** If a session has no `action_logs` yet, the metrics will be zeroed and the conclusion will fall to the default CASE.

---

### 2.4 `GET /api/v1/sessions`

Get all sessions for a user (history). Used by the student's profile/history view and by the dashboard.

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
GET /api/v1/sessions?level=3&limit=10&offset=0
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
      "actions": [
        {
          "log_id": 1301,
          "action_type": "click",
          "context_level": 3,
          "cnn_prediction": 0.91,
          "decision": "accept",
          "override_label": null,
          "is_correct": 1,
          "latency_ms": 1200,
          "timestamp": "2025-07-09T10:36:12.000Z"
        },
        {
          "log_id": 1302,
          "action_type": "click",
          "context_level": 3,
          "cnn_prediction": 0.65,
          "decision": "override",
          "override_label": "serigala",
          "is_correct": 1,
          "latency_ms": 5200,
          "timestamp": "2025-07-09T10:38:45.000Z"
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
      "actions": []
    }
  ]
}
```

> **Note:** `actions` array is included by default but can be excluded with `?include_actions=false` for lightweight listing. When `actions` is empty `[]`, it means the detailed log was not requested or the session data is summary-only.

**Error Responses:**

| Status | Condition                               | Body                                                |
|--------|-----------------------------------------|-----------------------------------------------------|
| 401    | Missing or invalid token                | `{"ok":false,"error":"unauthorized"}`               |
| 403    | Student querying another user_id        | `{"ok":false,"error":"forbidden: can only view your own sessions"}` |
| 400    | Invalid level filter                    | `{"ok":false,"error":"level must be between 1 and 6"}` |
| 500    | Database error                          | `{"ok":false,"error":"internal server error"}`      |

**Implementation Notes:**
- **Pagination:** `total` reflects the count after filters, before `limit`/`offset`. Client uses `total` + `limit` to know if more pages exist.
- **Sorting:** Sessions returned in reverse chronological order (`started_at DESC`).
- **Action detail:** Including `actions` inline avoids N+1 queries on the client. If performance becomes an issue with large datasets, use `?include_actions=false`.

---

### 2.5 `POST /api/v1/analyze`

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
| `accuracy`            | SUM(is_correct=1) / COUNT(all decisions where is_correct IS NOT NULL) |
| `avg_confidence_gap`  | AVG(top1_conf - top2_conf) — how "certain" the AI appears    |
| `avg_latency_ms`      | AVG(latency_ms) — how long student takes to decide            |
| `override_accuracy`   | SUM(override AND is_correct=1) / COUNT(override) — are overrides correct? |

**Success Response — `200 OK`:**
```json
{
  "ok": true,
  "meta": {
    "n_clusters": 3,
    "features_used": [
      "override_rate",
      "accept_rate",
      "accuracy",
      "avg_confidence_gap",
      "avg_latency_ms",
      "override_accuracy"
    ],
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

**Implementation Notes:**
- **K-Means library:** Use [`ml-kmeans`](https://github.com/mljs/kmeans) (pure JS) or call Python's `sklearn.cluster.KMeans` via a child process for larger datasets.
- **Feature scaling:** All features MUST be standardized (z-score) before clustering. Raw values have different scales (latency in ms vs rates 0–1).
- **Cluster labels:** Auto-generated based on centroid characteristics:
  - High `accept_rate` + low `accuracy` → "AI Dependent"
  - Moderate `override_rate` + moderate `accuracy` → "Developing Critical Thinker"
  - High `override_rate` + high `override_accuracy` → "Critical Thinker"
- **Caching:** Results are NOT cached. Each request runs a fresh analysis. If the dataset grows large, add a `?cached=true` option.
- **Performance:** With ≤100 students and ≤50 decisions each, the computation finishes in <200ms.
- **Why POST, not GET:** The request body contains analysis parameters that are too complex for query strings, and triggering computation is a state-changing action.

---

### 2.6 `GET /api/v1/recommendations/{user_id}`

Personalized tips and recommendations based on the student's cluster assignment from the most recent K-Means analysis.

**Request Headers:**
```json
{
  "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9..."
}
```

**URL Parameters:**

| Param      | Type    | Required | Description                   |
|------------|---------|----------|-------------------------------|
| `user_id`  | integer | **Yes**  | User ID to get recommendations for |

**Example Request:**
```
GET /api/v1/recommendations/1
```

**Success Response — `200 OK`** (Critical Thinker):
```json
{
  "ok": true,
  "user": {
    "user_id": 1,
    "nis": "20250101",
    "name": "Aisyah Putri",
    "class_id": "7A"
  },
  "cluster": {
    "cluster_id": 2,
    "label": "Critical Thinker",
    "description": "Siswa secara aktif meng-override prediksi AI yang salah. Override accuracy tinggi, menunjukkan pemahaman baik."
  },
  "metrics": {
    "override_rate": 0.52,
    "accuracy": 0.89,
    "override_accuracy": 0.83,
    "avg_latency_ms": 4100,
    "total_decisions": 47
  },
  "recommendations": [
    {
      "id": "rec_ct_01",
      "title": "Coba Level yang Lebih Sulit!",
      "message": "Kamu sudah menunjukkan pemikiran kritis yang baik. Level 5 dan 6 akan memberikan tantangan yang lebih menarik — AI akan membuat lebih banyak kesalahan halus.",
      "action": "navigate",
      "action_data": { "level": 5 },
      "priority": 1
    },
    {
      "id": "rec_ct_02",
      "title": "Ajarkan Temanmu",
      "message": "Kamu bisa menjadi tutor sebaya! Bantu teman yang masih sering menerima prediksi AI tanpa berpikir kritis. Jelaskan mengapa kamu memilih untuk meng-override.",
      "action": null,
      "action_data": null,
      "priority": 2
    },
    {
      "id": "rec_ct_03",
      "title": "Eksplorasi Bias AI",
      "message": "Coba perhatikan: di jenis gambar apa AI paling sering salah? Apakah ada pola? Ini disebut 'bias' dalam AI — topik yang menarik untuk dipelajari lebih lanjut!",
      "action": null,
      "action_data": null,
      "priority": 3
    }
  ]
}
```

**Success Response — `200 OK`** (AI Dependent):
```json
{
  "ok": true,
  "user": {
    "user_id": 2,
    "nis": "20250102",
    "name": "Budi Santoso",
    "class_id": "7A"
  },
  "cluster": {
    "cluster_id": 0,
    "label": "AI Dependent",
    "description": "Siswa cenderung menerima prediksi AI tanpa mempertimbangkan. Override rate rendah, akurasi menurun saat AI salah."
  },
  "metrics": {
    "override_rate": 0.08,
    "accuracy": 0.62,
    "override_accuracy": 0.33,
    "avg_latency_ms": 1800,
    "total_decisions": 45
  },
  "recommendations": [
    {
      "id": "rec_ad_01",
      "title": "Jangan Buru-buru Percaya!",
      "message": "AI tidak selalu benar. Sebelum menekan 'Accept', tanyakan pada dirimu: 'Apakah gambar ini benar-benar seperti yang AI katakan?' Coba bandingkan dengan gambarmu sendiri.",
      "action": "navigate",
      "action_data": { "level": 2 },
      "priority": 1
    },
    {
      "id": "rec_ad_02",
      "title": "Latihan Override",
      "message": "Coba mainkan Level 2 lagi dan tantang dirimu untuk meng-override minimal 3 kali. Perhatikan: apakah pilihanmu lebih benar dari AI?",
      "action": "navigate",
      "action_data": { "level": 2 },
      "priority": 2
    },
    {
      "id": "rec_ad_03",
      "title": "Perhatikan Confidence Bar",
      "message": "Ketika bar confidence AI pendek (di bawah 60%), itu artinya AI tidak yakin. Ini saat yang tepat untuk memikirkan ulang jawabannya!",
      "action": null,
      "action_data": null,
      "priority": 3
    }
  ]
}
```

**Success Response — `200 OK`** (no cluster assigned yet):
```json
{
  "ok": true,
  "user": {
    "user_id": 5,
    "nis": "20250105",
    "name": "Eka Prasetya",
    "class_id": "7B"
  },
  "cluster": null,
  "metrics": {
    "override_rate": 0.0,
    "accuracy": 0.0,
    "override_accuracy": 0.0,
    "avg_latency_ms": 0,
    "total_decisions": 0
  },
  "recommendations": [
    {
      "id": "rec_new_01",
      "title": "Mulai Bermain!",
      "message": "Kamu belum memiliki data yang cukup. Mainkan beberapa level terlebih dahulu, dan kami akan memberikan rekomendasi yang dipersonalisasi untukmu.",
      "action": "navigate",
      "action_data": { "level": 1 },
      "priority": 1
    }
  ]
}
```

**Error Responses:**

| Status | Condition                               | Body                                                |
|--------|-----------------------------------------|-----------------------------------------------------|
| 401    | Missing or invalid token                | `{"ok":false,"error":"unauthorized"}`               |
| 403    | Student querying another user_id        | `{"ok":false,"error":"forbidden: can only view your own recommendations"}` |
| 404    | User not found                          | `{"ok":false,"error":"user not found"}`             |
| 500    | Database error                          | `{"ok":false,"error":"internal server error"}`      |

**Implementation Notes:**
- **Cluster lookup:** The endpoint checks the most recent K-Means analysis result (stored server-side in memory or an `analysis_cache` table) for the user's cluster assignment. If no analysis has been run, `cluster` is `null`.
- **Recommendation templates:** Pre-defined per cluster label. The mapping is:
  - `"AI Dependent"` → `rec_ad_*` templates (encourage override, teach skepticism)
  - `"Developing Critical Thinker"` → `rec_dct_*` templates (reinforce behavior, deepen understanding)
  - `"Critical Thinker"` → `rec_ct_*` templates (challenge further, teach about AI bias)
  - `null` (no cluster) → `rec_new_*` templates (get started)
- **`action` field:** If non-null, the client can use this to auto-navigate (e.g., open a specific level). `navigate` = go to the level specified in `action_data.level`.
- **Dynamic metrics:** The `metrics` object reflects the user's actual aggregated data from `action_logs`, not just the cluster centroid.

---

## §3 — Common Patterns

### 3.1 Authentication Flow

```
┌──────────┐          ┌──────────┐          ┌──────────┐
│  Client  │          │  Server  │          │  SQLite  │
└────┬─────┘          └────┬─────┘          └────┬─────┘
     │  POST /api/v1/auth/login  │                   │
     │  { nis, name }           │                   │
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
Client builds payload (session_id, action_type, raw_data, decision, latency)
        │
        ▼
POST /api/v1/logs  ──────>  Server validates JWT
                                    │
                                    ▼
                              Extract user_id from JWT
                              (NOT from body — prevents impersonation)
                                    │
                                    ▼
                              Auto-create session if needed
                                    │
                                    ▼
                              INSERT into action_logs
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

Example with validation details:

```json
{
  "ok": false,
  "error": "validation failed",
  "details": {
    "context_level": "must be between 1 and 6",
    "cnn_prediction": "must be between 0.0 and 1.0"
  }
}
```

### 3.4 Rate Limiting

| Endpoint                        | Limit                          |
|---------------------------------|--------------------------------|
| `POST /api/v1/auth/login`       | 5 requests / minute / IP      |
| `POST /api/v1/logs`             | 60 requests / minute / user   |
| `GET /api/v1/analytics/{id}`    | 30 requests / minute / user   |
| `GET /api/v1/sessions`          | 30 requests / minute / user   |
| `POST /api/v1/analyze`          | 5 requests / minute / user    |
| `GET /api/v1/recommendations/{id}` | 30 requests / minute / user |

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

## §4 — Endpoint Summary Table

| # | Method | Endpoint                              | Auth | Description                           |
|---|--------|---------------------------------------|------|---------------------------------------|
| 1 | POST   | `/api/v1/auth/login`                  | No   | NIS+name auth, auto-register, returns JWT |
| 2 | POST   | `/api/v1/logs`                        | JWT  | Core HITL decision logging            |
| 3 | GET    | `/api/v1/analytics/{session_id}`      | JWT  | Get session analytics + conclusion    |
| 4 | GET    | `/api/v1/sessions`                    | JWT  | Get all sessions for a user (history) |
| 5 | POST   | `/api/v1/analyze`                     | JWT+ | Trigger K-Means clustering analysis   |
| 6 | GET    | `/api/v1/recommendations/{user_id}`   | JWT  | Personalized tips based on cluster    |

> **Auth column:** "No" = no token required. "JWT" = Bearer token required. "JWT+" = Bearer token + teacher/admin role required.

---

## §5 — Future Extensions (Out of Scope for v1.0)

| Feature                          | Why Not Now                            | Endpoint Sketch              |
|----------------------------------|----------------------------------------|------------------------------|
| Password authentication          | Not needed for internal school lab     | `POST /api/v1/auth/register` |
| Session start/end endpoints      | Auto-creation in `/api/v1/logs` is simpler | `POST /api/v1/sessions/start` |
| Per-action detail endpoint       | Included inline in `GET /api/v1/sessions` | `GET /api/v1/logs/:log_id`   |
| Export CSV                       | Bu Hesti can use dashboard for now     | `GET /api/v1/export?format=csv` |
| Real-time WebSocket notifications| Dashboard is pull-based for v1         | `WS /ws/dashboard`           |
| Multi-teacher admin roles        | Single teacher (Bu Hesti) for research | Add `role` to `users` table  |
| Analysis result persistence      | Fresh analysis each time is fine       | `analysis_results` table     |
| Batch logging endpoint           | One action per request keeps it simple | `POST /api/v1/logs/batch`    |

---

## §6 — Implementation Checklist

- [ ] Create SQLite schema (users, sessions, action_logs)
- [ ] Create `analytics_summary` VIEW with CASE WHEN conclusion
- [ ] Implement JWT token generation/validation middleware
- [ ] Implement `POST /api/v1/auth/login` with auto-register
- [ ] Implement `POST /api/v1/logs` with session auto-creation
- [ ] Implement `GET /api/v1/analytics/{session_id}` using VIEW
- [ ] Implement `GET /api/v1/sessions` with pagination
- [ ] Implement `POST /api/v1/analyze` with ml-kmeans
- [ ] Implement `GET /api/v1/recommendations/{user_id}` with cluster-based templates
- [ ] Add rate limiting middleware
- [ ] Add CORS configuration
- [ ] Add request validation middleware (Joi/Zod)
- [ ] Write integration tests for each endpoint
- [ ] Seed script for demo data (28 students × ~50 actions each)
