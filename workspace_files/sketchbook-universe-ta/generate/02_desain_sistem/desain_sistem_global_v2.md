# Desain Sistem Global V2 — Sketchbook Universe

> **Proyek:** Sketchbook Universe — Simulasi Interaktif Literasi AI untuk Siswa SMP Kelas 7-9
> **Arsitektur:** Hybrid — Browser-Based Inference (TF.js) + Server-Side Active Services (REST API, SQLite, K-Means)
> **Tim:** Can 🔵 (Frontend / Kaplay.js / MediaPipe / Maskot / Gameplay / UI) | Dias 🟢 (Backend / CNN / TensorFlow.js / API / DB / K-Means) | Shared ⚪ (Business Logic / State / HITL / Session)
> **Format:** INPUT → PROSES → OUTPUT — satu diagram global, berwarna, shape flowchart standar

---

## Daftar Isi

1. [Legenda Warna & Simbol](#1-legenda-warna--simbol)
2. [Diagram Global IPO](#2-diagram-global-ipo)
3. [Detail Arsitektur 3 Layer](#3-detail-arsitektur-3-layer)
4. [Data Flow: Real-Time vs Batch](#4-data-flow-real-time-vs-batch)
5. [Perbandingan dengan Versi Lama](#5-perbandingan-dengan-versi-lama)
6. [Komponen per Anggota](#6-komponen-per-anggota)
7. [Catatan Keputusan Desain](#7-catatan-keputusan-desain)

---

## 1. Legenda Warna & Simbol

### Legenda Warna Tim

| Warna | Kode | Anggota | Cakupan |
|-------|------|---------|---------|
| 🔵 BIRU | `🔵` | Can | Frontend, Kaplay.js, MediaPipe, Maskot Momo, Gameplay, UI, Event Packager |
| 🟢 HIJAU | `🟢` | Dias | Backend, CNN MobileNet, TensorFlow.js, REST API, SQLite, K-Means, Dashboard |
| ⚪ ABU-ABU | `⚪` | Shared | State Management, HITL Orchestrator, Session Manager, Validasi, Auth Logic |

### Legenda Shape Flowchart

| Shape | Karakter ASCII | Fungsi |
|-------|---------------|--------|
| Parallelogram | `▱▱▱` atau `/  /` | INPUT / OUTPUT |
| Rectangle | `┌───┐` | PROSES |
| Diamond | `◇──◇` | KEPUTUSAN (Decision) |
| Oval | `(   )` | START / END |
| Panah | `──▶` | Arah alur data |

### Legenda Arsitektur Layer

| Layer | Warna | Komponen Utama |
|-------|-------|----------------|
| LAYER 1: Presentation | 🔵 Can | Kaplay.js, Maskot Momo, Level Renderer, UI, MediaPipe, Drawing Canvas |
| LAYER 2: Business Logic | ⚪ Shared | State Manager, HITL Orchestrator, Session Manager, Validation Engine |
| LAYER 3: Data & AI | 🟢 Dias | CNN MobileNet, TF.js Runtime, K-Means Clustering, SQLite, REST API Analytics |

---

## 2. Diagram Global IPO

```
╔══════════════════════════════════════════════════════════════════════════════════════════╗
║                           DESAIN SISTEM GLOBAL V2 — IPO                                 ║
║                Sketchbook Universe — Simulasi Interaktif Literasi AI                    ║
║                         Siswa SMP Kelas 7, 8, 9                                         ║
╚══════════════════════════════════════════════════════════════════════════════════════════╝

  ( START )
      │
      ▼
╔══════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                        ║
║   ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱   ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱   ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱   ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱    ║
║  ▱ Kredensial Login  ▱ ▱ Gesture Tangan    ▱ ▱ Gambar Sketsa     ▱ ▱ Konteks Level    ▱ ║
║  ▱  (Email/Password) ▱ ▱ (Kamera/MediaPipe)▱ ▱  dari Canvas      ▱ ▱ Rintangan/Aturan ▱ ║
║   ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱   ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱   ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱   ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱    ║
║        ⚪ Shared            🔵 Can              🔵 Can              🔵 Can              ║
║                                                                                        ║
╠══════════════════════════════════════════════════════════════════════════════════════════╣
║                               I N P U T                                                ║
╚════════════════════════════════╤═════════════════════════════════════════════════════════╝
                                 │
                                 ▼
╔══════════════════════════════════════════════════════════════════════════════════════════╗
║  Fase 0: Autentikasi & Onboarding ⚪🔵                                                ║
║                                                                                        ║
║  ┌──────────────────────┐                                                               ║
║  │ ⚪ Session Manager   │                                                               ║
║  │   Login WAJIB        │                                                               ║
║  │   Email + Password   │                                                               ║
║  └──────────┬───────────┘                                                               ║
║             │                                                                          ║
║             ▼                                                                          ║
║       ◇──────────◇                                                                     ║
║      ◇  Login     ◇                                                                    ║
║      ◇  Valid?    ◇                                                                    ║
║        ◇──────◇                                                                        ║
║        │    │                                                                           ║
║     Ya │    │ Tidak                                                                     ║
║        ▼    ▼                                                                           ║
║  ┌──────────┐  ┌──────────────┐                                                        ║
║  │ ⚪ Buat  │  │ 🔵 Tampilkan │                                                        ║
║  │ Session  │  │ Error Login  │                                                        ║
║  │ Token    │  │ + Retry      │                                                        ║
║  └────┬─────┘  └──────────────┘                                                        ║
║       │                                                                                ║
║       ▼                                                                                ║
║  ┌──────────────────────┐                                                               ║
║  │ 🔵 Onboarding Screen │                                                               ║
║  │   Tutorial General   │                                                               ║
║  │   Maskot Momo Intro  │                                                               ║
║  │   (Bubble Teks)      │                                                               ║
║  └──────────┬───────────┘                                                               ║
║             │                                                                          ║
╚════════════╧═════════════════════════════════════════════════════════════════════════════╝
              │
              ▼
╔══════════════════════════════════════════════════════════════════════════════════════════╗
║  Fase 1: Input Interaksi 🔵                                                            ║
║                                                                                        ║
║  ┌──────────────────┐    ┌──────────────────┐    ┌──────────────────────┐               ║
║  │ 🔵 MediaPipe     │───▶│ 🔵 Drawing Canvas│───▶│ 🔵 Kaplay.js         │               ║
║  │   Hand Tracking  │    │   (Input Sketsa) │    │   Game Engine        │               ║
║  │   Finger Pointer │    │   Clear/Redraw   │    │   State Management   │               ║
║  └──────────────────┘    └────────┬─────────┘    └──────────────────────┘               ║
║                                   │                                                    ║
║                         Canvas Image Data                                                ║
║                                   │                                                    ║
╚═══════════════════════════════════╧═══════════════════════════════════════════════════════╝
                                    │
                                    ▼
╔══════════════════════════════════════════════════════════════════════════════════════════╗
║  Fase 2: Klasifikasi AI 🟢                                                             ║
║                                                                                        ║
║  ┌──────────────────┐    ┌──────────────────┐    ┌──────────────────────┐               ║
║  │ 🟢 Image         │───▶│ 🟢 CNN MobileNet │───▶│ 🟢 TensorFlow.js     │               ║
║  │   Preprocessing  │    │   Feature Extract│    │   Top-3 Prediction   │               ║
║  │   Resize 28×28   │    │   Inference      │    │   + Confidence Score │               ║
║  │   Grayscale/Norm │    │   (Browser-side) │    │   + Confidence Gap   │               ║
║  └──────────────────┘    └──────────────────┘    └──────────┬───────────┘               ║
║                                                              │                         ║
║                                                  Top-3 + Confidence                         ║
║                                                              │                         ║
╚══════════════════════════════════════════════════════════════╧═══════════════════════════╝
                                                               │
                                                               ▼
╔══════════════════════════════════════════════════════════════════════════════════════════╗
║  Fase 3: HITL Probe & Keputusan ⚪🔵🟢                                                ║
║                                                                                        ║
║  ┌──────────────────────┐                                                               ║
║  │ ⚪ HITL Orchestrator │                                                               ║
║  │   Koordinasi probe   │                                                               ║
║  │   antara AI & siswa  │                                                               ║
║  └──────────┬───────────┘                                                               ║
║             │                                                                          ║
║             ▼                                                                          ║
║  ┌──────────────────────┐                                                               ║
║  │ 🔵 Probe UI          │◀── Top-3 + Confidence dari Fase 2                           ║
║  │   Tampilkan Prediksi │                                                               ║
║  │   Momo Bubble Teks   │                                                               ║
║  └──────────┬───────────┘                                                               ║
║             │                                                                          ║
║             ▼                                                                          ║
║       ◇──────────◇                                                                     ║
║      ◇  Keputusan  ◇    Siswa membaca prediksi AI, lalu memilih:                      ║
║      ◇  Siswa      ◇    Accept / Correct / Override                                   ║
║        ◇──────◇                                                                        ║
║             │                                                                          ║
║        ┌────┴────┐                                                                     ║
║        ▼         ▼                                                                     ║
║   🔵 Accept   🔵 Override                                                              ║
║   (Setuju     (Koreksi Label)                                                          ║
║    AI benar)                                                                            ║
║        │         │                                                                     ║
║        └────┬────┘                                                                     ║
║             ▼                                                                          ║
║  ┌──────────────────────┐    ┌──────────────────────┐                                  ║
║  │ ⚪ Decision Resolver │───▶│ ⚪ Object Behavior   │                                  ║
║  │   (Final Label)      │    │   Mapper              │                                  ║
║  └──────────────────────┘    │   Solid / Danger      │                                  ║
║                              │   (Duri)              │                                  ║
║                              └──────────────────────┘                                  ║
║             ⚪ Shared              ⚪ Shared                                            ║
╚═══════════════════════════════════════════════════════════════════════════════════════════╝
                                   │
                                   ▼
╔══════════════════════════════════════════════════════════════════════════════════════════╗
║  Fase 4: Simulasi & Konsekuensi 🔵⚪                                                   ║
║                                                                                        ║
║  ┌──────────────────┐    ┌──────────────────┐    ┌──────────────────────┐               ║
║  │ 🔵 Level         │───▶│ 🔵 Game Physics  │───▶│ 🔵 Maskot Momo       │               ║
║  │   Controller     │    │   Collision      │    │   Feedback Edukatif  │               ║
║  │   (Level 1-3)    │    │   Success/Fail   │    │   Refleksi Keputusan │               ║
║  └──────────────────┘    └────────┬─────────┘    │   (Bubble Teks)      │               ║
║                                   │              └──────────┬───────────┘               ║
║                                   ▼                         │                           ║
║                            ◇──────────◇                     │                           ║
║                           ◇  Gameplay  ◇                    │                           ║
║                           ◇  Progress  ◇                    │                           ║
║                           ◇  Feedback? ◇                    │                           ║
║                             ◇──────◇                        │                           ║
║                             │    │                          │                           ║
║                          Ya │    │ Tidak                    │                           ║
║                             ▼    ▼                          │                           ║
║                    ┌──────────┐  ┌──────────┐               │                           ║
║                    │ 🔵 Next  │  │ 🔵 Retry │               │                           ║
║                    │ Level    │  │ Fase 2   │               │                           ║
║                    │ (Lanjut) │  │ (Redraw) │               │                           ║
║                    └────┬─────┘  └──────────┘               │                           ║
║                         │                                    │                           ║
║                         ▼                                    ▼                           ║
║                  ┌──────────────────────────────────────────────┐                       ║
║                  │ ⚪ State Manager                             │                       ║
║                  │   Update skor, level, waktu                 │                       ║
║                  └──────────────────┬───────────────────────────┘                       ║
╚════════════════════════════════════╧═══════════════════════════════════════════════════════╝
                                     │
                                     ▼
╔══════════════════════════════════════════════════════════════════════════════════════════╗
║  Fase 5: Logging & Backend 🟢⚪                                                        ║
║                                                                                        ║
║  ┌──────────────────┐    ┌──────────────────────────────────────────────────┐           ║
║  │ 🔵 Event         │───▶│ 🟢 REST API                                      │           ║
║  │   Packager       │    │                                                  │           ║
║  │   (Client-side)  │    │  ┌────────────────────────────────────────────┐  │           ║
║  └──────────────────┘    │  │ POST /api/log                              │  │           ║
║                          │  │   → Simpan interaction event ke SQLite     │  │           ║
║                          │  │                                            │  │           ║
║                          │  │ GET /api/sessions                         │  │           ║
║                          │  │   → Ambil data sesi untuk dashboard       │  │           ║
║                          │  │                                            │  │           ║
║                          │  │ POST /api/analyze                         │  │           ║
║                          │  │   → Trigger K-Means clustering            │  │           ║
║                          │  └────────────────────────────────────────────┘  │           ║
║                          │                                                  │           ║
║                          │  ┌────────────────────────────────────────────┐  │           ║
║                          │  │ ⚪ JWT Authentication                      │  │           ║
║                          │  │   Login WAJIB untuk akses dashboard       │  │           ║
║                          │  │   Verifikasi token di setiap request      │  │           ║
║                          │  └────────────────────────────────────────────┘  │           ║
║                          └──────────────────────┬───────────────────────────┘           ║
║                                                 │                                      ║
║                                                 ▼                                      ║
║                          ┌──────────────────────────────────────┐                      ║
║                          │ 🟢 SQLite Database                   │                      ║
║                          │                                      │                      ║
║                          │   users                               │                      ║
║                          │     id, email, password_hash, name   │                      ║
║                          │                                      │                      ║
║                          │   interaction_logs                    │                      ║
║                          │     id, user_id, session_id,         │                      ║
║                          │     level, sketch_label, ai_top3,    │                      ║
║                          │     confidence, decision, final_label│                      ║
║                          │     decision_time, timestamp         │                      ║
║                          │                                      │                      ║
║                          │   sessions                            │                      ║
║                          │     id, user_id, start_time,         │                      ║
║                          │     end_time, levels_completed       │                      ║
║                          │                                      │                      ║
║                          │   cluster_results                     │                      ║
║                          │     id, user_id, cluster_id,         │                      ║
║                          │     features_json, analyzed_at       │                      ║
║                          │                                      │                      ║
║                          └──────────────────────┬───────────────┘                      ║
╚═════════════════════════════════════════════════╧════════════════════════════════════════╝
                                                  │
                                                  ▼
╔══════════════════════════════════════════════════════════════════════════════════════════╗
║  Fase 6: Analisis & Dashboard 🟢                                                       ║
║                                                                                        ║
║  ┌──────────────────┐    ┌──────────────────┐    ┌──────────────────────┐               ║
║  │ 🟢 Feature       │───▶│ 🟢 K-Means       │───▶│ 🟢 Dashboard Guru    │               ║
║  │   Engineering    │    │   Clustering     │    │   Visualisasi &      │               ║
║  │   Accept rate    │    │   Pola Keputusan │    │   Export CSV/JSON    │               ║
║  │   Override rate  │    │   Siswa SMP      │    │                      │               ║
║  │   Avg dec. time  │    │   (Server-side)  │    │                      │               ║
║  │   Danger accept  │    │                  │    │                      │               ║
║  │   Success rate   │    │                  │    │                      │               ║
║  └──────────────────┘    └──────────────────┘    └──────────────────────┘               ║
║                                                                                        ║
╚══════════════════════════════════════════════════════════════════════════════════════════╝
              │
              ▼
╔══════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                        ║
║   ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱   ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱   ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱                   ║
║  ▱ Prototype Simulasi  ▱ ▱ Pengalaman HITL   ▱ ▱ Dataset Log Interaksi  ▱               ║
║  ▱ Interaktif Berlevel ▱ ▱ Evaluasi AI       ▱ ▱ Terstruktur (SQLite)   ▱               ║
║   ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱   ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱   ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱                   ║
║        🔵 Can                 🔵 Can                🟢 Dias                             ║
║                                                                                        ║
║   ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱   ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱   ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱                   ║
║  ▱ Analisis Pola       ▱ ▱ Dashboard Guru    ▱ ▱ Model TF.js + Confidence ▱             ║
║  ▱ Keputusan Siswa     ▱ ▱ + Export Data     ▱ ▱ Score (Browser-side)    ▱              ║
║   ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱   ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱   ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱                   ║
║        🟢 Dias                🟢 Dias               🟢 Dias                              ║
║                                                                                        ║
╠══════════════════════════════════════════════════════════════════════════════════════════╣
║                               O U T P U T                                              ║
╚══════════════════════════════════════════════════════════════════════════════════════════╝
              │
              ▼
         ( END )
```

### Alur Data Ringkas (Satu Baris)

```
Login ⚪ ──▶ Gesture + Sketsa 🔵 ──▶ CNN + TF.js 🟢 ──▶ Probe + HITL ⚪🔵 ──▶ Decision + Simulasi 🔵⚪ ──▶ Logging 🟢 ──▶ K-Means + Dashboard 🟢
```

### Titik Temu Antar Fase

```
    🔵 Fase 1                 🟢 Fase 2                  ⚪🔵 Fase 3                🔵 Fase 4
    ┌──────────────┐         ┌──────────────┐          ┌──────────────┐          ┌──────────────┐
    │ Drawing      │─Canvas─▶│ CNN MobileNet│──Top-3──▶│ HITL Probe   │─Label──▶│ Game Physics │
    │ Canvas       │  Image  │ + TF.js      │  +Conf.  │ + Decision   │  Final  │ + Collision  │
    └──────────────┘         └──────────────┘          └──────┬───────┘          └──────┬───────┘
                                                              │                         │
                                                        Interaction                  Level
                                                         Event JSON                  Result
                                                              │                         │
                                                              ▼                         ▼
                                                        🟢 Fase 5                 🔵 Fase 4b
                                                        ┌──────────────┐          ┌──────────────┐
                                                        │ REST API     │          │ Maskot Momo  │
                                                        │ + SQLite     │          │ Feedback     │
                                                        └──────┬───────┘          └──────────────┘
                                                               │
                                                               ▼
                                                         🟢 Fase 6
                                                         ┌──────────────┐
                                                         │ K-Means +    │
                                                         │ Dashboard    │
                                                         └──────────────┘
```

---

## 3. Detail Arsitektur 3 Layer

### 🔵 LAYER 1: PRESENTATION (Can)

**Tanggung jawab:** Seluruh interaksi pengguna, rendering visual, input gesture, dan gameplay di browser.

```
┌─────────────────────────────────────────────────────────────────────┐
│                     🔵 LAYER 1: PRESENTATION                       │
│                                                                     │
│  ┌─────────────────┐  ┌─────────────────┐  ┌──────────────────┐   │
│  │ Kaplay.js        │  │ MediaPipe       │  │ UI Components    │   │
│  │ Game Engine      │  │ Hand Tracking   │  │                  │   │
│  │                  │  │                 │  │  ┌ Login Screen  │   │
│  │  ┌ Game Loop     │  │  ┌ Hand Landmark│  │  ├ Probe UI     │   │
│  │  ├ Sprite Sys    │  │  ├ Finger Point │  │  ├ Score Panel  │   │
│  │  ├ Physics 2D    │  │  ├ Deadzone     │  │  ├ Timer Display│   │
│  │  ├ Collision     │  │  └ Stabilizer   │  │  ├ Level Select │   │
│  │  └ Scene Mgmt   │  │                 │  │  └ Result Screen│   │
│  └────────┬────────┘  └────────┬────────┘  └──────────────────┘   │
│           │                    │                                     │
│  ┌────────┴────────┐  ┌───────┴─────────┐  ┌──────────────────┐   │
│  │ Level Renderer   │  │ Drawing Canvas  │  │ Maskot Momo      │   │
│  │                  │  │                 │  │                  │   │
│  │  ┌ Background   │  │  ┌ Stroke Input │  │  ┌ Idle Anim     │   │
│  │  ├ Objek Solid  │  │  ├ Clear/Redraw │  │  ├ Happy Anim    │   │
│  │  ├ Objek Duri   │  │  ├ Color Select │  │  ├ Sad Anim      │   │
│  │  ├ Character    │  │  └ Submit Sketch│  │  ├ Think Anim    │   │
│  │  ├ Obstacle     │  │                 │  │  └ Bubble Teks   │   │
│  │  └ Finish Line  │  │                 │  │                  │   │
│  └─────────────────┘  └─────────────────┘  └──────────────────┘   │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

**Spesifikasi Teknis:**
- Engine: Kaplay.js (Kaboom.js fork) — 2D game engine berbasis web
- Input: MediaPipe Hands — 21 landmark per tangan, 30+ FPS
- Rendering: HTML5 Canvas — 60 FPS target
- Maskot: Sprite-based animation + teks bubble (tanpa suara, tanpa NLP)
- Objek: Hanya 2 kategori — **Solid** (aman, bisa diinjak) dan **Danger/Duri** (berbahaya, harus dihindari)
- Level: 3 level — Level 1 (target 2 menit, gampang) → Level 2 → Level 3 (menantang)
- Tutorial: General di Level 1, clue berkurang di Level 2-3

### ⚪ LAYER 2: BUSINESS LOGIC (Shared)

**Tanggung jawab:** Orkestrasi alur HITL, manajemen state, validasi data, dan logika sesi. Ini adalah "otak koordinasi" yang menghubungkan Presentation dan Data/AI.

```
┌─────────────────────────────────────────────────────────────────────┐
│                    ⚪ LAYER 2: BUSINESS LOGIC                       │
│                                                                     │
│  ┌─────────────────┐  ┌─────────────────┐  ┌──────────────────┐   │
│  │ State Manager    │  │ HITL Orchestrator│  │ Session Manager  │   │
│  │                  │  │                  │  │                  │   │
│  │  ┌ Game State    │  │  ┌ Probe Trigger │  │  ┌ Login WAJIB  │   │
│  │  ├ Current Level │  │  ├ Timer Control │  │  ├ JWT Token    │   │
│  │  ├ Score         │  │  ├ Decision Wait │  │  ├ Session ID   │   │
│  │  ├ Time Elapsed  │  │  ├ Result Route  │  │  ├ History Cek  │   │
│  │  └ Level Progres│  │  └ Feedback Loop │  │  └ Progress Save│   │
│  └─────────────────┘  └─────────────────┘  └──────────────────┘   │
│                                                                     │
│  ┌─────────────────┐  ┌─────────────────┐                          │
│  │ Validation Engine│  │ Decision Resolver│                         │
│  │                  │  │                  │                         │
│  │  ┌ Input Valid   │  │  ┌ Accept Route  │                         │
│  │  ├ Schema Check  │  │  ├ Override Route│                         │
│  │  ├ Confidence Th │  │  ├ Final Label   │                         │
│  │  └ Sanitize Data │  │  └ Category Map  │                         │
│  │                  │  │   (Solid/Danger) │                         │
│  └─────────────────┘  └─────────────────┘                          │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

**Spesifikasi Teknis:**
- State: JavaScript object-based, reactive updates ke Kaplay.js scene
- HITL: Orkestrasi 3-stage — Show Prediction → Wait Decision → Route Result
- Decision: Accept (AI benar) atau Override (siswa koreksi label)
- Validasi: Client-side input sanitization + server-side payload validation
- Session: JWT-based, wajib login untuk simpan history dan progress
- Kategori Objek: Hanya **Solid** dan **Danger** (duri) — dekoratif dihapus

### 🟢 LAYER 3: DATA & AI (Dias)

**Tanggung jawab:** Inference CNN, penyimpanan data, analisis K-Means, dan dashboard guru.

```
┌─────────────────────────────────────────────────────────────────────┐
│                     🟢 LAYER 3: DATA & AI                          │
│                                                                     │
│  ┌─────────────────┐  ┌─────────────────┐  ┌──────────────────┐   │
│  │ CNN MobileNet    │  │ REST API Server  │  │ K-Means Pipeline │   │
│  │                  │  │                  │  │                  │   │
│  │  ┌ Feature Ext   │  │  ┌ POST /api/log │  │  ┌ Feature Eng  │   │
│  │  ├ Transfer Learn│  │  ├ GET /api/sess │  │  ├ Normalize    │   │
│  │  ├ Classif Head  │  │  ├ POST /api/ana │  │  ├ Elbow Method │   │
│  │  ├ TF.js Export  │  │  ├ JWT Verify    │  │  ├ Cluster K=2-5│   │
│  │  └ Confidence    │  │  └ Payload Valid │  │  └ Interpret    │   │
│  └────────┬────────┘  └────────┬────────┘  └──────────────────┘   │
│           │                    │                                     │
│  ┌────────┴────────┐  ┌───────┴─────────┐  ┌──────────────────┐   │
│  │ TF.js Runtime    │  │ SQLite Database  │  │ Dashboard Guru   │   │
│  │ (Browser-side)   │  │                  │  │                  │   │
│  │                  │  │  ┌ users         │  │  ┌ Session List  │   │
│  │  ┌ Load Model    │  │  ├ interact_logs│  │  ├ Cluster Viz   │   │
│  │  ├ Preprocess    │  │  ├ sessions     │  │  ├ Export CSV    │   │
│  │  ├ Predict       │  │  └ cluster_res  │  │  ├ Export JSON   │   │
│  │  └ Top-3 + Score │  │                  │  │  └ Narasi Auto  │   │
│  └─────────────────┘  └─────────────────┘  └──────────────────┘   │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

**Spesifikasi Teknis:**
- Model: CNN MobileNet (transfer learning) — trained offline, exported ke TF.js format
- Inference: TensorFlow.js — berjalan sepenuhnya di browser siswa (client-side)
- Preprocessing: Resize 28×28, grayscale, normalisasi piksel [0,1]
- Output: Top-3 prediction + confidence score + confidence gap
- API: Express.js REST API — 3 endpoint utama + JWT verification
- DB: SQLite — ringan, server-side, 4 tabel utama
- Clustering: K-Means (scikit-learn, server-side) — pengelompokan pola keputusan siswa
- Dashboard: Web-based — visualisasi cluster + export data + narasi auto-generate

### Interaksi Antar Layer

```
    🔵 LAYER 1                    ⚪ LAYER 2                    🟢 LAYER 3
  Presentation                  Business Logic                 Data & AI

  ┌──────────┐    event data    ┌──────────┐    validated     ┌──────────┐
  │ MediaPipe │───────────────▶│ State    │──data──────────▶│ REST API │
  │ Canvas    │                │ Manager  │                  │ SQLite   │
  │ Probe UI  │    user        └──────────┘    payload       └──────────┘
  │ Momo      │◀─decision────  │ HITL     │◀──inference────  │ CNN TF.js│
  │ Level     │                │ Orchestr.│   Top-3 + Conf   │ K-Means  │
  └──────────┘                └──────────┘                  └──────────┘
       ▲                           ▲                             │
       │        render update      │    session token            │
       └───────────────────────────┘                             │
                              │                                  ▼
                    ⚪ Session Manager                   ┌──────────┐
                    ⚪ Decision Resolver                  │Dashboard │
                                                         │  Guru    │
                                                         └──────────┘
```

---

## 4. Data Flow: Real-Time vs Batch

Sistem memiliki dua jalur data yang berbeda secara fundamental: **real-time** (interaksi gameplay) dan **batch** (analisis pasca-permainan).

### Real-Time Flow (Selama Gameplay)

```
  INPUT                       PROSES                              OUTPUT
  ─────                       ──────                              ──────

  Gesture Tangan    ──▶  MediaPipe Detection           ──▶  Finger Pointer
  (30+ FPS)              (21 landmark, deadzone)             (Canvas koordinat)

  Finger Pointer    ──▶  Drawing Canvas Stroke          ──▶  Sketsa Gambar
  (real-time)            (Kaplay.js canvas)                  (image data)

  Sketsa Gambar     ──▶  Image Preprocessing            ──▶  Tensor Input
  (on submit)            (resize, grayscale, norm)           (28×28×1)

  Tensor Input      ──▶  CNN MobileNet Inference        ──▶  Top-3 + Conf
  (TF.js)                (browser-side, <100ms)              (prediction)

  Top-3 + Conf      ──▶  HITL Probe UI                  ──▶  Decision Siswa
  (display)              (Momo bubble, timer)                (Accept/Override)

  Decision Siswa    ──▶  Decision Resolver               ──▶  Final Label
  (button click)         (final label + category)            (Solid/Danger)

  Final Label       ──▶  Object Behavior + Physics       ──▶  Game Outcome
  (spawn objek)          (collision, success/fail)           (visual feedback)

  Game Outcome      ──▶  Momo Feedback                   ──▶  Refleksi Siswa
  (real-time)            (bubble teks edukatif)              (pemahaman AI)
```

**Latensi target:** <100ms per inference, <16ms per frame rendering, <1s probe display

### Batch Flow (Pasca-Permainan)

```
  INPUT                       PROSES                              OUTPUT
  ─────                       ──────                              ──────

  Interaction       ──▶  Event Packager                   ──▶  JSON Payload
  Events             │   (client-side bundling)                (structured)
  (selama main)      │
                     │   JSON Payload                       ──▶  Validated Data
                     ├──▶ Payload Validation                   (sanitized)
                     │   (server-side schema check)
                     │
                     │   Validated Data                     ──▶  Stored Records
                     ├──▶ SQLite INSERT                        (persisted)
                     │   (interaction_logs, sessions)
                     │
                     ├──▶ Session Grouping                  ──▶  User Sessions
                     │   (by user_id + time window)            (aggregated)
                     │
                     │   ── ── ── ── ── ── ── ── ── ── ──
                     │   POST /api/analyze (trigger)
                     │   ── ── ── ── ── ── ── ── ── ── ──
                     │
                     ├──▶ Feature Engineering               ──▶  Feature Vector
                     │   (accept rate, override rate,          (numerical)
                     │    avg decision time,
                     │    danger accept rate,
                     │    success rate)
                     │
                     ├──▶ K-Means Clustering               ──▶  Cluster Labels
                     │   (server-side, scikit-learn)           (grouped)
                     │   K=2-5, Elbow Method
                     │
                     └──▶ Cluster Interpretation            ──▶  Insight Narasi
                         (pola "percaya AI" vs                   (auto-generate)
                          "koreksi AI")
```

**Jadwal:** Batch analysis di-trigger via `POST /api/analyze` setelah sesi berakhir atau atas permintaan guru.

### Perbandingan Real-Time vs Batch

| Aspek | Real-Time Flow | Batch Flow |
|-------|---------------|------------|
| **Kapan** | Selama gameplay aktif | Setelah sesi berakhir |
| **Latensi** | <100ms kritis | Tidak kritis (detik-menit) |
| **Lokasi** | 100% browser (client-side) | Server-side |
| **Teknologi** | Kaplay.js, MediaPipe, TF.js | Express.js, SQLite, scikit-learn |
| **Data** | Image tensor, prediction, decision | Interaction logs, feature vectors |
| **Output** | Visual feedback, game outcome | Cluster labels, dashboard, insight |
| **API** | Tidak ada (semua lokal) | POST /api/log, GET /api/sessions, POST /api/analyze |
| **Penanggung jawab** | 🔵 Can + ⚪ Shared | 🟢 Dias + ⚪ Shared |

---

## 5. Perbandingan dengan Versi Lama

### Tabel Perubahan Utama

| No | Aspek | V1 (Lama) | V2 (Baru) | Alasan Perubahan |
|----|-------|-----------|-----------|------------------|
| 1 | **Diagram** | 1 diagram tapi tanpa Fase 0 (login) | **1 diagram + Fase 0 Autentikasi** | Login WAJIB (Bu Hesti: "Mending pakai login") |
| 2 | **Warna** | 🔵🟢 (2 warna) | **🔵🟢⚪ (3 warna + Shared)** | Business Logic layer perlu pewarnaan sendiri |
| 3 | **Login** | Session-only (tidak eksplisit di diagram) | **Login WAJIB + JWT + tabel users** | Perlu save history, progress, ~30 menit bermain |
| 4 | **Kategori Objek** | Solid / Danger / Decorative (3) | **Solid / Danger-Duri (2)** | Dekoratif dihapus (Bu Hesti: "kalau masih ragu mending jangan") |
| 5 | **Decision Shape** | Diamond ada tapi kurang jelas | **Diamond eksplisit di Fase 3 + Fase 4** | Gameplay progress feedback = decision (Bu Hesti) |
| 6 | **Arsitektur Layer** | Tidak dijelaskan secara eksplisit | **3 Layer: Presentation / Business Logic / Data & AI** | Dokumentasi arsitektur lebih komprehensif |
| 7 | **Data Flow** | Satu alur saja | **Real-Time vs Batch — dua jalur terpisah** | Perlu membedakan latency requirements dan lokasi proses |
| 8 | **Maskot** | "Feedback edukatif" ( ambigu) | **Bubble Teks saja, tanpa suara/NLP** | Bu Hesti: "Teks aja sih, kayak bubble gitulah" |
| 9 | **Objek Danger** | "Danger" (visual tidak dispesifik) | **Danger = Duri (thorns)** | Lebih soft dan aman untuk konteks anak SMP |
| 10 | **Tabel DB** | Disebut tapi tidak dijelaskan field-nya | **4 tabel + field detail** | Perlu spesifikasi untuk implementasi |
| 11 | **Retry Flow** | Tidak ada jalur retry eksplisit | **Decision: Ya→Next Level, Tidak→Retry Fase 2** | Bu Hesti: "Opsi di sini decision dong" |
| 12 | **Komponen Shared** | Tidak ada, semuanya Can atau Dias | **⚪ Shared layer: State, HITL Orchestrator, Session, Validation** | Arsitektur 3-layer lebih bersih |
| 13 | **Tutorial** | Tidak dispesifikasi | **General di L1, clue berkurang L2-3** | Bu Hesti: "Jangan mengguide step-by-step" |
| 14 | **Narasi Analisis** | Hanya angka (kuantitatif) | **Kuantitatif + Kualitatif auto-generate** | Bu Hesti: "Narasi harus auto generate, panggil API" |

### Apa yang Dihapus dari V1

| Dihapus | Alasan |
|---------|--------|
| Kategori "Decorative / Tembus Pandang" | Bu Hesti: kalau ragu fungsinya, jangan dimasukkan dulu |
| Label "from" (dari Can, dari Dias) | Bu Hesti: "Gak usah pakai kata from, langsung nama fasenya" |
| Emoji dekoratif (📷🎨🧠🎮💬🎭📥🔑💾📊📈📦) | Bu Hesti: hapus dekoratif, fokus HITL |
| Session-only auth | Bu Hesti: wajib login, harus ada history |
| Diagram terpisah per anggota | Bu Hesti: satu diagram besar, bedakan warna |

### Apa yang Ditambahkan di V2

| Ditambahkan | Alasan |
|-------------|--------|
| Fase 0: Autentikasi & Onboarding | Login WAJIB + tutorial general |
| ⚪ Shared layer (abu-abu) | Business logic perlu pewarnaan sendiri |
| Decision diamond di Fase 4 (Gameplay Progress) | Feedback = opsi = decision |
| Retry flow (Tidak → Fase 2 Redraw) | Siswa bisa mengulang jika gagal |
| Detail tabel SQLite (4 tabel + field) | Spesifikasi implementasi |
| Real-Time vs Batch data flow | Dua jalur berbeda secara fundamental |
| 3-Layer Architecture Detail | Dokumentasi arsitektur komprehensif |
| Narasi auto-generate (kualitatif) | Analisis tidak berhenti di angka |
| Maskot = Bubble Teks saja | Tanpa suara, tanpa NLP |
| Danger = Duri (thorns) | Visual lebih soft untuk anak SMP |

---

## 6. Komponen per Anggota

### 🔵 Can — Frontend / Interaksi / Gameplay / UI

| No | Komponen | Fase | Layer | Deskripsi |
|----|----------|------|-------|-----------|
| 1 | Login Screen | Fase 0 | Presentation | Form login email + password, tampilkan error |
| 2 | Onboarding Screen | Fase 0 | Presentation | Tutorial general, intro Momo (bubble teks) |
| 3 | MediaPipe Hand Tracking | Fase 1 | Presentation | Deteksi tangan + jari dari kamera, finger pointer |
| 4 | Drawing Canvas | Fase 1 | Presentation | Area gambar sketsa via finger pointer, clear/redraw |
| 5 | Kaplay.js Game Engine | Fase 1, 4 | Presentation | Engine game 2D — game loop, sprite, physics, collision, scene |
| 6 | Probe UI | Fase 3 | Presentation | Tampilkan prediksi AI, confidence score, minta keputusan siswa |
| 7 | Maskot Momo | Fase 3, 4 | Presentation | Agen pedagogis — bubble teks edukatif, sprite animation (idle/happy/sad/think) |
| 8 | Level Controller | Fase 4 | Presentation | Level 1-3 progres, aturan, rintangan, difficulty adaptif |
| 9 | Game Physics & Collision | Fase 4 | Presentation | Deteksi tabrakan objek solid/duri, success/fail/retry |
| 10 | Level Renderer | Fase 4 | Presentation | Render background, objek, karakter, obstacle, finish line |
| 11 | Animation System | Fase 4 | Presentation | Sprite animation, transisi level, efek visual |
| 12 | Score & Timer UI | Fase 4 | Presentation | Tampilkan skor, waktu, level saat ini |
| 13 | Event Packager | Fase 5 | Presentation | Membentuk interaction event JSON, kirim async via REST API |

### 🟢 Dias — Backend / AI / Data / Analisis

| No | Komponen | Fase | Layer | Deskripsi |
|----|----------|------|-------|-----------|
| 1 | Image Preprocessing | Fase 2 | Data & AI | Resize 28×28, konversi grayscale, normalisasi piksel [0,1] |
| 2 | CNN MobileNet | Fase 2 | Data & AI | Model klasifikasi sketsa — transfer learning, training offline |
| 3 | TensorFlow.js Runtime | Fase 2 | Data & AI | Runtime inference di browser — load model.json + predict |
| 4 | Confidence Score + Gap | Fase 2 | Data & AI | Kalkulasi confidence score + gap antar top prediksi |
| 5 | Model File Serving | Fase 2 | Data & AI | Serving aset statis model.json + weights.bin ke browser |
| 6 | REST API Server | Fase 5 | Data & AI | Express.js — 3 endpoint utama + payload validation |
| 7 | SQLite Database | Fase 5 | Data & AI | Penyimpanan 4 tabel: users, interaction_logs, sessions, cluster_results |
| 8 | JWT Authentication | Fase 5 | Data & AI | Autentikasi login WAJIB + verifikasi token tiap request |
| 9 | Feature Engineering | Fase 6 | Data & AI | Accept rate, override rate, avg decision time, danger accept, success rate |
| 10 | K-Means Clustering | Fase 6 | Data & AI | Pengelompokan pola keputusan siswa — scikit-learn, server-side |
| 11 | Dashboard Guru | Fase 6 | Data & AI | Visualisasi hasil analisis + cluster + export CSV/JSON |
| 12 | Narasi Auto-Generate | Fase 6 | Data & AI | Analisis kualitatif otomatis via AI API (Gemini) — penjelasan narasi dari matriks |

### ⚪ Shared — Business Logic / Orkestrasi

| No | Komponen | Fase | Layer | Deskripsi |
|----|----------|------|-------|-----------|
| 1 | Session Manager | Fase 0, 5 | Business Logic | Login WAJIB, JWT token management, history & progress tracking |
| 2 | State Manager | Semua | Business Logic | Game state (level, skor, waktu), reactive updates ke UI |
| 3 | HITL Orchestrator | Fase 3 | Business Logic | Koordinasi probe: trigger → tampilkan → tunggu decision → route result |
| 4 | Decision Resolver | Fase 3 | Business Logic | Tentukan final label dari keputusan siswa (Accept/Override) |
| 5 | Object Behavior Mapper | Fase 3 | Business Logic | Petakan final label ke kategori Solid / Danger (duri) |
| 6 | Validation Engine | Fase 3, 5 | Business Logic | Client-side input validation + server-side payload schema check |
| 7 | Difficulty Adapter | Fase 4 | Business Logic | Sesuaikan kesulitan level berdasarkan performa siswa |

### Dependency Matrix (Siapa Bergantung ke Siapa)

```
              Bergantung ke ──▶
  Bergantung     🔵 Can    ⚪ Shared   🟢 Dias
  dari           ───────   ─────────   ───────
  🔵 Can           —         ✅          ✅
  ⚪ Shared        ❌         —          ✅
  🟢 Dias          ❌         ❌          —

  Penjelasan:
  🔵 Can bergantung ke ⚪ Shared (state, HITL) dan 🟢 Dias (inference, API)
  ⚪ Shared bergantung ke 🟢 Dias (data schema, model output format)
  🟢 Dias TIDAK bergantung ke siapapun — layer paling independen
```

### Kontrak Data Antar Layer

**Layer 1 → Layer 2 (Can → Shared):**
```json
{
  "type": "sketch_submitted",
  "imageData": "<base64 canvas>",
  "level": 1,
  "timestamp": 1718544000000
}
```

**Layer 2 → Layer 3 (Shared → Dias):**
```json
{
  "type": "interaction_event",
  "userId": "uuid-string",
  "sessionId": "uuid-string",
  "level": 1,
  "sketchLabel": "pohon",
  "aiTop3": ["pohon", "bunga", "rumah"],
  "confidence": [0.72, 0.15, 0.08],
  "confidenceGap": 0.57,
  "decision": "accept",
  "finalLabel": "pohon",
  "category": "solid",
  "decisionTimeMs": 3400,
  "outcome": "success",
  "timestamp": 1718544000000
}
```

**Layer 3 → Layer 2 (Dias → Shared):**
```json
{
  "type": "prediction_result",
  "top3": ["pohon", "bunga", "rumah"],
  "confidence": [0.72, 0.15, 0.08],
  "confidenceGap": 0.57,
  "suggestedCategory": "solid"
}
```

---

## 7. Catatan Keputusan Desain

### Keputusan Arsitektur

| Keputusan | Pilihan | Alternatif yang Ditolak | Alasan |
|-----------|---------|------------------------|--------|
| Inference lokasi | Browser (TF.js) | Server-side API | Privasi data siswa, latensi rendah, offline-ready |
| Database | SQLite | PostgreSQL, MongoDB | Ringan, cukup untuk skala TA, mudah deploy |
| Game Engine | Kaplay.js | Phaser, vanilla Canvas | API sederhana, cocok untuk 2D side-scroller |
| Auth | JWT | Session cookie | Stateless, cocok untuk REST API |
| Clustering | K-Means (scikit-learn) | DBSCAN, Hierarchical | Sederhana, interpretable, cocok untuk pola keputusan |
| Maskot feedback | Bubble teks | Suara TTS, NLP chat | Bu Hesti: "Teks aja, kayak bubble gitulah" |
| Objek kategori | 2 (Solid, Danger) | 3 (+ Decorative) | Bu Hesti: "Kalau ragu mending jangan" |

### Keputusan dari Bimbingan Bu Hesti (16/6/26)

| No | Keputusan | Implementasi di V2 |
|----|-----------|---------------------|
| 1 | SATU diagram global, jangan split | Satu diagram IPO utuh dari START sampai END |
| 2 | Bedakan Can vs Dias pakai warna | 🔵🟢⚪ di setiap komponen |
| 3 | Format INPUT → PROSES → OUTPUT | Seluruh diagram mengikuti format IPO |
| 4 | Shape flowchart harus benar | Parallelogram=I/O, Rectangle=Proses, Diamond=Decision |
| 5 | Hapus kata "from" | Langsung nama fase/komponen tanpa "dari" |
| 6 | Login WAJIB | Fase 0 Autentikasi + JWT + tabel users |
| 7 | API endpoints spesifik | POST /api/log, GET /api/sessions, POST /api/analyze |
| 8 | Hapus dekoratif | Hanya 🔵🟢⚪, tanpa emoji dekoratif |
| 9 | Gameplay progress = decision | Diamond di Fase 4: Ya→Next, Tidak→Retry |
| 10 | Maskot = bubble teks | Tanpa suara, tanpa NLP |
| 11 | Danger = duri | Bukan pisau/senjata, lebih soft |
| 12 | 3 level saja | Level 1-3, tidak ditambah |
| 13 | Tutorial general | Jangan step-by-step, clue berkurang per level |

### Risiko & Mitigasi

| Risiko | Dampak | Mitigasi |
|--------|--------|----------|
| TF.js inference lambat di device lama | Gameplay tersendat | Target <100ms, fallback ke loading screen |
| MediaPipe tidak detect tangan | Input gesture gagal | Fallback ke mouse/touch input |
| K-Means hasil tidak bermakna | Analisis clustering kurang berguna | Elbow Method + silhouette score, K=2-5 |
| Siswa tidak memahami Probe UI | HITL tidak berjalan efektif | Tutorial general di Level 1, Momo bubble panduan |
| SQLite concurrent write | Data loss pada multi-user | WAL mode, write queue |
| Model CNN akurasi rendah | Prediksi tidak akurat, siswa selalu override | Fine-tuning, augmentasi dataset, confidence threshold |

---

*Dokumen Desain Sistem Global V2 ini disusun berdasarkan: (1) Desain Sistem V1, (2) Keputusan Bu Hesti dari bimbingan 16 Juni 2026, (3) Prinsip arsitektur hybrid browser-based inference + server-side active services. Seluruh keputusan mengikuti format INPUT → PROSES → OUTPUT, satu diagram global berwarna, shape flowchart standar ALPRO, tanpa label "from", tanpa elemen dekoratif.*
