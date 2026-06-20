# Metodologi Mixed Method Integration — Sketchbook Universe

## Project: "Escape the Sketchbook" — HITL AI Literacy Simulation

> **Dibuat:** 2026-07-04  
> **Revisi:** v2.0 — Ekspansi Fishbone 4→5 tulang, integrasi Metopen, SQL Analytics View  
> **Status:** Living Document — update kalau ada perubahan dari diskusi/dosen  
> **Konteks:** Can (D4 TRM PENS) — saran Bu Hesti: Metodologi MIX (Kuantitatif + Kualitatif) + Fishbone analysis + Metopen  
> **Sumber:** `08_cache/metodologi_raw.md` (4-tulang) → dokumen ini (5-tulang reconciled)

---

## DAFTAR ISI

1. [Fishbone Analysis — 5 Tulang (Reconciled)](#1-fishbone-analysis--5-tulang-reconciled)
2. [Metodologi MIX (Kuantitatif + Kualitatif)](#2-metodologi-mix-kuantitatif--kualitatif)
3. [Metrik vs Matriks](#3-metrik-vs-matriks)
4. [Metopen Framework (5 Tahapan)](#4-metopen-framework-5-tahapan)
5. [Data Log Schema (Definitif)](#5-data-log-schema-definitif)
6. [SQL Analytics View (Auto-Conclusion)](#6-sql-analytics-view-auto-conclusion)
7. [Referensi Akademik](#7-referensi-akademik)

---

## 1. Fishbone Analysis — 5 Tulang (Reconciled)

### 1.1 Rekonsiliasi: Dari 4 Tulang ke 5 Tulang

Versi sebelumnya menggunakan **4 tulang** (Manusia, Metode, Media, Materi). Versi ini menambahkan **Lingkungan (Environment)** sebagai tulang kelima berdasarkan pertimbangan berikut:

| Versi | Tulang | Justifikasi |
|-------|--------|-------------|
| **v1 (4-tulang)** | Manusia, Metode, Media, Materi | Domain-specific, menghilangkan Measurement & Mother Nature yang terlalu generik |
| **v2 (5-tulang)** | Manusia, Metode, Mesin, Materi, Lingkungan | Mengakomodasi perspektif 5M+1E (Man, Method, Machine, Material, Environment) yang umum di penelitian TI pendidikan [Sugiyono, 2019; Ishikawa, 1982] |

**Perubahan kunci:**

1. **Media → Mesin**: Rename untuk konsistensi dengan terminologi "Machine" dalam framework 5M+1E. "Mesin" mencakup seluruh infrastruktur teknologi (bukan hanya "media" yang bisa diartikan sempit sebagai UI).
2. **Lingkungan (BARU)**: Faktor kontekstual yang mempengaruhi pengalaman pengguna — spesifikasi perangkat, kondisi lab, pencahayaan, kebisingan — yang sebelumnya tidak tertangkap.

**Mengapa 5 tulang, bukan 6M tradisional?**

Diagram Ishikawa tradisional menggunakan **6M** (Man, Machine, Method, Material, Measurement, Mother Nature). Namun untuk konteks simulasi interaktif literasi AI di SMP:

- **Measurement** sudah tercakup dalam Matriks Decision Log (bukan tulang tersendiri)
- **Mother Nature** terlalu generik; kita menggunakan **Lingkungan** yang lebih spesifik ke konteks penggunaan TI di sekolah

Keempat tulang awal + Lingkungan membentuk **ecosystem model** — setiap tulang saling mempengaruhi dan tidak bisa dipisahkan.

---

### 1.2 Diagram Fishbone ASCII — 5 Tulang

```
                        ┌──────────────────────────────────────────────────┐
                        │             MATERI (Material)                    │
                        │          Konten Edukasi AI Literacy              │
                        │                                                  │
                        │  • Confidence Score (0-100%)                     │
                        │  • Probabilitas AI & Margin of Error             │
                        │  • Decision-Making Framework                     │
                        │  • Override vs Compliance Scenario               │
                        │  • Eksplanasi AI "Why"                           │
                        │  • Skala Ketidakpastian                          │
                        └──────────────────────┬───────────────────────────┘
                                               │
┌──────────────────────────────────┐    ┌──────┴───────────────────────────┐
│       MANUSIA (Man)              │    │       LINGKUNGAN (Environment)   │
│    Faktor Siswa SMP 7-9         │    │    Konteks Penggunaan            │
│                                  │    │                                  │
│  • Automation Bias              │    │  • Device Spec (RAM, GPU, OS)   │
│  • Pengalaman Teknologi         │    │  • Kondisi Lab Sekolah          │
│  • Usia Kognitif (12-15 th)     │    │  • Pencahayaan (Lighting)       │
│  • Digital Native Assumption    ├──┐ │  • Tingkat Kebisingan (Noise)   │
│  • Prior AI Knowledge           │  │ │  • Konektivitas Internet        │
│  • Trust Calibration Ability    │  │ │  • Waktu Penggunaan (Slot)     │
│  • Risk Perception              │  │ └──────────────────────────────────┘
└──────────────────────────────────┘  │
                                      │   ┌──────────────────────────────┐
                                      ├──►│     EFEK (Problem)           │
                                      │   │                              │
                                      │   │  Rendahnya Literasi AI pada  │
                                      │   │  Siswa SMP Kelas 7-9         │
                                      │   │  (Blind Trust / Rejection    │
                                      │   │   Extremes)                  │
                                      │   │                              │
                                      │   │  ──► Target: Siswa mampu     │
                                      │   │  mengkritisi keputusan AI,   │
                                      │   │  bukan hanya mengikuti       │
                                      │   └──────────────┬───────────────┘
                                      │                  │
                                      │   ┌──────────────┴───────────────┐
                                      │   │       METODE (Method)        │
                                      │   │    Pendekatan Pengajaran     │
                                      │   │                              │
                                      │   │  • HITL (Human-in-the-Loop) │
                                      │   │  • Controlled Ambiguity      │
                                      │   │  • Level Progression         │
                                      │   │  • Scaffolding & Hint System │
                                      │   │  • Immediate Feedback Loop   │
                                      │   │  • Decision Override Mechanism│
                                      │   └──────────────┬───────────────┘
                                      │                  │
                                      │   ┌──────────────┴───────────────┐
                                      └───│       MESIN (Machine)        │
                                          │   Platform dan Teknologi     │
                                          │                              │
                                          │  • Browser-based (No Install)│
                                          │  • TensorFlow.js (Inference) │
                                          │  • MediaPipe (Gesture Input) │
                                          │  • Kaplay.js (Game Engine)   │
                                          │  • Decision Log System       │
                                          │  • CNN Accuracy & Latency    │
                                          │  • Client-side Processing    │
                                          └──────────────────────────────┘
```

**Versi ringkas (diagram kerangka):**

```
      MANUSIA                    MATERI
     (Man)                     (Material)
        \                        /
         \                      /
          \                    /
           +---→ EFEK ←------+
           |   (Literasi AI)  |
          /                    \
         /                      \
        /                        \
     METODE                   MESIN
    (Method)                (Machine)
        \                        /
         \                      /
          \                    /
           +--→ LINGKUNGAN ←--+
              (Environment)
```

---

### 1.3 Penjelasan Detail Setiap Tulang

#### Tulang 1: MANUSIA (Man) — Faktor Siswa

Tulang ini menganalisis **karakteristik subjek penelitian** (siswa SMP kelas 7-9, usia 12-15 tahun) sebagai faktor yang mempengaruhi literasi AI.

| Sub-faktor | Penjelasan | Indikator dalam Simulasi |
|------------|------------|--------------------------|
| **Automation Bias** | Kecenderungan manusia untuk secara otomatis menerima saran dari sistem komputer tanpa verifikasi kritis (Parasuraman & Riley, 1997) | Siswa langsung "ya" ke rekomendasi AI tanpa mempertimbangkan confidence score |
| **Pengalaman Teknologi** | Tingkat paparan dan kenyamanan siswa dengan teknologi digital | Seberapa sering siswa menggunakan AI tools (ChatGPT, dll.) sebelum simulasi |
| **Usia Kognitif** | Tahap perkembangan kognitif Piaget — siswa SMP berada di transisi concrete-operational ke formal-operational | Kemampuan memahami konsep abstrak seperti probabilitas dan ketidakpastian |
| **Digital Native Assumption** | Asumsi bahwa generasi muda otomatis paham teknologi — padahal literasi AI ≠ literasi digital | Siswa mungkin bisa menggunakan gadget tapi tidak memahami bagaimana AI membuat keputusan |
| **Prior AI Knowledge** | Pengetahuan awal tentang AI sebelum mengikuti simulasi | Pre-test score tentang konsep dasar AI |
| **Trust Calibration Ability** | Kemampuan menyesuaikan tingkat kepercayaan sesuai kemampuan aktual sistem | Override ratio — kapan siswa memilih menolak saran AI |
| **Risk Perception** | Bagaimana siswa mempersepsi risiko dari keputusan yang salah | Reaksi siswa ketika AI memberikan jawaban yang salah atau ambigu |

**MATRIKS yang dihasilkan:**

```
┌─────────┬──────┬─────────────────┬──────────────┬───────────────┬─────────┐
│ user_id │ age  │ tech_experience │ prior_ai_kn  │ pre_test_scr  │ cluster │
├─────────┼──────┼─────────────────┼──────────────┼───────────────┼─────────┤
│ S001    │ 13   │ high            │ low          │ 45            │ A       │
│ S002    │ 14   │ medium          │ medium       │ 62            │ B       │
│ S003    │ 12   │ low             │ low          │ 30            │ C       │
└─────────┴──────┴─────────────────┴──────────────┴───────────────┴─────────┘
```

---

#### Tulang 2: METODE (Method) — Pendekatan Pengajaran

Tulang ini menganalisis **strategi pedagogis** yang digunakan untuk mengajarkan literasi AI melalui simulasi interaktif.

| Sub-faktor | Penjelasan | Implementasi dalam Simulasi |
|------------|------------|-----------------------------|
| **HITL (Human-in-the-Loop)** | Siswa bukan pasif menerima output AI, tapi aktif membuat keputusan dan bisa override keputusan AI (Mosqueira-Rey et al., 2023) | Pada setiap level, AI memberikan rekomendasi + confidence score, siswa memilih: ikuti AI atau override |
| **Controlled Ambiguity** | Sengaja memasukkan ambiguitas terkendali ke dalam skenario agar siswa berlatih menghadapi ketidakpastian | AI kadang memberikan confidence score rendah atau rekomendasi yang kontradiktif — siswa harus memutuskan |
| **Level Progression** | Meningkatkan kompleksitas secara bertahap: dari skenario sederhana ke kompleks | Level 1: AI jelas benar → Level 2: AI ambigu → Level 3: AI menipu / adversarial |
| **Scaffolding & Hint System** | Memberikan bantuan kontekstual yang berkurang seiring kemampuan siswa meningkat | Hint di awal ("Perhatikan confidence score!"), lalu dihilangkan di level lanjut |
| **Immediate Feedback Loop** | Siswa langsung melihat konsekuensi dari keputusan mereka | Setelah override/compliance, simulasi menunjukkan outcome dan eksplanasi |
| **Decision Override Mechanism** | Mekanisme eksplisit bagi siswa untuk menolak saran AI | Tombol "Saya tidak setuju" + alasan, dicatat di decision log |

**MATRIKS yang dihasilkan:**

```
┌─────────┬───────┬────────────┬───────────────────┬─────────────────┬──────────────────────┐
│ user_id │ level │ hint_used  │ feedback_received │ scaffolding_lvl │ decision_after_feed │
├─────────┼───────┼────────────┼───────────────────┼─────────────────┼──────────────────────┤
│ S001    │ 1     │ yes        │ yes               │ high            │ compliance          │
│ S001    │ 2     │ partial    │ yes               │ medium          │ override            │
│ S001    │ 3     │ no         │ yes               │ low             │ override            │
└─────────┴───────┴────────────┴───────────────────┴─────────────────┴──────────────────────┘
```

---

#### Tulang 3: MESIN (Machine) — Platform dan Teknologi

Tulang ini menganalisis **infrastruktur teknis** yang memungkinkan simulasi berjalan dan mengumpulkan data. Catatan: tulang ini sebelumnya bernama "Media" dan di-rename menjadi "Mesin" untuk konsistensi dengan terminologi Machine dalam framework 5M+1E.

| Sub-faktor | Penjelasan | Peran dalam Simulasi |
|------------|------------|----------------------|
| **Browser-based (No Install)** | Simulasi berjalan di browser tanpa instalasi — menghilangkan barrier adopsi di sekolah | Akses via URL, kompatibel dengan Chrome/Firefox di laptop sekolah |
| **TensorFlow.js** | Library ML yang berjalan di browser — inference AI terjadi di client-side | Model klasifikasi gambar/teks berjalan langsung di browser siswa |
| **MediaPipe** | Library computer vision real-time dari Google — gesture & pose detection | Input gesture (tangan, pose) sebagai mekanisme interaksi |
| **Kaplay.js** | Game engine JavaScript ringan untuk 2D game | Rendering level, sprite, animasi, dan game loop |
| **Decision Log System** | Sistem pencatatan otomatis setiap keputusan siswa | Setiap interaksi dicatat: timestamp, confidence, decision, latency, level |
| **CNN Accuracy & Latency** | Akurasi model klasifikasi dan waktu inferensi | Mengukur kualitas output AI yang diterima siswa |
| **Client-side Processing** | Semua pemrosesan AI terjadi di perangkat siswa, tidak perlu server | Privasi data terjaga, tidak perlu infrastruktur server mahal |

**MATRIKS yang dihasilkan:**

```
┌────────────┬───────┬───────────┬────────────────┬─────────────────┬──────────────┬─────────────┐
│ session_id │ level │ load_time │ inference_time │ gesture_accuracy│ browser      │ device_type │
├────────────┼───────┼───────────┼────────────────┼─────────────────┼──────────────┼─────────────┤
│ SESS001    │ 1     │ 1200      │ 340            │ 0.92            │ Chrome 120   │ laptop      │
│ SESS001    │ 2     │ 800       │ 380            │ 0.88            │ Chrome 120   │ laptop      │
│ SESS002    │ 1     │ 2500      │ 620            │ 0.71            │ Firefox 118  │ tablet      │
└────────────┴───────┴───────────┴────────────────┴─────────────────┴──────────────┴─────────────┘
```

---

#### Tulang 4: MATERI (Material) — Konten Edukasi

Tulang ini menganalisis **substansi edukasi** yang diajarkan melalui simulasi.

| Sub-faktor | Penjelasan | Contoh dalam Simulasi |
|------------|------------|------------------------|
| **Confidence Score (0-100%)** | Angka yang menunjukkan seberapa yakin AI dengan jawabannya — konsep kunci untuk memahami bahwa AI tidak 100% akurat | AI: "Saya 73% yakin ini adalah kucing" — siswa harus memutuskan apakah 73% cukup |
| **Probabilitas AI & Margin of Error** | Memahami bahwa output AI bersifat probabilistik, bukan deterministik | AI memberikan 3 kemungkinan jawaban dengan probabilitas masing-masing |
| **Decision-Making Framework** | Kerangka berpikir untuk membuat keputusan berdasarkan informasi yang tidak lengkap | "Jika confidence < 60%, pertimbangkan untuk override" |
| **Override vs Compliance Scenario** | Skenario di mana mengikuti AI adalah pilihan terbaik vs skenario di mana override lebih baik | Level 1: AI benar, ikuti → Level 3: AI salah, harus override |
| **Eksplanasi AI "Why"** | AI menjelaskan alasan di balik rekomendasinya — membangun kemampuan mengevaluasi reasoning | AI: "Saya merekomendasikan X karena fitur A dan B cocok, tapi fitur C tidak cocok" |
| **Skala Ketidakpastian** | Memahami spektrum dari "sangat yakin" hingga "tidak tahu sama sekali" | Visualisasi bar merah-kuning-hijau untuk confidence level |

**MATRIKS yang dihasilkan:**

```
┌─────────┬───────┬──────────────────┬──────────────┬─────────────────┬────────────────────┐
│ user_id │ level │ confidence_shown │ concept_type │ override_correct│ comprehension_score│
├─────────┼───────┼──────────────────┼──────────────┼─────────────────┼────────────────────┤
│ S001    │ 1     │ 92               │ high_conf    │ yes             │ 80                 │
│ S001    │ 2     │ 62               │ ambiguity    │ no              │ 65                 │
│ S001    │ 3     │ 41               │ adversarial  │ yes             │ 75                 │
└─────────┴───────┴──────────────────┴──────────────┴─────────────────┴────────────────────┘
```

---

#### Tulang 5: LINGKUNGAN (Environment) — Konteks Penggunaan [BARU]

Tulang ini menganalisis **faktor kontekstual** di luar kendali desain simulasi yang mempengaruhi pengalaman dan hasil penggunaan. Tulang ini ditambahkan karena:

1. Simulasi dijalankan di **lab sekolah** dengan kondisi bervariasi (device spec, internet, ruangan)
2. Faktor lingkungan bisa menjadi **confounding variable** yang mengganggu validitas hasil
3. Framework 5M+1E secara eksplisit menyertakan Lingkungan sebagai kategori analisis

| Sub-faktor | Penjelasan | Potensi Dampak pada Data |
|------------|------------|--------------------------|
| **Device Spec** | Spesifikasi perangkat siswa (RAM, GPU, OS, browser version) | TF.js inference time bervariasi; gesture detection accuracy menurun di device low-end |
| **Kondisi Lab Sekolah** | Set-up fisik lab komputer (jumlah PC, kondisi periferal) | Siswa mungkin berbagi PC; webcam quality berbeda-beda |
| **Pencahayaan (Lighting)** | Kondisi cahaya ruangan yang mempengaruhi MediaPipe gesture detection | Gesture detection accuracy turun di pencahayaan rendah |
| **Tingkat Kebisingan (Noise)** | Suara lingkungan yang mengganggu konsentrasi | Latency meningkat karena distraksi; keputusan kurang deliberatif |
| **Konektivitas Internet** | Kecepatan dan stabilitas koneksi (untuk load aset awal) | Loading time awal lambat; simulasi tidak bisa diakses jika offline |
| **Waktu Penggunaan (Slot)** | Jam pelajaran yang tersedia (45-90 menit) vs total waktu simulasi (~30 menit) | Siswa mungkin terburu-buru di akhir sesi; data level terakhir bisa bias |

**MATRIKS yang dihasilkan:**

```
┌────────────┬──────────────┬──────────┬──────────────┬─────────┬───────────┬──────────────┐
│ session_id │ device_ram_gb│ browser  │ lighting_cond│ noise   │ net_speed │ time_slot    │
├────────────┼──────────────┼──────────┼──────────────┼─────────┼───────────┼──────────────┤
│ SESS001    │ 8            │ Chrome   │ good         │ low     │ 50 Mbps   │ 08:00-08:45  │
│ SESS002    │ 4            │ Firefox  │ moderate     │ high    │ 10 Mbps   │ 10:00-10:45  │
│ SESS003    │ 2            │ Chrome   │ poor         │ medium  │ 5 Mbps    │ 13:00-13:45  │
└────────────┴──────────────┴──────────┴──────────────┴─────────┴───────────┴──────────────┘
```

---

### 1.4 Interaksi Antar-Tulang (5 Ecosystem)

```
MANUSIA ──mempengaruhi──→ METODE
  │                          │
  │ (automation bias         │ (HITL membutuhkan
  │  menentukan desain       │  decision log dari
  │  scaffolding)            │  MANUSIA)
  │                          │
  ▼                          ▼
MESIN   ←──mendukung──── MATERI
  │       (TF.js memungkinkan │
  │        confidence score   │
  │        real-time)         │
  │                          │
  └──── mempengaruhi ────────┘
               ▲
               │
        LINGKUNGAN
    (device spec mempengaruhi
     MESIN performance;
     noise mempengaruhi
     MANUSIA konsentrasi;
     internet mempengaruhi
     MESIN loading)
```

**Contoh interaksi lintas-tulang:**

| Interaksi | Penjelasan |
|-----------|------------|
| MANUSIA → METODE | Automation bias tinggi → Metode harus menyertakan level yang menunjukkan kegagalan AI |
| METODE → MATERI | HITL membutuhkan materi berupa skenario override/compliance → Materi harus didesain dengan pilihan yang meaningful |
| MATERI → MESIN | Confidence score real-time membutuhkan TF.js inference di browser → Mesin harus mendukung client-side ML |
| MESIN → MANUSIA | Browser-based tanpa instalasi → Mengurangi barrier adopsi → Siswa lebih mudah mengakses |
| LINGKUNGAN → MESIN | Device low-end → inference time tinggi → Menurunkan akurasi gesture detection |
| LINGKUNGAN → MANUSIA | Noise tinggi → konsentrasi menurun → latency meningkat → keputusan kurang deliberatif |
| LINGKUNGAN → METODE | Waktu terbatas → Level terakhir harus compact → Data level akhir mungkin bias |

---

## 2. Metodologi MIX (Kuantitatif + Kualitatif)

### 2.1 Mengapa Mixed Methods?

Metodologi MIX dipilih karena penelitian ini memiliki **dua jenis pertanyaan** yang tidak bisa dijawab oleh satu pendekatan saja:

| Pertanyaan Penelitian | Pendekatan | Mengapa? |
|----------------------|------------|----------|
| Apakah simulasi mengubah pola keputusan siswa? | **Kuantitatif** | Perlu angka: seberapa sering override, berapa latency, confidence berapa |
| MENGAPA siswa membuat keputusan tertentu? | **Kualitatif** | Perlu narasi: alasan, pemahaman, perubahan persepsi |

**Prinsip MIX**: Kuantitatif menjawab **"apa"** dan **"berapa"**, Kualitatif menjawab **"mengapa"** dan **"bagaimana"**. Keduanya saling melengkapi — bukan sekadar ditumpuk (Creswell & Plano Clark, 2018).

---

### 2.2 Kuantitatif — Analisis MATRIKS (Decision Log)

#### Sumber Data: Decision Log Matrix

Setiap kali siswa berinteraksi dengan simulasi, sistem mencatat keputusan ke dalam **matriks decision log**:

```
┌─────────┬───────┬─────────────┬──────────────┬─────────┬──────────┬─────────┐
│ user_id │ level │ confidence  │ decision     │ latency │ override │ cluster │
│         │       │ score (%)   │ type         │ (ms)    │ ratio    │         │
├─────────┼───────┼─────────────┼──────────────┼─────────┼──────────┼─────────┤
│ S001    │ 1     │ 92          │ compliance   │ 1200    │ 0.00     │ A       │
│ S001    │ 2     │ 78          │ compliance   │ 2100    │ 0.00     │ A       │
│ S001    │ 3     │ 65          │ override     │ 4500    │ 0.33     │ B       │
│ S002    │ 1     │ 95          │ compliance   │ 800     │ 0.00     │ A       │
│ S002    │ 2     │ 88          │ compliance   │ 1100    │ 0.00     │ A       │
│ S002    │ 3     │ 71          │ compliance   │ 1800    │ 0.00     │ A       │
└─────────┴───────┴─────────────┴──────────────┴─────────┴──────────┼─────────┘
                                                     K-Means assign ▲
                                                     cluster berdasarkan
                                                     pola multi-dimensi
```

#### Analisis Kuantitatif

**a) K-Means Clustering** — Mengelompokkan Siswa Berdasarkan Pola Perilaku

```
Input:  Matriks decision log (N siswa × M variabel)
Output: K cluster, masing-masing merepresentasikan profil perilaku

Cluster A (Blind Trusters):     compliance tinggi, latency rendah, override ratio ≈ 0
Cluster B (Critical Thinkers):  override meningkat seiring level, latency sedang
Cluster C (AI Skeptics):        override tinggi dari awal, latency tinggi
```

Proses:
1. **Preprocessing**: Normalisasi variabel numerik (confidence, latency, override_ratio) ke skala 0-1
2. **Feature Engineering**: Override trajectory (Δ override_ratio / Δ level), decision consistency, latency trend
3. **Determine K**: Elbow method + silhouette score
4. **Run K-Means**: K-Means++ initialization → assign → update centroid → repeat
5. **Interpretasi**: Karakterisasi setiap cluster berdasarkan centroid

**b) Paired t-test** — Mengukur Perubahan Sebelum dan Sesudah

```
H₀: Tidak ada perbedaan signifikan antara pre-test dan post-test
H₁: Ada perbedaan signifikan (simulasi mengubah pola keputusan)

Variabel yang diuji (semua dari MATRIKS):
- Override ratio: level awal vs level akhir
- Latency: level awal vs level akhir
- Pre-test score vs post-test score (pengetahuan AI)

Desain: One-Group Pretest-Posttest (within-subject)
```

Proses:
1. Data paired: Setiap siswa memiliki dua pengukuran (pre vs post)
2. Hitung selisih: dᵢ = postᵢ - preᵢ untuk setiap siswa
3. Hitung t-statistik: t = d̄ / (sᵈ / √n)
4. Bandingkan dengan t-kritis pada α = 0.05
5. Kesimpulan: Jika p-value < 0.05, tolak H₀ — simulasi berpengaruh signifikan

**c) SUS (System Usability Scale)** — Mengukur Usability

```
10 pernyataan, skala Likert 1-5
Skor SUS = (Σ odd_converted + Σ even_converted) × 2.5
Rentang: 0-100

Interpretasi (Bangor et al., 2009):
  90-100 → A+ (Best Imaginable)
  80-89  → A  (Excellent)
  70-79  → B  (Good)
  60-69  → C  (OK / Marginal)
  50-59  → D  (Poor)
  0-49   → F  (Worst Imaginable)

Target: SUS ≥ 68 (rata-rata acceptable)
```

---

### 2.3 Kualitatif — Narasi dan Interpretasi

#### Sumber Data

| Sumber | Deskripsi | Cara Pengumpulan |
|--------|-----------|------------------|
| **Think-aloud protocol** | Siswa berbicara saat membuat keputusan | Rekaman audio saat sesi simulasi |
| **Post-simulation interview** | Wawancara semi-terstruktur setelah simulasi | Panduan wawancara tentang pengalaman dan pemahaman |
| **Open-ended survey** | Pertanyaan terbuka tentang perubahan persepsi | Form digital setelah simulasi |
| **Researcher observation** | Pengamatan langsung perilaku siswa | Catatan lapangan (field notes) |
| **AI-assisted narrative generation** | Auto-generate narasi analisis menggunakan AI API (Gemini API) — sesuai instruksi Bu Hesti | Feed matriks data ke API → output "kesimpulan kalimat" |

#### Analisis Kualitatif

**a) Thematic Analysis** — Mengikuti framework Braun & Clarke (2006):

```
Tahap 1: Familiarization — Membaca ulang semua transkrip dan catatan
Tahap 2: Generating Initial Codes — Memberi kode pada potongan data
Tahap 3: Searching for Themes — Mengelompokkan kode menjadi tema
Tahap 4: Reviewing Themes — Memeriksa apakah tema konsisten dan distinct
Tahap 5: Defining & Naming Themes — Mendefinisikan dan memberi nama tema
Tahap 6: Producing the Report — Menulis narasi akhir
```

**Contoh tema yang mungkin muncul:**

| Kutipan Siswa | Tema |
|--------------|------|
| "Awalnya saya percaya AI karena kayak Google" | **Authority Attribution** |
| "Setelah AI salah, jadi ragu" | **Trust Disruption** |
| "Saya cek confidence score dulu baru memutuskan" | **Calibrated Decision-Making** |
| "Saya cuma ikut aja biar cepat selesai" | **Compliance Convenience** |

**b) Narrative Synthesis** — Menggabungkan Tema Menjadi Narasi Koheren

Hasil thematic analysis disintesiskan menjadi **narasi** yang menjelaskan:

1. **Bagaimana** siswa berubah sepanjang simulasi (trajectory)
2. **Mengapa** siswa membuat keputusan tertentu (reasoning)
3. **Apa** faktor yang mempengaruhi perubahan (triggers)

**c) AI-Assisted Auto-Generate Narasi** — Sesuai Instruksi Bu Hesti

> "Matriknya itu yang kuantitatif. Yang kualitatif penjelasan terhadap matriknya itu. Narasi harus auto generate. Panggil API." — Bu Hesti, 16/6/26

Mekanisme:
1. Sistem mengumpulkan matriks data per siswa / per cluster
2. Matriks dikirim ke AI API (Gemini API) dengan prompt terstruktur
3. API mengembalikan **"kesimpulan kalimat"** — narasi yang menjelaskan pola perilaku
4. Narasi diverifikasi oleh peneliti (human-in-the-loop for validation)

```
┌──────────────┐     ┌──────────────────┐     ┌──────────────────────┐
│  MATRIKS     │────►│  AI API          │────►│  KESIMPULAN KALIMAT  │
│  (Data Log)  │     │  (Gemini API)    │     │  (Narasi Auto-Gen)   │
│              │     │                  │     │                      │
│  user_id     │     │  Prompt:         │     │  "Siswa S001         │
│  level       │     │  "Analisis pola  │     │   menunjukkan pening- │
│  confidence  │     │   perilaku dari  │     │   katan override dari │
│  decision    │     │   matriks ini    │     │   level 2 ke level 3, │
│  latency     │     │   dan buat       │     │   mengindikasikan     │
│  override    │     │   kesimpulan     │     │   transisi dari       │
│  cluster     │     │   kalimat"       │     │   blind trust ke      │
└──────────────┘     └──────────────────┘     │   critical thinking" │
                                               └──────────────────────┘
```

---

### 2.4 Integration & Triangulation

```
┌──────────────────────────────────────────────────────────────────────────┐
│                         METODOLOGI MIX                                    │
│                                                                          │
│  ┌─────────────────────┐              ┌──────────────────────────┐      │
│  │   KUANTITATIF        │              │   KUALITATIF              │      │
│  │                      │              │                           │      │
│  │  Sumber: MATRIKS     │              │  Sumber: NARASI           │      │
│  │  (Decision Log)      │              │  (Interview, Survey,      │      │
│  │                      │              │   Observation, AI API)    │      │
│  │  Analisis:           │              │                           │      │
│  │  • K-Means Clustering│              │  Analisis:                │      │
│  │  • Paired t-test     │              │  • Thematic Analysis      │      │
│  │  • SUS Scoring       │              │  • Narrative Synthesis    │      │
│  │                      │              │  • AI Auto-Generate       │      │
│  │  Output:             │              │                           │      │
│  │  • Cluster profiles  │              │  Output:                  │      │
│  │  • Significance      │              │  • Tema-tema perilaku     │      │
│  │    values            │              │  • Narasi perubahan       │      │
│  │  • SUS scores        │              │  • Kesimpulan kalimat     │      │
│  └──────────┬───────────┘              └────────────┬──────────────┘      │
│             │                                       │                     │
│             │    ┌──────────────────────────┐        │                     │
│             └───►│   TRIANGULASI            │◄───────┘                     │
│                  │                          │                               │
│                  │  Kuantitatif: APA        │                               │
│                  │  Kualitatif: MENGAPA     │                               │
│                  │                          │                               │
│                  │  Contoh:                 │                               │
│                  │  Cluster A = 40% siswa   │                               │
│                  │  (Blind Trusters) — KUANT │                               │
│                  │  + MENGAPA? Karena       │                               │
│                  │  authority attribution   │                               │
│                  │  — KUAL                  │                               │
│                  │  = TRIANGULASI VALID     │                               │
│                  └──────────────────────────┘                               │
└──────────────────────────────────────────────────────────────────────────┘
```

**Strategi integrasi: Connecting Approach** (Creswell & Plano Clark, 2018):

| Langkah | Kuantitatif | Kualitatif | Integrasi |
|---------|-------------|------------|-----------|
| 1. Identifikasi pola | K-Means → Cluster profiles | — | — |
| 2. Jelaskan alasan | — | Thematic analysis → Tema per cluster | Cross-validate: Apakah tema kualitatif konsisten dengan profil kuantitatif? |
| 3. Ukur signifikansi | Paired t-test → p-value | — | — |
| 4. Kontekstualisasi | — | Narasi + AI auto-generate | Narasi menjelaskan mengapa perubahan signifikan/ tidak |
| 5. Konklusi terintegrasi | Metrik + Matriks | Tema + Narasi | **Triangulasi**: Dua sumber konvergen → Temuan lebih robust |

---

## 3. Metrik vs Matriks

### 3.1 Mengapa Distingsi Ini Penting?

Dalam diskusi sebelumnya, terjadi kebingungan antara **metrik** (angka tunggal) dan **matriks** (tabel multi-dimensi). Ini adalah distingsi fundamental yang mempengaruhi:

- **Cara kita menganalisis data** — analisis single value vs analisis multi-dimensi
- **Cara kita memahami Fishbone** — setiap tulang menghasilkan matriks, bukan sekadar metrik
- **Cara kita menulis proposal** — metodologi kuantitatif berbasis matriks, bukan pengukuran tunggal
- **Instruksi Bu Hesti** — data log harus punya "kesimpulan kalimat" di samping angka

### 3.2 Definisi

| Aspek | **METRIK** | **MATRIKS** |
|-------|-----------|-------------|
| **Definisi** | Satu angka/ukuran tunggal | Tabel lengkap dengan banyak dimensi |
| **Analogi** | Satu foto | Album foto dengan metadata |
| **Contoh** | `trust_score = 0.73` | Tabel: `user_id, level, confidence, decision, latency, override, cluster` |
| **Informasi** | Terbatas — satu dimensi | Kaya — banyak dimensi yang saling terkait |
| **Analisis** | Bandingkan angka | K-Means, t-test, cross-tabulation |
| **Kesimpulan** | "Trust score tinggi" | "Siswa S001 menunjukkan peningkatan override dari level 2 ke 3, mengindikasikan transisi dari blind trust ke critical evaluation" |
| **Konteks** | Cukup untuk dashboard sederhana | Diperlukan untuk penelitian akademis |

### 3.3 Contoh Konkret

**Pendekatan METRIK (tidak memadai untuk penelitian ini):**

```
trust_score = 0.73
accuracy = 85%
override_rate = 23%
```

Masalah: Angka-angka ini tidak menunjukkan **siapa**, **kapan**, **dalam konteks apa**, dan **bagaimana polanya**.

**Pendekatan MATRIKS + KESIMPULAN KALIMAT (benar untuk penelitian ini):**

```
┌─────────┬───────┬─────────────┬──────────────┬─────────┬──────────┬─────────┐
│ user_id │ level │ confidence  │ decision     │ latency │ override │ cluster │
├─────────┼───────┼─────────────┼──────────────┼─────────┼──────────┼─────────┤
│ S001    │ 1     │ 92          │ compliance   │ 1200    │ 0.00     │ A       │
│ S001    │ 2     │ 78          │ compliance   │ 2100    │ 0.00     │ A       │
│ S001    │ 3     │ 65          │ override     │ 4500    │ 0.33     │ B       │
│ S002    │ 1     │ 95          │ compliance   │ 800     │ 0.00     │ A       │
│ S002    │ 2     │ 88          │ compliance   │ 1100    │ 0.00     │ A       │
│ S002    │ 3     │ 71          │ compliance   │ 1800    │ 0.00     │ A       │
└─────────┴───────┴─────────────┴──────────────┴─────────┴──────────┴─────────┘

KESIMPULAN KALIMAT (auto-generated):
"Siswa S001 menunjukkan transisi perilaku dari compliance (level 1-2) ke override
(level 3) seiring menurunnya confidence score AI, mengindikasikan perkembangan
calibrated decision-making. Sementara S002 tetap compliance meskipun confidence
menurun, menunjukkan pola blind trust yang persisten."
```

### 3.4 Fishbone Menggunakan MATRIKS

Setiap tulang Fishbone menghasilkan data dalam bentuk **matriks**, bukan metrik tunggal:

| Tulang | MATRIKS yang Dihasilkan | Kolom Utama |
|--------|------------------------|-------------|
| **Manusia** | Matriks profil siswa | `user_id, age, tech_experience, prior_ai_knowledge, pre_test_score, cluster` |
| **Metode** | Matriks interaksi metode | `user_id, level, hint_used, feedback_received, scaffolding_level, decision_after_feedback` |
| **Mesin** | Matriks performa teknis | `session_id, level, load_time, inference_time, gesture_accuracy, browser, device_type` |
| **Materi** | Matriks respons konten | `user_id, level, confidence_shown, concept_type, override_correct, comprehension_score` |
| **Lingkungan** | Matriks konteks penggunaan | `session_id, device_ram_gb, browser, lighting_condition, noise_level, net_speed, time_slot` |

**Implikasi**: Analisis Fishbone bukan sekadar "tulang A menyebabkan efek X", tetapi **"interaksi antar-matriks dari 5 tulang menghasilkan pola multi-dimensi yang mempengaruhi literasi AI"**.

### 3.5 Ringkasan Perbandingan

```
METRIK                              MATRIKS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
trust_score = 0.73                  ┌──────┬───────┬──────┬───────┬─────────┐
                                    │ user │ level │ conf │ dec   │ cluster │
Satu angka                          │ S001 │ 3     │ 65   │ over  │ B       │
Tidak ada konteks                   │ S002 │ 3     │ 71   │ comp  │ A       │
Tidak bisa di-cluster               │ S003 │ 3     │ 59   │ over  │ B       │
Tidak bisa di-cross-tab             └──────┴───────┴──────┴───────┴─────────┘
Tidak punya "kesimpulan kalimat"          │        │       │         │
                                           ▼        ▼       ▼         ▼
                                        Bisa K-Means, t-test, cross-tab,
                                        analisis multi-dimensi,
                                        + auto-generate kesimpulan kalimat
```

---

## 4. Metopen Framework (5 Tahapan)

### 4.1 Mengapa Metopen?

**Metopen** (Metodologi Penelitian) adalah kerangka metodologis yang digunakan di lingkungan PENS (Politeknik Elektronika Negeri Surabaya) untuk penelitian pengembangan (R&D). Metopen menyediakan struktur tahapan yang **sistematis dan terdokumentasi** dari perencanaan hingga pelaporan.

Metopen dipilih karena:

1. **Sesuai konteks PENS** — Kerangka ini diakui dan digunakan di lingkungan kampus
2. **Kompatibel dengan R&D** — Metopen mendukung penelitian yang menghasilkan produk
3. **Iteratif** — Tahapan pengamatan dan refleksi memungkinkan perbaikan berkelanjutan
4. **Terintegrasi dengan MIX** — Setiap tahapan Metopen menghasilkan data kuantitatif DAN kualitatif

### 4.2 Diagram Alir Metopen

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                         METOPEN FRAMEWORK                                       │
│                 (5 Tahapan Penelitian Pengembangan)                              │
│                                                                                 │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐                       │
│  │  1. PERENCANAAN│──►│ 2. PELAKSANAAN│──►│ 3. PENGAMATAN│──┐                   │
│  │               │    │               │    │               │  │                   │
│  │ • Definisi MVP│    │ • Sprint-based│    │ • User testing│  │                   │
│  │ • Tech stack  │    │   development │    │ • Data coll.  │  │                   │
│  │ • Studi literi│    │ • SDLC:       │    │ • Observation │  │                   │
│  │ • Fishbone    │    │   Waterfall+  │    │ • Think-aloud │  │                   │
│  │ • MATRIKS spec│    │   Prototype   │    │ • SUS survey  │  │                   │
│  └──────────────┘    └──────────────┘    └──────────────┘  │                   │
│                                                            │                   │
│                        ┌──────────────┐    ┌──────────────┐│                   │
│                        │ 5. PELAPORAN │◄───│ 4. REFLEKSI  │◄┘                   │
│                        │               │    │               │                    │
│                        │ • Dokumentasi │    │ • Retrospective                    │
│                        │ • Thesis write│    │ • Iterate design│                  │
│                        │ • Publikasi   │    │ • Fishbone rev │                  │
│                        │ • Source code │    │ • Revise MATRIKS│                  │
│                        └──────────────┘    └──────┬───────┘                   │
│                                                    │                           │
│                                                    ▼                           │
│                                              ┌──────────┐                     │
│                                              │ Iterasi? │── Yes ──► Kembali ke │
│                                              └────┬─────┘           Tahap 2     │
│                                                   │ No                            │
│                                                   ▼                               │
│                                              Selesai (Laporan)                  │
└─────────────────────────────────────────────────────────────────────────────────┘
```

### 4.3 Detail Setiap Tahapan

#### Tahap 1: PERENCANAAN (Planning)

| Aktivitas | Output | Metode MIX |
|-----------|--------|------------|
| Definisi MVP scope | Dokumen spesifikasi MVP | — |
| Pemilihan tech stack | Daftar teknologi (TF.js, MediaPipe, Kaplay.js, SQLite) | — |
| Studi literatur AI literacy | Kajian pustaka (Bab 2) | Kualitatif (literature review) |
| Analisis Fishbone 5-tulang | Diagram Fishbone + matriks per tulang | Kuantitatif (matriks) + Kualitatif (analisis naratif) |
| Definisi variabel & MATRIKS | Skema data log (lihat Bagian 5) | Kuantitatif (definisi variabel) |
| Desain eksperimen | Protokol pengujian | Kuantitatif (desain statistik) |

**Metrik keberhasilan tahap ini:**
- Fishbone diagram lengkap dengan 5 tulang
- Skema MATRIKS terdefinisi (kolom, tipe data, constraint)
- Protokol pengujian disetujui pembimbing

---

#### Tahap 2: PELAKSANAAN (Execution)

| Aktivitas | Output | Metode MIX |
|-----------|--------|------------|
| Sprint-based development | Prototype v0.1 → v1.0 | — |
| SDLC: Waterfall + Prototype | Dokumentasi per fase (Analysis → Design → Code → Test → Deploy) | — |
| Implementasi Decision Log System | Sistem pencatatan matriks otomatis | Kuantitatif (logging) |
| Implementasi AI inference (TF.js + CNN) | Model klasifikasi gambar client-side | Kuantitatif (akurasi, latency) |
| Implementasi HITL mechanism | Tombol Accept/Correct/Override | — |
| Implementasi level progression | 3 level dengan scaffolding | — |
| Integrasi Gemini API untuk narasi | Auto-generate "kesimpulan kalimat" | Kualitatif (narasi otomatis) |

**Metrik keberhasilan tahap ini:**
- Prototype v0.1: MVP 1 level, decision log berfungsi
- Prototype v0.2: 3 level lengkap, HITL berfungsi
- Prototype v1.0: Fitur lengkap, siap user testing

**SDLC: Waterfall + Prototype detail:**

```
  WATERFALL (Kerangka Utama)
  ═══════════════════════════

  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐
  │ Analysis │──►│  Design  │──►│  Code    │──►│  Test    │──►│ Deploy   │
  └──────────┘   └──────────┘   └──────────┘   └──────────┘   └──────────┘
       │              │              │              │              │
       ▼              ▼              ▼              ▼              ▼
  Requirements   Architecture    Implementation   Black-Box     Go Live
  Fishbone       Level Design    TF.js/MediaPipe  SUS           Production
  Variables      UI/UX Wireframe Kaplay.js        K-Means       Maintenance
  MATRIKS spec   Storyboard      Decision Log     t-test

  + PROTOTYPE (Validasi Inkremental)
  ══════════════════════════════════

  ┌────────────┐     ┌────────────┐     ┌────────────┐
  │  Prototype │────►│  Review &  │────►│  Refine    │──► (ulangi sampai OK)
  │  v0.1      │     │  Feedback  │     │  Prototype │
  │  (MVP: 1   │     │  (Bu Hesti │     │  v0.2,     │
  │   level)   │     │   + user   │     │  v0.3...)  │
  └────────────┘     │   testing) │     └────────────┘
                     └────────────┘
```

---

#### Tahap 3: PENGAMATAN (Observation)

| Aktivitas | Output | Metode MIX |
|-----------|--------|------------|
| User testing session | Decision log matriks (raw data) | **Kuantitatif** (matriks data) |
| Think-aloud recording | Transkrip audio | **Kualitatif** (narasi siswa) |
| Researcher observation | Field notes | **Kualitatif** (catatan perilaku) |
| SUS survey | Skor SUS per siswa | **Kuantitatif** (skor 0-100) |
| Post-simulation interview | Transkrip wawancara | **Kualitatif** (refleksi siswa) |
| Kondisi lingkungan dicatat | Matriks lingkungan per sesi | **Kuantitatif** (device, lighting, noise) |

**Protokol pengamatan:**

```
┌─────────────────────────────────────────────────────────────────┐
│                    SESI PENGAMATAN (per siswa)                   │
│                                                                 │
│  1. Pre-test (5 menit)                                         │
│     └── Kuesioner pengetahuan AI awal                           │
│                                                                 │
│  2. Simulasi (~25 menit)                                       │
│     ├── Level 1: Trust Building (AI jelas benar)               │
│     ├── Level 2: Ambiguity Zone (AI kurang yakin)              │
│     └── Level 3: Critical Override (AI menyesatkan)            │
│     │                                                           │
│     │ Selama simulasi:                                          │
│     ├── Decision log matriks tercatat otomatis                 │
│     ├── Think-aloud direkam (opsional)                         │
│     └── Observer mencatat field notes                           │
│                                                                 │
│  3. Post-test (5 menit)                                        │
│     ├── Kuesioner pengetahuan AI akhir                          │
│     ├── SUS survey (10 pernyataan)                              │
│     └── Open-ended questions (perubahan persepsi)              │
│                                                                 │
│  4. Interview (5-10 menit)                                     │
│     └── Wawancara semi-terstruktur                              │
│                                                                 │
│  Total: ~40-45 menit per siswa                                  │
│  Catatan lingkungan: device spec, lighting, noise, internet     │
└─────────────────────────────────────────────────────────────────┘
```

---

#### Tahap 4: REFLEKSI (Reflection)

| Aktivitas | Output | Metode MIX |
|-----------|--------|------------|
| K-Means clustering | Cluster profiles | **Kuantitatif** (unsupervised ML) |
| Paired t-test | p-value, effect size | **Kuantitatif** (statistik inferensial) |
| Thematic analysis | Tema-tema perilaku | **Kualitatif** (Braun & Clarke) |
| AI auto-generate narasi | Kesimpulan kalimat per cluster/siswa | **Kualitatif** (AI-assisted) |
| Triangulasi | Temuan terintegrasi | **MIX** (kuantitatif + kualitatif) |
| Retrospective desain | Rekomendasi perbaikan | **Kualitatif** (refleksi peneliti) |
| Fishbone revision | Updated Fishbone diagram | **MIX** (data-driven revision) |

**Keputusan iterasi:**

```
┌─────────────────────────────────────────┐
│         REFLEKSI CHECKPOINT             │
│                                         │
│  Apakah data MATRIKS menunjukkan        │
│  pola yang bisa diinterpretasi?         │
│       │           │                     │
│      YES          NO                    │
│       │           │                     │
│       ▼           ▼                     │
│  Triangulasi   Revisi protokol          │
│  dengan KUAL   pengamatan               │
│       │           │                     │
│       ▼           ▼                     │
│  Apakah      Kembali ke Tahap 3         │
│  temuan      (Pengamatan) dengan         │
│  robust?      protokol yang direvisi    │
│       │                                  │
│      YES → Lanjut ke Tahap 5            │
└─────────────────────────────────────────┘
```

---

#### Tahap 5: PELAPORAN (Reporting)

| Aktivitas | Output | Metode MIX |
|-----------|--------|------------|
| Dokumentasi hasil | Laporan penelitian lengkap | **MIX** (kuantitatif + kualitatif) |
| Thesis writing | Bab 1-5 lengkap | — |
| Cluster profiles + narasi | Temuan terintegrasi per cluster | **MIX** |
| Fishbone final | Diagram Fishbone revisi final | **MIX** |
| Source code & data | Repository + dataset matriks | — |
| Presentasi sidang | Slide deck | — |

### 4.4 Timeline Metopen

| Tahapan | Aktivitas Utama | Output | Durasi |
|---------|----------------|--------|--------|
| **1. Perencanaan** | Studi literatur, Fishbone, definisi variabel & MATRIKS, desain eksperimen | Fishbone diagram, skema MATRIKS, protokol pengujian | 4-5 minggu |
| **2. Pelaksanaan** | Sprint-based development, SDLC Waterfall+Prototype, Decision Log, Gemini API | Prototype v0.1 → v1.0 | 8-10 minggu |
| **3. Pengamatan** | User testing, think-aloud, SUS, interview, catatan lingkungan | Decision log matriks, transkrip, SUS scores, field notes | 2-3 minggu |
| **4. Refleksi** | K-Means, t-test, thematic analysis, triangulasi, retrospective | Cluster profiles, temuan terintegrasi, rekomendasi perbaikan | 3-4 minggu |
| **5. Pelaporan** | Dokumentasi, thesis writing, presentasi | Laporan lengkap, thesis Bab 1-5, source code | 4-5 minggu |

---

## 5. Data Log Schema (Definitif)

### 5.1 Skema Relasional

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         DATA LOG SCHEMA (Definitif)                         │
│                                                                             │
│  ┌──────────────┐      ┌──────────────┐      ┌──────────────────┐          │
│  │   users      │      │  sessions    │      │  decision_log    │          │
│  │──────────────│      │──────────────│      │──────────────────│          │
│  │ user_id (PK) │◄─────│ user_id (FK) │◄─────│ session_id (FK)  │          │
│  │ username     │      │ session_id(PK)│      │ log_id (PK)      │          │
│  │ age          │      │ started_at   │      │ level            │          │
│  │ class_grade  │      │ ended_at     │      │ confidence_score │          │
│  │ school       │      │ device_type  │      │ decision_type    │          │
│  │ created_at   │      │ browser      │      │ latency_ms       │          │
│  └──────────────┘      │ device_ram_gb│      │ override_ratio   │          │
│                        │ net_speed_mbps│     │ ai_prediction    │          │
│                        │ lighting_cond│      │ user_label       │          │
│                        │ noise_level  │      │ is_correct       │          │
│                        │ time_slot    │      │ hint_used        │          │
│                        └──────┬───────┘      │ feedback_shown   │          │
│                               │              │ created_at       │          │
│                               │              └──────┬───────────┘          │
│                               │                     │                      │
│  ┌──────────────┐      ┌─────┴────────┐     ┌──────┴───────────┐          │
│  │  pre_test    │      │  sus_results │     │  cluster_assign  │          │
│  │──────────────│      │──────────────│     │──────────────────│          │
│  │ user_id (FK) │      │ user_id (FK) │     │ user_id (FK)     │          │
│  │ q1..q10      │      │ q1..q10      │     │ cluster_id       │          │
│  │ total_score  │      │ sus_score    │     │ cluster_name     │          │
│  │ created_at   │      │ grade        │     │ confidence_pct   │          │
│  └──────────────┘      │ created_at   │     │ assigned_at      │          │
│  ┌──────────────┐      └──────────────┘     └──────────────────┘          │
│  │  post_test   │                                                           │
│  │──────────────│      ┌──────────────────────┐                            │
│  │ user_id (FK) │      │  env_conditions      │                            │
│  │ q1..q10      │      │──────────────────────│                            │
│  │ total_score  │      │ session_id (FK)       │                            │
│  │ delta_score  │      │ device_spec           │                            │
│  │ created_at   │      │ lighting_condition    │                            │
│  └──────────────┘      │ noise_level_db        │                            │
│                        │ internet_speed_mbps   │                            │
│                        │ lab_room              │                            │
│                        │ observer_name         │                            │
│                        │ notes                 │                            │
│                        └──────────────────────┘                            │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 5.2 Definisi Tabel: `decision_log` (Tabel Utama)

| Kolom | Tipe | Constraint | Deskripsi | Contoh |
|-------|------|-----------|-----------|--------|
| `log_id` | INTEGER | PRIMARY KEY AUTOINCREMENT | ID unik log | 1, 2, 3 |
| `session_id` | TEXT | FOREIGN KEY → sessions | ID sesi penggunaan | `SESS_20260704_S001` |
| `user_id` | TEXT | FOREIGN KEY → users | ID siswa | `S001` |
| `level` | INTEGER | NOT NULL, CHECK (1-3) | Level simulasi | 1, 2, 3 |
| `round` | INTEGER | NOT NULL | Nomor ronde dalam level | 1, 2, 3, ... |
| `confidence_score` | REAL | NOT NULL, CHECK (0-100) | Confidence AI saat keputusan (%) | 92.5, 65.0, 41.3 |
| `ai_prediction` | TEXT | NOT NULL | Label prediksi AI | `kucing`, `rumah` |
| `ai_top3` | TEXT | JSON array | Top-3 prediksi + confidence | `[{"label":"kucing","conf":65},{"label":"anjing","conf":22},{"label":"burung","conf":8}]` |
| `decision_type` | TEXT | NOT NULL, CHECK ('compliance','override') | Keputusan siswa | `compliance`, `override` |
| `user_label` | TEXT | NULLABLE | Label yang dipilih siswa (jika override) | `anjing` (override), NULL (compliance) |
| `is_correct` | INTEGER | NOT NULL, CHECK (0,1) | Apakah keputusan siswa benar? | 1, 0 |
| `latency_ms` | INTEGER | NOT NULL | Waktu keputusan (ms) | 1200, 4500 |
| `override_ratio` | REAL | NOT NULL, CHECK (0-1) | Kumulatif override ratio hingga ronde ini | 0.00, 0.33, 0.50 |
| `hint_used` | INTEGER | NOT NULL, CHECK (0,1) | Apakah hint digunakan? | 0, 1 |
| `feedback_shown` | INTEGER | NOT NULL, CHECK (0,1) | Apakah feedback ditampilkan? | 1 |
| `object_category` | TEXT | NOT NULL, CHECK ('solid','danger') | Kategori objek (Bu Hesti: hanya solid & danger) | `solid`, `danger` |
| `created_at` | TEXT | NOT NULL, DEFAULT CURRENT_TIMESTAMP | Waktu pencatatan | `2026-07-04T10:23:45` |

### 5.3 Definisi Tabel: `sessions` (Sesi Penggunaan)

| Kolom | Tipe | Constraint | Deskripsi | Contoh |
|-------|------|-----------|-----------|--------|
| `session_id` | TEXT | PRIMARY KEY | ID sesi unik | `SESS_20260704_S001` |
| `user_id` | TEXT | FOREIGN KEY → users | ID siswa | `S001` |
| `started_at` | TEXT | NOT NULL | Waktu mulai sesi | `2026-07-04T10:00:00` |
| `ended_at` | TEXT | NULLABLE | Waktu selesai sesi | `2026-07-04T10:35:00` |
| `device_type` | TEXT | NOT NULL | Jenis perangkat | `laptop`, `tablet` |
| `browser` | TEXT | NOT NULL | Browser + versi | `Chrome 126` |
| `device_ram_gb` | INTEGER | NULLABLE | RAM perangkat (GB) | 8, 4, 2 |
| `net_speed_mbps` | REAL | NULLABLE | Kecepatan internet (Mbps) | 50.0, 10.0 |
| `lighting_cond` | TEXT | NULLABLE, CHECK ('good','moderate','poor') | Kondisi pencahayaan | `good`, `poor` |
| `noise_level` | TEXT | NULLABLE, CHECK ('low','medium','high') | Tingkat kebisingan | `low`, `high` |
| `time_slot` | TEXT | NOT NULL | Slot waktu penggunaan | `08:00-08:45` |

### 5.4 Definisi Tabel: `cluster_assign` (Hasil K-Means)

| Kolom | Tipe | Constraint | Deskripsi | Contoh |
|-------|------|-----------|-----------|--------|
| `user_id` | TEXT | PRIMARY KEY, FOREIGN KEY → users | ID siswa | `S001` |
| `cluster_id` | INTEGER | NOT NULL | Nomor cluster | 0, 1, 2 |
| `cluster_name` | TEXT | NOT NULL | Nama deskriptif cluster | `Blind Trusters`, `Critical Thinkers`, `AI Skeptics` |
| `confidence_pct` | REAL | NOT NULL | Confidence assignment K-Means | 0.89 |
| `avg_override_ratio` | REAL | NOT NULL | Rata-rata override ratio siswa | 0.33 |
| `avg_latency_ms` | REAL | NOT NULL | Rata-rata latency siswa | 2400 |
| `n_decisions` | INTEGER | NOT NULL | Jumlah keputusan yang dicatat | 15 |
| `auto_conclusion` | TEXT | NOT NULL | Kesimpulan kalimat (auto-generated) | "Siswa menunjukkan peningkatan..." |
| `assigned_at` | TEXT | NOT NULL, DEFAULT CURRENT_TIMESTAMP | Waktu assignment | `2026-07-04T12:00:00` |

---

## 6. SQL Analytics View (Auto-Conclusion)

### 6.1 View: `v_user_profile` — Profil Per Siswa

```sql
CREATE VIEW v_user_profile AS
SELECT
    u.user_id,
    u.age,
    u.class_grade,
    s.session_id,
    s.device_type,
    s.browser,
    s.device_ram_gb,
    s.lighting_cond,
    s.noise_level,

    -- KUANTITATIF: Metrik dari matriks decision log
    COUNT(dl.log_id)                                          AS total_decisions,
    SUM(CASE WHEN dl.decision_type = 'override' THEN 1 ELSE 0 END)
        * 1.0 / COUNT(dl.log_id)                             AS overall_override_ratio,
    AVG(dl.latency_ms)                                        AS avg_latency_ms,
    AVG(dl.confidence_score)                                  AS avg_confidence_faced,

    -- Override ratio per level
    AVG(CASE WHEN dl.level = 1 THEN dl.override_ratio END)   AS override_ratio_l1,
    AVG(CASE WHEN dl.level = 2 THEN dl.override_ratio END)   AS override_ratio_l2,
    AVG(CASE WHEN dl.level = 3 THEN dl.override_ratio END)   AS override_ratio_l3,

    -- Latency per level
    AVG(CASE WHEN dl.level = 1 THEN dl.latency_ms END)       AS latency_l1,
    AVG(CASE WHEN dl.level = 2 THEN dl.latency_ms END)       AS latency_l2,
    AVG(CASE WHEN dl.level = 3 THEN dl.latency_ms END)       AS latency_l3,

    -- Accuracy
    SUM(CASE WHEN dl.is_correct = 1 THEN 1 ELSE 0 END)
        * 1.0 / COUNT(dl.log_id)                             AS decision_accuracy,

    -- Hint usage
    SUM(dl.hint_used) * 1.0 / COUNT(dl.log_id)              AS hint_usage_rate,

    -- Pre/Post test delta
    pt.total_score                                            AS pre_test_score,
    pt2.total_score                                           AS post_test_score,
    (pt2.total_score - pt.total_score)                        AS delta_score,

    -- SUS
    sr.sus_score,
    sr.grade                                                  AS sus_grade

FROM users u
JOIN sessions s ON u.user_id = s.user_id
JOIN decision_log dl ON s.session_id = dl.session_id
LEFT JOIN pre_test pt ON u.user_id = pt.user_id
LEFT JOIN post_test pt2 ON u.user_id = pt2.user_id
LEFT JOIN sus_results sr ON u.user_id = sr.user_id
GROUP BY u.user_id, s.session_id;
```

### 6.2 View: `v_cluster_summary` — Ringkasan Per Cluster

```sql
CREATE VIEW v_cluster_summary AS
SELECT
    ca.cluster_id,
    ca.cluster_name,
    COUNT(*)                                                  AS n_students,
    AVG(ca.avg_override_ratio)                                AS cluster_avg_override,
    AVG(ca.avg_latency_ms)                                    AS cluster_avg_latency,
    AVG(vp.decision_accuracy)                                 AS cluster_avg_accuracy,
    AVG(vp.sus_score)                                         AS cluster_avg_sus,
    AVG(vp.delta_score)                                       AS cluster_avg_delta_score
FROM cluster_assign ca
JOIN v_user_profile vp ON ca.user_id = vp.user_id
GROUP BY ca.cluster_id, ca.cluster_name;
```

### 6.3 View: `v_auto_conclusion` — Auto-Generated Kesimpulan Kalimat

```sql
CREATE VIEW v_auto_conclusion AS
SELECT
    vp.user_id,
    vp.age,
    vp.total_decisions,
    vp.overall_override_ratio,
    vp.avg_latency_ms,
    vp.avg_confidence_faced,
    vp.decision_accuracy,
    vp.override_ratio_l1,
    vp.override_ratio_l3,
    vp.delta_score,
    vp.sus_score,
    ca.cluster_name,

    -- ═══════════════════════════════════════════════════════════
    -- KESIMPULAN KALIMAT (Auto-Generated via SQL CASE WHEN)
    -- Catatan: Versi lengkap menggunakan AI API (Gemini) untuk
    -- narasi yang lebih kaya. SQL CASE WHEN ini sebagai baseline.
    -- ═══════════════════════════════════════════════════════════

    -- Pattern 1: Override trajectory
    CASE
        WHEN vp.override_ratio_l3 > vp.override_ratio_l1 + 0.2
        THEN 'Siswa menunjukkan peningkatan signifikan override dari level awal ke akhir, mengindikasikan transisi dari blind trust ke critical evaluation.'
        WHEN vp.override_ratio_l3 > vp.override_ratio_l1 + 0.05
        THEN 'Siswa menunjukkan peningkatan moderat override seiring kemajuan level, mengindikasikan perkembangan calibrated decision-making.'
        WHEN vp.override_ratio_l3 <= vp.override_ratio_l1
        THEN 'Siswa tidak menunjukkan peningkatan override; pola compliance tetap konsisten, mengindikasikan persistensi blind trust atau kepercayaan yang tepat terhadap AI.'
        ELSE 'Data tidak cukup untuk menentukan pola override.'
    END AS conclusion_override_trajectory,

    -- Pattern 2: Decision accuracy vs confidence
    CASE
        WHEN vp.avg_confidence_faced > 70 AND vp.decision_accuracy < 0.5
        THEN 'Siswa menghadapi confidence score tinggi namun akurasi keputusan rendah, mengindikasikan kemungkinan over-trust terhadap AI yang salah.'
        WHEN vp.avg_confidence_faced < 50 AND vp.decision_accuracy > 0.7
        THEN 'Siswa berhasil membuat keputusan akurat meskipun confidence score AI rendah, mengindikasikan kemampuan evaluasi independen yang baik.'
        WHEN vp.avg_confidence_faced < 50 AND vp.decision_accuracy < 0.5
        THEN 'Siswa mengalami kesulitan ketika confidence score AI rendah, mengindikasikan kebutuhan scaffolding lebih lanjut di zona ambiguitas.'
        ELSE 'Pola keputusan siswa sejalan dengan confidence score AI.'
    END AS conclusion_accuracy_pattern,

    -- Pattern 3: Latency pattern
    CASE
        WHEN vp.avg_latency_ms > 4000 AND vp.overall_override_ratio > 0.3
        THEN 'Siswa menunjukkan deliberasi tinggi (latency lambat) dengan override signifikan, mengindikasikan proses evaluasi yang mendalam sebelum keputusan.'
        WHEN vp.avg_latency_ms < 1500 AND vp.overall_override_ratio < 0.1
        THEN 'Siswa menunjukkan keputusan cepat dengan compliance tinggi, mengindikasikan kemungkinan automation bias — menerima saran AI tanpa evaluasi.'
        WHEN vp.avg_latency_ms > 4000 AND vp.overall_override_ratio < 0.1
        THEN 'Siswa menunjukkan deliberasi tinggi namun tetap compliance, mengindikasikan ketidakpastian yang membuat siswa memilih "aman" mengikuti AI.'
        ELSE 'Pola latency siswa seimbang antara deliberasi dan respons.'
    END AS conclusion_latency_pattern,

    -- Pattern 4: Learning gain
    CASE
        WHEN vp.delta_score > 20
        THEN 'Siswa menunjukkan peningkatan pengetahuan AI yang signifikan (delta score > 20), mengindikasikan efektivitas simulasi dalam membangun pemahaman.'
        WHEN vp.delta_score BETWEEN 5 AND 20
        THEN 'Siswa menunjukkan peningkatan pengetahuan AI yang moderat, mengindikasikan dampak parsial dari simulasi.'
        WHEN vp.delta_score <= 5
        THEN 'Siswa tidak menunjukkan peningkatan pengetahuan AI yang berarti, mengindikasikan kebutuhan revisi konten atau durasi simulasi.'
        ELSE 'Data pre/post test tidak tersedia.'
    END AS conclusion_learning_gain,

    -- ═══════════════════════════════════════════════════════════
    -- SYNTHESIS: Kesimpulan terintegrasi (untuk AI API enhancement)
    -- ═══════════════════════════════════════════════════════════
    CASE
        WHEN ca.cluster_name = 'Blind Trusters'
        THEN 'Siswa terklasifikasi sebagai Blind Truster: cenderung menerima rekomendasi AI tanpa evaluasi kritis. Rekomendasi: tingkatkan controlled ambiguity di level awal untuk memecah pola compliance otomatis.'
        WHEN ca.cluster_name = 'Critical Thinkers'
        THEN 'Siswa terklasifikasi sebagai Critical Thinker: menunjukkan kemampuan evaluasi terhadap output AI dan override ketika tepat. Rekomendasi: pertahankan level progression saat ini; siswa ini mendapat manfaat optimal dari simulasi.'
        WHEN ca.cluster_name = 'AI Skeptics'
        THEN 'Siswa terklasifikasi sebagai AI Skeptic: cenderung menolak rekomendasi AI meskipun AI benar. Rekomendasi: tambahkan skenario di mana AI jelas benar untuk menunjukkan bahwa trust yang tepat juga penting.'
        ELSE 'Cluster belum di-assign. Jalankan K-Means terlebih dahulu.'
    END AS conclusion_cluster_synthesis

FROM v_user_profile vp
JOIN cluster_assign ca ON vp.user_id = ca.user_id;
```

### 6.4 Query: AI API Integration Prompt Template

```sql
-- Template untuk mengirim data ke Gemini API
-- Output query ini di-feed ke AI API sebagai prompt context

SELECT json_object(
    'user_id', vp.user_id,
    'cluster', ca.cluster_name,
    'metrics', json_object(
        'override_ratio', ROUND(vp.overall_override_ratio, 2),
        'avg_latency_ms', ROUND(vp.avg_latency_ms, 0),
        'avg_confidence_faced', ROUND(vp.avg_confidence_faced, 1),
        'decision_accuracy', ROUND(vp.decision_accuracy, 2),
        'override_l1', ROUND(COALESCE(vp.override_ratio_l1, 0), 2),
        'override_l3', ROUND(COALESCE(vp.override_ratio_l3, 0), 2),
        'delta_score', COALESCE(vp.delta_score, 0),
        'sus_score', COALESCE(vp.sus_score, 0)
    ),
    'fishbone_context', json_object(
        'manusia', json_object('age', vp.age, 'cluster', ca.cluster_name),
        'metode', json_object('hint_usage_rate', ROUND(vp.hint_usage_rate, 2)),
        'mesin', json_object('device_type', vp.device_type, 'device_ram_gb', vp.device_ram_gb),
        'lingkungan', json_object('lighting', vp.lighting_cond, 'noise', vp.noise_level)
    )
) AS api_payload
FROM v_user_profile vp
JOIN cluster_assign ca ON vp.user_id = ca.user_id
WHERE vp.user_id = :target_user_id;
```

**Prompt template untuk Gemini API:**

```
Kamu adalah analis data penelitian pendidikan. Berdasarkan matriks data berikut,
buATlah kesimpulan kalimat (maksimal 3 kalimat) yang menjelaskan pola perilaku
siswa dalam simulasi literasi AI. Sertakan aspek Fishbone yang relevan.

DATA MATRIKS:
{api_payload}

FORMAT OUTPUT:
- Kalimat 1: Pola utama perilaku (berdasarkan override trajectory & latency)
- Kalimat 2: Faktor Fishbone yang paling mempengaruhi (Man/Metode/Mesin/Materi/Lingkungan)
- Kalimat 3: Rekomendasi perbaikan untuk siswa ini
```

### 6.5 View: `v_fishbone_analysis` — Cross-Tab Fishbone

```sql
CREATE VIEW v_fishbone_analysis AS
SELECT
    -- Tulang: LINGKUNGAN
    s.lighting_cond,
    s.noise_level,
    s.device_type,
    s.device_ram_gb,

    -- Tulang: MANUSIA (via cluster)
    ca.cluster_name,

    -- Tulang: METODE (hint & feedback usage)
    AVG(dl.hint_used) * 1.0   AS avg_hint_usage,
    AVG(dl.feedback_shown) * 1.0 AS avg_feedback_shown,

    -- Tulang: MESIN (inference-related)
    AVG(dl.latency_ms)        AS avg_decision_latency,

    -- Tulang: MATERI (confidence & accuracy)
    AVG(dl.confidence_score)  AS avg_confidence_shown,
    SUM(dl.is_correct) * 1.0 / COUNT(*) AS decision_accuracy,

    -- Cross-tab: Environment × Cluster
    COUNT(*)                  AS n_observations

FROM decision_log dl
JOIN sessions s ON dl.session_id = s.session_id
JOIN cluster_assign ca ON dl.user_id = ca.user_id
GROUP BY s.lighting_cond, s.noise_level, s.device_type, ca.cluster_name;
```

---

## 7. Referensi Akademik

### Fishbone & Ishikawa

| No | Referensi | Topik |
|----|-----------|-------|
| [1] | Ishikawa, K. (1982). *Guide to Quality Control*. Asian Productivity Organization. | Diagram Ishikawa, root cause analysis |
| [2] | Brassard, M. (1989). *The Memory Jogger Plus+*. GOAL/QPC. | 7M/6M framework, cause-effect tools |
| [3] | Sugiyono. (2019). *Metode Penelitian Pendidikan: Pendekatan Kuantitatif, Kualitatif, dan R&D*. Alfabeta. | Metopen, fishbone dalam konteks pendidikan Indonesia |

### Mixed Methods

| No | Referensi | Topik |
|----|-----------|-------|
| [4] | Creswell, J. W., & Plano Clark, V. L. (2018). *Designing and Conducting Mixed Methods Research* (3rd ed.). SAGE. | Connecting approach, triangulasi |
| [5] | Johnson, R. B., & Onwuegbuzie, A. J. (2004). Mixed Methods Research: A Research Paradigm Whose Time Has Come. *Educational Researcher*, 33(7), 14-26. | Justifikasi mixed methods |
| [6] | Braun, V., & Clarke, V. (2006). Using Thematic Analysis in Psychology. *Qualitative Research in Psychology*, 3(2), 77-101. | 6-tahap thematic analysis |

### Automation Bias & Trust in AI

| No | Referensi | Topik |
|----|-----------|-------|
| [7] | Parasuraman, R., & Riley, V. (1997). Humans and Automation: Use, Misuse, Disuse, Abuse. *Human Factors*, 39(2), 230-253. | Automation bias, trust calibration |
| [8] | Lee, J. D., & See, K. A. (2004). Trust in Automation: Designing for Appropriate Reliance. *Human Factors*, 46(1), 50-80. | Appropriate trust, over-reliance |
| [9] | Bommasani, R., et al. (2022). *On the Opportunities and Risks of Foundation Models*. Stanford CRFM. | Foundation model risks, HITL |

### AI Literacy & HITL

| No | Referensi | Topik |
|----|-----------|-------|
| [10] | Ng, D. T. K., Leung, J. K. L., Chu, S. K. W., & Qiao, M. S. (2021). Conceptualizing AI Literacy: An Exploratory Review. *Computers and Education: Artificial Intelligence*, 2, 100041. | AI literacy framework |
| [11] | Long, D., & Magerko, B. (2020). What is AI Literacy? Competencies and Design Considerations. *CHI '20*, 1-16. | AI literacy competencies |
| [12] | Mosqueira-Rey, E., et al. (2023). HITL machine learning: A state of the art. *AI Review*, 56, 3005-3054. | Human-in-the-loop ML |
| [13] | Memarian, B., & Doleck, T. (2024). HITL in AIED. *Computers in Human Behavior: Artificial Humans*, 2, 100053. | HITL in AI education |

### K-Means & Clustering

| No | Referensi | Topik |
|----|-----------|-------|
| [14] | MacQueen, J. (1967). Some Methods for Classification and Analysis of Multivariate Observations. *Proceedings of the 5th Berkeley Symposium*, 281-297. | K-Means original |
| [15] | Arthur, D., & Vassilvitskii, S. (2007). K-Means++: The Advantages of Careful Seeding. *SODA '07*. | K-Means++ initialization |
| [16] | Pansri, P., et al. (2024). Understanding student learning behavior: K-Means. *Education Sciences*, 14(12), 1291. | K-Means untuk perilaku belajar |
| [17] | Alzahrani, A., et al. (2025). Identifying weekly student engagement via K-Means. *Electronics*, 14(15), 3018. | K-Means untuk student engagement |

### SUS (System Usability Scale)

| No | Referensi | Topik |
|----|-----------|-------|
| [18] | Brooke, J. (1996). SUS: A 'Quick and Dirty' Usability Scale. *Usability Evaluation in Industry*, 189-194. | SUS methodology |
| [19] | Bangor, A., Kortum, P., & Miller, J. (2009). Determining What Individual SUS Scores Mean: Adding an Adjective Rating Scale. *Journal of Usability Studies*, 4(3), 114-123. | SUS interpretation |

### R&D & Metopen

| No | Referensi | Topik |
|----|-----------|-------|
| [20] | Borg, W. R., & Gall, M. D. (1983). *Educational Research: An Introduction* (4th ed.). Longman. | R&D methodology |
| [21] | Casal-Otero, V., et al. (2023). AI literacy in K-12. *Intl J STEM Education*, 10, 29. | AI literacy K-12, CCI |

### Explainable AI & Confidence

| No | Referensi | Topik |
|----|-----------|-------|
| [22] | Khosravi, H., et al. (2022). XAI in education. *Computers and Education: AI*, 3, 100074. | Explainable AI for education |
| [23] | Karran, A., Demazure, T., & Hudelot, C. (2022). Designing for confidence. *Frontiers in Neuroscience*, 16. | Confidence visualization |

### Game-Based Learning

| No | Referensi | Topik |
|----|-----------|-------|
| [24] | Videnovik, M., et al. (2023). Game-based learning in CS education. *Intl J STEM Education*, 10, 54. | GBL effectiveness |
| [25] | Chan, R., Wan, J., & King, V. (2021). Performance over enjoyment? *Frontiers in Education*, 6, 660376. | Flow theory in GBL |

---

> **Catatan terakhir**: Dokumen ini menggantikan `08_cache/metodologi_raw.md` sebagai sumber definitif untuk metodologi penelitian. Perubahan utama: (1) Fishbone 4→5 tulang dengan Lingkungan, (2) Metopen Framework 5 tahapan, (3) Data Log Schema definitif, (4) SQL Analytics View dengan auto-conclusion, (5) Reconciled 5M+1E terminology. Setiap perubahan dari diskusi dengan Bu Hesti atau temuan baru dari riset harus di-update di sini.
