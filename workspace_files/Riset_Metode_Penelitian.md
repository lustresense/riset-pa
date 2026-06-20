# Riset Mendalam: Metode Penelitian untuk Proposal TA
## Project: "Escape the Sketchbook" — HITL AI Literacy Simulation

> **Dibuat:** 2026-06-15  
> **Status:** Living Document — update kalau ada perubahan dari diskusi/dosen  
> **Konteks:** Can (D4 TRM PENS) butuh riset metode penelitian karena proposal belum ada bagian metode, dan Bu Hesti menyarankan fishbone

---

## DAFTAR ISI

1. [Hierarki Metode Penelitian — Dari Umum ke Spesifik](#1-hierarki-metode-penelitian)
2. [Kuantitatif vs Kualitatif vs Mixed — Rinci Lengkap](#2-kuantitatif-vs-kualitatif-vs-mixed)
3. [Fishbone/Ishikawa — Apa Itu, Kategori Apa, dan Bagaimana Dipakai di Proposal](#3-fishboneishikawa)
4. [Metode Pengembangan Perangkat Lunak (SDLC)](#4-metode-pengembangan-perangkat-lunak-sdlc)
5. [Metode Pengujian — Usability, SUS, Black-Box](#5-metode-pengujian)
6. [Komparasi & Rekomendasi untuk Project Ini](#6-komparasi--rekomendasi)
7. [Contoh Penerapan di Proposal](#7-contoh-penerapan-di-proposal)
8. [Daftar Referensi Akademik](#8-daftar-referensi-akademik)

---

## 1. Hierarki Metode Penelitian

Banyak yang bingung soal "metode penelitian" karena istilahnya overlapping. Ini hierarkinya dari atas ke bawah:

```
PENELITIAN (Research)
│
├── 1. PENDEKATAN (Approach / Paradigma)
│   ├── Kuantitatif
│   ├── Kualitatif
│   └── Mixed Methods
│
├── 2. JENIS/METODE (Type / Method)
│   ├── Deskriptif
│   ├── Eksperimen (True, Quasi, Pre-experimental)
│   ├── R&D (Research & Development)
│   ├── Studi Kasus (Case Study)
│   ├── Action Research
│   ├── Evaluatif
│   ├── Korelasional
│   └── Etnografi
│
├── 3. DESAIN PENELITIAN (Research Design)
│   ├── One-Group Pretest-Posttest
│   ├── Pretest-Posttest Control Group
│   ├── Solomon Four-Group
│   ├── Factorial
│   ├── Repeated Measures
│   ├── Cross-Sectional
│   └── Longitudinal
│
├── 4. METODE PENGEMBANGAN (Development Method / SDLC)
│   ├── Waterfall
│   ├── Prototype
│   ├── Iterative/Incremental
│   ├── Spiral
│   ├── Agile (Scrum, Kanban, XP)
│   ├── RAD (Rapid Application Development)
│   └── MDLC (Multimedia Development Life Cycle)
│
├── 5. TEKNIK PENGUMPULAN DATA
│   ├── Kuesioner/Survey
│   ├── Observasi
│   ├── Wawancara
│   ├── Tes/Pretest-Posttest
│   ├── Dokumentasi
│   └── Log Data (Instrumentasi Sistem)
│
├── 6. TEKNIK ANALISIS DATA
│   ├── Statistik Deskriptif
│   ├── Statistik Inferensial (t-test, ANOVA, dll)
│   ├── Analisis Kualitatif (Thematic, Content Analysis)
│   ├── Fishbone / Ishikawa Diagram
│   ├── Pareto Analysis
│   ├── Root Cause Analysis (5 Whys)
│   └── K-Means Clustering
│
└── 7. METODE PENGUJIAN (Testing Method)
    ├── Black-Box Testing
    ├── Usability Testing (SUS, UMUX, SUMI)
    ├── White-Box Testing
    ├── Alpha/Beta Testing
    └── A/B Testing
```

**PENTING:** Fishbone itu masuk di **Level 6 — Teknik Analisis Data**, BUKAN di Level 2 (Jenis/Metode) atau Level 1 (Pendekatan). Fishbone itu ALAT ANALISIS, bukan metode penelitian itu sendiri.

---

## 2. Kuantitatif vs Kualitatif vs Mixed

### 2.1 Kuantitatif

**Definisi:** Penelitian yang berdasarkan data angka, statistik, dan pengukuran objektif. Menguji hipotesis dengan data numerik.

**Ciri-ciri:**
- Data berupa angka/numerik
- Menggunakan statistik (deskriptif & inferensial)
- Sampel besar (idealnya >30 per kelompok)
- Hasil bisa digeneralisasi
- Variabel terukur dan terkontrol
- Menggunakan instrumen terstandar (kuesioner, tes)

**Jenis penelitian kuantitatif:**
| Jenis | Tujuan | Contoh di Project Ini |
|---|---|---|
| **Deskriptif** | Menggambarkan fenomena secara numerik | Mengukur rata-rata skor SUS usability |
| **Korelasional** | Mencari hubungan antar variabel | Hubungan confidence score dengan keputusan override |
| **Eksperimen** | Menguji pengaruh treatment | Membandingkan pretest vs posttest AI literacy |
| **Quasi-Eksperimen** | Eksperimen tanpa randomisasi penuh | One-group pretest-posttest AI literacy siswa SMP |
| **Survei** | Mengumpulkan data dari sampel besar | Survei persepsi siswa terhadap AI |

**Kelebihan:**
- Objektif dan terukur
- Bisa di-generalisasi kalau sampel cukup
- Hasil jelas (angka, signifikansi)
- Dosen & reviewer mudah terima

**Kelemahan:**
- Nggak bisa capture konteks mendalam
- Butuh sampel besar
- Butuh instrumen yang valid & reliable
- Kurang fleksibel — protocol sudah ditentukan sejak awal

---

### 2.2 Kualitatif

**Definisi:** Penelitian yang berbasis deskripsi, interpretasi, dan pemahaman mendalam. Fokus pada "mengapa" dan "bagaimana", bukan "berapa".

**Ciri-ciri:**
- Data berupa teks, gambar, observasi, wawancara
- Tidak menggunakan statistik inferensial
- Sampel kecil (bisa 5-15 orang)
- Temuan tidak digeneralisasi
- Fleksibel — bisa berubah selama penelitian
- Coding tematik / content analysis

**Jenis penelitian kualitatif:**
| Jenis | Tujuan | Contoh di Project Ini |
|---|---|---|
| **Studi Kasus** | Memahami kasus spesifik secara mendalam | Studi kasus interaksi 5 siswa dengan Probe UI |
| **Fenomenologi** | Memahami pengalaman subjektif | Pengalaman siswa saat AI salah klasifikasi |
| **Etnografi** | Memahami budaya/komunitas | Observasi bagaimana siswa berinteraksi dalam simulasi |
| **Grounded Theory** | Membangun teori dari data | Membangun model perilaku HITL dari data log |
| **Narrative Research** | Menganalisis narasi/cerita | Cerita siswa tentang pengalaman mereka dengan AI |

**Kelebihan:**
- Mendalam — bisa capture nuance & konteks
- Fleksibel
- Cocok untuk eksplorasi topik baru
- Tidak butuh sampel besar

**Kelemahan:**
- Subjektif — bias peneliti bisa masuk
- Tidak bisa digeneralisasi
- Sulit dipertanggungjawabkan secara statistik
- Reviewer kadang meragukan validitasnya

---

### 2.3 Mixed Methods (Metode Campuran)

**Definisi:** Pendekatan yang menggabungkan kuantitatif DAN kualitatif dalam satu studi untuk mendapatkan pemahaman yang lebih lengkap.

**Tipe desain mixed methods:**
| Tipe | Penjelasan | Kapan Dipakai |
|---|---|---|
| **Convergent Parallel** | Kuan & Kual dikumpulkan bersamaan, lalu dibandingkan | Kalau mau cross-validate temuan |
| **Explanatory Sequential** | Kuan dulu → hasilnya dijelaskan dengan Kual | Kalau mau tau "mengapa" angka menunjukkan X |
| **Exploratory Sequential** | Kual dulu → temuan diuji dengan Kuan | Kalau belum tau variabel apa yang penting |
| **Embedded/Nested** | Satu metode dominan, yang lain sebagai pelengkap | Kalau satu metode lebih penting |

**Contoh penerapan di project ini:**
1. **Kuantitatif**: SUS skor usability + pretest-posttest AI literacy + confidence score statistics
2. **Kualitatif**: Wawancara post-play tentang pengalaman HITL + observasi think-aloud saat Probe UI muncul

**Kelebihan:**
- Paling lengkap — angka + konteks
- Cross-validation antar metode
- Reviewer & dosen suka kelengkapan ini

**Kelemahan:**
- Lebih banyak kerja
- Butuh expertise di dua metode
- Waktu lebih lama

---

## 3. Fishbone/Ishikawa

### 3.1 Apa Itu Fishbone Diagram?

Fishbone Diagram (juga disebut **Ishikawa Diagram**, **Cause-and-Effect Diagram**, atau **Diagram Tulang Ikan**) adalah **alat analisis visual** yang digunakan untuk mengidentifikasi, mengorganisir, dan menganalisis **akar penyebab (root cause)** dari suatu masalah.

**Dikembangkan oleh:** Kaoru Ishikawa (1950-an), sebagai bagian dari **Total Quality Management (TQM)** dan **Seven Basic Quality Tools**.

**Bentuknya:** Seperti tulang ikan —
- **Kepala** (kanan) = Masalah/Effect yang ingin dianalisis
- **Tulang utama** (horizontal) = Garis utama sebab-akibat
- **Tulang cabang** = Kategori penyebab

### 3.2 Kategori 6M (Standar Ishikawa)

| Kategori | Penjelasan | Contoh di Project Ini |
|---|---|---|
| **Man** (Manusia) | Faktor manusia/sdm | Siswa SMP belum familiar dengan konsep AI error |
| **Machine** (Mesin) | Faktor peralatan/teknologi | CNN MobileNet memiliki akurasi terbatas untuk sketsa |
| **Method** (Metode) | Faktor prosedur/cara | Mekanisme HITL perlu dirancang agar tidak mengganggu flow |
| **Material** (Material) | Faktor bahan/data | Dataset Quick Draw memiliki bias budaya (Western-centric) |
| **Measurement** (Pengukuran) | Faktor cara mengukur | Confidence score tidak selalu merepresentasikan "kebenaran" |
| **Environment** (Lingkungan) | Faktor kondisi sekitar | Koneksi internet tidak stabil di sekolah Indonesia |

**Variasi:** Ada juga 5M+1E (Man, Machine, Method, Material, Measurement + Environment), 4M, 8P (People, Process, Place, dll), dll — tergantung konteks.

### 3.3 Fishbone Masuk Kategori Apa?

**INI YANG SERING BINGUNG — JAWABANNYA:**

```
Fishbone Diagram = TEKNIK ANALISIS DATA
                  ≠ METODE PENELITIAN (Level 2)
                  ≠ PENDEKATAN PENELITIAN (Level 1)
```

**Fishbone itu BUKAN:**
- Bukan metode penelitian kuantitatif
- Bukan metode penelitian kualitatif
- Bukan metode penelitian itu sendiri

**Fishbone itu:**
- Alat/teknik analisis di DALAM suatu metode penelitian
- Biasanya dipakai di DALAM penelitian **deskriptif kualitatif**
- Atau sebagai bagian dari analisis di penelitian **R&D**
- Termasuk ke dalam **Seven Basic Quality Tools** (alat manajemen kualitas)

**Jadi kalau dosen bilang "pake fishbone", yang dimaksud:**
> "Gunakan fishbone diagram sebagai **teknik analisis** untuk mengidentifikasi dan menganalisis akar penyebab masalah, dan masukkan itu ke dalam metodologi penelitianmu."

**Bukan:** "Metode penelitianmu adalah fishbone."

### 3.4 Fishbone dalam Konteks Proposal TA

Di proposal TA, fishbone biasanya muncul di:

1. **Bab 1 — Latar Belakang/Pembatasan Masalah** → Fishbone dipakai untuk mengidentifikasi akar masalah yang mendasari kenapa project ini perlu dibuat
2. **Bab 3 — Metodologi Penelitian** → Fishbone dipakai sebagai teknik analisis masalah, di dalam subsection analisis data

**Struktur yang benar di proposal:**

```
3.x Metode Penelitian
    Jenis Penelitian: Deskriptif Kualitatif / R&D / dll
    ↓
3.x.1 Teknik Analisis Data
    - Fishbone Diagram (Ishikawa) untuk identifikasi root cause masalah
    - [teknik lain: statistik deskriptif, K-Means, dll]
```

### 3.5 Contoh Fishbone untuk "Escape the Sketchbook"

```
                        FISHBONE: Siswa SMP Tidak Memahami Keterbatasan AI
                        ═══════════════════════════════════════════════════

Man (Manusia)          Method (Metode)           Machine (Mesin)
├─ Siswa tidak         ├─ Pembelajaran AI        ├─ AI terlihat "magis"
│  tahu cara AI        │  di SMP minim           │  tanpa penjelasan
├─ Guru tidak          ├─ Tidak ada simulasi     ├─ Black-box AI tidak
│  familiar AI         │  interaktif AI           │  terlihat prosesnya
└─ Persepsi AI         ├─ Kurikulum belum        └─ Confidence score
   selalu benar           cover AI literacy         tidak ditampilkan
      │                      │                          │
      │                      │                          │
      ┼──────────────────────┼──────────────────────────┼─────►
      │                      │                          │     MASALAH:
      │                      │                          │     Siswa SMP tidak
Material (Material)   Measurement (Ukur)       Environment (Lingk)  memahami
├─ Dataset AI          ├─ Tidak ada              ├─ Akses teknologi    keterbatasan
│  Western-centric     │  ukuran AI literacy     │  terbatas di        AI
├─ Konten edukasi      ├─ Assessment             │  sekolah Indonesia
│  AI untuk SMP        │  hanya teori             ├─ Infrastruktur
│  belum ada           ├─ Belum ada cara          │  internet tidak
└─ Bahasa              │  ukur interaksi          │  stabil
   konten Inggris      │  manusia-AI              └─ Device siswa
                                                          terbatas
```

### 3.6 Kenapa Fishbone Enak untuk Proposal Ini?

1. **Mengidentifikasi masalah secara visual** — Bu Hesti bisa langsung lihat kenapa project ini perlu
2. **Systematic** — 6M framework memastikan semua aspek tercover
3. **Bisa dijadikan "bridge"** antara Bab 1 (masalah) dan Bab 3 (solusi)
4. **Sering dipakai di TA** — Dosen familiar, banyak referensi
5. **Simple tapi powerful** — Nggak butuh statistik rumit
6. **Cocok untuk problem-driven project** — Project ini lahir dari masalah nyata

---

## 4. Metode Pengembangan Perangkat Lunak (SDLC)

Ini **BEDA** dengan metode penelitian. SDLC itu metode untuk **mengembangkan produk**, bukan metode untuk **meneliti**. Tapi di TA/D4 TRM, keduanya biasanya digabung.

### 4.1 Model SDLC yang Umum Dipakai di TA

| Model | Prinsip | Kelebihan | Kelemahan | Cocok untuk |
|---|---|---|---|---|
| **Waterfall** | Sequential, linear | Terstruktur, dokumentasi lengkap, mudah dijelaskan di proposal | Rigid, sulit adaptasi perubahan | Project dengan requirement jelas dari awal |
| **Prototype** | Bikin prototype dulu, iterasi berdasarkan feedback | Cepat dapat feedback user, cocok untuk UI/UX | Scope bisa melebar, dokumentasi kurang | Project yang butuh validasi user dini |
| **Iterative/Incremental** | Bangun per modul, tiap modul dikembangkan lengkap | Risiko rendah per iterasi | Butuh planning baik | Project modular |
| **Spiral** | Iteratif + risk analysis di tiap loop | Sangat risk-aware, cocok untuk project besar | Kompleks, butuh expertise risk analysis | Project high-risk |
| **Agile** | Iteratif, adaptive, sprint-based | Fleksibel, cepat adaptasi | Dokumentasi minim, scope bisa berubah | Project dinamis |
| **RAD** | Rapid prototyping, component reuse | Cepat | Butuh skill tinggi, kurang kontrol | Project simple & cepat |
| **MDLC** | Khusus multimedia: Konsep→Material→Desain→Pembuatan→Testing→Distribusi | Spesifik untuk multimedia | Kurang dikenal di luar multimedia | Project multimedia/game |

### 4.2 Mana yang Cocok untuk "Escape the Sketchbook"?

**Rekomendasi: Waterfall + Prototype (Hybrid)**

Alasan:
- **Waterfall** sebagai kerangka utama — karena requirement sudah jelas (3 level, HITL mechanism, Probe UI, data log)
- **Prototype** di tahap desain — karena butuh validasi UI/UX dengan user sebelum full development
- Ini kombinasi yang paling sering dipakai di TA D4 TRM PENS

**Alternatif: MDLC (Multimedia Development Life Cycle)**

MDLC punya 6 tahap:
1. **Concept** — Definisi konsep, requirement, target user
2. **Design** — Desain UI, flow, level, mekanisme
3. **Material Collecting** — Pengumpulan asset (gambar, suara, dataset)
4. **Assembly/Manufacturing** — Pembuatan/programming
5. **Testing** — Pengujian (black-box, usability)
6. **Distribution** — Deployment

MDLC cocok karena project ini memang multimedia (game 2D interaktif). Tapi MDLC kurang dikenal dibanding Waterfall, jadi perlu dijelaskan lebih detail di proposal.

### 4.3 Contoh di TRM PENS

Dari website TRM PENS:
> "Pengembangan sistem menggunakan metode Software Development Life Cycle (SDLC) model Waterfall, sedangkan pengujiannya dilakukan dengan metode black box."

Ini pola yang paling umum di TRM PENS.

---

## 5. Metode Pengujian

### 5.1 Usability Testing

**Apa itu?** Pengujian untuk mengukur seberapa mudah, efektif, dan memuaskan suatu sistem digunakan.

**Metode pengukuran usability:**

| Metode | Fokus | Skala | Kelebihan | Kelemahan |
|---|---|---|---|---|
| **SUS** (System Usability Scale) | Usability secara umum | 0-100 (10 pertanyaan Likert) | Paling populer, banyak referensi, gratis | Hanya skor global, tidak detail per aspek |
| **UMUX** (Usability Metrics for User Experience) | Usability + Usefulness | 0-100 (4 pertanyaan) | Lebih singkat dari SUS | Kurang dikenal |
| **SUMI** (Software Usability Measurement Inventory) | Usability detail | 5 subscale (50 pertanyaan) | Sangat detail | Berbayar, panjang |
| **QUIS** (Questionnaire for User Interaction Satisfaction) | Kepuasan interaksi | 27-108 (27 pertanyaan) | Detail per aspek | Panjang |
| **HEART** (Google) | Happiness, Engagement, Adoption, Retention, Task Success | Framework | Komprehensif | Lebih untuk produk besar |
| **NASA-TLX** | Cognitive workload | 6 dimensi | Cocok untuk mengukur beban mental | Fokus ke workload, bukan usability |

### 5.2 SUS (System Usability Scale) — Rekomendasi

**Kenapa SUS?**
- Paling sering dipakai di TA (indikator aman)
- Brodkin (2009): SUS adalah "quick and dirty" usability scale
- Bangor et al. (2009): Norma interpretasi skor SUS:
  - < 50 = Not Acceptable
  - 50-70 = Marginal
  - > 70 = Acceptable
  - > 85 = Excellent

**10 Pertanyaan SUS (adaptasi Bahasa Indonesia):**

| # | Pertanyaan | Tipe |
|---|---|---|
| 1 | Saya rasa akan sering menggunakan simulasi ini | Positif |
| 2 | Saya merasa simulasi ini terlalu kompleks | Negatif |
| 3 | Saya merasa simulasi ini mudah digunakan | Positif |
| 4 | Saya butuh bantuan teknis untuk menggunakan simulasi ini | Negatif |
| 5 | Saya merasa fungsi-fungsi dalam simulasi ini terintegrasi dengan baik | Positif |
| 6 | Saya merasa ada terlalu banyak ketidakkonsistenan dalam simulasi ini | Negatif |
| 7 | Saya membayangkan kebanyakan orang akan belajar menggunakan simulasi ini dengan cepat | Positif |
| 8 | Saya merasa simulasi ini sangat rumit untuk digunakan | Negatif |
| 9 | Saya merasa sangat percaya diri menggunakan simulasi ini | Positif |
| 10 | Saya perlu belajar banyak hal sebelum bisa menggunakan simulasi ini | Negatif |

### 5.3 Black-Box Testing

**Apa itu?** Pengujian fungsionalitas tanpa mengetahui kode internal. Cek input → output sesuai ekspektasi.

**Teknik black-box:**
- **Equivalence Partitioning** — Membagi input ke kelas ekuivalen
- **Boundary Value Analysis** — Test di batas nilai
- **Decision Table** — Test berdasarkan kombinasi kondisi
- **State Transition** — Test perubahan state sistem

**Relevansi ke project ini:** Black-box untuk test fungsionalitas game (start → level → Probe UI → result), sedangkan SUS untuk test usability.

### 5.4 Pretest-Posttest Design

**Apa itu?** Mengukur sesuatu SEBELUM dan SESUDAH treatment/intervensi.

**Jenis:**
| Desain | Penjelasan | Kapan Dipakai |
|---|---|---|
| **One-Group Pretest-Posttest** | 1 kelompok, diukur 2x (sebelum & sesudah) | Kalau nggak punya kelompok kontrol |
| **Pretest-Posttest Control Group** | 2 kelompok (eksperimen + kontrol) | Kalau bisa bikin kelompok kontrol |
| **Solomon Four-Group** | 4 kelompok untuk control pretest effect | Kalau mau sangat rigorous |

**Relevansi ke project ini:** 
- One-Group Pretest-Posttest bisa dipakai untuk mengukur perubahan AI literacy siswa sebelum dan sesudah bermain simulasi
- Tapi hati-hati — tanpa kelompok kontrol, kita nggak bisa bilang "peningkatan itu karena simulasi kita"
- Di konteks TA D4, one-group biasanya sudah cukup

---

## 6. Komparasi & Rekomendasi

### 6.1 Tabel Komparasi Metode Penelitian untuk Project Ini

| Metode | Cocok? | Alasan |
|---|---|---|
| **Kuantitatif Deskriptif** | ✅ Cocok | Untuk mengukur SUS score, statistik data log, confidence score |
| **Kuantitatif Eksperimen** | ⚠️ Mungkin | One-group pretest-posttest bisa, tapi butuh instrumen AI literacy yang valid |
| **Kualitatif Deskriptif** | ✅ Cocok | Untuk menganalisis pengalaman user, think-aloud, observasi |
| **R&D** | ✅✅ Sangat Cocok | Project ini memang mengembangkan produk (simulasi interaktif) |
| **Mixed Methods** | ✅✅ Ideal | Kombinasi pengukuran (kuan) + pemahaman mendalam (kual) |
| **Studi Kasus** | ⚠️ Mungkin | Kalau fokus ke beberapa siswa saja |
| **Action Research** | ❌ Kurang Cocok | Ini bukan improvement siklus di komunitas |
| **Korelasional** | ⚠️ Mungkin | Bisa untuk analisis hubungan confidence score vs override rate |

### 6.2 Rekomendasi Final

**Metode Penelitian yang Direkomendasikan:**

```
Pendekatan: Mixed Methods (Kuantitatif + Kualitatif)
  │
  ├── Jenis: R&D (Research and Development)
  │     └── Menghasilkan produk "Escape the Sketchbook"
  │         sekaligus menguji keefektifannya
  │
  ├── Metode Pengembangan: SDLC Waterfall + Prototype
  │     ├── Waterfall sebagai kerangka utama
  │     └── Prototype di tahap desain UI/UX
  │
  ├── Teknik Analisis Masalah:
  │     └── Fishbone Diagram (Ishikawa) — 6M Framework
  │         untuk identifikasi akar penyebab masalah
  │
  ├── Teknik Pengumpulan Data:
  │     ├── Kuesioner SUS (usability)
  │     ├── Pretest-Posttest (AI literacy)
  │     ├── Data Log (interaction data dari sistem)
  │     └── Observasi + Think-Aloud
  │
  ├── Teknik Analisis Data:
  │     ├── Statistik Deskriptif (SUS score, confidence distribution)
  │     ├── Paired t-test / Wilcoxon (pretest vs posttest)
  │     ├── Fishbone Diagram (root cause analysis)
  │     ├── K-Means Clustering (clustering perilaku user)
  │     └── Thematic Analysis (data kualitatif wawancara)
  │
  └── Metode Pengujian:
        ├── Black-Box Testing (fungsionalitas)
        └── Usability Testing — SUS (usability)
```

### 6.3 Kenapa Mixed Methods + R&D + Fishbone?

1. **Mixed Methods** → Karena project ini butuh angka (SUS, pretest-posttest) DAN pemahaman mendalam (observasi, wawancara). Kalau cuma kuantitatif, kita kehilangan konteks "mengapa siswa melakukan override". Kalau cuma kualitatif, kita nggak punya bukti terukur bahwa simulasi berhasil.

2. **R&D** → Karena project ini memang MENGEMBANGKAN PRODUK (simulasi interaktif). R&D itu metode penelitian yang tujuannya menghasilkan produk DAN menguji keefektifannya. Ini definisi persis dari Sugiyono (2020): "Metode penelitian dan pengembangan (R&D) digunakan apabila peneliti bermaksud menghasilkan produk tertentu, dan sekaligus menguji keefektifan produk tersebut."

3. **Fishbone** → Karena Bu Hesti menyarankan, dan emang cocok untuk mengidentifikasi akar masalah kenapa AI literacy di SMP itu rendah. Fishbone meng-bridge Bab 1 (masalah) dengan Bab 3 (solusi).

---

## 7. Contoh Penerapan di Proposal

### 7.1 Contoh Sub-Bab Metodologi (Bab 3)

```latex
\section{Metode Penelitian}

\subsection{Pendekatan dan Jenis Penelitian}
Penelitian ini menggunakan pendekatan \textit{mixed methods} 
yang menggabungkan metode kuantitatif dan kualitatif. 
Jenis penelitian yang digunakan adalah \textit{Research and Development} 
(R&D) yang bertujuan menghasilkan produk berupa simulasi interaktif 
HITL AI literacy ``Escape the Sketchbook'' dan sekaligus menguji 
keefektifannya (Sugiyono, 2020).

\subsection{Metode Pengembangan}
Pengembangan sistem menggunakan metode \textit{Software Development 
Life Cycle} (SDLC) model \textit{Waterfall} dengan pendekatan 
\textit{Prototype} pada tahap desain. Model \textit{Waterfall} 
dipilih karena requirement sistem telah terdefinisi dengan jelas, 
sementara pendekatan \textit{Prototype} digunakan pada tahap desain 
UI/UX untuk mendapatkan \textit{feedback} pengguna secara dini.

\subsection{Analisis Masalah}
Analisis masalah dilakukan menggunakan \textit{Fishbone Diagram} 
(Ishikawa Diagram) dengan model 6M (\textit{Man, Machine, Method, 
Material, Measurement, Environment}) untuk mengidentifikasi akar 
penyebab rendahnya literasi AI pada siswa SMP dan merumuskan 
solusi yang tepat melalui desain simulasi interaktif.

\subsection{Teknik Pengumpulan Data}
\begin{enumerate}
    \item \textbf{Kuesioner} — System Usability Scale (SUS) 
          untuk mengukur tingkat usability simulasi
    \item \textbf{Pretest-Posttest} — Mengukur perubahan 
          pemahaman AI siswa sebelum dan sesudah menggunakan simulasi
    \item \textbf{Data Log} — Data interaksi pengguna yang terekam 
          secara otomatis oleh sistem (confidence score, keputusan 
          override, durasi keputusan)
    \item \textbf{Observasi} — Observasi terstruktur saat siswa 
          berinteraksi dengan simulasi
\end{enumerate}

\subsection{Teknik Analisis Data}
\begin{enumerate}
    \item \textbf{Statistik Deskriptif} — Menghitung rata-rata 
          skor SUS, distribusi confidence score, dan statistik 
          data log
    \item \textbf{Paired t-test} — Menguji perbedaan signifikan 
          antara skor pretest dan posttest
    \item \textbf{K-Means Clustering} — Mengelompokkan pola 
          perilaku pengguna berdasarkan data log
    \item \textbf{Fishbone Diagram} — Analisis akar penyebab 
          masalah untuk menjembatani identifikasi masalah dan 
          perumusan solusi
\end{enumerate}

\subsection{Metode Pengujian}
\begin{enumerate}
    \item \textbf{Black-Box Testing} — Pengujian fungsionalitas 
          sistem berdasarkan spesifikasi requirement
    \item \textbf{Usability Testing (SUS)} — Pengujian tingkat 
          kemudahan penggunaan simulasi menggunakan 
          \textit{System Usability Scale}
\end{enumerate}
```

### 7.2 Diagram Alir Metodologi (Contoh Flow)

```
┌──────────────────────────────────────────────────────────────────┐
│                    DIAGRAM ALIR METODE PENELITIAN                 │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌─────────────────────┐                                         │
│  │ 1. IDENTIFIKASI     │ ← Fishbone Diagram (6M)                 │
│  │    MASALAH          │   Identifikasi akar penyebab             │
│  └─────────┬───────────┘   rendahnya AI literacy SMP             │
│            │                                                    │
│            ▼                                                    │
│  ┌─────────────────────┐                                         │
│  │ 2. STUDI LITERATUR  │ ← Jurnal, buku, referensi              │
│  │    & REFERENSI      │   AI literacy, HITL, GBL,              │
│  └─────────┬───────────┘   CNN, usability testing               │
│            │                                                    │
│            ▼                                                    │
│  ┌─────────────────────┐                                         │
│  │ 3. PERANCANGAN      │ ← SDLC Waterfall + Prototype            │
│  │    SISTEM           │   Desain level, Probe UI,              │
│  └─────────┬───────────┘   data log, dashboard                  │
│            │                                                    │
│            ▼                                                    │
│  ┌─────────────────────┐                                         │
│  │ 4. IMPLEMENTASI     │ ← Kaplay.js, TF.js,                    │
│  │                     │   MediaPipe, REST API                   │
│  └─────────┬───────────┘                                         │
│            │                                                    │
│            ▼                                                    │
│  ┌─────────────────────┐                                         │
│  │ 5. PENGUJIAN        │ ← Black-Box + SUS +                     │
│  │                     │   Pretest-Posttest                      │
│  └─────────┬───────────┘                                         │
│            │                                                    │
│            ▼                                                    │
│  ┌─────────────────────┐                                         │
│  │ 6. ANALISIS DATA    │ ← Statistik Deskriptif +                │
│  │    & KESIMPULAN     │   K-Means + Thematic Analysis           │
│  └─────────────────────┘                                         │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

---

## 8. Daftar Referensi Akademik

### Tentang Metode Penelitian Umum
- Sugiyono. (2020). *Metode Penelitian Kuantitatif, Kualitatif, dan R&D*. Bandung: Alfabeta.
- Creswell, J.W. (2014). *Research Design: Qualitative, Quantitative, and Mixed Methods Approaches*. 4th ed. Sage Publications.
- Creswell, J.W. & Plano Clark, V.L. (2017). *Designing and Conducting Mixed Methods Research*. 3rd ed. Sage Publications.

### Tentang Fishbone/Ishikawa
- Ishikawa, K. (1986). *Guide to Quality Control*. 2nd ed. Tokyo: Asian Productivity Organization.
- ASQ (American Society for Quality). (2024). "What is a Fishbone Diagram?" https://asq.org/quality-resources/fishbone
- Tague, N.R. (2005). *The Quality Toolbox*. 2nd ed. ASQ Quality Press.

### Tentang R&D dalam Teknologi Pendidikan
- Borg, W.R. & Gall, M.D. (1983). *Educational Research: An Introduction*. 4th ed. Longman.
- Sugiyono. (2020). *Metode Penelitian dan Pengembangan (R&D)*. Bandung: Alfabeta.

### Tentang Usability Testing / SUS
- Brooke, J. (1996). "SUS: A 'Quick and Dirty' Usability Scale." In *Usability Evaluation in Industry*, 189-194. Taylor & Francis.
- Bangor, A., Kortum, P.T., & Miller, J.T. (2008). "An Empirical Evaluation of the System Usability Scale." *International Journal of Human-Computer Interaction*, 24(6), 574-594.
- Brooke, J. (2013). "SUS: A Retrospective." *Journal of Usability Studies*, 8(2), 29-40.

### Tentang SDLC / Metode Pengembangan
- Pressman, R.S. (2014). *Software Engineering: A Practitioner's Approach*. 8th ed. McGraw-Hill.
- Sommerville, I. (2015). *Software Engineering*. 10th ed. Pearson.
- Luther, A.C. (1998). *Authoring Interactive Multimedia*. AP Professional. (untuk MDLC)

### Tentang Pretest-Posttest Design
- Campbell, D.T. & Stanley, J.C. (1963). *Experimental and Quasi-Experimental Designs for Research*. Houghton Mifflin.
- Hastjarjo, T.D. (2019). "Quasi Experimental Design." *Buletin Psikologi*, 27(2), 187-202.

---

## APPENDIX: Quick Reference Card

```
┌─────────────────────────────────────────────────────────────────┐
│              QUICK REFERENCE: METODE PENELITIAN                 │
│              untuk "Escape the Sketchbook"                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  PENDEKATAN    : Mixed Methods (Kuantitatif + Kualitatif)      │
│  JENIS         : Research and Development (R&D)                │
│  SDLC          : Waterfall + Prototype                         │
│  ANALISIS MASALAH: Fishbone Diagram (Ishikawa, 6M)            │
│  PENGUMPULAN DATA: SUS + Pretest-Posttest + Log + Observasi    │
│  ANALISIS DATA : Statistik Deskriptif + Paired t-test +        │
│                  K-Means Clustering + Thematic Analysis         │
│  PENGUJIAN     : Black-Box + Usability Testing (SUS)           │
│                                                                 │
│  REF UTAMA     : Sugiyono (2020), Creswell (2014),             │
│                  Brooke (1996), Ishikawa (1986)                 │
│                                                                 │
│  CATATAN: Fishbone = TEKNIK ANALISIS, bukan METODE PENELITIAN  │
│           Fishbone masuk di Bab 1 (identifikasi masalah)        │
│           dan Bab 3 (teknik analisis data)                      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

*Document ini akan di-update seiring diskusi dengan Can dan masukan dari Bu Hesti.*
