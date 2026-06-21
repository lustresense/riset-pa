# Style Guide v1 — Proposal Can & Dias (Sketchbook Universe)

> **Task ID**: format-izzah-daffa-v1
> **Tanggal**: 17/6/26
> **Patokan utama**: Proposal Izzah (PilAItes, PENS 2025) — diadopsi struktur, format tabel, format gambar, citation, timeline.
> **Patokan duo project**: Proposal Daffa-Seto (RFID+AR+Blockchain, PENS 2025) — diadopsi pola "Pembagian Tugas dan Alur Pengerjaan", timeline shared, kontrak data.

---

## 1. Executive Summary

### Target Halaman
- **Bab 1**: ~5 halaman (shared, identik Can & Dias)
- **Bab 2**: ~8–10 halaman (BEDA Can vs Dias, ringkas)
- **Bab 3**: ~18–22 halaman (BEDA Can vs Dias, DETAIL)
- **Grand total Bab 1–3**: ~31–37 halaman (target 35 halaman)
- Frontmatter (cover, pengesahan, abstrak, daftar isi/gambar/tabel) tidak dihitung.

### Prinsip Utama
1. **Bab 1 IDENTIK** Can & Dias — selaras, beda hanya paragraf pembatas masalah yang spesifik scope.
2. **Bab 2 BEDA TOTAL** — masing-masing fokus scope sendiri; teori penunjang ringkas (detail di Bab 3).
3. **Bab 3 BEDA TOTAL, DETAIL** — masing-masing detail scope sendiri; urutan mengikuti Izzah: Deskripsi Solusi → Metodologi → Desain Sistem (sub-sub detail) → Mockup → Jadwal.
4. **Metode**: Waterfall (SDLC) + Fishbone (teknik analisis 6M).
5. **Tabel + chart POLOSAN** — tanpa fill color, tanpa alternate row color, border tipis hitam.
6. **Timeline SINKRON** Can & Dias — 1 tabel shared, kolom Bulan 1–12 (atau 1–6 bila pakai semester), rows kegiatan + inisial C/D.
7. **Citation IEEE** numbered `[1]`, urut by kemunculan; Daftar Pustaka format PENS-IEEE.

---

## 2. Analisis Format Izzah (Patokan Utama)

### 2.1 Struktur Bab 1 (Izzah, 4 halaman)
| Sub-bab | Halaman | Panjang | Tone |
|---|---|---|---|
| 1.1 Latar Belakang | 1–4 | ~2 halaman | Naratif akademis, 4–5 paragraf, kutipan [1][2][3] inline |
| 1.2 Permasalahan | 2 | ~0.5 halaman | 1 paragraf padat, problem statement eksplisit |
| 1.3 Batasan Masalah | 2–3 | ~0.5 halaman | Naratif batasan (bukan bullet), sebutkan teknologi & ruang lingkup |
| 1.4 Tujuan | 3 | ~0.5 halaman | 1 paragraf, sebutkan apa yang dikembangkan |
| 1.5 Manfaat | 3–4 | ~0.5 halaman | Bullet list bernomor (1, 2, 3) |
| 1.6 Sistematika Penulisan | 3–4 | ~0.5 halaman | Paragraf per BAB (Bab I, Bab II, Bab III, Daftar Pustaka) |

### 2.2 Struktur Bab 2 (Izzah, 14 halaman)
- **2.1 Deskripsi Permasalahan** (~1 halaman, hal 5–6) — 3 paragraf naratif
- **2.2 Teori Penunjang** (~7 halaman, hal 6–13) — 9 sub-sub teori, masing-masing 0.5–1.5 halaman
  - Pola: definisi → penjelasan → posisi dalam penelitian → (opsional) gambar/ilustrasi
- **2.3 Penelitian Terkait** (~4 halaman, hal 13–18)
  - 4 sub-sub penelitian terkait (aplikasi komersial + 3 paper akademis)
  - Ditutup dengan **Tabel 2.1 State of The Art** (matriks perbandingan: No, Penelitian, Arsitektur, Dataset, Klasifikasi, Akurasi)

### 2.3 Struktur Bab 3 (Izzah, 19 halaman)
| Section | Halaman | Konten kunci |
|---|---|---|
| 3.1 Deskripsi Solusi | 19–20 | 3–4 paragraf solusi + 2 tahap (training & testing) |
| 3.2 Metodologi Penelitian | 20–21 | Gambar 3.1 Metodologi Penelitian, narasi alur |
| 3.3 Desain Sistem | 21–36 | Sub-sub detail (3.3.1–3.3.6) |
| 3.3.1 Dataset | 22–24 | Gambar 3.2 struktur folder, Tabel 3.1 sample dataset |
| 3.3.2 Desain Sistem DL | 24–25 | Gambar 3.3 Pra-Pemrosesan |
| 3.3.3 Arsitektur ResNet-50 | 25–27 | Gambar 3.4 Arsitektur, Tabel 3.2 Hyperparameter |
| 3.3.4 Kalibrasi & Inferensi RT | 27–28 | Narasi kalibrasi, jarak kamera, pencahayaan |
| 3.3.5 Desain Sistem Website | 28–29 | Gambar 3.5 Rancangan Database, Gambar 3.6 Flowchart |
| 3.3.6 Rencana Pengujian | 29–32 | Gambar 3.7 Confusion Matrix, rumus akurasi/precision/recall/F1, langkah SUS a–g |
| 3.2.6 Mockup | 32–36 | 6 mockup (Homepage, Login, Select Pose, Studio, History, User Guide) |
| 3.3 Jadwal Penelitian | 36–37 | Tabel 3.3 Timeline, 9 kegiatan × 12 bulan |

**Catatan**: Izzah menomori sub-bab mockup sebagai "3.2.6" (typo di source), tetapi secara konseptual termasuk sub dari 3.3. Untuk Can & Dias, kita rapikan jadi 3.3.7.

### 2.4 Format Tabel (Izzah)
- Caption **DI ATAS** tabel: `Tabel X.Y Keterangan Tabel` (caption bold, label bold)
- Border: `booktabs` style (tidak ada vertical line, hanya `\hline` horizontal)
- Header: bold, semua huruf kapital (untuk header cell)
- **POLosan** — tidak ada warna, tidak ada alternate row
- Numbering per chapter: Tabel 2.1, 2.2; Tabel 3.1, 3.2, 3.3
- Caption position: `aboveskip=6pt, belowskip=0pt`

### 2.5 Format Gambar (Izzah)
- Caption **DI BAWAH** gambar: `Gambar X.Y Keterangan Gambar`
- Caption bold untuk label (`Gambar 3.1`), normal untuk keterangan
- Source attribution bila bukan bikin sendiri: `(Sumber: Author, Year)` di bawah caption utama
- Numbering per chapter: Gambar 2.1–2.3; Gambar 3.1–3.13
- Centered, `width=\textwidth` default
- Caption position: `belowskip=6pt, aboveskip=0pt`

### 2.6 Citation Style (Izzah)
- **IEEE numbered** inline: `[1]`, `[2]`, `[3]`, ...
- Format penulisan: `Pilates[1]` (tanpa spasi sebelum kurung) atau `...manusia [4]` (dengan spasi setelah kata)
- Multiple citation: `[6][7]` atau `[1][3]` (tidak digabung jadi `[1,3]`)
- Tidak ada footnote tengah halaman
- Semua masuk Daftar Pustaka di akhir

### 2.7 Daftar Pustaka (Izzah)
- Urut by nomor `[1]`, `[2]`, ... sesuai urutan muncul di text
- Format: `Author. (Year). Title. Venue, vol. X, no. Y, pp. Z–W. doi: ...`
- Contoh Izzah `[1]`: `C. Wells, G. S. Kolt, and A. Bialocerkowski, "Defining Pilates exercise: A systematic review," Complement Ther Med, vol. 20, no. 4, pp. 253–262, Aug. 2012, doi: 10.1016/j.ctim.2012.02.005.`
- Format mendekati IEEE: inisial depan, nama belakang, judul dalam `"..."`, venue italic, volume/no, halaman, tahun, DOI.

### 2.8 Timeline Format (Izzah)
- Tabel 3.3 Tabel Timeline Pengerjaan
- Kolom: `No | Nama Kegiatan | Bulan` (Bulan dipecah jadi 12 kolom: 1, 2, 3, ..., 12)
- Rows: 9 kegiatan (Studi Literatur, Arsitektur, Pengumpulan Dataset, Labeling, Training, Development, Evaluasi, Integrasi, Penulisan)
- Cell diisi dengan tanda `X` atau shading (untuk duo project: bisa pakai inisial `C`/`D`)
- Caption di atas tabel
- **POLosan** — border tipis hitam

---

## 3. Analisis Format Daffa-Seto (Duo Project Pattern)

### 3.1 Struktur Bab 1 (Daffa, 5 halaman)
- 1.1 Latar Belakang (~3 halaman, hal 1–3) — lebih panjang dari Izzah
- 1.2 Permasalahan (~0.5 halaman, hal 3) — bullet bernomor, 2 pertanyaan riset
- **TIDAK ADA** Batasan Masalah (Daffa skip section ini)
- 1.3 Tujuan (~1 halaman, hal 3–4) — bullet bernomor 3 poin
- 1.4 Manfaat (~1.5 halaman, hal 4–5) — 4 kategori (Mahasiswa, Program Studi, Masyarakat, IPTEK)
- 1.5 Sistematika Penulisan (~1 halaman, hal 5)
- **Untuk Can & Dias**: ikuti pola Izzah (ada Batasan Masalah), karena proposal existing Can & Dias sudah pakai pola Izzah.

### 3.2 Struktur Bab 2 (Daffa, 7 halaman)
- 2.1 Deskripsi Permasalahan (~1 halaman)
- 2.2 Teori Penunjang (~5 halaman) — 5 sub-sub teori, masing-masing 0.5–1.5 halaman
  - Pola: definisi + 1–2 paragraf konteks + citation [5][6]
- 2.3 Penelitian Terkait (~2 halaman) — Tabel 2.1 matrix perbandingan
  - Kolom matrix: Penulis, Metode, Temuan, Kontribusi, Kelebihan, Kekurangan

### 3.3 Struktur Bab 3 (Daffa, 21 halaman)
| Section | Halaman | Konten kunci |
|---|---|---|
| 3.1 Deskripsi Solusi | 13–15 | Gambar 3.1 Metode waterfall, 5 tahap (A–E) |
| 3.2 Desain Sistem | 15–32 | Sub-sub detail (3.2.1–3.2.5) |
| 3.2.1 Alur Permainan | 18–21 | Gambar 3.3, 3.4 alur permainan |
| **3.2.2 Pembagian Tugas dan Alur Pengerjaan** | 21–27 | **KEY DUO PATTERN** — Gambar 3.5 Pembagian tugas, eksplisit siapa ngapain |
| 3.2.3 Integrasi Unity-Blockchain | 27–29 | Gambar 3.10 Diagram Integrasi |
| 3.2.4 Percobaan Implementasi AR | 29–30 | Gambar 3.11 |
| 3.2.5 Skenario Pengujian | 30–32 | Black Box + Usability (SUS) |
| 3.3 Jadwal Penelitian | 33 | Tabel 3.1, 10 kegiatan × 6 bulan |

### 3.4 DUO PATTERN — Yang Diadopsi untuk Can & Dias

#### 3.4.1 Section "Pembagian Tugas dan Alur Pengerjaan" (Daffa 3.2.2)
Pola kalimat pembuka:
> "Pengembangan proyek akhir ini dilakukan oleh dua orang dalam satu tim, yaitu penulis dan [Nama Rekan] sebagai rekan kerja. Pembagian tugas disesuaikan dengan bidang keahlian masing-masing anggota. Untuk memperjelas kontribusi dari tiap anggota, proyek ini disertai dengan diagram desain sistem yang menampilkan alur kerja dan komponen teknis berdasarkan warna."

- Diagram pembagian tugas dengan **warna**:
  - **BIRU** = scope penulis (Daffa/Can/Dias — siapa yang nulis proposal ini)
  - **KUNING** (atau abu-abu, karena kita polosan) = scope rekan
- Penjelasan naratif: penulis bertanggung jawab pada [scope X, Y, Z], rekan bertanggung jawab pada [scope A, B, C]
- Detail alur pengerjaan dalam 4–6 tahap utama (research → production → integration → testing)

#### 3.4.2 Section "Kontrak Data" (Dias proposal existing 3.14)
- Eksplisit batas tanggung jawab antar scope
- Format data yang dipertukarkan (JSON payload)
- Endpoint yang digunakan (`POST /api/logs/interaction`)
- Titik temu: Probe UI (untuk Can-Dias)

#### 3.4.3 Timeline Shared untuk Duo
- **1 tabel sama** untuk Can & Dias (tidak 2 tabel terpisah)
- Kolom Bulan 1–12 (atau 1–6)
- Rows: kegiatan + inisial (C/D) yang ngapain
- Contoh:
  ```
  | No | Kegiatan            | Pelaksana | 1 | 2 | 3 | 4 | 5 | 6 |
  | 1  | Studi Literatur    | C, D      | X | X |   |   |   |   |
  | 2  | Pengumpulan Dataset| D         |   | X | X |   |   |   |
  | 3  | Desain Wireframe   | C         |   | X | X |   |   |   |
  | ...| ...                | ...       |   |   |   |   |   |   |
  ```

#### 3.4.4 Daftar Pustaka Terpisah
- Can & Dias masing-masing punya Daftar Pustaka sendiri di proposal masing-masing
- Referensi shared (AI literacy, HITL, SUS) akan muncul di kedua daftar pustaka dengan nomor yang berbeda (karena urutan kemunculan beda)

#### 3.4.5 Bab 1 IDENTIK
- Konten identik, beda hanya:
  - Nama penulis & NRP di cover
  - Paragraf "Permasalahan" yang menyebutkan scope spesifik (Can: simulasi interaktif & finger tracking; Dias: klasifikasi sketsa & clustering)
  - Tujuan & Manfaat yang spesifik scope
- Untuk Can & Dias existing: Bab 1 sudah hampir identik, hanya perlu konfirmasi selaras.

---

## 4. Style Guide Can & Dias — Struktur Bab 1, 2, 3

### 4.A Struktur Bab 1 — SHARED (Identik Can & Dias)

**Total target: ~5 halaman**

| Sub-bab | Estimasi Halaman | Catatan |
|---|---|---|
| 1.1 Latar Belakang | ~2 halaman | Naratif 5–6 paragraf: AI literacy umum → K-12 → kebutuhan media interaktif → finger tracking/sketsa → ruang gap → solusi |
| 1.2 Permasalahan | ~0.5 halaman | 1 paragraf padat, problem statement spesifik scope (Can: media interaktif HITL; Dias: model klasifikasi + logging + analisis) |
| 1.3 Batasan Masalah | ~0.5 halaman | Bullet list 4–5 poin, sebutkan teknologi & non-goals |
| 1.4 Tujuan | ~0.5 halaman | 1 paragraf + bullet 3 poin khusus scope |
| 1.5 Manfaat | ~0.5 halaman | Bullet 4 poin (siswa, guru, peneliti, pengembangan media) |
| 1.6 Sistematika Penulisan | ~0.5 halaman | Paragraf per BAB (I, II, III, Daftar Pustaka) |

**Catatan**: Bab 1 Can & Dias existing sudah aligned dengan pola ini. **JANGAN diubah** — hanya pastikan selaras.

### 4.B Struktur Bab 2 — BEDA Can vs Dias (RINGKAS)

**Total target: ~8–10 halaman per proposal**

#### Bab 2 — Can (Frontend/HITL/UI-UX)
| Sub-bab | Estimasi Halaman | Teori yang dibahas |
|---|---|---|
| 2.1 Deskripsi Permasalahan | ~1 halaman | Narasi gap media interaktif untuk AI literacy |
| 2.2 Teori Penunjang | ~5–6 halaman (ringkas!) | 2.2.1 Literasi AI K-12, 2.2.2 HITL, 2.2.3 XAI & Confidence Score, 2.2.4 Game-Based Learning & Scaffolding, 2.2.5 Pedagogical Agent, 2.2.6 CCI untuk SMP, 2.2.7 System Usability Scale (SUS) |
| 2.3 Penelitian Terkait + State of the Art | ~2–3 halaman | 4 penelitian terkait + Tabel 2.1 State of the Art |

**Detail di Bab 3** — Bab 2 cukup definisi + posisi dalam penelitian (1–2 paragraf per teori).

#### Bab 2 — Dias (Backend/CNN/Data Analysis)
| Sub-bab | Estimasi Halaman | Teori yang dibahas |
|---|---|---|
| 2.1 Deskripsi Permasalahan | ~1 halaman | Narasi gap klasifikasi sketsa + analisis pola keputusan |
| 2.2 Teori Penunjang | ~5–6 halaman (ringkas!) | 2.2.1 Literasi AI, 2.2.2 HITL untuk Klasifikasi, 2.2.3 CNN & MobileNet, 2.2.4 TensorFlow.js & Client-Side Inference, 2.2.5 Confidence Score, 2.2.6 Data Logging, 2.2.7 K-Means Clustering |
| 2.3 Penelitian Terkait + State of the Art | ~2–3 halaman | 4 penelitian terkait + Tabel 2.1 State of the Art |

### 4.C Struktur Bab 3 — BEDA Can vs Dias (DETAIL)

**Total target: ~18–22 halaman per proposal**

#### Bab 3 — Can (URUTAN FOLLOW IZZAH)

| Sub-bab | Estimasi Halaman | Konten |
|---|---|---|
| 3.1 Deskripsi Solusi | ~1–2 halaman | Narasi solusi + 4 prinsip akademis (AI literacy, XAI, HITL, GBL) + 3 level progresi + Momo + technical stack ringkas |
| 3.2 Metodologi Penelitian | ~2–3 halaman | Waterfall (SDLC) 5 tahap + Fishbone 6M (analisis masalah) + SUS + Black-Box |
| 3.3 Desain Sistem | ~12–15 halaman | DETAIL — sub-sub di bawah |
| 3.3.1 Kebutuhan Pengguna + Use Case (termasuk superadmin) | ~2 halaman | Tabel kebutuhan pengguna, use case diagram (Siswa, Admin/Guru, Superadmin) |
| 3.3.2 Alur Pengguna (User Flow) | ~1.5 halaman | Onboarding → Core Gameplay → Level Summary (Can isi sendiri detail alur) |
| 3.3.3 Desain Level (3 level) | ~3 halaman | Level 1 Trust Building, Level 2 Ambiguous Choice, Level 3 Risk & Override — Tabel spesifikasi teknis per level |
| 3.3.4 Mekanisme HITL (Top-6 check) | ~2 halaman | Top-3 tampil, Top-6 cek backend, override flow, anti-cheat |
| 3.3.5 Maskot Momo (deskripsi tekstual + placeholder sketsa) | ~1 halaman | Konsep, 5 state ekspresi, prinsip 8-bit geometric, text bubble only |
| 3.3.6 Wireframe (Onboarding, Main Gameplay, Probe UI, Result) | ~2.5 halaman | 4–6 wireframe, masing-masing dengan keterangan fungsi |
| 3.3.7 Rancangan Pengujian (SUS) | ~1.5 halaman | Black-Box + SUS questionnaire, prosedur pengujian |
| 3.4 Jadwal Penelitian | ~1 halaman | Tabel timeline SINKRON dengan Dias (1 tabel shared) |

**Sub 3.3.2 Alur Pengguna**: User menentukan sendiri detail alur (sesuai task description: "user flow placement — Can isi sendiri").

#### Bab 3 — Dias (URUTAN FOLLOW IZZAH)

| Sub-bab | Estimasi Halaman | Konten |
|---|---|---|
| 3.1 Deskripsi Solusi | ~1–2 halaman | Narasi solusi + 4 prinsip (CNN MobileNet, TF.js, REST API logging, K-Means) + 5 komponen teknis |
| 3.2 Metodologi Penelitian | ~2–3 halaman | Waterfall (SDLC) 5 tahap + Fishbone 6M + SUS + Black-Box + akurasi model (confusion matrix) |
| 3.3 Desain Sistem | ~12–15 halaman | DETAIL — sub-sub di bawah |
| 3.3.1 Perancangan Sistem Global (IPO) | ~1.5 halaman | Input → 4 Layer (Interactive Sim, AI Classification, Decision & Consequence, Data & Analysis) → Output |
| 3.3.2 Arsitektur Sistem Hybrid | ~1.5 halaman | Browser-based inference + server-side services, Node.js/Express, SQLite |
| 3.3.3 Model CNN MobileNet | ~2 halaman | Pemilihan kategori dataset, arsitektur, training, konversi TF.js, Tabel hyperparameter |
| 3.3.4 Skema Data Log + Backend API | ~2 halaman | Struktur JSON log (Tabel), endpoint REST API (Tabel), alur logging |
| 3.3.5 K-Means Clustering | ~2 halaman | Feature engineering, penentuan k (Elbow/Silhouette), interpretasi cluster |
| 3.3.6 Admin Dashboard | ~1.5 halaman | Fitur dashboard, alur penggunaan |
| 3.3.7 Pembagian Tugas dan Alur Pengerjaan (DUO PATTERN) | ~1.5 halaman | Diagram pembagian tugas (warna BIRU=Can, ABU=Dias), narasi pembagian, titik temu (Probe UI) |
| 3.3.8 Kontrak Data Dias-Can | ~1 halaman | Format JSON payload, endpoint, batas tanggung jawab |
| 3.3.9 Rancangan Pengujian | ~1.5 halaman | Black-Box + akurasi model + SUS untuk dashboard |
| 3.4 Jadwal Penelitian | ~1 halaman | Tabel timeline SINKRON dengan Can |

**Catatan urutan**: Metodologi DITEMPATKAN SETELAH Deskripsi Solusi (mengikuti pola Izzah & Daffa), BUKAN di akhir Bab 3 seperti di proposal Can & Dias existing.

### 4.D Format Tabel & Gambar — POLOSAN

#### Tabel
```latex
\begin{table}[H]
\centering
\caption{Keterangan Tabel}
\label{tab:label-tabel}
\begin{tabular}{|l|l|l|}
\hline
\textbf{Kolom 1} & \textbf{Kolom 2} & \textbf{Kolom 3} \\ \hline
Data 1           & Data 2           & Data 3           \\ \hline
\end{tabular}
\end{table}
```

**Aturan**:
- **POLOSAN** — TIDAK ADA `\rowcolor`, TIDAK ADA `\cellcolor`, TIDAK ADA `colortbl` package
- Border: `|l|l|l|` (vertical line tipis) + `\hline` (horizontal line tipis) — alternatif: `booktabs` style `\toprule \midrule \bottomrule` tanpa vertical line
- Header: bold (`\textbf{...}`)
- Caption: DI ATAS tabel (`\caption` sebelum `\begin{tabular}`)
- Numbering: per chapter (`Tabel 2.1`, `Tabel 3.1`, dst.)
- Label format: `tab:kebutuhan-pengguna` (kebab-case)

#### Gambar
```latex
\begin{figure}[H]
    \centering
    \includegraphics[width=\textwidth]{gambar/nama-file.png}
    \caption{Keterangan Gambar}
    \label{fig:label-gambar}
\end{figure}
```

**Aturan**:
- Caption: DI BAWAH gambar (`\caption` setelah `\includegraphics`)
- Source attribution bila bukan bikin sendiri: tambahkan `(Sumber: Author, Year)` di bawah caption utama, atau gunakan sub-caption
- Numbering: per chapter (`Gambar 2.1`, `Gambar 3.1`, dst.)
- Label format: `fig:alur-pengguna` (kebab-case)
- Format file: PNG (untuk screenshot/mockup/diagram) atau PDF (untuk vector diagram)
- Width default: `\textwidth`; untuk gambar kecil gunakan `width=0.7\textwidth` atau `width=0.5\textwidth`

### 4.E Citation Style

- **IEEE numbered** inline: `[1]`, `[2]`, ...
- Format penulisan inline:
  - Tanpa spasi sebelum kurung bila langsung menempel pada kata: `Pilates[1]`
  - Dengan spasi setelah kata bila merujuk ke konsep: `...human action recognition [4]`
  - Multiple citation: `[6][7]` (tidak digabung `[6,7]`)
- Tidak ada footnote tengah halaman
- Semua referensi masuk Daftar Pustaka di akhir proposal
- Pakai `\cite{ref1}` di LaTeX (otomatis terurut by kemunculan)

### 4.F Daftar Pustaka Format

- Urut by nomor `[1]`, `[2]`, ... **sesuai urutan muncul** di text (bukan alfabetis)
- Format PENS-IEEE (mendekati Izzah):
  - **Jurnal**: `A. Author, B. Author, and C. Author, "Title of paper," Journal Name, vol. X, no. Y, pp. Z–W, Mon. Year, doi: 10.xxxx/xxxx.`
  - **Konferensi**: `A. Author, "Title of paper," in Proc. Conference Name, Year, pp. Z–W. doi: 10.xxxx/xxxx.`
  - **Buku**: `A. Author, Title of Book, Xth ed. City: Publisher, Year.`
  - **arXiv/online**: `A. Author, "Title," arXiv:XXXX.XXXXX, Year. [Online]. Available: URL`
- Setiap entri diketik dengan hanging indent
- Pisah per proposal (Can & Dias masing-masing punya Daftar Pustaka sendiri di proposal masing-masing)
- Referensi shared (AI literacy, HITL, SUS) akan muncul di kedua daftar pustaka dengan nomor yang berbeda

---

## 5. Duo Project Treatment (Ringkas)

| Aspek | Pola |
|---|---|
| Bab 1 | IDENTIK Can & Dias (selaras, beda paragraf Permasalahan & Tujuan yang spesifik scope) |
| Bab 2 | BEDA TOTAL — masing-masing fokus scope sendiri |
| Bab 3 | BEDA TOTAL — masing-masing detail scope sendiri |
| Section "Pembagian Tugas dan Alur Pengerjaan" | ADA di salah satu proposal (rekomendasi: di **Dias** Bab 3.3.7, karena Dias existing sudah punya "Kontrak Data" — lebih natural di backend). Narasi: penulis (Dias) ↔ rekan (Can) |
| Section "Kontrak Data Dias-Can" | ADA di Dias Bab 3.3.8 (batas tanggung jawab, format JSON, endpoint) |
| Timeline | SAMA persis Can & Dias (1 tabel shared, kolom Bulan + inisial C/D) |
| Daftar Pustaka | PISAH per proposal (masing-masing punya sendiri) |
| Mockup/Wireframe | BEDA — Can punya wireframe UI siswa; Dias punya mockup dashboard admin |
| Diagram pembagian tugas | DENGAN WARNA (BIRU=Can, ABU/Dias=Dias) — exception terhadap aturan "polosan" karena fungsional, bukan dekoratif |

---

## 6. LaTeX Preamble (Ready-to-Use)

Preamble di bawah ini adalah **template PENS standard** yang diadopsi dari format Izzah (A4, 12pt TNR, 1.5 spacing, 4cm/3cm margin). **Mengganti** preamble A5/10pt yang ada di proposal Can & Dias existing.

```latex
% ============================================================
% PROPOSAL PROYEK AKHIR — [NAMA MAHASISWA]
% [JUDUL PROYEK AKHIR]
% Format: PENS Standard (A4, 12pt TNR, 1.5 spacing, 4cm/3cm margin)
% Mengikuti pola format Izzah (PilAItes 2025)
% ============================================================

\documentclass[12pt,a4paper,oneside,openany]{report}

% ============================================================
% PACKAGES
% ============================================================
\usepackage[top=4cm,left=4cm,right=3cm,bottom=3cm]{geometry}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{array}
\usepackage{tabularx}
\usepackage{longtable}
\usepackage{float}
\usepackage{caption}
\usepackage{titlesec}
\usepackage{indentfirst}
\usepackage{setspace}
\usepackage{etoolbox}
\usepackage{fancyhdr}
\usepackage{afterpage}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{url}
\usepackage{hyperref}
\hypersetup{colorlinks=false, pdfborder={0 0 0}}

% Times New Roman (compilasi pdflatex standar)
\usepackage{times}
\renewcommand{\rmdefault}{ptm}

% ============================================================
% LINE SPACING 1.5
% ============================================================
\setstretch{1.5}

% ============================================================
% PARAGRAPH INDENT (1.25 cm, PENS standard)
% ============================================================
\setlength{\parindent}{1.25cm}
\setlength{\parskip}{0pt}

% ============================================================
% CHAPTER / SECTION / SUBSECTION FORMATTING
% (Pola Izzah — UPPERCASE for chapter & section, Title Case for subsection)
% ============================================================
\titleformat{\chapter}[display]
  {\normalfont\fontsize{14pt}{16.8pt}\selectfont\bfseries\centering}
  {BAB \thechapter}
  {12pt}
  {\MakeUppercase}

\titleformat{\section}
  {\normalfont\fontsize{12pt}{14.4pt}\selectfont\bfseries}
  {\thesection}
  {1em}
  {\MakeUppercase}

\titleformat{\subsection}
  {\normalfont\fontsize{12pt}{14.4pt}\selectfont\bfseries}
  {\thesubsection}
  {1em}
  {}

\titleformat{\subsubsection}
  {\normalfont\fontsize{12pt}{14.4pt}\selectfont\bfseries\itshape}
  {\thesubsubsection}
  {1em}
  {}

\titlespacing*{\chapter}{0pt}{0pt}{24pt}
\titlespacing*{\section}{0pt}{18pt}{12pt}
\titlespacing*{\subsection}{0pt}{14pt}{8pt}

% ============================================================
% CAPTION FORMATTING (Pola Izzah)
% - Tabel: caption DI ATAS, font 11pt, label bold
% - Gambar: caption DI BAWAH, font 11pt, label bold
% ============================================================
\captionsetup[table]{font=small,labelfont=bf,name={Tabel},labelsep=period,justification=centering,aboveskip=6pt,belowskip=0pt,position=top}
\captionsetup[figure]{font=small,labelfont=bf,name={Gambar},labelsep=period,justification=centering,aboveskip=0pt,belowskip=6pt,position=bottom}

% ============================================================
% HEADER / FOOTER (Pola Izzah — page number top-right)
% ============================================================
\pagestyle{fancy}
\fancyhf{}
\fancyhead[R]{\thepage}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}

\fancypagestyle{plain}{
  \fancyhf{}
  \fancyhead[R]{\thepage}
  \renewcommand{\headrulewidth}{0pt}
}

% ============================================================
% BLANK PAGE COMMAND (Pola Izzah — "Halaman ini sengaja dikosongkan")
% ============================================================
\newcommand{\blankpage}{%
  \afterpage{%
    \null
    \vfill
    \begin{center}
      {\small Halaman ini sengaja dikosongkan}
    \end{center}
    \vfill
    \thispagestyle{plain}
    \newpage
  }%
}

% ============================================================
% CUSTOM COMMANDS — \gbr{filename}{caption}{label}
%                  \tabel{caption}{content}{label}
% ============================================================
\newcommand{\gbr}[3]{%
  \begin{figure}[H]
    \centering
    \includegraphics[width=\textwidth]{#1}
    \caption{#2}
    \label{#3}
  \end{figure}
}

\newcommand{\gbrsrc}[4]{%
  \begin{figure}[H]
    \centering
    \includegraphics[width=\textwidth]{#1}
    \caption{#2}
    \label{#3}
    \begin{center}\small (Sumber: #4)\end{center}
  \end{figure}
}

\newcommand{\tabel}[3]{%
  \begin{table}[H]
    \centering
    \caption{#1}
    \label{#3}
    #2
  \end{table}
}

% ============================================================
% TOC FORMATTING
% ============================================================
\renewcommand{\contentsname}{DAFTAR ISI}
\renewcommand{\listfigurename}{DAFTAR GAMBAR}
\renewcommand{\listtablename}{DAFTAR TABEL}

% ============================================================
\begin{document}
% ============================================================

% --- COVER PAGE ---
\begin{titlepage}
\centering
\vspace*{1cm}

{\fontsize{14pt}{16pt}\selectfont PROPOSAL PROYEK AKHIR}

\vspace{2cm}

{\fontsize{14pt}{18pt}\selectfont\bfseries\MakeUppercase{[JUDUL PROYEK AKHIR — ISI DI SINI]}}

\vspace{3cm}

{\fontsize{12pt}{14pt}\selectfont Oleh:}\\[0.3cm]
{\fontsize{12pt}{14pt}\selectfont\bfseries [NAMA MAHASISWA]}\\[0.2cm]
{\fontsize{12pt}{14pt}\selectfont NRP. [NRP]}

\vspace{3cm}

{\fontsize{12pt}{14pt}\selectfont Dosen Pembimbing:}\\[0.3cm]
{\fontsize{12pt}{14pt}\selectfont [Nama Dosen Pembimbing]}\\[0.2cm]
{\fontsize{12pt}{14pt}\selectfont NIP. [NIP]}

\vspace{3cm}

{\fontsize{12pt}{14pt}\selectfont PROGRAM STUDI SARJANA TERAPAN TEKNOLOGI REKAYASA MULTIMEDIA}\\[0.2cm]
{\fontsize{12pt}{14pt}\selectfont JURUSAN TEKNOLOGI MULTIMEDIA DAN JARINGAN}\\[0.2cm]
{\fontsize{12pt}{14pt}\selectfont POLITEKNIK ELEKTRONIKA NEGERI SURABAYA}\\[0.2cm]
{\fontsize{12pt}{14pt}\selectfont 2025}

\end{titlepage}

\blankpage

% --- HALAMAN PENGESAHAN ---
\chapter*{HALAMAN PENGESAHAN}
\addcontentsline{toc}{chapter}{HALAMAN PENGESAHAN}

% [Isi halaman pengesahan — lihat template existing]

\blankpage

% --- ABSTRAK ---
\chapter*{ABSTRAK}
\addcontentsline{toc}{chapter}{ABSTRAK}

% [Isi abstrak — 1 paragraf 200–250 kata + kata kunci]

\blankpage

% --- ABSTRACT ---
\chapter*{ABSTRACT}
\addcontentsline{toc}{chapter}{ABSTRACT}

% [English version of abstrak]

\blankpage

% --- DAFTAR ISI ---
\chapter*{DAFTAR ISI}
\addcontentsline{toc}{chapter}{DAFTAR ISI}
\tableofcontents
\clearpage

% --- DAFTAR GAMBAR ---
\chapter*{DAFTAR GAMBAR}
\addcontentsline{toc}{chapter}{DAFTAR GAMBAR}
\listoffigures
\clearpage

% --- DAFTAR TABEL ---
\chapter*{DAFTAR TABEL}
\addcontentsline{toc}{chapter}{DAFTAR TABEL}
\listoftables
\clearpage

% --- BAB 1: PENDAHULUAN ---
\chapter{PENDAHULUAN}
\label{chap:bab1}

\section{LATAR BELAKANG}
\label{sec:latar-belakang}
% [Isi Bab 1.1 — JANGAN diubah dari existing, hanya format convert]

\section{PERMASALAHAN}
\label{sec:permasalahan}

\section{BATASAN MASALAH}
\label{sec:batasan-masalah}

\section{TUJUAN}
\label{sec:tujuan}

\section{MANFAAT}
\label{sec:manfaat}

\section{SISTEMATIKA PENULISAN}
\label{sec:sistematika-penulisan}

% --- BAB 2: KAJIAN PUSTAKA ---
\chapter{KAJIAN PUSTAKA}
\label{chap:bab2}

\section{DESKRIPSI PERMASALAHAN}
\label{sec:deskripsi-permasalahan}

\section{TEORI PENUNJANG}
\label{sec:teori-penunjang}

% [Subsections — 6–7 teori, ringkas @ 0.5–1 halaman per teori]

\section{PENELITIAN TERKAIT}
\label{sec:penelitian-terkait}

% [4 penelitian terkait + Tabel State of the Art]

% --- BAB 3: DESKRIPSI SISTEM ---
\chapter{DESKRIPSI SISTEM}
\label{chap:bab3}

\section{DESKRIPSI SOLUSI}
\label{sec:deskripsi-solusi}

\section{METODOLOGI PENELITIAN}
\label{sec:metodologi-penelitian}

\section{DESAIN SISTEM}
\label{sec:desain-sistem}

% [Subsections detail — sesuai tabel 4.C di Style Guide]

\section{JADWAL PENELITIAN}
\label{sec:jadwal-penelitian}

% [Tabel timeline sinkron dengan rekan]

% --- DAFTAR PUSTAKA ---
\chapter*{DAFTAR PUSTAKA}
\addcontentsline{toc}{chapter}{DAFTAR PUSTAKA}

% [Referensi IEEE urut by kemunculan]

\end{document}
```

---

## 7. Mapping ke Existing Proposal (Can & Dias)

### 7.1 Can (proposal-can.tex existing) — KEEP / REVISE / ADD / REMOVE

#### KEEP (Pertahankan)
- ✅ Bab 1 seluruhnya (1.1–1.6) — sudah aligned dengan pola Izzah, **JANGAN diubah**
- ✅ Bab 2 sub-bab (2.1, 2.2, 2.3) — struktur sudah benar
- ✅ Teori penunjang Bab 2 (8 sub-sub) — konten sudah lengkap
- ✅ Bab 3.1 Deskripsi Solusi — konten sudah baik
- ✅ Bab 3.2 Desain Sistem (kebutuhan pengguna, use case, desain level, mekanisme HITL, mapping perilaku, wireframe)
- ✅ Tabel spesifikasi teknis Level 1, 2, 3 — sudah polosan ✓
- ✅ Citations IEEE [1]–[22] di Daftar Pustaka
- ✅ Konsep "Probe UI", "Top-3 prediction", "Override", "Scaffolding", "Flow Theory"
- ✅ Referensi [1] Ng, [2] Casal-Otero, [3] Khosravi, [4] Mosqueira-Rey, [5] Memarian, [6] Videnovik, [7] Chan, [8] Schroeder

#### REVISE (Ubah)
- 🔄 **Format dokumen**: A5/10pt/single spacing → **A4/12pt/1.5 spacing/4cm-3cm margin** (PENS standard ikut Izzah)
- 🔄 **Preamble LaTeX**: ganti seluruh preamble dengan preamble baru (lihat Section 6)
- 🔄 **Urutan Bab 3**: pindah `METODOLOGI PENELITIAN` dari section 3.4 (akhir) ke section 3.2 (setelah Deskripsi Solusi) — sesuai pola Izzah & Daffa
- 🔄 **JADWAL PENELITIAN**: posisi dari section 3.3 ke section 3.4 (paling akhir Bab 3) — sesuai pola Izzah
- 🔄 **Sub-bab Mockup**: tambahkan sub-bab `3.3.6 Wireframe` eksplisit dengan 4–6 mockup (saat ini wireframe sudah ada tapi tersebar di subsection berbeda)
- 🔄 **Tabel kebutuhan pengguna**: pertahankan format polosan, tambah kolom "Ref." bila perlu
- 🔄 **Sistematika Penulisan (1.6)**: pastikan mention "BAB III Deskripsi Sistem: membahas deskripsi solusi, metodologi penelitian, desain sistem, dan jadwal penelitian" — urutan sesuai urutan di Bab 3
- 🔄 **Pivot decisions 16/6/26**: apply ke Bab 3 — login pakai nomor absen (bukan finger tracking), mekanisme Top-6 check (bukan Override Budget), tambah timer, tambah resize/rotate buttons, hapus Decorative category (hanya Solid & Danger)

#### ADD (Tambah)
- ➕ **Sub-bab 3.3.4 Mekanisme HITL Top-6 check** (revisi dari mapping perilaku objek lama) — mekanisme override baru yang lebih elegant
- ➕ **Sub-bab 3.3.5 Maskot Momo** — deskripsi tekstual konsep maskot (pilih dari OPSI E "Doodle Cube" atau OPSI G "Eraser Ghost" — rekomendasi dari task maskot-face-options-v3), 5 state ekspresi, prinsip 8-bit geometric, text bubble only, NO voice/NLP, NO legs/wings, float only
- ➕ **Use Case Superadmin** di sub-bab 3.3.1 (pivot #1 dari 16/6/26) — superadmin bikin tab sekolah → kelas → nomor siswa
- ➕ **Diagram Pembagian Tugas** (DUO PATTERN dari Daffa 3.2.2) — narasi pembagian Can vs Dias dengan warna BIRU/ABU
- ➕ **Timeline shared dengan Dias** — 1 tabel dengan kolom Bulan + inisial C/D
- ➕ **Section "Metodologi Penelitian" lengkap** — Waterfall 5 tahap (Analisis → Perancangan → Implementasi → Integrasi & Pengujian → Pemeliharaan) + Fishbone 6M (Man, Machine, Method, Material, Measurement, Environment) + SUS procedure
- ➕ **Section "Kontrak Data Can-Dias"** (atau refer ke Dias Bab 3.3.8) — titik temu di Probe UI

#### REMOVE (Hapus)
- ❌ **Finger tracking MediaPipe sebagai login** — DEPRECATED post-pivot 16/6/26 (lihat MEMORY.md Section 10 PIVOT #1). Ganti dengan nomor absen.
- ❌ **Override Budget (limited overrides per level: L2=2, L3=1)** — DEPRECATED post-pivot 16/6/26 (PIVOT #2). Ganti dengan Top-6 check.
- ❌ **Mapping Perilaku Objek "Decorative"** — hapus kategori Decorative post-pivot (DECISION #5 validated RSI-1). Hanya Solid & Danger.
- ❌ **Referensi [15] Meng 2024 MediaPipe** — DEPRECATED (gesture login dihapus). Bisa tetap dipertahankan dengan note DEPRECATED bila finger tracking masih dipakai untuk navigasi (bukan login).
- ❌ **Format A5/10pt/single spacing** — ganti dengan A4/12pt/1.5 spacing PENS standard

### 7.2 Dias (proposal-dias.tex existing) — KEEP / REVISE / ADD / REMOVE

#### KEEP
- ✅ Bab 1 seluruhnya (1.1–1.6) — sudah aligned, **JANGAN diubah**
- ✅ Bab 2 sub-bab (2.1, 2.2, 2.3) — struktur sudah benar
- ✅ Teori penunjang Bab 2 (8 sub-sub) — konten lengkap
- ✅ Bab 3.1 Deskripsi Solusi + 5 komponen teknis
- ✅ Detail teknis: CNN MobileNet, TF.js, REST API, K-Means, Admin Dashboard
- ✅ Tabel JSON log, endpoint API, behavior mapping, tech stack — semua sudah polosan ✓
- ✅ Citations IEEE [1]–[22] di Daftar Pustaka
- ✅ Referensi [6] Xu, [7] Goh, [8] Smilkov, [10] Pansri, [11] Alzahrani

#### REVISE
- 🔄 **Format dokumen**: A5/10pt/single → A4/12pt/1.5 spacing PENS standard
- 🔄 **Preamble LaTeX**: ganti seluruh preamble
- 🔄 **Judul Bab 3**: dari `PERANCANGAN SISTEM` → `DESKRIPSI SISTEM` (konsisten dengan Can & pola Izzah)
- 🔄 **Konsolidasi 15 section jadi 4 section utama** ( Deskripsi Solusi / Metodologi / Desain Sistem / Jadwal) — sesuai pola Izzah. Sub-sections existing dipertahankan sebagai `subsection` di bawah `3.3 Desain Sistem`.
- 🔄 **Urutan**: pindah `Metodologi Penelitian` dari 3.15 (akhir) ke 3.2 (setelah Deskripsi Solusi)
- 🔄 **Jadwal Penelitian**: tambahkan section 3.4 (saat ini MISSING di existing!)
- 🔄 **Sistematika Penulisan (1.6)**: ubah mention "BAB III Perancangan Sistem" → "BAB III Deskripsi Sistem" + tambah mention jadwal penelitian

#### ADD
- ➕ **Section 3.4 Jadwal Penelitian** — TIDAK ADA di existing, WAJIB tambah. Sinkron dengan Can (1 tabel shared).
- ➕ **Sub-bab 3.3.7 Pembagian Tugas dan Alur Pengerjaan** (DUO PATTERN) — diagram pembagian tugas, narasi Dias (backend) ↔ Can (frontend), titik temu Probe UI
- ➕ **Sub-bab 3.3.8 Kontrak Data Dias-Can** — sudah ada di existing (3.14), cukup pindah posisi & rapikan
- ➕ **Fishbone 6M di Metodologi** — sudah ada di existing 3.15.4 (Analisis Masalah), pertahankan tapi pindah ke 3.2
- ➕ **Wireframe Admin Dashboard** — mockup dashboard guru (saat ini hanya naratif)

#### REMOVE
- ❌ **15 section terpisah di Bab 3** — terlalu fragmented; konsolidasi jadi 4 main sections dengan subsections
- ❌ **Format A5/10pt/single spacing** — ganti PENS standard
- ❌ **Judul "PERANCANGAN SISTEM"** — ganti "DESKRIPSI SISTEM" untuk konsistensi dengan Can & Izzah

### 7.3 Timeline Sinkronisasi Can & Dias (SHARED TABLE)

**Kegiatan + inisial pelaksana**:

| No | Kegiatan | Pelaksana |
|---|---|---|
| 1 | Studi Literatur & Pengumpulan Referensi | C, D |
| 2 | Penyusunan Proposal | C, D |
| 3 | Analisis Kebutuhan & Fishbone 6M | C, D |
| 4 | Desain Sistem (Wireframe Can, ERD/API Dias) | C, D |
| 5 | Pengumpulan & Preprocessing Dataset Quick Draw | D |
| 6 | Training Model CNN MobileNet | D |
| 7 | Konversi Model ke TensorFlow.js | D |
| 8 | Implementasi Backend API + SQLite | D |
| 9 | Implementasi Frontend (Kaplay.js, MediaPipe) | C |
| 10 | Implementasi Probe UI & Momo Animation | C |
| 11 | Implementasi K-Means Clustering | D |
| 12 | Implementasi Admin Dashboard | D |
| 13 | Integrasi Can-Dias (Kontrak Data) | C, D |
| 14 | Black-Box Testing | C, D |
| 15 | Usability Testing (SUS) | C, D |
| 16 | Analisis Data Log & Clustering | D |
| 17 | Penulisan Laporan | C, D |

**Catatan**: C = Can (Frontend), D = Dias (Backend). Tabel berisi 12 bulan (atau 6 bulan bila pakai semester). Format cell: `X` untuk kegiatan berlangsung di bulan tersebut.

---

## 8. Checklist Akhir

- [x] Analisis format Izzah (patokan rapih) — selesai
- [x] Analisis format Daffa-Seto (duo project treatment) — selesai
- [x] Struktur Bab 1, 2, 3 dengan estimasi halaman — selesai
- [x] Format Tabel & Gambar (POLOSAN, no color) — selesai
- [x] Citation & Daftar Pustaka format — selesai
- [x] Duo Project Treatment — selesai
- [x] LaTeX Preamble (siap copy-paste) — selesai
- [x] Mapping ke existing proposal (keep/revise/add/remove) — selesai
- [ ] LaTeX skeleton files (latex_skeleton_can.tex, latex_skeleton_dias.tex) — generated separately
- [ ] Apply ke proposal final — Phase 2 (next agent)

---

## 9. Path Output Files

1. **Style Guide**: `Style_Guide_v1.md` (file ini)
2. **LaTeX Skeleton Can**: `latex_skeleton_can.tex`
3. **LaTeX Skeleton Dias**: `latex_skeleton_dias.tex`

---

## 10. Referensi Sumber

- **Izzah proposal**: `/tmp/izzah.txt` (Nurul Izzah — PilAItes, PENS 2025)
- **Daffa proposal**: `/tmp/daffa.txt` (Muhammad Daffa Husen Nadia — RFID+AR+Blockchain, PENS 2025)
- **Existing Can proposal**: `../archive_escape_the_sketchbook/01_proposal/can/proposal-can.tex`
- **Existing Dias proposal**: `../archive_escape_the_sketchbook/01_proposal/dias/proposal-dias.tex`
- **MEMORY.md**: `../../../MEMORY.md` (pivot decisions 16/6/26, RSI-1)
- **Worklog**: `/home/z/my-project/worklog.md`
