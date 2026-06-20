# Desain Sistem — Simulasi Interaktif Literasi AI

> **Proyek:** Simulasi Interaktif Literasi AI untuk Siswa SMP Kelas 7-9
> **Arsitektur:** Hybrid — Browser-Based Inference (TF.js) + Server-Side Active Services (REST API, SQLite, K-Means)
> **Tim:** Can 🔵 (Frontend/Kaplay.js/MediaPipe/Maskot/Gameplay/UI) | Dias 🟢 (Backend/CNN/TensorFlow.js/API/DB/K-Means)
> **Format:** INPUT → PROSES → OUTPUT (satu diagram global, berwarna)

---

## Daftar Isi

1. [Diagram Global Baru (berwarna)](#1-diagram-global-baru-berwarna)
2. [Diagram Lama (perbandingan)](#2-diagram-lama-perbandingan)
3. [Tabel Perbandingan Lama vs Baru](#3-tabel-perbandingan-lama-vs-baru)
4. [Komponen per Anggota (Can=BIRU, Dias=HIJAU)](#4-komponen-per-anggota-canbiru-diashijau)

---

## 1. Diagram Global Baru (berwarna)

### Legenda

| Simbol | Bentuk | Fungsi |
|--------|--------|--------|
| 🔵 | Komponen Can (BIRU) | Frontend, Interaksi, Gameplay, UI |
| 🟢 | Komponen Dias (HIJAU) | AI, Backend, Data, Analisis |
| ▱▱▱ | Parallelogram | INPUT / OUTPUT |
| ┌───┐ | Rectangle | PROSES |
| ◇──◇ | Diamond | KEPUTUSAN (Decision) |

### Diagram Global IPO — Satu Diagram, Berwarna

```
╔══════════════════════════════════════════════════════════════════════════════════╗
║                          DESAIN SISTEM GLOBAL IPO                               ║
║            Simulasi Interaktif Literasi AI — Siswa SMP Kelas 7-9                ║
╚══════════════════════════════════════════════════════════════════════════════════╝

┌─────────────────────────────────────────────────────────────────────────────────┐
│  ▱▱▱  INPUT  ▱▱▱                                                               │
│                                                                                 │
│    ▱▱▱▱▱▱▱▱▱▱▱▱▱▱    ▱▱▱▱▱▱▱▱▱▱▱▱▱    ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱    ▱▱▱▱▱▱▱▱▱▱▱▱▱▱   │
│   ▱ Siswa SMP Kelas ▱  ▱ Gesture Tangan   ▱  ▱ Gambar Sketsa   ▱  ▱ Konteks Level  ▱  │
│   ▱    7, 8, 9       ▱  ▱ (Kamera/MediaPipe)▱  ▱ dari Canvas   ▱  ▱ Rintangan/Aturan▱  │
│    ▱▱▱▱▱▱▱▱▱▱▱▱▱▱    ▱▱▱▱▱▱▱▱▱▱▱▱▱    ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱    ▱▱▱▱▱▱▱▱▱▱▱▱▱▱   │
│         🔵 Can                🔵 Can              🔵 Can             🔵 Can       │
└──────────────────────────┬──────────────────────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│  PROSES — Fase 1: Input Interaksi 🔵                                           │
│                                                                                 │
│  ┌──────────────────┐   ┌──────────────────┐   ┌──────────────────────┐         │
│  │ 🔵 MediaPipe     │──▶│ 🔵 Drawing Canvas│──▶│ 🔵 Kaplay.js         │         │
│  │   Hand Tracking  │   │   (Input Sketsa) │   │   Game Engine        │         │
│  └──────────────────┘   └────────┬─────────┘   └──────────────────────┘         │
│                                  │                                               │
└──────────────────────────────────┼──────────────────────────────────────────────┘
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│  PROSES — Fase 2: Klasifikasi AI 🟢                                            │
│                                                                                 │
│  ┌──────────────────┐   ┌──────────────────┐   ┌──────────────────────┐         │
│  │ 🟢 Image         │──▶│ 🟢 CNN MobileNet │──▶│ 🟢 TensorFlow.js     │         │
│  │   Preprocessing  │   │   Inference       │   │   Top-3 + Confidence │         │
│  └──────────────────┘   └──────────────────┘   └──────────┬───────────┘         │
│                                                            │                    │
└────────────────────────────────────────────────────────────┼────────────────────┘
                                                             │
                                                             ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│  PROSES — Fase 3: HITL Probe & Keputusan 🔵🟢                                  │
│                                                                                 │
│  ┌──────────────────────┐                                                       │
│  │ 🔵 Probe UI          │◀── Confidence Score + Top-3 dari Fase 2              │
│  │   (Tampil Prediksi)  │                                                       │
│  └──────────┬───────────┘                                                       │
│             │                                                                   │
│             ▼                                                                   │
│       ◇──────────◇                                                              │
│      ◇ Keputusan  ◇     Siswa membaca prediksi AI, lalu memilih:               │
│       ◇  Siswa    ◇     Accept / Correct / Override                            │
│         ◇──────◇                                                                │
│             │                                                                   │
│        ┌────┴────┐                                                              │
│        ▼         ▼                                                              │
│   🔵 Accept   🔵 Override                                                      │
│   (Setuju)    (Koreksi Label)                                                   │
│        │         │                                                              │
│        └────┬────┘                                                              │
│             ▼                                                                   │
│  ┌──────────────────────┐   ┌──────────────────────┐                            │
│  │ 🔵 Decision Resolver │──▶│ 🔵 Object Behavior   │                            │
│  │   (Final Label)      │   │   Mapper              │                            │
│  └──────────────────────┘   │   Solid/Danger/Decor  │                            │
│                              └──────────────────────┘                            │
│             🔵 Can              🔵 Can                                            │
└─────────────────────────────────────────────────────────────────────────────────┘
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│  PROSES — Fase 4: Simulasi & Konsekuensi 🔵                                    │
│                                                                                 │
│  ┌──────────────────┐   ┌──────────────────┐   ┌──────────────────────┐         │
│  │ 🔵 Level         │──▶│ 🔵 Game Physics  │──▶│ 🔵 Maskot Momo       │         │
│  │   Controller     │   │   Collision      │   │   Feedback Edukatif  │         │
│  │   (Level 1-3)    │   │   Success/Fail   │   │   Refleksi Keputusan│         │
│  └──────────────────┘   └──────────────────┘   └──────────┬───────────┘         │
│                                                          │                     │
│                              🔵 Kaplay.js Engine         │                     │
└──────────────────────────────────────────────────────────┼──────────────────────┘
                                                           │
                                                           ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│  PROSES — Fase 5: Logging & Backend 🟢                                         │
│                                                                                 │
│  ┌──────────────────┐   ┌──────────────────────────────────────────────┐        │
│  │ 🔵 Event         │──▶│ 🟢 REST API                                  │        │
│  │   Packager       │   │                                              │        │
│  │   (Client-side)  │   │  ┌─────────────────────────────────────┐     │        │
│  └──────────────────┘   │  │ POST /api/log                       │     │        │
│                          │  │   → Simpan interaction event ke DB  │     │        │
│                          │  │                                     │     │        │
│                          │  │ GET /api/sessions                   │     │        │
│                          │  │   → Ambil data sesi untuk dashboard│     │        │
│                          │  │                                     │     │        │
│                          │  │ POST /api/analyze                   │     │        │
│                          │  │   → Trigger K-Means clustering      │     │        │
│                          │  └─────────────────────────────────────┘     │        │
│                          └──────────────────────┬───────────────────────┘        │
│                                                 │                               │
│                                                 ▼                               │
│                          ┌──────────────────────────────────────┐                │
│                          │ 🟢 SQLite Database                   │                │
│                          │   interaction_logs                    │                │
│                          │   sessions                            │                │
│                          │   cluster_results                     │                │
│                          └──────────────────────┬───────────────┘                │
│                                                 │                               │
└─────────────────────────────────────────────────┼───────────────────────────────┘
                                                  │
                                                  ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│  PROSES — Fase 6: Analisis & Dashboard 🟢                                      │
│                                                                                 │
│  ┌──────────────────┐   ┌──────────────────┐   ┌──────────────────────┐         │
│  │ 🟢 Feature       │──▶│ 🟢 K-Means       │──▶│ 🟢 Dashboard Guru    │         │
│  │   Engineering    │   │   Clustering     │   │   Visualisasi &      │         │
│  │   Accept rate    │   │   Pola Keputusan │   │   Export CSV/JSON    │         │
│  │   Override rate  │   │   Siswa SMP      │   │                      │         │
│  │   Avg dec. time  │   │                  │   │                      │         │
│  └──────────────────┘   └──────────────────┘   └──────────────────────┘         │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│  ▱▱▱  OUTPUT  ▱▱▱                                                               │
│                                                                                 │
│    ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱   ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱   ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱                 │
│   ▱ Prototype Simulasi ▱  ▱ Pengalaman HITL  ▱  ▱ Dataset Log Interaksi ▱      │
│   ▱ Interaktif Berlevel▱  ▱ Evaluasi AI      ▱  ▱ Terstruktur (SQLite)  ▱      │
│    ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱   ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱   ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱                 │
│         🔵 Can               🔵 Can                🟢 Dias                      │
│                                                                                 │
│    ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱   ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱   ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱                 │
│   ▱ Analisis Pola      ▱  ▱ Dashboard Guru   ▱  ▱ Model TF.js + Confidence▱    │
│   ▱ Keputusan Siswa    ▱  ▱ + Export Data    ▱  ▱ Score (Client-side)     ▱    │
│    ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱   ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱   ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱                 │
│         🟢 Dias               🟢 Dias                🟢 Dias                     │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

### Alur Data Ringkas

```
    Gambar Sketsa          AI Inference           HITL Probe           Logging           Analisis
    🔵 Can                 🟢 Dias                🔵 Can               🟢 Dias           🟢 Dias
  ────────────── ──▶ ──────────────── ──▶ ──────────────── ──▶ ──────────────── ──▶ ────────────────
  Canvas + Gesture    CNN MobileNet +      Probe UI +           POST /api/log +     K-Means +
  MediaPipe           TF.js + Top-3 +      Decision +           GET /api/sessions +  Feature Eng. +
                      Confidence Score      Object Behavior      POST /api/analyze    Dashboard
```

### Penjelasan Fase per Fase

**Fase 1 — Input Interaksi (🔵 Can):** Siswa memasuki simulasi via MediaPipe hand tracking dan menggambar sketsa di canvas. Kaplay.js sebagai game engine mengelola seluruh siklus interaksi di browser.

**Fase 2 — Klasifikasi AI (🟢 Dias):** Gambar dari canvas dipreprocess (resize 28×28, grayscale), lalu diklasifikasikan oleh CNN MobileNet via TensorFlow.js. Inference berjalan sepenuhnya di browser (client-side) — model diload dari aset statis server, tapi prediksi tidak memerlukan round-trip ke server. Output: Top-3 prediction + confidence score + confidence gap.

**Fase 3 — HITL Probe & Keputusan (🔵🟢):** Titik temu Can dan Dias. Probe UI menampilkan prediksi AI (dari Dias) ke siswa (diimplementasi oleh Can). Siswa membaca confidence score, memutuskan: Accept (setuju), Correct (koreksi ke prediksi lain), atau Override (ganti label). Decision resolver menentukan final label, lalu dipetakan ke behavior objek (Solid / Danger / Decorative).

**Fase 4 — Simulasi & Konsekuensi (🔵 Can):** Final label menjadi objek di game. Level controller mengatur progres Level 1-3. Physics engine menghasilkan collision dan outcome (success / fail / retry). Momo memberikan feedback edukatif yang merefleksikan keputusan siswa.

**Fase 5 — Logging & Backend (🟢 Dias):** Event packager di client membentuk interaction event, dikirim asinkron via REST API. Tiga endpoint utama:
- `POST /api/log` — simpan interaction event ke SQLite
- `GET /api/sessions` — ambil data sesi untuk dashboard
- `POST /api/analyze` — trigger proses K-Means clustering

**Fase 6 — Analisis & Dashboard (🟢 Dias):** Feature engineering menghasilkan fitur (accept rate, override rate, avg decision time, danger acceptance, success rate). K-Means clustering mengelompokkan pola keputusan siswa. Dashboard guru memvisualisasikan hasil dan menyediakan export CSV/JSON.

---

## 2. Diagram Lama (perbandingan)

Berikut adalah desain sistem versi sebelumnya (dari sesi riset terdahulu). Versi lama memiliki kelemahan: terpecah menjadi beberapa diagram kecil, tidak ada pewarnaan per anggota, mengandung elemen dekoratif, hanya berbasis session (tanpa login), dan endpoint API tidak dispesifikasikan.

### Diagram Lama — Arsitektur Global (Tanpa Warna)

```
┌─────────────────────────────────────────────────────────────────┐
│  CLIENT (Browser)                                               │
│                                                                 │
│  📱 MediaPipe Hand Tracking                                     │
│  🎨 Canvas Drawing Input                                        │
│  🧠 TensorFlow.js CNN MobileNet Inference                       │
│  🎮 Kaplay.js Game Engine + Physics                             │
│  💬 Probe UI HITL Decision Interface                            │
│  🎭 Momo Pedagogical Agent                                      │
│                                                                 │
└──────────────────────────┬──────────────────────────────────────┘
                           │
              JSON log (async)
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│  SERVER (Backend Services)                                      │
│                                                                 │
│  📥 REST API   (endpoint tidak dispesifikasi)                   │
│  🔑 JWT Auth   (dashboard guru)                                 │
│  💾 SQLite Database                                             │
│  📊 K-Means Clustering Analysis                                 │
│  📈 Dashboard Visualisasi & Export                              │
│  📦 Model File Serving (statis)                                 │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Diagram Lama — IPO Global (Terpecah, Tanpa Warna)

```
INPUT                    PROSES                              OUTPUT
──────                   ──────                              ──────

Siswa SMP         Interactive Simulation Layer         Prototype sistem
Gesture tangan    ┌─ Onboarding & tutorial             literasi AI
Gambar sketsa     ├─ Finger tracking MediaPipe          Pengalaman HITL
Keputusan user    ├─ Drawing canvas                     Objek game
Konteks level     ├─ Probe UI                           Dataset log
                  └─ Gameplay 2D

                  AI Classification Layer
                  ┌─ Image preprocessing
                  ├─ CNN MobileNet TF.js
                  ├─ Top-3 prediction
                  └─ Confidence score

                  Decision & Consequence Layer
                  ┌─ Final label resolver
                  ├─ Object behavior mapper
                  └─ Gameplay outcome

                  Data & Analysis Layer
                  ┌─ Interaction logging
                  ├─ REST API → Database
                  ├─ Feature engineering
                  ├─ K-Means clustering
                  └─ Dashboard / export
```

### Diagram Lama — Scope Can (Terpisah)

```
INPUT (Scope Can)          PROSES (Scope Can)               OUTPUT (Scope Can)
──────────────             ─────────────────                ─────────────────

Siswa SMP            Interaction Entry                Playable prototype
Kamera/webcam        ┌─ Onboarding screen             Alur HITL di Probe UI
Gerakan tangan       ├─ Momo introduction             Objek game final
Gambar sketsa        └─ Tutorial aturan               Feedback Momo
Hasil prediksi Dias                                     Interaction event
Keputusan user       Finger Tracking & Drawing
                     ┌─ MediaPipe detection
                     ├─ Finger pointer mapping
                     ├─ Deadzone/stabilisasi
                     ├─ Drawing canvas
                     └─ Clear/redraw control

                     HITL Interface
                     ┌─ Probe UI muncul
                     ├─ Momo reaction
                     ├─ Prediction panel
                     └─ Decision button

                     Decision to Gameplay
                     ┌─ Final label resolver
                     ├─ Object behavior mapper
                     └─ Spawn object ke world

                     2D Gameplay Simulation
                     ┌─ Level manager
                     ├─ Stickman control
                     ├─ Collision detection
                     ├─ Success/fail/retry
                     └─ Momo feedback

                     Event Packaging
                     ┌─ Membentuk interaction event
                     └─ Mengirim via REST API
```

### Diagram Lama — Scope Dias (Terpisah)

```
INPUT (Scope Dias)          PROSES (Scope Dias)               OUTPUT (Scope Dias)
───────────────             ──────────────────                ──────────────────

Dataset sketsa        Dataset & Model Preparation       Model TF.js
Daftar kelas objek    ┌─ Seleksi kelas dataset          Top-3 + confidence
Mapping kategori      ├─ Data cleaning                  Structured log
Canvas image (Can)    ├─ Resize/grayscale/normalisasi   Fitur analisis
Interaction event     └─ Train-test split               Cluster pola
                      AI Model Development              Dashboard/CSV/JSON
                      ┌─ Training CNN MobileNet
                      ├─ Model evaluation
                      ├─ Optimization
                      └─ Export TF.js

                      Runtime Inference Contract
                      ┌─ Load model.json + weights
                      ├─ Runtime preprocessing
                      ├─ Predict sketch class
                      ├─ Generate Top-3
                      └─ Calculate confidence

                      Data Contract to Can
                      ┌─ Prediction response format
                      ├─ Label map
                      └─ Category map

                      Backend Services
                      ┌─ REST API (endpoint tidak spesifik)
                      ├─ Payload validation
                      ├─ SQLite storage
                      ├─ Session grouping
                      └─ JWT auth

                      Analysis Pipeline
                      ┌─ Data cleaning log
                      ├─ Feature engineering
                      ├─ Descriptive statistics
                      ├─ K-Means clustering
                      └─ Cluster interpretation
```

### Masalah Diagram Lama

1. **Terpecah-pecah** — Desain lama memisahkan menjadi 4+ diagram kecil (Global, Scope Can, Scope Dias, Data Flow). Pembaca harus melompat-lompat untuk memahami sistem utuh.
2. **Tidak berwarna** — Tidak ada pewarnaan per anggota tim, sehingga sulit membedakan kontribusi Can vs Dias.
3. **Elemen dekoratif** — Menggunakan emoji dekoratif (📷🎨🧠🎮💬🎭📥🔑💾📊📈📦) yang menambah noise visual tanpa informasi.
4. **Session-only** — Hanya menyebut session-based grouping, tidak ada mekanisme login/auth yang eksplisit di diagram.
5. **Endpoint API tidak spesifik** — Hanya menyebut "REST API" tanpa menuliskan endpoint konkret (POST /api/log, GET /api/sessions, POST /api/analyze).
6. **"from" labels** — Menggunakan label seperti "dari Can", "dari Dias" yang membuat diagram terasa seperti diagram terpisah, bukan satu sistem utuh.
7. **Tidak ada fase bernomor** — Alur tidak dikelompokkan dalam fase berurutan (Fase 1-6).

---

## 3. Tabel Perbandingan Lama vs Baru

| Aspek | Desain Lama | Desain Baru |
|-------|-------------|-------------|
| **Jumlah diagram** | 4+ diagram terpisah (Global, Can, Dias, Data Flow) | **1 diagram global utuh** |
| **Pewarnaan tim** | Tidak ada — semua hitam-putih | 🔵 BIRU (Can) + 🟢 HIJAU (Dias) |
| **Format** | Beberapa sub-diagram IPO terpisah | SATU diagram IPO global + detail per fase |
| **Fase berurutan** | Tidak ada penomoran fase | Fase 1-6, berurutan |
| **Bentuk flowchart** | Tidak konsisten — semua rectangle | Parallelogram (I/O), Rectangle (Proses), Diamond (Decision) |
| **Label "from"** | Menggunakan "dari Can", "dari Dias" | Langsung menamai komponen tanpa "from" |
| **Endpoint API** | Hanya "REST API" generik | `POST /api/log`, `GET /api/sessions`, `POST /api/analyze` |
| **Keputusan (Decision)** | Tidak ada diamond shape | Diamond shape untuk keputusan siswa |
| **Elemen dekoratif** | Emoji dekoratif berlebihan | Ikon warna saja (🔵🟢), tanpa dekorasi |
| **Auth / Login** | Session-only, tidak eksplisit | JWT Auth eksplisit di Fase 5 |
| **Alur data** | Tersembunyi di diagram terpisah | Terlihat jelas: drawing → inference → confidence → HITL → decision → log → K-Means |
| **Keterbacaan** | Perlu melompat antar diagram untuk konteks | Satu diagram = satu pandangan utuh |
| **Kesesuaian permintaan Bu Hesti** | Tidak memenuhi (terpecah, tidak berwarna) | Memenuhi semua kriteria |

---

## 4. Komponen per Anggota (Can=BIRU, Dias=HIJAU)

### 🔵 Can — Frontend / Interaksi / Gameplay / UI

| No | Komponen | Fase | Deskripsi |
|----|----------|------|-----------|
| 1 | MediaPipe Hand Tracking | Fase 1 | Deteksi tangan dan jari dari kamera untuk gesture input |
| 2 | Drawing Canvas | Fase 1 | Area gambar sketsa menggunakan finger pointer |
| 3 | Kaplay.js Game Engine | Fase 1, 4 | Engine game 2D — physics, collision, sprite, animasi |
| 4 | Probe UI | Fase 3 | Interface HITL — tampilkan prediksi AI, minta keputusan siswa |
| 5 | Decision Resolver | Fase 3 | Menentukan final label berdasarkan keputusan siswa |
| 6 | Object Behavior Mapper | Fase 3 | Memetakan final label ke Solid / Danger / Decorative |
| 7 | Maskot Momo | Fase 4 | Agen pedagogis — memberi feedback edukatif dan refleksi |
| 8 | Level Controller | Fase 4 | Mengatur progres Level 1-3, aturan, dan rintangan |
| 9 | Game Physics & Collision | Fase 4 | Deteksi tabrakan, success/fail/retry |
| 10 | Animation System | Fase 4 | Sprite animation, transisi, efek visual |
| 11 | Event Packager | Fase 5 | Membentuk interaction event dan mengirim via REST API (async) |
| 12 | Frontend (Browser UI) | Semua | Keseluruhan antarmuka pengguna di browser |

### 🟢 Dias — Backend / AI / Data / Analisis

| No | Komponen | Fase | Deskripsi |
|----|----------|------|-----------|
| 1 | Image Preprocessing | Fase 2 | Resize 28×28, konversi grayscale, normalisasi piksel |
| 2 | CNN MobileNet | Fase 2 | Model klasifikasi sketsa — training di campus server/Colab |
| 3 | TensorFlow.js Inference | Fase 2 | Runtime inference di browser — load model + predict |
| 4 | Confidence Score + Gap | Fase 2 | Kalkulasi skor kepercayaan dan gap antar prediksi |
| 5 | REST API | Fase 5 | `POST /api/log`, `GET /api/sessions`, `POST /api/analyze` |
| 6 | SQLite Database | Fase 5 | Penyimpanan interaction_logs, sessions, cluster_results |
| 7 | JWT Authentication | Fase 5 | Autentikasi akses dashboard guru |
| 8 | Feature Engineering | Fase 6 | Accept rate, override rate, avg decision time, danger acceptance |
| 9 | K-Means Clustering | Fase 6 | Pengelompokan pola keputusan siswa (scikit-learn, server-side) |
| 10 | Dashboard Guru | Fase 6 | Visualisasi hasil analisis + export CSV/JSON |
| 11 | Model File Serving | Fase 2 | Serving aset statis model.json + weights ke browser |

### Titik Temu Can ↔ Dias

```
    🔵 Can (Fase 1)              🟢 Dias (Fase 2)              🔵 Can (Fase 3)
    ┌──────────────┐            ┌──────────────┐            ┌──────────────┐
    │ Drawing      │──Canvas──▶ │ CNN MobileNet│──Top-3 +──▶│ Probe UI     │
    │ Canvas       │   Image    │ + TF.js      │  Conf.     │ + Decision   │
    └──────────────┘            └──────────────┘            └──────┬───────┘
                                                              │
                                                              │ Interaction
                                                              │ Event
                                                              ▼
                                                         🟢 Dias (Fase 5)
                                                         ┌──────────────┐
                                                         │ REST API     │
                                                         │ + SQLite     │
                                                         └──────┬───────┘
                                                                │
                                                                ▼
                                                         🟢 Dias (Fase 6)
                                                         ┌──────────────┐
                                                         │ K-Means +    │
                                                         │ Dashboard    │
                                                         └──────────────┘
```

> **Prinsip arsitektur:** Inferensi AI berjalan di browser siswa (client-side) untuk privasi data dan latensi rendah. Server tidak dipakai untuk menebak gambar — server menyediakan layanan pendukung: penyimpanan log, autentikasi, analisis clustering, dan dashboard guru.

---

*Diagram ini dirancang sesuai permintaan Bu Hesti: satu diagram global berwarna, format INPUT → PROSES → OUTPUT, tanpa label "from", dengan bentuk flowchart yang konsisten.*
