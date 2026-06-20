# Referensi Akademik & Justifikasi Fitur — Escape the Sketchbook

> **File ini living document.** Update saat diskusi berjalan.  
> **Aturan sitasi:** Bab 2 = teori + sitasi, Bab 3 = pemakaian teori tsb untuk justify desain.  
> **Bab 1 TIDAK diubah.**

---

## Daftar Referensi Aktif (Terpakai di Proposal)

### Referensi Can (Frontend/UI/UX/HITL)

| No | Referensi | Topik | Dipakai di Bab 2 | Dipakai di Bab 3 |
|----|-----------|-------|-------------------|-------------------|
| [1] | Ng et al. (2021). Conceptualizing AI literacy. *Computers and Education: AI*, 2, 100041. | AI Literacy Framework | 2.2.1 Literasi KB | 3.2.1 Kebutuhan Pengguna, 3.1 Deskripsi Solusi |
| [2] | Casal-Otero et al. (2023). AI literacy in K-12. *Intl J STEM Education*, 10, 29. | AI Literacy K-12 | 2.2.1, 2.3.1 | 3.2.4 Desain Level |
| [3] | Khosravi et al. (2022). XAI in education. *Computers and Education: AI*, 3, 100074. | Explainable AI Edu | 2.2.3 Explainable Interface | 3.2.9 Probe UI, 3.2.5 HITL |
| [4] | Mosqueira-Rey et al. (2023). HITL machine learning: A state of the art. *AI Review*, 56, 3005-3054. | HITL | 2.2.2, 2.3.2 | 3.2.5 Mekanisme HITL |
| [5] | Memarian & Doleck (2024). HITL in AIED. *Computers in Human Behavior: Artificial Humans*, 2, 100053. | HITL in Education | 2.2.2 | 3.2.5 Mekanisme HITL |
| [6] | Videnovik et al. (2023). Game-based learning in CS education. *Intl J STEM Education*, 10, 54. | Game-Based Learning | 2.2.4, 2.3.3 | 3.2.4 Desain Level |
| [7] | Chan, Wan & King (2021). Performance over enjoyment? *Frontiers in Education*, 6, 660376. | Flow Theory + GBL | 2.2.4 | 3.2.4 Desain Level |
| [8] | Schroeder, Davis & Yang (2025). Pedagogical agents: Umbrella review. *J Educational Computing Research*, 62(8). | Pedagogical Agent | 2.2.6 | 3.2.7-3.2.10 Wireframe |
| [9] | Meng et al. (2024). Real-time hand gesture monitoring based on MediaPipe. *Sensors*, 24(19), 6262. | Finger Tracking | 2.2.5, 2.3.4 | 3.2.7 Wireframe Onboarding |
| [10] | Karran, Demazure & Hudelot (2022). Designing for confidence. *Frontiers in Neuroscience*, 16. | Confidence Visualization | 2.2.3 | 3.2.9 Probe UI |

### Referensi Dias (Backend/CNN/Logging/Clustering)

| No | Referensi | Topik | Dipakai di Bab 2 | Dipakai di Bab 3 |
|----|-----------|-------|-------------------|-------------------|
| [1] | Ng et al. (2021) — sama | AI Literacy | 2.2.1 | 3.1 Deskripsi Solusi |
| [2] | Casal-Otero et al. (2023) — sama | AI Literacy K-12 | 2.2.1 | — |
| [3] | Khosravi et al. (2022) — sama | XAI in Education | 2.2.2 HITL Klasifikasi | 3.2.5 Client-Side Inference |
| [4] | Mosqueira-Rey et al. (2023) — sama | HITL | 2.2.2 | 3.2.6 Skema Data Log |
| [5] | Memarian & Doleck (2024) — sama | HITL in AIED | 2.2.2 | — |
| [6] | Xu et al. (2023). Deep learning for free-hand sketch. *IEEE TPAMI*, 45(1), 285-312. | Sketch Classification | 2.2.3, 2.3.1 | 3.2.1 Dataset, 3.2.2 Preprocessing |
| [7] | Goh, Ho & Abas (2023). Front-end DL web apps. *Applied Intelligence*, 53, 15923-15945. | Front-End DL | 2.2.5, 2.3.2 | 3.2.4 Konversi TF.js, 3.2.5 |
| [8] | Smilkov et al. (2019). TensorFlow.js: ML for the web. *arXiv:1901.05350*. | TensorFlow.js | 2.2.5 | 3.2.4 Konversi TF.js |
| [9] | Karran et al. (2022) — sama | Confidence Visualization | 2.2.6 | 3.2.6 Skema Data Log |
| [10] | Pansri et al. (2024). Understanding student learning behavior: K-Means. *Education Sciences*, 14(12), 1291. | K-Means Behavior | 2.2.8, 2.3.4 | 3.2.9 K-Means |
| [11] | Alzahrani et al. (2025). Identifying weekly student engagement via K-Means. *Electronics*, 14(15), 3018. | K-Means Engagement | 2.2.8, 2.3.4 | 3.2.9 K-Means |

---

## Mapping Fitur → Justifikasi Akademik

### CAN (Frontend)

| Fitur | Kenapa Ada? | Dasar Akademik | Sitasi |
|-------|-------------|-----------------|--------|
| **Simulasi Interaktif Berlevel** | Konsep AI abstrak bagi SMP; butuh media konkret bertahap | AI literacy K-12 requires age-appropriate, experience-based strategies | [2] |
| **3 Level (Trust→Ambiguity→Override)** | Scaffolding: bantuan awal lalu tanggung jawab berpindah ke learner; Flow Theory: skill-challenge balance bertahap | Game-based learning mendukung engagement melalui pengalaman aktif + feedback; Flow Theory dalam GBL non-kompetitif | [6][7] |
| **Level 1: conf >85%** | Membangun trust dulu sebelum menghadirkan ambiguitas; Flow: skill > challenge mencegah frustrasi | Performance over enjoyment — GBL non-kompetitif lebih efektif saat challenge bertahap | [7] |
| **Level 2: conf 55-70%** | Memperkenalkan ambiguitas terkontrol; Flow: masuk flow channel | HITL: manusia dilibatkan saat model tidak pasti | [4][5] |
| **Level 3: conf 35-51%** | Memaksa evaluasi kritis + override; Flow: controlled anxiety | XAI in education: user perlu melihat ketidakpastian untuk belajar evaluasi | [3][10] |
| **Finger Tracking MediaPipe** | Interaksi natural buat SMP; menggambar = eksplorasi visual | MediaPipe real-time hand gesture monitoring valid untuk interaksi gestural | [9] |
| **Canvas Drawing** | Input visual untuk klasifikasi; siswa "merasakan" proses AI | AI literacy: pengalaman langsung dengan input/output sistem | [1][2] |
| **Top-3 Prediction + Confidence Score** | Siswa harus melihat kemungkinan, bukan jawaban tunggal; mencegah automation bias | XAI: explainability perlu disesuaikan untuk user; Confidence visualization membantu pengguna menimbang | [3][10] |
| **Probe UI (Pause-and-Evaluate)** | Gameplay HARUS berhenti agar siswa membaca confidence sebelum keputusan; mencegah asal klik | HITL: manusia sebagai evaluator; XAI: transparency pada momen keputusan | [4][3][10] |
| **Mekanisme Accept/Correct/Override** | Inti HITL: siswa menentukan label akhir; keputusan berdampak | HITL: keterlibatan manusia memperkuat kontrol; Memarian: ER analysis peran manusia | [4][5] |
| **Momo (Pedagogical Agent)** | Personify AI agar SMP ngerasa interaktif, bukan digurui; feedback kontekstual | Pedagogical agent mendukung belajar jika sesuai konteks dan tidak membebani | [8] |
| **Momo Non-NLP (Rule-Based)** | Momo bukan chatbot; feedback berbasis kondisi sistem (conf rendah, override, danger) — defensible secara akademis | Pedagogical agent yang sederhana dan kontekstual lebih efektif dari yang kompleks/overwhelming | [8] |
| **Solid/Danger/Decorative** | Sistem taruhan (stakes) agar keputusan punya konsekuensi; mengukur probabilistic reasoning | Game-based learning: consequence-driven learning lebih engaging; Flow: stakes meningkatkan engagement | [6][7] |
| **Onboarding** | Siswa harus paham aturan sebelum data dianggap valid; scaffolding | CCI: siswa SMP butuh arahan jelas sebelum otonomi; Scaffolding: bantuan awal | [2][6] |
| **Alur Linear** | Mencegah choice paralysis; fokus ke momen keputusan (HITL) | CCI: siswa SMP butuh kesederhanaan tanpa terasa kekanak-kanakan | [2] |
| **Feedback Non-Menghukum** | Retry bukan punishment; mendorong eksplorasi | CCI: feedback tidak bersifat menghukum agar siswa belajar tanpa tekanan | [2] |
| **Usability Testing (bukan pre-post)** | Mengukur keterbacaan alur, bukan peningkatan kemampuan — sesuai arahan Bu Hesti | HITL in AIED: behavioral evidence (log) sebagai proxy, bukan learning outcome claim | [5] |

### DIAS (Backend)

| Fitur | Kenapa Ada? | Dasar Akademik | Sitasi |
|-------|-------------|-----------------|--------|
| **CNN MobileNet** | Model ringan untuk client-side inference; bisa ekstraksi pola visual sketsa | MobileNet dirancang untuk perangkat terbatas; CNN efektif untuk pengolahan citra | [6][7] |
| **Top-3 Prediction** | Siswa harus melihat beberapa kemungkinan, bukan label tunggal | XAI: explainability mencegah penerimaan otomatis | [3][9] |
| **Confidence Score** | Menunjukkan tingkat keyakinan model; bukan kebenaran mutlak | Confidence visualization: user perlu melihat uncertainty untuk mengambil keputusan informed | [9] |
| **Confidence Gap** | Selisih confidence top-1 vs pilihan user; indikator evaluatif | HITL: gap menunjukkan seberapa jauh user menilai berbeda dari model | [4] |
| **Client-Side Inference TF.js** | Tidak butuh server AI; inferensi dekat user; arsitektur ringan | TF.js: ML di browser tanpa backend; Front-end DL: deployment web viable | [7][8] |
| **REST API Logging** | Pencatatan data interaksi untuk analisis pola keputusan | HITL in AIED: data log sebagai basis analisis perilaku evaluatif | [5] |
| **SQLite** | Ringan untuk prototype; data bisa diekspor ke CSV/JSON | Praktis untuk skala prototype | — |
| **K-Means Clustering** | Mengelompokkan pola keputusan: Trust Acceptor, Critical Evaluator, Uncertain Explorer | K-Means bisa mengidentifikasi pola perilaku belajar dari data aktivitas | [10][11] |
| **Dashboard Analisis** | Alat bantu peneliti membaca data; bukan fitur pembelajaran siswa | Analisis log mendukung interpretasi pola perilaku | [10] |
| **Subset Dataset (bukan full QuickDraw)** | Hanya kategori yang bisa dipetakan ke Solid/Danger/Decorative | Sketch recognition: preprocessing dan pemilihan arsitektur perlu diperhatikan | [6] |

---

## Konsep Kunci yang Perlu Diperkuat di Bab 2

### 1. Controlled Ambiguity (Ambiguitas Terkontrol)
- **Inti:** AI sengaja TIDAK sempurna agar momen HITL bisa terjadi
- **Justifikasi:** Khosravi et al. [3] — XAI in education menekankan bahwa user perlu melihat ketidakpastian; Karran et al. [10] — confidence visualization membantu user memahami uncertainty
- **Masuk di:** Bab 2 Can → 2.2.3 (Explainable Interface), Bab 3 Can → 3.2.4 (Desain Level)

### 2. Automation Bias & Probabilistic Reasoning
- **Inti:** Tanpa intervensi, user cenderung menerima output AI tanpa evaluasi
- **Justifikasi:** Mosqueira-Rey et al. [4] — HITL penting untuk mencegah over-reliance; Ng et al. [1] — kemampuan mengevaluasi output AI = bagian AI literacy
- **Masuk di:** Bab 2 Can → 2.2.2 (HITL), Bab 2 Dias → 2.2.2 (HITL pada Klasifikasi)

### 3. Scaffolding dalam Level Progression
- **Inti:** 3 level = bantuan awal (L1) → tanggung jawab bertambah (L2) → otonomi evaluatif (L3)
- **Justifikasi:** Videnovik et al. [6] — GBL mendukung keterlibatan bertahap; Chan et al. [7] — Flow Theory dalam GBL non-kompetitif
- **Masuk di:** Bab 2 Can → 2.2.4 (Simulasi Interaktif Berlevel), Bab 3 Can → 3.2.4 (Desain Level)

### 4. CCI untuk Siswa SMP
- **Inti:** Desain antarmuka untuk remaja butuh keseimbangan: sederhana tapi tidak kekanak-kanakan
- **Justifikasi:** Casal-Otero et al. [2] — AI literacy K-12 memerlukan strategi sesuai perkembangan usia
- **Masuk di:** Bab 2 Can → 2.2.7 (CCI untuk SMP), perlu diperkuat dengan sitasi langsung

### 5. Pedagogical Agent (Rule-Based, Non-NLP)
- **Inti:** Momo sebagai companion berbasis kondisi, bukan chatbot
- **Justifikasi:** Schroeder et al. [8] — pedagogical agent efektif jika sesuai konteks dan tidak membebani
- **Masuk di:** Bab 2 Can → 2.2.6, Bab 3 Can → 3.2.7-3.2.10

---

## Istilah Terlarang (JANGAN PAKAI)

| Jangan | Ganti Dengan |
|--------|--------------|
| "adaptif" | "bertahap" / "berlevel" |
| "sistem ini belajar dari user" | "sistem mencatat keputusan user sebagai log" |
| "meningkatkan kemampuan siswa" | "memfasilitasi interaksi reflektif" |
| "melatih berpikir kritis" | "memperlihatkan proses evaluasi terhadap output AI" |
| "siswa paham AI" | "siswa memiliki data untuk mengevaluasi output AI" |
| "sistem pembelajaran" | "sistem interaktif dengan konsekuensi nyata" |

---

## Catatan Per Bab

### Bab 2 (Kajian Pustaka) — Teori + Sitasi
- Setiap sub-teori HARUS ada sitasi [X]
- Setiap sitasi HARUS ada penjelasan "apa relevansinya ke proyek ini"
- Deskripsi Permasalahan harus sudah menyentuh kenapa media yang ada belum cukup

### Bab 3 (Deskripsi Sistem) — Pemakaian Teori
- Setiap keputusan desain harus punya "kenapa" yang mengacu ke Bab 2
- Contoh: "Penggunaan tiga level dipilih berdasarkan prinsip scaffolding [6][7]"
- Tidak perlu re-explain teori, cukup refer ke Bab 2 + jelaskan penerapannya

---

*Last updated: 2026-06-15*
