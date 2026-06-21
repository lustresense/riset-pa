# Metodologi Penelitian: Simulasi Interaktif Literasi AI untuk Siswa SMP Kelas 7-9

## Project: "Escape the Sketchbook" — HITL AI Literacy Simulation

> **Dibuat:** 2026-06-15  
> **Revisi:** 2026-03-05 — Overhaul total: struktur Fishbone 4-tulang, Metodologi MIX, distingsi Metrik vs Matriks  
> **Status:** Living Document — update kalau ada perubahan dari diskusi/dosen  
> **Konteks:** Can (D4 TRM PENS) — saran Bu Hesti: Metodologi MIX (Kuantitatif + Kualitatif) + Fishbone analysis  

---

## DAFTAR ISI

1. [Diagram Fishbone (Ishikawa) — 4 Tulang](#1-diagram-fishbone-ishikawa--4-tulang)
2. [Metodologi MIX (Kuantitatif + Kualitatif)](#2-metodologi-mix-kuantitatif--kualitatif)
3. [Distingsi Kritis: Metrik vs Matriks](#3-distingsi-kritis-metrik-vs-matriks)
4. [Kerangka R&D (Research & Development)](#4-kerangka-rd-research--development)
5. [Metode Pengujian](#5-metode-pengujian)
6. [Daftar Referensi Akademik](#6-daftar-referensi-akademik)

---

## 1. Diagram Fishbone (Ishikawa) — 4 Tulang

### 1.1 Mengapa 4 Tulang, Bukan 6M Tradisional?

Diagram Ishikawa tradisional menggunakan **6M** (Man, Machine, Method, Material, Measurement, Mother Nature). Namun untuk konteks **simulasi interaktif literasi AI di SMP**, 6M terlalu generik dan ada overlap yang membingungkan. Oleh karena itu, kita menggunakan **4 tulang** yang disesuaikan dengan domain penelitian ini:

| Tulang | Fokus | Mengapa Relevan? |
|--------|-------|-------------------|
| **Manusia** | Faktor siswa (subjek penelitian) | Siswa SMP adalah pengguna utama; kognisi & bias mereka yang diukur |
| **Metode** | Pendekatan pengajaran | HITL, controlled ambiguity, dan level progression adalah inti desain pedagogis |
| **Media** | Platform dan teknologi | Browser-based, TF.js, MediaPipe, Kaplay.js adalah infrastruktur yang memungkinkan |
| **Materi** | Konten edukasi | Confidence score, probabilitas AI, decision-making adalah substansi yang diajarkan |

Keempat tulang ini membentuk **ecosystem model** — setiap tulang saling mempengaruhi dan tidak bisa dipisahkan. Misalnya: **Metode** (HITL) mempengaruhi bagaimana **Materi** (confidence score) disampaikan, yang kemudian mempengaruhi **Manusia** (automation bias siswa), dan semuanya berjalan di atas **Media** (browser).

---

### 1.2 Diagram Fishbone ASCII

```
                                                                         ┌─────────────────────────────────┐
                                                                         │         MATERI (Materi)         │
                                                                         │  Konten Edukasi AI Literacy     │
                                                                         │                                 │
                                                                         │  • Confidence Score (0-100%)     │
                                                                         │  • Probabilitas AI & Margin of  │
                                                                         │    Error                        │
                                                                         │  • Decision-Making Framework    │
                                                                         │  • Override vs Compliance       │
                                                                         │    Scenario                     │
                                                                         │  • Eksplanasi AI "Why"          │
                                                                         │  • Skala Ketidakpastian         │
                                                                         │                                 │
                                                                         └──────────────┬──────────────────┘
                                                                                        │
┌─────────────────────────────────┐                                     ┌──────────────┴──────────────────┐
│         MANUSIA (Manusia)        │                                     │                                  │
│      Faktor Siswa SMP 7-9       │                                     │      EFEK (Problem Statement)    │
│                                 │                                     │                                  │
│  • Automation Bias              ├─────────────────────────────────────►│  Rendahnya Literasi AI pada      │
│  • Pengalaman Teknologi         │                                     │  Siswa SMP Kelas 7-9             │
│  • Usia Kognitif (12-15 th)     │                                     │  (Blind Trust / Rejection        │
│  • Digital Native Assumption    │                                     │   Extremes)                      │
│  • Prior AI Knowledge           │                                     │                                  │
│  • Trust Calibration Ability    │                                     │  ──► Target: Siswa mampu         │
│  • Risk Perception              │                                     │  mengkritisi keputusan AI,       │
│                                 │                                     │  bukan hanya mengikuti           │
└─────────────────────────────────┘                                     └──────────────┬──────────────────┘
                                                                                        │
                                                                       ┌──────────────┴──────────────────┐
                                                                       │         METODE (Metode)          │
                                                                       │    Pendekatan Pengajaran         │
                                                                       │                                  │
                                                                       │  • HITL (Human-in-the-Loop)      │
                                                                       │  • Controlled Ambiguity          │
                                                                       │    (ambiguitas terkendali)        │
                                                                       │  • Level Progression             │
                                                                       │    (mudah → sulit)                │
                                                                       │  • Scaffolding & Hint System     │
                                                                       │  • Immediate Feedback Loop       │
                                                                       │  • Decision Override Mechanism   │
                                                                       │                                  │
                                                                       └──────────────┬──────────────────┘
                                                                                      │
                                                                       ┌──────────────┴──────────────────┐
                                                                       │          MEDIA (Media)           │
                                                                       │   Platform dan Teknologi         │
                                                                       │                                  │
                                                                       │  • Browser-based (No Install)    │
                                                                       │  • TensorFlow.js (Inference)     │
                                                                       │  • MediaPipe (Gesture Input)     │
                                                                       │  • Kaplay.js (Game Engine)       │
                                                                       │  • Decision Log System           │
                                                                       │  • Responsive Web Design         │
                                                                       │  • Client-side Processing        │
                                                                       │                                  │
                                                                       └─────────────────────────────────┘
```

**Versi ringkas (diagram kerangka):**

```
    MANUSIA                    MATERI
   (Siswa)                   (Konten)
      \                        /
       \                      /
        \                    /
         +---→ EFEK ←------+
         |   (Literasi AI)  |
        /                    \
       /                      \
      /                        \
   METODE                    MEDIA
  (Pengajaran)            (Teknologi)
```

---

### 1.3 Penjelasan Detail Setiap Tulang

#### 🧑 Tulang 1: MANUSIA — Faktor Siswa

Tulang ini menganalisis **karakteristik subjek penelitian** (siswa SMP kelas 7-9, usia 12-15 tahun) sebagai faktor yang mempengaruhi literasi AI.

| Sub-faktor | Penjelasan | Indikator dalam Simulasi |
|------------|------------|--------------------------|
| **Automation Bias** | Kecenderungan manusia untuk secara otomatis menerima saran dari sistem komputer tanpa verifikasi kritis (Parasuraman & Riley, 1997) | Siswa langsung "ya" ke rekomendasi AI tanpa mempertimbangkan confidence score |
| **Pengalaman Teknologi** | Tingkat paparan dan kenyamanan siswa dengan teknologi digital | Seberapa sering siswa menggunakan AI tools (ChatGPT, dll.) sebelum simulasi |
| **Usia Kognitif** | Tahap perkembangan kognitif Piaget — siswa SMP berada di transisi concrete-operational ke formal-operational | Kemampuan memahami konsep abstrak seperti probabilitas dan ketidakpastian |
| **Digital Native Assumption** | Asumsi bahwa generasi muda otomatis paham teknologi — padahal literasi AI berbeda dari literasi digital | Siswa mungkin bisa menggunakan gadget tapi tidak memahami bagaimana AI membuat keputusan |
| **Prior AI Knowledge** | Pengetahuan awal tentang AI sebelum mengikuti simulasi | Pre-test score tentang konsep dasar AI |
| **Trust Calibration Ability** | Kemampuan menyesuaikan tingkat kepercayaan sesuai kemampuan aktual sistem | Override ratio — kapan siswa memilih menolak saran AI |
| **Risk Perception** | Bagaimana siswa mempersepsi risiko dari keputusan yang salah | Reaksi siswa ketika AI memberikan jawaban yang salah atau ambigu |

**Mengapa ini penting?**  
Tanpa memahami faktor manusia, kita tidak bisa mendesain simulasi yang efektif. Misalnya, jika automation bias sangat kuat, maka level awal simulasi harus secara eksplisit mendemonstrasikan kegagalan AI agar siswa sadar bahwa AI bisa salah.

---

#### 📐 Tulang 2: METODE — Pendekatan Pengajaran

Tulang ini menganalisis **strategi pedagogis** yang digunakan untuk mengajarkan literasi AI melalui simulasi interaktif.

| Sub-faktor | Penjelasan | Implementasi dalam Simulasi |
|------------|------------|-----------------------------|
| **HITL (Human-in-the-Loop)** | Siswa bukan pasif menerima output AI, tapi aktif membuat keputusan dan bisa override keputusan AI (Bommasani et al., 2022) | Pada setiap level, AI memberikan rekomendasi + confidence score, siswa memilih: ikuti AI atau override |
| **Controlled Ambiguity** | Sengaja memasukkan ambiguitas terkendali ke dalam skenario agar siswa berlatih menghadapi ketidakpastian | AI kadang memberikan confidence score rendah atau rekomendasi yang kontradiktif — siswa harus memutuskan |
| **Level Progression** | Meningkatkan kompleksitas secara bertahap: dari skenario sederhana ke kompleks | Level 1-3: AI jelas benar/salah → Level 4-6: AI ambigu → Level 7+: AI menipu / adversarial |
| **Scaffolding & Hint System** | Memberikan bantuan kontekstual yang berkurang seiring kemampuan siswa meningkat | Hint di awal ("Perhatikan confidence score!"), lalu dihilangkan di level lanjut |
| **Immediate Feedback Loop** | Siswa langsung melihat konsekuensi dari keputusan mereka | Setelah override/compliance, simulasi menunjukkan outcome dan eksplanasi |
| **Decision Override Mechanism** | Mekanisme eksplisit bagi siswa untuk menolak saran AI | Tombol "Saya tidak setuju" + alasan, dicatat di decision log |

**Mengapa ini penting?**  
Metode HITL adalah inti dari "Escape the Sketchbook" — tanpa mekanisme override dan controlled ambiguity, simulasi hanya menjadi demonstrasi pasif, bukan latihan kritis. Metode ini membedakan produk ini dari edugame AI lain yang hanya mengajarkan *apa itu AI* tanpa melatih *bagaimana berinteraksi dengan AI secara kritis*.

---

#### 💻 Tulang 3: MEDIA — Platform dan Teknologi

Tulang ini menganalisis **infrastruktur teknis** yang memungkinkan simulasi berjalan dan mengumpulkan data.

| Sub-faktor | Penjelasan | Peran dalam Simulasi |
|------------|------------|----------------------|
| **Browser-based (No Install)** | Simulasi berjalan di browser tanpa instalasi — menghilangkan barrier adopsi di sekolah | Akses via URL, kompatibel dengan Chrome/Firefox di laptop sekolah |
| **TensorFlow.js** | Library ML yang berjalan di browser — inference AI terjadi di client-side | Model klasifikasi gambar/teks berjalan langsung di browser siswa |
| **MediaPipe** | Library computer vision real-time dari Google — gesture & pose detection | Input gesture (tangan, pose) sebagai mekanisme interaksi alih-alih hanya klik |
| **Kaplay.js** | Game engine JavaScript ringan untuk 2D game | Rendering level, sprite, animasi, dan game loop |
| **Decision Log System** | Sistem pencatatan otomatis setiap keputusan siswa | Setiap interaksi dicatat: timestamp, confidence, decision, latency, level |
| **Responsive Web Design** | Tampilan menyesuaikan ukuran layar | Bisa diakses dari laptop atau tablet sekolah |
| **Client-side Processing** | Semua pemrosesan AI terjadi di perangkat siswa, tidak perlu server | Privasi data terjaga, tidak perlu infrastruktur server mahal |

**Mengapa ini penting?**  
Pilihan teknologi mempengaruhi aksesibilitas dan skalabilitas. Browser-based + client-side berarti simulasi bisa di-deploy ke sekolah manapun tanpa requirement khusus. Ini juga mempengaruhi jenis data yang bisa dikumpulkan — decision log system memungkinkan pengumpulan matriks data yang kaya untuk analisis kuantitatif.

---

#### 📚 Tulang 4: MATERI — Konten Edukasi

Tulang ini menganalisis **substansi edukasi** yang diajarkan melalui simulasi.

| Sub-faktor | Penjelasan | Contoh dalam Simulasi |
|------------|------------|------------------------|
| **Confidence Score (0-100%)** | Angka yang menunjukkan seberapa yakin AI dengan jawabannya — konsep kunci untuk memahami bahwa AI tidak 100% akurat | AI: "Saya 73% yakin ini adalah kucing" — siswa harus memutuskan apakah 73% cukup |
| **Probabilitas AI & Margin of Error** | Memahami bahwa output AI bersifat probabilistik, bukan deterministik | AI memberikan 3 kemungkinan jawaban dengan probabilitas masing-masing |
| **Decision-Making Framework** | Kerangka berpikir untuk membuat keputusan berdasarkan informasi yang tidak lengkap | "Jika confidence < 60%, pertimbangkan untuk override" |
| **Override vs Compliance Scenario** | Skenario di mana mengikuti AI adalah pilihan terbaik vs skenario di mana override lebih baik | Level 2: AI benar, ikuti → Level 5: AI salah, harus override |
| **Eksplanasi AI "Why"** | AI menjelaskan alasan di balik rekomendasinya — membangun kemampuan mengevaluasi reasoning | AI: "Saya merekomendasikan X karena fitur A dan B cocok, tapi fitur C tidak cocok" |
| **Skala Ketidakpastian** | Memahami spektrum dari "sangat yakin" hingga "tidak tahu sama sekali" | Visualisasi bar merah-kuning-hijau untuk confidence level |

**Mengapa ini penting?**  
Materi menentukan **apa yang siswa pelajari**. Tanpa konten yang tepat, simulasi hanyalah game tanpa nilai edukasi. Confidence score dan probabilitas adalah konsep fundamental yang membedakan literasi AI dari sekadar "tahu cara pakai AI" — ini mengajarkan **berpikir kritis tentang AI**.

---

### 1.4 Interaksi Antar-Tulang

Keempat tulang tidak berdiri sendiri — mereka membentuk **sistem ekologis** yang saling mempengaruhi:

```
MANUSIA ──mempengaruhi──→ METODE
  │                          │
  │                          │
  │    (automation bias      │    (HITL membutuhkan
  │     menentukan desain    │     decision log dari
  │     scaffolding)         │     MANUSIA)
  │                          │
  ▼                          ▼
MEDIA  ←──mendukung──── MATERI
           (TF.js memungkinkan
            confidence score
            real-time)
```

**Contoh interaksi:**
- **MANUSIA → METODE**: Automation bias siswa yang tinggi → Metode harus menyertakan level yang secara eksplisit menunjukkan kegagalan AI
- **METODE → MATERI**: HITL membutuhkan materi berupa skenario override/compliance → Materi harus didesain dengan pilihan yang meaningful
- **MATERI → MEDIA**: Confidence score real-time membutuhkan TF.js inference di browser → Media harus mendukung client-side ML
- **MEDIA → MANUSIA**: Browser-based tanpa instalasi → Mengurangi barrier adopsi → Siswa lebih mudah mengakses

---

## 2. Metodologi MIX (Kuantitatif + Kualitatif)

### 2.1 Mengapa Mixed Methods?

Metodologi MIX dipilih karena penelitian ini memiliki **dua jenis pertanyaan** yang tidak bisa dijawab oleh satu pendekatan saja:

| Pertanyaan Penelitian | Pendekatan | Mengapa? |
|----------------------|------------|----------|
| Apakah simulasi mengubah pola keputusan siswa? | **Kuantitatif** | Perlu angka: seberapa sering override, berapa latency, confidence berapa |
| MENGAPA siswa membuat keputusan tertentu? | **Kualitatif** | Perlu narasi: alasan, pemahaman, perubahan persepsi |

**Prinsip MIX**: Kuantitatif menjawab **"apa"** dan **"berapa"**, Kualitatif menjawab **"mengapa"** dan **"bagaimana"**. Keduanya saling melengkapi — bukan sekadar ditumpuk.

---

### 2.2 Kuantitatif — Analisis MATRIKS (Decision Log)

#### ⚠️ PENTING: Kuantitatif Menggunakan MATRIKS, Bukan Metrik Tunggal

Bagian kuantitatif penelitian ini **BUKAN** mengukur satu metrik tunggal (misalnya "trust_score = 0.73"). Sebaliknya, kuantitatif menggunakan **MATRIKS** — yaitu tabel multi-dimensi yang mencatat berbagai variabel secara simultan. Lihat [Bagian 3](#3-distingsi-kritis-metrik-vs-matriks) untuk penjelasan lengkap perbedaan ini.

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
│ S001    │ 4     │ 45          │ override     │ 6200    │ 0.50     │ B       │
│ S001    │ 5     │ 31          │ override     │ 3800    │ 0.60     │ B       │
│ S002    │ 1     │ 95          │ compliance   │ 800     │ 0.00     │ A       │
│ S002    │ 2     │ 88          │ compliance   │ 1100    │ 0.00     │ A       │
│ S002    │ 3     │ 71          │ compliance   │ 1800    │ 0.00     │ A       │
│ S002    │ 4     │ 52          │ compliance   │ 2400    │ 0.00     │ C       │
│ ...     │ ...   │ ...         │ ...          │ ...     │ ...      │ ...     │
└─────────┴───────┴─────────────┴──────────────┴─────────┴──────────┼─────────┘
                                                                     ▲
                                                      K-Means assign
                                                      cluster berdasarkan
                                                      pola multi-dimensi
```

#### Variabel dalam Matriks

| Variabel | Tipe | Deskripsi | Contoh Nilai |
|----------|------|-----------|--------------|
| `user_id` | Identifier | ID unik siswa | S001, S002 |
| `level` | Ordinal | Level simulasi (1-7+) | 1, 2, 3, 4, 5 |
| `confidence_score` | Numerik | Confidence AI saat keputusan dibuat (%) | 92, 78, 65, 45 |
| `decision_type` | Kategorikal | Keputusan siswa: compliance (ikut AI) atau override (tolak AI) | compliance, override |
| `latency` | Numerik | Waktu yang dibutuhkan siswa untuk membuat keputusan (ms) | 1200, 4500, 6200 |
| `override_ratio` | Numerik | Rasio override terhadap total keputusan hingga level tersebut | 0.00, 0.33, 0.50 |
| `cluster` | Kategorikal | Cluster hasil K-Means — mengelompokkan siswa berdasarkan pola perilaku | A, B, C |

#### Analisis Kuantitatif

**a) K-Means Clustering** — Mengelompokkan Siswa Berdasarkan Pola Perilaku

```
Input: Matriks decision log (N siswa × M variabel)
Output: K cluster, masing-masing merepresentasikan profil perilaku

Cluster A (Blind Trusters):  compliance tinggi, latency rendah, override ratio ≈ 0
Cluster B (Critical Thinkers): override meningkat seiring level, latency sedang
Cluster C (AI Skeptics):      override tinggi dari awal, latency tinggi
```

Proses:
1. **Preprocessing**: Normalisasi variabel numerik (confidence, latency, override_ratio) ke skala 0-1
2. **Determine K**: Elbow method atau silhouette score untuk menentukan jumlah cluster optimal
3. **Run K-Means**: Assign setiap siswa ke cluster berdasarkan pola multi-dimensi
4. **Interpretasi**: Karakterisasi setiap cluster berdasarkan centroid

**Mengapa K-Means?**  
K-Means cocok karena kita ingin **menemukan pola** dalam data multi-dimensi tanpa label sebelumnya (unsupervised). Kita tidak tahu sebelumnya ada berapa tipe siswa — K-Means membantu mengidentifikasi tipologi secara data-driven.

**b) Paired t-test** — Mengukur Perubahan Sebelum dan Sesudah

```
H₀: Tidak ada perbedaan signifikan antara pre-test dan post-test
H₁: Ada perbedaan signifikan (simulasi mengubah pola keputusan)

Variabel yang diuji:
- Override ratio: level awal vs level akhir
- Latency: level awal vs level akhir  
- Pre-test score vs post-test score (pengetahuan AI)
```

Proses:
1. **Data paired**: Setiap siswa memiliki dua pengukuran (pre vs post)
2. **Hitung selisih**: dᵢ = postᵢ - preᵢ untuk setiap siswa
3. **Hitung t-statistik**: t = d̄ / (sᵈ / √n)
4. **Bandingkan** dengan t-kritis pada α = 0.05
5. **Kesimpulan**: Jika p-value < 0.05, tolak H₀ — simulasi berpengaruh signifikan

**Mengapa Paired t-test?**  
Karena kita mengukur subjek yang SAMA sebelum dan sesudah treatment (simulasi). Ini adalah desain within-subject, bukan between-subject.

---

### 2.3 Kualitatif — Narasi dan Interpretasi

#### Sumber Data

| Sumber | Deskripsi | Cara Pengumpulan |
|--------|-----------|------------------|
| **Think-aloud protocol** | Siswa berbicara saat membuat keputusan | Rekaman audio saat sesi simulasi |
| **Post-simulation interview** | Wawancara semi-terstruktur setelah simulasi | Panduan wawancara tentang pengalaman dan pemahaman |
| **Open-ended survey** | Pertanyaan terbuka tentang perubahan persepsi | Form digital setelah simulasi |
| **Researcher observation** | Pengamatan langsung perilaku siswa | Catatan lapangan (field notes) |
| **AI-assisted analysis (opsional)** | Menggunakan AI (e.g., Gemini) untuk mengidentifikasi pola dalam narasi | Feed transkrip ke AI untuk thematic coding assistance |

#### Analisis Kualitatif

**a) Thematic Analysis** — Mengidentifikasi Tema dari Data Naratif

Mengikuti framework Braun & Clarke (2006):

```
Tahap 1: Familiarization — Membaca ulang semua transkrip dan catatan
Tahap 2: Generating Initial Codes — Memberi kode pada potongan data
Tahap 3: Searching for Themes — Mengelompokkan kode menjadi tema
Tahap 4: Reviewing Themes — Memeriksa apakah tema konsisten dan distinct
Tahap 5: Defining & Naming Themes — Mendefinisikan dan memberi nama tema
Tahap 6: Producing the Report — Menulis narasi akhir
```

**Contoh tema yang mungkin muncul:**
- "Awalnya saya percaya AI karena kayak Google" → Tema: **Authority Attribution**
- "Setelah AI salah, jadi ragu" → Tema: **Trust Disruption**
- "Saya cek confidence score dulu baru memutuskan" → Tema: **Calibrated Decision-Making**
- "Saya cuma ikut aja biar cepat selesai" → Tema: **Compliance Convenience**

**b) Narrative Synthesis** — Menggabungkan Tema Menjadi Narasi Koheren

Hasil thematic analysis tidak hanya didaftar, tapi disintesiskan menjadi **narasi** yang menjelaskan:

1. **Bagaimana** siswa berubah sepanjang simulasi (trajectory)
2. **Mengapa** siswa membuat keputusan tertentu (reasoning)
3. **Apa** faktor yang mempengaruhi perubahan (triggers)

Contoh narasi:
> "Siswa di Cluster A (Blind Trusters) menunjukkan pola compliance tinggi di level awal. Dari wawancara, terungkap bahwa mereka mengasosiasikan AI dengan mesin pencari yang 'selalu benar'. Setelah mengalami kegagalan AI di level 4, beberapa siswa mulai menunjukkan perilaku override, sementara yang lain tetap compliance karena 'AI pasti tahu lebih banyak dari saya'."

---

### 2.4 Integrasi MIX — Menggabungkan Kuantitatif dan Kualitatif

```
┌──────────────────────────────────────────────────────────────────┐
│                     METODOLOGI MIX                               │
│                                                                  │
│  ┌─────────────────────┐        ┌──────────────────────────┐    │
│  │   KUANTITATIF        │        │   KUALITATIF              │    │
│  │                      │        │                           │    │
│  │  Sumber: MATRIKS     │        │  Sumber: NARASI           │    │
│  │  (Decision Log)      │        │  (Interview, Survey,      │    │
│  │                      │        │   Observation)            │    │
│  │  Analisis:           │        │                           │    │
│  │  • K-Means Clustering│        │  Analisis:                │    │
│  │  • Paired t-test     │        │  • Thematic Analysis      │    │
│  │                      │        │  • Narrative Synthesis     │    │
│  │  Output:             │        │                           │    │
│  │  • Cluster profiles  │        │  Output:                  │    │
│  │  • Significance      │        │  • Tema-tema perilaku     │    │
│  │    values            │        │  • Narasi perubahan       │    │
│  └──────────┬───────────┘        └────────────┬──────────────┘    │
│             │                                  │                   │
│             │    ┌─────────────────────┐       │                   │
│             └───►│   INTEGRASI         │◄──────┘                   │
│                  │                     │                           │
│                  │  Kuantitatif: APA   │                           │
│                  │  Kualitatif: MENGAPA│                           │
│                  │                     │                           │
│                  │  Contoh:            │                           │
│                  │  Cluster A = 40%    │                           │
│                  │  siswa (Blind       │                           │
│                  │  Trusters) — KUANT  │                           │
│                  │  + MENGAPA? Karena  │                           │
│                  │  authority          │                           │
│                  │  attribution — KUAL │                           │
│                  └─────────────────────┘                           │
└──────────────────────────────────────────────────────────────────┘
```

**Strategi integrasi: Connecting Approach** (Creswell & Plano Clark, 2018):
1. Kuantitatif mengidentifikasi **APA** (cluster, pola, signifikansi)
2. Kualitatif menjelaskan **MENGAPA** (alasan, pemahaman, konteks)
3. Integrasi: Setiap temuan kuantitatif diverifikasi dan diperkaya dengan temuan kualitatif

---

## 3. Distingsi Kritis: Metrik vs Matriks

### 3.1 Mengapa Distingsi Ini Penting?

Dalam diskusi sebelumnya, terjadi kebingungan antara **metrik** (angka tunggal) dan **matriks** (tabel multi-dimensi). Ini adalah distingsi fundamental yang mempengaruhi:

- **Cara kita menganalisis data** — analisis single value vs analisis multi-dimensi
- **Cara kita memahami Fishbone** — setiap tulang menghasilkan matriks, bukan sekadar metrik
- **Cara kita menulis proposal** — metodologi kuantitatif berbasis matriks, bukan pengukuran tunggal

### 3.2 Definisi

| | **METRIK** | **MATRIKS** |
|---|---|---|
| **Definisi** | Satu angka/ukuran tunggal | Tabel lengkap dengan banyak dimensi |
| **Analogi** | Satu foto | Album foto dengan metadata |
| **Contoh** | `trust_score = 0.73` | Tabel: `user_id, level, confidence, decision, latency, override, cluster` |
| **Informasi** | Terbatas — satu dimensi | Kaya — banyak dimensi yang saling terkait |
| **Analisis** | Bandingkan angka | K-Means, t-test, cross-tabulation |
| **Konteks** | Cukup untuk dashboard sederhana | Diperlukan untuk penelitian akademis |

### 3.3 Contoh Konkret

**❌ Pendekatan METRIK (salah untuk penelitian ini):**
```
trust_score = 0.73
accuracy = 85%
override_rate = 23%
```
Masalah: Angka-angka ini tidak menunjukkan **siapa**, **kapan**, **dalam konteks apa**, dan **bagaimana polanya**.

**✅ Pendekatan MATRIKS (benar untuk penelitian ini):**
```
┌─────────┬───────┬─────────────┬──────────────┬─────────┬──────────┬─────────┐
│ user_id │ level │ confidence  │ decision     │ latency │ override │ cluster │
├─────────┼───────┼─────────────┼──────────────┼─────────┼──────────┼─────────┤
│ S001    │ 1     │ 92          │ compliance   │ 1200    │ 0.00     │ A       │
│ S001    │ 2     │ 78          │ compliance   │ 2100    │ 0.00     │ A       │
│ S001    │ 3     │ 65          │ override     │ 4500    │ 0.33     │ B       │
│ S001    │ 4     │ 45          │ override     │ 6200    │ 0.50     │ B       │
│ S002    │ 1     │ 95          │ compliance   │ 800     │ 0.00     │ A       │
│ S002    │ 2     │ 88          │ compliance   │ 1100    │ 0.00     │ A       │
│ S002    │ 3     │ 71          │ compliance   │ 1800    │ 0.00     │ A       │
│ S002    │ 4     │ 52          │ compliance   │ 2400    │ 0.00     │ C       │
└─────────┴───────┴─────────────┴──────────────┴─────────┴──────────┴─────────┘
```
Keunggulan: Dari matriks ini, kita bisa melihat bahwa S001 mulai melakukan override di level 3 (confidence 65%) dan meningkat di level 4, sementara S002 tetap compliance meskipun confidence rendah. **K-Means bisa mengelompokkan mereka ke cluster yang berbeda** berdasarkan pola multi-dimensi ini.

### 3.4 Fishbone Menggunakan MATRIKS

Setiap tulang Fishbone menghasilkan data dalam bentuk **matriks**, bukan metrik tunggal:

| Tulang | MATRIKS yang Dihasilkan | Kolom Contoh |
|--------|------------------------|--------------|
| **Manusia** | Matriks profil siswa | `user_id, age, tech_experience, prior_ai_knowledge, pre_test_score, cluster` |
| **Metode** | Matriks interaksi metode | `user_id, level, hint_used, feedback_received, scaffolding_level, decision_after_feedback` |
| **Media** | Matriks performa teknis | `session_id, level, load_time, inference_time, gesture_accuracy, browser, device_type` |
| **Materi** | Matriks respons konten | `user_id, level, confidence_shown, concept_type, override_correct, comprehension_score` |

**Implikasi**: Analisis Fishbone bukan sekadar "tulang A menyebabkan efek X", tetapi "interaksi antar-matriks dari 4 tulang menghasilkan pola multi-dimensi yang mempengaruhi literasi AI".

### 3.5 Ringkasan Perbandingan

```
METRIK                          MATRIKS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
trust_score = 0.73              ┌──────┬───────┬──────┬───────┬─────────┐
                                │ user │ level │ conf │ dec   │ cluster │
Satu angka                      │ S001 │ 3     │ 65   │ over  │ B       │
Tidak ada konteks               │ S002 │ 3     │ 71   │ comp  │ A       │
Tidak bisa di-cluster           │ S003 │ 3     │ 59   │ over  │ B       │
Tidak bisa di-cross-tab         └──────┴───────┴──────┴───────┴─────────┘
                                      │        │       │         │
                                      ▼        ▼       ▼         ▼
                                   Bisa K-Means, t-test, cross-tab,
                                   analisis multi-dimensi
```

---

## 4. Kerangka R&D (Research & Development)

### 4.1 Mengapa R&D?

Penelitian ini termasuk kategori **Research & Development** (Borg & Gall, 1983) karena:

1. **Tujuan utama**: Mengembangkan produk (simulasi interaktif literasi AI)
2. **Tujuan sekunder**: Meneliti efektivitas produk tersebut
3. **Ada siklus desain–bangun–uji** yang iteratif

R&D berbeda dari penelitian murni (pure research) yang hanya bertujuan menghasilkan teori. R&D bertujuan menghasilkan **produk yang teruji**.

### 4.2 Model R&D yang Digunakan

Menggunakan model **ADDIE** yang disederhanakan, dikombinasikan dengan SDLC **Waterfall + Prototype**:

```
┌────────────────────────────────────────────────────────────────────────┐
│                    MODEL R&D (ADDIE Simplified)                        │
│                                                                        │
│  1. ANALYZE ────► 2. DESIGN ────► 3. DEVELOP ────► 4. IMPLEMENT ──► 5. EVALUATE  │
│       │                 │                │                 │              │         │
│       │                 │                │                 │              │         │
│  • Kebutuhan       • Arsitektur     • Koding          • Deploy       • SUS       │
│    siswa SMP         sistem            simulasi          ke subjek     • Black-Box │
│  • Analisis        • Desain level   • Integrasi        • Koleksi      • K-Means   │
│    Fishbone          & skenario      TF.js +           data matriks   • t-test    │
│  • Definisi        • Desain UI/UX     MediaPipe +                     • Thematic  │
│    variabel        • Storyboard       Kaplay.js                         Analysis  │
│  • Studi literasi                    • Decision                      • Narative  │
│    AI sebelumnya                      Log System                     Synthesis   │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘
```

### 4.3 SDLC: Waterfall + Prototype

Metode pengembangan perangkat lunak menggunakan **Waterfall** sebagai kerangka utama dengan **Prototype** untuk validasi inkremental:

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

**Mengapa Waterfall + Prototype?**

| Aspek | Waterfall | Prototype | Kombinasi |
|-------|-----------|-----------|-----------|
| Struktur | Fase jelas, sekuensial | Iteratif, fleksibel | Fase utama jelas + validasi di setiap fase |
| Dokumentasi | Lengkap di setiap fase | Minimal di awal | Dokumentasi lengkap + prototipe untuk validasi |
| Risiko | Perubahan mahal di akhir | Perubahan murah di awal | Risiko diminimalisir dengan prototipe di awal |
| Cocok untuk | Proyek dengan requirement jelas | Proyet dengan requirement belum pasti | Requirement penelitian jelas, tapi desain perlu validasi |

### 4.4 Timeline R&D

| Fase | Aktivitas | Output | Durasi |
|------|-----------|--------|--------|
| **Analyze** | Studi literasi AI, Fishbone, definisi variabel & MATRIKS | Dokumen analisis, Fishbone diagram | 3-4 minggu |
| **Design** | Arsitektur sistem, desain level, UI/UX, storyboard | Dokumen desain, wireframe | 3-4 minggu |
| **Develop** | Koding simulasi, integrasi TF.js/MediaPipe/Kaplay.js | Prototipe v0.1 → v1.0 | 8-10 minggu |
| **Implement** | Deploy ke subjek penelitian, koleksi data matriks & narasi | Decision log matriks, transkrip wawancara | 2-3 minggu |
| **Evaluate** | SUS, Black-Box, K-Means, t-test, thematic analysis | Laporan evaluasi, cluster profiles, narasi | 3-4 minggu |

---

## 5. Metode Pengujian

### 5.1 Overview Metode Pengujian

```
┌────────────────────────────────────────────────────────────────────────┐
│                        METODE PENGUJIAN                               │
│                                                                        │
│  ┌─────────────────────────┐  ┌─────────────────────────────────────┐  │
│  │   PENGUJIAN PERANGKAT   │  │   PENGUJIAN PENELITIAN              │  │
│  │   LUNAK (Software)      │  │   (Research)                        │  │
│  │                         │  │                                     │  │
│  │  • Black-Box Testing    │  │  • SUS (Usability)                  │  │
│  │  • Functional Testing   │  │  • K-Means Clustering (Pattern)     │  │
│  │                         │  │  • Paired t-test (Significance)      │  │
│  │  Tujuan: Software bekerja│  │  • Thematic Analysis (Qualitative)  │  │
│  │  sesuai spesifikasi     │  │                                     │  │
│  │                         │  │  Tujuan: Bukti efektivitas simulasi │  │
│  └─────────────────────────┘  └─────────────────────────────────────┘  │
└────────────────────────────────────────────────────────────────────────┘
```

### 5.2 SUS (System Usability Scale)

**Tujuan**: Mengukur kegunaan (usability) simulasi dari perspektif pengguna (siswa SMP).

**Prosedur**:
1. Siswa mengisi kuesioner SUS setelah menggunakan simulasi
2. Kuesioner terdiri dari 10 pernyataan dengan skala Likert 1-5
3. Skor dihitung dengan formula SUS (rentang 0-100)

**10 Pernyataan SUS**:

| No | Pernyataan | Tipe |
|----|-----------|------|
| 1 | Saya rasa saya akan sering menggunakan simulasi ini | Positif |
| 2 | Saya merasa simulasi ini terlalu kompleks | Negatif |
| 3 | Saya rasa simulasi ini mudah digunakan | Positif |
| 4 | Saya rasa saya butuh bantuan teknis untuk menggunakan simulasi ini | Negatif |
| 5 | Saya merasa fitur-fitur dalam simulasi ini terintegrasi dengan baik | Positif |
| 6 | Saya rasa ada terlalu banyak ketidakkonsistenan dalam simulasi ini | Negatif |
| 7 | Saya membayangkan kebanyakan orang bisa belajar menggunakan simulasi ini dengan cepat | Positif |
| 8 | Saya merasa simulasi ini sangat rumit untuk digunakan | Negatif |
| 9 | Saya merasa sangat percaya diri menggunakan simulasi ini | Positif |
| 10 | Saya perlu belajar banyak hal sebelum bisa menggunakan simulasi ini | Negatif |

**Formula Skor SUS**:
```
Skor SUS = (Σ odd_items_converted + Σ even_items_converted) × 2.5

Konversi:
- Pernyataan positif (ganjil): skor = response - 1
- Pernyataan negatif (genap):  skor = 5 - response
```

**Interpretasi Skor SUS** (Bangor et al., 2009):

```
┌────────────────────────────────────────────────────┐
│  Skor SUS    │  Grade  │  Interpretasi             │
├────────────────────────────────────────────────────┤
│  90-100      │  A+     │  Best Imaginable          │
│  80-89       │  A      │  Excellent                │
│  70-79       │  B      │  Good                     │
│  60-69       │  C      │  OK / Marginal            │
│  50-59       │  D      │  Poor                     │
│  0-49        │  F      │  Worst Imaginable         │
└────────────────────────────────────────────────────┘

Target untuk simulasi ini: SUS ≥ 68 (rata-rata acceptable)
```

### 5.3 Black-Box Testing

**Tujuan**: Memastikan semua fungsi simulasi bekerja sesuai spesifikasi tanpa memeriksa kode internal.

**Cakupan Black-Box Testing**:

| Modul | Test Case | Input | Expected Output |
|-------|-----------|-------|-----------------|
| **Level Loading** | Level 1 dimuat dengan benar | Klik "Mulai" | Level 1 tampil, AI aktif, confidence score visible |
| **Decision Log** | Keputusan dicatat di matriks | Pilih "Ikuti AI" | Record baru di decision log: {user_id, level=1, decision=compliance, ...} |
| **Override Mechanism** | Override berhasil | Klik "Tidak Setuju" + alasan | Decision tercatat sebagai override, feedback ditampilkan |
| **Confidence Score** | Confidence score tampil | AI inferensi gambar | Confidence score 0-100% ditampilkan |
| **Level Progression** | Level berikutnya terbuka | Selesaikan level 1 | Level 2 terbuka |
| **TF.js Inference** | Klasifikasi gambar berjalan | Upload/capture gambar | Model mengembalikan label + confidence |
| **MediaPipe Gesture** | Gesture terdeteksi | Tunjuk tangan ke kamera | Input gesture terdeteksi dan diproses |
| **Data Export** | Decision log bisa diekspor | Klik "Export Data" | File CSV/JSON berisi matriks decision log |

### 5.4 K-Means Clustering (Untuk Analisis Pola)

**Tujuan**: Mengelompokkan siswa berdasarkan pola perilaku dalam matriks decision log.

**Detail Implementasi**:

```
Input:  Matriks decision log (N records × M variabel)
        N = jumlah total keputusan dari semua siswa
        M = {level, confidence_score, latency, override_ratio}

Langkah:
1. Preprocessing
   - Normalisasi min-max untuk variabel numerik
   - Encoding untuk variabel kategorikal (decision_type → 0=compliance, 1=override)
   
2. Feature Engineering
   - Override trajectory: perubahan override ratio per level (Δ override_ratio / Δ level)
   - Decision consistency: variasi decision_type per level
   - Latency trend: regresi linear latency terhadap level
   
3. Determine K
   - Elbow Method: plot within-cluster sum of squares (WCSS) vs K
   - Silhouette Score: ukuran kualitas clustering
   - Target: K = 3-5 cluster (berdasarkan literatur, tipikal user profiles)
   
4. Run K-Means
   - Inisialisasi: K-Means++ untuk centroid awal yang optimal
   - Iterasi: assign ke centroid terdekat → update centroid → repeat
   - Convergence: berhenti saat centroid tidak berubah
   
5. Interpretasi Cluster
   - Analisis centroid: profil rata-rata tiap cluster
   - Naming: beri nama deskriptif (e.g., "Blind Trusters", "Critical Thinkers")
```

### 5.5 Paired t-test (Untuk Signifikansi Statistik)

**Tujuan**: Menguji apakah ada perubahan signifikan pada perilaku siswa sebelum dan sesudah simulasi.

**Detail Implementasi**:

```
Desain: One-Group Pretest-Posttest

     Pre-test        Treatment        Post-test
     (ukur X₁)       (simulasi)       (ukur X₂)
         │                │                │
         ▼                ▼                ▼
    ┌─────────┐    ┌─────────────┐    ┌─────────┐
    │ Matriks │    │ Simulasi    │    │ Matriks │
    │ Level 1 │    │ Interaktif  │    │ Level N │
    │ (awal)  │    │ Literasi AI │    │ (akhir) │
    └─────────┘    └─────────────┘    └─────────┘

Variabel yang Diuji (semua dari MATRIKS):

1. Override ratio
   - Pre:  rata-rata override_ratio di level 1-2
   - Post: rata-rata override_ratio di level terakhir
   
2. Latency
   - Pre:  rata-rata latency di level 1-2
   - Post: rata-rata latency di level terakhir

3. Pengetahuan AI
   - Pre:  pre-test score
   - Post: post-test score

Hipotesis:
   H₀: μ_d = 0 (tidak ada perubahan)
   H₁: μ_d ≠ 0 (ada perubahan)
   
   di mana μ_d = rata-rata selisih (post - pre)
   
Kriteria:
   α = 0.05 (tingkat signifikansi 5%)
   df = n - 1 (degrees of freedom)
   
Kesimpulan:
   Jika p-value < 0.05 → Tolak H₀ → Simulasi berpengaruh signifikan
```

### 5.6 Ringkasan Metode Pengujian

| Metode | Tipe | Data | Tujuan | Output |
|--------|------|------|--------|--------|
| **SUS** | Kuantitatif | Kuesioner 10 pernyataan | Ukur usability | Skor SUS (0-100) |
| **Black-Box** | Teknis | Test case results | Validasi fungsional | Pass/Fail per test case |
| **K-Means** | Kuantitatif | MATRIKS decision log | Identifikasi pola perilaku | Cluster profiles |
| **Paired t-test** | Kuantitatif | MATRIKS pre vs post | Ukur signifikansi | p-value, effect size |
| **Thematic Analysis** | Kualitatif | Transkrip, catatan | Pahami reasoning siswa | Tema-tema perilaku |

---

## 6. Daftar Referensi Akademik

### Fishbone & Ishikawa
1. Ishikawa, K. (1982). *Guide to Quality Control*. Asian Productivity Organization.
2. Brassard, M. (1989). *The Memory Jogger Plus+*. GOAL/QPC.

### Mixed Methods
3. Creswell, J. W., & Plano Clark, V. L. (2018). *Designing and Conducting Mixed Methods Research* (3rd ed.). SAGE.
4. Johnson, R. B., & Onwuegbuzie, A. J. (2004). Mixed Methods Research: A Research Paradigm Whose Time Has Come. *Educational Researcher*, 33(7), 14-26.

### Automation Bias & Trust in AI
5. Parasuraman, R., & Riley, V. (1997). Humans and Automation: Use, Misuse, Disuse, Abuse. *Human Factors*, 39(2), 230-253.
6. Bommasani, R., et al. (2022). *On the Opportunities and Risks of Foundation Models*. Stanford CRFM.
7. Lee, J. D., & See, K. A. (2004). Trust in Automation: Designing for Appropriate Reliance. *Human Factors*, 46(1), 50-80.

### K-Means & Clustering
8. MacQueen, J. (1967). Some Methods for Classification and Analysis of Multivariate Observations. *Proceedings of the 5th Berkeley Symposium*, 281-297.
9. Arthur, D., & Vassilvitskii, S. (2007). K-Means++: The Advantages of Careful Seeding. *SODA '07*.

### Thematic Analysis
10. Braun, V., & Clarke, V. (2006). Using Thematic Analysis in Psychology. *Qualitative Research in Psychology*, 3(2), 77-101.

### SUS (System Usability Scale)
11. Brooke, J. (1996). SUS: A 'Quick and Dirty' Usability Scale. *Usability Evaluation in Industry*, 189-194.
12. Bangor, A., Kortum, P., & Miller, J. (2009). Determining What Individual SUS Scores Mean: Adding an Adjective Rating Scale. *Journal of Usability Studies*, 4(3), 114-123.

### R&D
13. Borg, W. R., & Gall, M. D. (1983). *Educational Research: An Introduction* (4th ed.). Longman.
14. Sugiyono. (2019). *Metode Penelitian Pendidikan: Pendekatan Kuantitatif, Kualitatif, dan R&D*. Alfabeta.

### AI Literacy
15. Long, D., & Magerko, B. (2020). What is AI Literacy? Competencies and Design Considerations. *CHI '20*, 1-16.
16. Ng, D. T. K., Leung, J. K. L., Chu, S. K. W., & Qiao, M. S. (2021). Conceptualizing AI Literacy: An Exploratory Review. *Computers and Education: Artificial Intelligence*, 2, 100041.

---

> **Catatan terakhir**: Dokumen ini adalah living document. Setiap perubahan dari diskusi dengan Bu Hesti atau temuan baru dari riset harus di-update di sini. Struktur Fishbone 4-tulang, distingsi Metrik vs Matriks, dan Metodologi MIX adalah keputusan metodologis yang harus dipertahankan di proposal.
