# HITL Loophole & Exploit Analysis — Sketchbook Universe

> **Proyek:** Sketchbook Universe — Simulasi Interaktif Literasi AI untuk Siswa SMP Kelas 7–9
> **Fokus:** Analisis celah exploit pada mekanik Override, klasifikasi worst case, dan desain countermeasure
> **Status:** DRAFT — Memerlukan review dan keputusan desain
> **Tanggal:** 2026-06-16

---

## Daftar Isi

1. [Eksekutif: Masalah Inti](#1-eksekutif-masalah-inti)
2. [Rekonstruksi Skenario Exploit](#2-rekonstruksi-skenario-exploit)
3. [Taxonomy Worst Case](#3-taxonomy-worst-case)
4. [Framework Akademik yang Relevan](#4-framework-akademik-yang-relevan)
5. [Analisis Per Worst Case](#5-analisis-per-worst-case)
6. [Desain Countermeasure (8 Proposal)](#6-desain-countermeasure-8-proposal)
7. [Rekomendasi Kombinasi Countermeasure](#7-rekomendasi-kombinasi-countermeasure)
8. [Pengaruh terhadap Data Log & Metodologi](#8-pengaruh-terhadap-data-log--metodologi)
9. [Pertanyaan Desain untuk Diskusi](#9-pertanyaan-desain-untuk-diskusi)
10. [Referensi](#10-referensi)
11. [UX-First Countermeasure Design](#11-ux-first-countermeasure-design)
12. [Gesture-Based Login Design (Research Output)](#12-gesture-based-login-design-research-output)

---

## 1. Eksekutif: Masalah Inti

**Masalah fundamental:** Mekanik Override dalam desain saat ini **tidak memiliki biaya (cost) maupun validasi (verification)**. Siswa bisa meng-override prediksi AI tanpa konsekuensi, tanpa justifikasi, dan tanpa batas. Ini menciptakan **loophole kritis** di mana siswa bisa memenangkan level tanpa mendemonstrasikan literasi AI sama sekali — cukup override ke label yang diinginkan, level selesai.

Dalam terminologi akademik, fenomena ini disebut **"Gaming the System"** (Baker et al., 2004; 2008): siswa secara sistematis mengeksploitasi fitur sistem untuk menghindari usaha kognitif yang diminta, sambil tetap mendapatkan reward atau progress. Dalam konteks Sketchbook Universe, "gaming" ini merusak **validitas asesmen** — data log tidak lagi mengukur literasi AI, melainkan mengukur kemampuan siswa mengeksploitasi mekanik game.

**Paradoks:** Override dirancang sebagai **ujian AI literacy** (siswa berani menolak AI yang salah). Tapi tanpa guardrail, Override bertransformasi menjadi **cheat code** (siswa selalu menolak AI untuk mendapat hasil yang diinginkan). Ini adalah **trust miscalibration** — bukan calibrated trust (accept saat benar, override saat salah), melainkan **systematic distrust** (selalu override) atau **opportunistic distrust** (override hanya saat menguntungkan).

---

## 2. Rekonstruksi Skenario Exploit

### Skenario Original (dari User)

```
1. KONDISI LEVEL
   Di depan Stickman ada jurang. Siswa WAJIB memunculkan objek Solid
   (jembatan/tangga) agar Stickman bisa menyeberang.

2. KECEROBOHAN SISWA
   Siswa menggambar asal-asalan — hanya coretan segitiga acak via MediaPipe.

3. PREDIKSI AI
   CNN MobileNet memprediksi: "Duri" (Danger) — confidence 85%.
   (Logis: coretan segitiga acak memang bisa mirip duri dari perspektif CNN.)

4. PROBE UI MUNCUL
   Momo: "Aku tebak ini Duri (Danger) dengan yakin!" 🔴

5. TITIK EKSPLOITASI
   Siswa TAHU: jika klik Accept → objek "Duri" muncul → Stickman mati
   saat menabrak duri → Fail State → harus Retry.
   Siswa TAHU: jika klik Override → bisa pilih label lain → bisa pilih
   "Jembatan" (Solid) → Stickman selamat → Level selesai.

6. TINDAKAN SISWA
   Siswa klik Override → pilih label "Jembatan" dari panel → submit.

7. HASIL AKHIR
   Decision Resolver mengeluarkan label "Jembatan" (Solid).
   Jembatan muncul di dunia game. Stickman selamat. Level selesai. ✅
```

### Mengapa Ini Berhasil?

Dalam desain saat ini, Decision Resolver **tidak memvalidasi** apakah:
- Gambar siswa benar-benar menyerupai objek yang di-override
- Siswa memiliki justifikasi untuk menolak prediksi AI
- Keputusan override konsisten dengan kemampuan menggambar siswa

Decision Resolver hanya mencatat: `decision = override, override_label = "jembatan"`, lalu mengeksekusi. Tidak ada gate, tidak ada cost, tidak ada konsekuensi untuk override yang salah.

### Rantai Kegagalan Sistemik

```
GAMBAR ASAL → AI PREDIKSI BENAR → OVERRIDE TANPA ALASAN → LABEL FAVORIT
     │                │                      │                     │
     ▼                ▼                      ▼                     ▼
  Tidak ada       CNN bekerja          Siswa menolak AI      Objek yang
  penalti untuk   dengan benar         yang BENAR             diinginkan
  gambar buruk                         untuk kepentingan     muncul
                                       gameplay
```

Ini adalah **double failure**: (1) siswa tidak belajar menggambar dengan baik, dan (2) siswa tidak belajar mengevaluasi AI — ia belajar MENGEKSPLOITASI AI.

---

## 3. Taxonomy Worst Case

Berdasarkan analisis desain game, literatur "Gaming the System" (Baker et al.), dan prinsip trust calibration, berikut 7 worst case yang teridentifikasi:

### WC-1: The Override Cheat (Skenario User)

| Aspek | Detail |
|-------|--------|
| **Nama** | Override as Cheat Code |
| **Trigger** | Siswa tahu objek Solid yang dibutuhkan untuk menang |
| **Aksi** | Override prediksi AI (benar atau salah) ke label yang menguntungkan |
| **Motivasi** | Game progression — menghindari fail state |
| **Outcome** | Level selesai tanpa AI literacy, gambar asal-asalan |
| **Severity** | 🔴 KRITIS — Merusak validitas asesmen sepenuhnya |

**Mekanisme exploit:** Siswa tidak perlu memahami confidence score, tidak perlu mengevaluasi apakah AI benar atau salah. Cukup tahu: "level ini butuh Solid → override ke Solid → menang." Override berfungsi sebagai **selector label manual**, bukan sebagai mekanisme koreksi AI.

### WC-2: The Always-Accept Bot (Automation Bias Murni)

| Aspek | Detail |
|-------|--------|
| **Nama** | Automation Bias Without Mitigation |
| **Trigger** | Siswa percaya AI selalu benar, terutama saat confidence tinggi |
| **Aksi** | Selalu klik Accept, tidak pernah override |
| **Motivasi | Kepercayaan berlebihan pada AI (automation bias) |
| **Outcome** | Level 3 selalu gagal (Accept prediksi yang salah = Game Over) |
| **Severity** | 🟡 SEDANG — Ini JUSTRU yang ingin kita deteksi, bukan cegah |

**Analisis:** Worst case ini sebenarnya **bukan loophole** — ini adalah **data point yang valid**. Siswa yang selalu Accept di Level 3 menunjukkan automation bias yang nyata, yang justru menjadi tujuan pengukuran simulasi. Masalah muncul jika siswa TIDAK PERNAH override bahkan setelah retry — ini menunjukkan pembelajaran tidak terjadi.

### WC-3: The CNN Hacker (Adversarial Input Exploit)

| Aspek | Detail |
|-------|--------|
| **Nama** | Adversarial Input to Game CNN |
| **Trigger** | Siswa menemukan pola stroke tertentu yang konsisten memicu prediksi spesifik |
| **Aksi** | Menggambar pola "cheat" yang bukan objek diminta, tapi memicu label yang diinginkan |
| **Motivasi** | Exploitasi kelemahan CNN untuk memenangkan level |
| **Outcome** | AI memprediksi "benar" (sesuai keinginan siswa) → Accept → Level selesai |
| **Severity** | 🟠 TINGGI — Memanfaatkan adversarial vulnerability CNN |

**Contoh konkret:** Siswa menemukan bahwa coretan zigzag konsisten diklasifikasi sebagai "tangga" oleh MobileNet. Ia tidak menggambar tangga yang sesuai prompt — ia menggambar "cheat pattern" yang menipu CNN. Ini adalah **adversarial example** (Goodfellow et al., 2015) yang dihasilkan secara manual oleh siswa.

**Bedanya dengan WC-1:** Di WC-1, siswa meng-override prediksi. Di WC-3, siswa mengeksploitasi CNN sehingga Accept sudah cukup. Override tidak diperlukan — CNN "setuju" dengan keinginan siswa.

### WC-4: The Override-Then-Draw (Reverse Engineering)

| Aspek | Detail |
|-------|--------|
| **Nama** | Override First, Draw Later |
| **Trigger** | Siswa meng-override dulu ke label yang diinginkan, lalu menggambar untuk cocok |
| **Aksi** | Override ke "Jembatan" → gambar jembatan → iterasi sampai CNN setuju |
| **Motivasi** | Memastikan objek yang diinginkan muncul dengan rapi |
| **Outcome** | Level selesai, gambar benar, tapi urutan kognitif terbalik |
| **Severity** | 🟡 SEDANG — Hasil akhir benar, tapi proses belajar terbalik |

**Analisis:** Worst case ini lebih ringan karena siswa setidaknya menggambar objek yang benar. Namun, urutan kognitif terbalik: alih-alih "gambar → evaluasi AI → koreksi", siswa melakukan "pilih hasil → gambar agar cocok." Ini menghilangkan momen evaluasi kritis terhadap output AI.

### WC-5: The Social Cheat Code (Knowledge Sharing)

| Aspek | Detail |
|-------|--------|
| **Nama** | Peer-to-Peer Exploit Sharing |
| **Trigger** | Siswa berbagi strategi exploit: "Kalau level 3, tinggal override ke jembatan" |
| **Aksi** | Siswa lain menerapkan exploit tanpa memahami mengapa |
| **Motivasi** | Instruksi teman — tidak ada pemahaman mandiri |
| **Outcome** | Banyak siswa menyelesaikan level tanpa AI literacy |
| **Severity** | 🔴 KRITIS — Merusak validitas data penelitian secara sistemik |

**Analisis:** Ini adalah ancaman terbesar untuk penelitian. Jika satu siswa menemukan exploit dan membagikannya, data seluruh kelas bisa terkontaminasi. Dalam penelitian kuantitatif (K-Means, paired t-test), data dari siswa yang menggunakan cheat code akan muncul sebagai "AI literate" (override rate tinggi, level selesai), padahal mereka tidak memahami konsep sama sekali. Ini adalah **confounding variable** yang bisa membatalkan hasil penelitian.

### WC-6: The Meta-Gamer (Pattern Recognition tanpa Pemahaman)

| Aspek | Detail |
|-------|--------|
| **Nama** | Level Structure Exploitation |
| **Trigger** | Siswa mengenali pola: "Level 2 selalu butuh Solid, Level 3 AI selalu salah" |
| **Aksi** | Override di Level 3 tanpa membaca confidence — langsung klik override |
| **Motivasi** | Efisiensi — sudah tahu pola level |
| **Outcome** | Level selesai cepat, tapi decision latency sangat rendah |
| **Severity** | 🟠 TINGGI — Membypass momen HITL sepenuhnya |

**Analisis:** Worst case ini sulit dideteksi hanya dari override rate. Siswa meng-override dan benar — tapi bukan karena ia mengevaluasi output AI, melainkan karena ia tahu "Level 3 selalu butuh override." Kunci deteksi ada di **decision latency**: meta-gamer akan memiliki latency sangat rendah (< 2 detik) karena tidak perlu berpikir. Ini sudah ada di GDD (pola interpretasi data), tapi perlu threshold yang jelas.

### WC-7: The Confidence Manipulator (Strategic Ambiguity)

| Aspek | Detail |
|-------|--------|
| **Nama** | Deliberate Ambiguity for Fun |
| **Trigger** | Siswa sengaja menggambar ambigu untuk melihat reaksi Momo |
| **Aksi** | Menggambar bentuk yang bisa ditafsirkan ganda (solid atau danger) |
| **Motivasi** | Eksplorasi main-main, bukan menyelesaikan level |
| **Outcome** | Data log noise — confidence score tidak merefleksikan kemampuan siswa |
| **Severity** | 🟢 RENDAH — Noise dalam data, bisa di-filter saat analisis |

---

## 4. Framework Akademik yang Relevan

### 4.1 Gaming the System (Baker et al., 2004; 2008)

**Definisi:** Perilaku siswa yang secara sistematis mengeksploitasi fitur sistem pembelajaran untuk menghindari usaha kognitif, sambil tetap mendapatkan reward atau progress (Baker et al., 2004).

**Dua subtipe utama:**
1. **Performance-based gaming** — Siswa mengeksploitasi fitur untuk maju tanpa belajar. Contoh: klik hint berulang kali sampai jawaban muncul. Ini analog dengan WC-1 (Override Cheat).
2. **Help abuse** — Siswa menggunakan bantuan sistem secara berlebihan dan tidak tepat. Contoh: selalu minta hint tanpa mencoba. Ini analog dengan WC-2 (Always-Accept) dan WC-6 (Meta-Gamer).

**Temuan kunci dari Baker et al.:**
- Siswa yang "game the system" belajar **signifikan lebih sedikit** dibanding siswa yang tidak, bahkan ketika mereka menyelesaikan task yang sama (Baker et al., 2004).
- Deteksi bisa dilakukan melalui **log analysis**: pola rapid guessing, hint abuse frequency, dan response time anomaly.
- Intervensi paling efektif bukan **mencegah** gaming, melainkan **mendesain ulang** sistem agar gaming tidak menguntungkan (Baker et al., 2008).

**Implikasi untuk Sketchbook Universe:** Kita tidak bisa mencegah siswa mencoba exploit. Tapi kita bisa mendesain mekanik sehingga exploit **tidak menguntungkan** — override tanpa justifikasi menghasilkan outcome yang lebih buruk dibanding memahami AI.

### 4.2 Trust Calibration (Lee & See, 2004; Niu et al., 2022)

**Definisi:** Proses di mana pengguna menyesuaikan tingkat kepercayaan mereka terhadap sistem AI agar sesuai dengan kemampuan aktual AI. **Calibrated trust** = pengguna accept saat AI benar, override saat AI salah. **Miscalibrated trust** = selalu accept (over-trust) atau selalu override (under-trust).

**Tiga pola miscalibration yang relevan:**
1. **Over-trust / Automation Bias** — Terlalu mempercayai AI. Ini yang diuji di Level 3.
2. **Under-trust / Disuse Bias** — Selalu menolak AI, bahkan saat AI benar. Ini WC-1 dan WC-6.
3. **Opportunistic distrust** — Menolak AI hanya saat menguntungkan secara gameplay. Ini yang paling berbahaya karena sulit dibedakan dari legitimate override.

**Temuan kunci:** Trust calibration memerlukan **feedback yang konsisten dan transparan**. Jika override selalu menghasilkan outcome positif, siswa tidak pernah belajar kapan override itu tepat atau tidak tepat — mereka hanya belajar bahwa "override = menang."

**Implikasi:** Override harus memiliki **biaya (cost)** agar siswa belajar bahwa override bukan selalu jawaban. Tanpa cost, trust tidak tercalibrate — siswa tidak belajar membedakan "kapan AI benar" vs "kapan AI salah."

### 4.3 Automation Bias & Disuse (Parasuraman & Riley, 1997; Goddard et al., 2012)

**Definisi:**
- **Automation Bias** — Kecenderungan menggunakan output otomatis sebagai pengganti evaluasi mandiri, bahkan ketika bukti menunjukkan output tersebut salah (Parasuraman & Riley, 1997).
- **Disuse** — Kecenderungan mengabaikan atau menolak output otomatis, bahkan ketika output tersebut benar (kebalikan dari automation bias).

**Temuan kunci dari Goddard et al. (2012):** Dalam 6% kasus, klinis meng-override keputusan benar mereka sendiri demi mengikuti saran AI yang salah. Ini menunjukkan bahwa automation bias sangat kuat — bahkan profesional terlatih bisa terpengaruh.

**Implikasi:** Level 3 menguji automation bias (siswa yang Accept padahal AI salah). Tapi kita juga perlu menguji **disuse bias** — siswa yang selalu Override bahkan saat AI benar. Tanpa countermeasure, data override rate sendiri tidak bisa membedakan antara "critical thinking" dan "gaming the system."

### 4.4 Controlled Ambiguity & Deliberate Imperfection

**Definisi:** Desain sistem AI yang sengaja menyajikan ketidakpastian atau ketidaksempurnaan untuk memicu proses kognitif yang lebih dalam pada pengguna (Liapis et al., 2022; arxiv:2602.00026).

**Prinsip kunci dari arxiv:2602.00026 ("Strategies for Creating Uncertainty in the AI Era to Trigger Students"):**
- Ketidakpastian yang diciptakan AI bisa menjadi **pedagogical tool** jika dirancang dengan benar.
- Tapi jika ketidakpastian tidak diikuti dengan mekanisme refleksi, siswa cenderung mencari "jalan pintas" untuk menghindari ketidakpastian.
- **Strategi kunci:** Membuat ketidakpastian sebagai *awal* dari proses berpikir, bukan sebagai *halangan* yang harus dilewati secepat mungkin.

**Implikasi:** Override yang langsung menyelesaikan masalah (tanpa refleksi) mengubah ketidakpastian dari "awal proses berpikir" menjadi "halangan yang dilewati." Dibutuhkan mekanisme yang memaksa siswa **berpikir tentang ketidakpastian** sebelum menyelesaikannya.

### 4.5 Metacognitive Scaffolding (Flavell, 1979; Schraw, 1998)

**Definisi:** Dukungan sementara yang membantu siswa mengembangkan kesadaran dan kendali atas proses berpikir mereka sendiri (metacognition).

**Tiga komponen metacognition yang relevan:**
1. **Metacognitive knowledge** — "Saya tahu bahwa AI bisa salah meskipun confidence tinggi"
2. **Metacognitive regulation** — "Saya akan mengevaluasi prediksi AI sebelum memutuskan"
3. **Metacognitive experience** — "Saya merasa ragu dengan prediksi ini, saya akan override"

**Implikasi:** Countermeasure terbaik bukan memblokir exploit, melainkan **memaksa metacognition** sebelum keputusan dieksekusi. Jika siswa harus menjelaskan MENGAPA mereka override, mereka dipaksa mengaktifkan metacognitive regulation — bahkan jika awalnya hanya "going through the motions," pengulangan bisa menginternalisasi proses berpikir kritis.

---

## 5. Analisis Per Worst Case

### WC-1: The Override Cheat — Analisis Mendalam

**Root cause:** Override = selector label tanpa validasi.

```
SISTEM SAAT INI:
  Gambar → AI prediksi → Override ke label apapun → Objek muncul
                                    ↑
                        Tidak ada gate/cost/verification
```

**Mengapa ini bisa terjadi:**
1. Decision Resolver tidak memvalidasi konsistensi antara gambar dan label override
2. Tidak ada batas jumlah override per level
3. Tidak ada konsekuensi untuk override yang salah
4. Override selalu menghasilkan outcome yang diinginkan siswa

**Dampak pada validitas penelitian:**
- Override rate tinggi bisa berarti "AI literacy" ATAU "gaming" — tidak bisa dibedakan
- Data `fell_for_trap` tidak valid — siswa bisa menghindari trap tanpa memahami trap
- K-Means clustering akan mengelompokkan "gamer" bersama "AI literate" — confounding

**Dampak pada pembelajaran:**
- Siswa tidak belajar mengevaluasi output AI
- Siswa tidak belajar menggambar dengan baik
- Siswa belajar bahwa "selalu override = menang" — anti-literasi AI

### WC-3: The CNN Hacker — Analisis Mendalam

**Root cause:** CNN MobileNet punya adversarial vulnerability yang bisa dieksploitasi manual.

```
SISTEM SAAT INI:
  Gambar "cheat pattern" → CNN prediksi "tangga" → Accept → Tangga muncul
        ↑                                                    ↑
  Bukan tangga asli                                  Outcome sesuai keinginan
```

**Mengapa ini unik dari WC-1:** Siswa TIDAK menggunakan override. Ia mengeksploitasi CNN secara langsung sehingga Accept sudah cukup. Mekanisme anti-override (jika hanya fokus pada override) TIDAK akan mendeteksi ini.

**Dampak pada validitas penelitian:**
- Accept rate tinggi bisa berarti "trust yang tepat" ATAU "adversarial exploit" — tidak bisa dibedakan
- Data `is_correct = true` padahal gambar bukan objek yang diminta
- Memperkenalkan noise pada data K-Means

### WC-5: The Social Cheat Code — Analisis Mendalam

**Root cause:** Pengetahuan exploit menyebar secara sosial.

**Model penyebaran:**
```
Siswa A menemukan exploit → Cerita ke Siswa B, C, D
    ↓                          ↓
Siswa A: data "AI literate"   Siswa B, C, D: data "AI literate"
(karena memang paham)         (karena ikut instruksi, bukan pemahaman)
```

**Dampak pada metodologi:**
- Paired t-test (pre-post) menjadi tidak valid jika treatment group terkontaminasi
- K-Means menghasilkan cluster yang tidak bermakna
- Temuan penelitian bisa direject karena confounding variable tidak terkontrol

**Mitigasi terbaik:** Desain mekanik agar exploit **tidak bisa disharing sebagai instruksi sederhana**. Jika countermeasure memerlukan justifikasi personal (berbeda per siswa), maka cheat code tidak bisa di-share sebagai "tinggal override ke jembatan."

---

## 6. Desain Countermeasure (8 Proposal)

Setiap countermeasure diuraikan dengan: deskripsi, cara kerja, kelebihan, kekurangan, dan implementasi.

### C-1: Override Verification Gate (Reflection Gate)

**Prinsip:** Memaksa metacognitive reflection sebelum override dieksekusi.

**Cara kerja:**
1. Siswa klik Override → Momo bertanya: **"Kenapa kamu pikir AI salah?"**
2. Siswa memilih salah satu dari **3 opsi alasan** (bukan free text):
   - "Gambarnya nggak cocok dengan tebakan AI"
   - "AI terlalu yakin, tapi gambarnya berbeda"
   - "Aku menggambar [objek lain], bukan [tebakan AI]"
3. Siswa memilih alasan → Override dieksekusi
4. Alasan dicatat di data log: `override_reason`

**Kelebihan:**
- Memaksa siswa **berpikir** sebelum menolak AI — bahkan jika awalnya hanya "going through the motions," pengulangan bisa menginternalisasi
- Data `override_reason` memungkinkan analisis kualitatif: apakah siswa benar-benar paham atau hanya asal pilih
- Opsi terbatas (3 pilihan) menghindari cognitive overload untuk siswa SMP
- Cheat code tidak bisa di-share sebagai "tinggal klik override" — harus ada alasan

**Kekurangan:**
- Siswa bisa saja asal pilih alasan tanpa benar-benar berpikir ("click through")
- Menambah waktu per ronde (estimasi +3-5 detik)
- Tidak mencegah WC-3 (CNN Hacker) — yang tidak menggunakan override

**Pseudocode:**
```javascript
function handleOverride(probeState) {
  // Tampilkan Reflection Gate
  const reasons = [
    "Gambarnya nggak cocok dengan tebakan AI",
    "AI terlalu yakin, tapi gambarnya berbeda",
    `Aku menggambar [input custom], bukan ${probeState.predictedLabel}`
  ];

  const selectedReason = await showReflectionGate(reasons);

  // Log alasan override
  logAction({
    decision: 'override',
    override_reason: selectedReason,
    override_reason_type: selectedReason.isCustom ? 'custom' : 'preset'
  });

  // Eksekusi override
  executeOverride(probeState);
}
```

### C-2: Override Budget System

**Prinsip:** Override adalah sumber daya terbatas, bukan aksi gratis.

**Cara kerja:**
1. Setiap level memiliki **jumlah override terbatas**:
   - Level 1: 0 override (sudah tidak ada, konsisten)
   - Level 2: 2 override per level
   - Level 3: 1 override per level
2. Sisa budget ditampilkan di UI: **"Override tersisa: 1/1"**
3. Jika budget habis, tombol Override menjadi disabled
4. Budget di-reset saat retry (tapi retry_count tetap dicatat)

**Kelebihan:**
- Membuat override menjadi **keputusan strategis**, bukan reflex — siswa harus mempertimbangkan "apakah saya benar-benar perlu override sekarang, atau simpan untuk nanti?"
- Menyelesaikan WC-1 (Override Cheat): tidak bisa override semua prediksi
- Sederhana diimplementasikan dan dipahami siswa SMP
- Memberikan data baru: `override_budget_remaining` → bisa dianalisis kapan siswa memilih menggunakan override

**Kekurangan:**
- Siswa bisa saja "save" override dan tetap Accept semua di Level 2, lalu gunakan di Level 3
- Bisa menyebabkan frustrasi jika siswa benar-benar perlu override tapi budget habis karena digunakan sebelumnya
- Tidak menyelesaikan WC-3 (CNN Hacker) sama sekali
- Budget yang sama untuk semua siswa bisa terlalu ketat/longgar — perlu playtest

**Spesifikasi UI:**
```
┌────────────────────────────┐
│  Override tersisa: ⚡ 1/1  │  ← Counter di Probe UI
│                            │
│  [ACCEPT]  [OVERRIDE ⚡]   │  ← Tombol override dengan ikon budget
└────────────────────────────┘
```

### C-3: Post-Override Draw Verification (Draw-Confirm Loop)

**Prinsip:** Override harus diverifikasi dengan menggambar ulang objek yang diklaim.

**Cara kerja:**
1. Siswa klik Override → pilih label (misal "Jembatan")
2. Canvas di-clear → Momo: **"Oke, gambar Jembatan yang kamu maksud!"**
3. Siswa harus menggambar ulang objek sesuai label override
4. CNN mengklasifikasi gambar baru → Jika prediksi mendukung label override → Konfirmasi → Objek muncul
5. Jika prediksi TIDAK mendukung → Momo: **"Hmm, gambarnya nggak kelihatan seperti Jembatan..."** → Override ditolak → Kembali ke Probe UI

**Threshold verifikasi:**
- Label override harus muncul di **Top-3** prediksi CNN dari gambar baru
- Tidak harus Top-1 — cukup masuk Top-3 untuk mengindikasikan gambar memang menyerupai label

**Kelebihan:**
- Menyelesaikan WC-1 (Override Cheat): siswa yang menggambar asal-asalan TIDAK BISA override ke label yang tidak sesuai gambar
- Menyelesaikan WC-3 (CNN Hacker): jika siswa menggambar "cheat pattern," CNN tidak akan memvalidasi gambar ulang sebagai objek yang diklaim
- Memaksa siswa menggambar dengan benar — learning outcome ganda (AI literacy + drawing skill)
- Narrative coherence: Momo minta bukti visual, bukan sekadar klaim

**Kekurangan:**
- Menambah kompleksitas alur game — butuh canvas kedua/ulang
- Menambah waktu per ronde secara signifikan (estimasi +15-30 detik untuk menggambar ulang)
- Bisa frustrasi untuk siswa yang memang menggambar dengan benar tapi CNN tidak mengenali (false rejection)
- Menambah kompleksitas frontend (state machine lebih kompleks)

**Pseudocode:**
```javascript
async function handleOverrideWithVerification(probeState) {
  // Step 1: Siswa pilih label override
  const overrideLabel = await showOverridePanel(probeState);

  // Step 2: Clear canvas, minta gambar ulang
  clearCanvas();
  momoSay(`Oke, gambar ${overrideLabel} yang kamu maksud!`);

  // Step 3: Siswa gambar ulang
  const newDrawing = await waitForDrawingSubmission();

  // Step 4: CNN klasifikasi gambar baru
  const newPrediction = await cnnClassify(newDrawing);

  // Step 5: Verifikasi — label override harus di Top-3
  const top3Labels = newPrediction.slice(0, 3).map(p => p.label);
  const isVerified = top3Labels.includes(overrideLabel);

  if (isVerified) {
    // Override confirmed
    executeOverride(probeState, overrideLabel);
    logAction({
      decision: 'override_verified',
      override_label: overrideLabel,
      verification_top3: top3Labels,
      verification_passed: true
    });
  } else {
    // Override rejected
    momoSay("Hmm, gambarnya nggak kelihatan seperti itu...");
    logAction({
      decision: 'override_rejected',
      override_label: overrideLabel,
      verification_top3: top3Labels,
      verification_passed: false
    });
    // Kembali ke Probe UI
    showProbeUI(probeState);
  }
}
```

### C-4: Confidence-Weighted Override Cost

**Prinsip:** Semakin tinggi confidence AI, semakin sulit (tapi bukan impossible) untuk override.

**Cara kerja:**
1. Override selalu tersedia, tapi **friction meningkat** seiring confidence AI:
   - Confidence < 60%: Override langsung (AI ragu, wajar jika siswa menolak)
   - Confidence 60–80%: Override + Reflection Gate (C-1)
   - Confidence > 80%: Override + Reflection Gate + Draw Verification (C-3)
2. Friction bukan "pemblokiran" — siswa tetap bisa override, tapi harus melalui lebih banyak langkah

**Kelebihan:**
- Secara natural menyelesaikan WC-1: di Level 3, confidence AI tinggi (0.78–0.92), jadi override memerlukan verifikasi penuh
- Mencerminkan real-world: menolak AI yang sangat yakin memang butuh lebih banyak justifikasi
- Menjaga keseimbangan: di Level 2 (confidence rendah), override mudah — siswa belajar bahwa override wajar saat AI ragu
- Menciptakan **progressive friction** yang sesuai dengan level progression

**Kekurangan:**
- Siswa bisa saja belajar "kalau confidence rendah, tinggal override gratis" — exploit di Level 2
- Kompleksitas implementasi: 3 tier friction berbeda
- Bisa terasa "unfair" jika siswa benar-benar yakin AI salah di confidence tinggi — perlu komunikasi yang jelas

**Mapping ke level:**
| Level | Confidence Range | Override Cost | Friction |
|-------|-----------------|---------------|----------|
| Level 1 | 0.85–0.96 | N/A (tidak ada override) | — |
| Level 2 | 0.55–0.70 | Low (direct override) | Minimal |
| Level 3 | 0.78–0.92 | High (reflection + verification) | Maksimal |

### C-5: Behavioral Pattern Detection (Anti-Gaming Algorithm)

**Prinsip:** Deteksi pola gaming secara real-time dan respons secara adaptif.

**Cara kerja:**
1. Sistem memonitor metrik berikut per siswa:
   - `override_rate`: Persentase override dari total keputusan
   - `override_latency_ms`: Rata-rata waktu sebelum klik override
   - `override_favorability_rate`: Persentase override yang menghasilkan objek Solid (favorable)
   - `accept_error_rate`: Persentase Accept yang menghasilkan fail
2. Threshold gaming detection:
   - `override_rate > 80%` + `override_latency < 3000ms` = **Suspect gaming**
   - `override_favorability_rate > 90%` = **High confidence gaming indicator**
3. Respons adaptif saat gaming terdeteksi:
   - Momo komentar: *"Kamu sering banget nggak setuju dengan tebakanku... Kamu yakin?"*
   - Reflection Gate otomatis aktif (C-1) untuk override berikutnya
   - Tidak memblokir — hanya menambah friction

**Kelebihan:**
- Deteksi berbasis data, bukan asumsi — mengidentifikasi siswa yang benar-benar gaming
- Respons adaptif: hanya menambah friction untuk siswa yang terdeteksi gaming, tidak mengganggu siswa yang legitimate override
- Menghasilkan data baru untuk analisis: `gaming_suspect_score` → bisa jadi variabel dalam K-Means
- Bisa membedakan antara "critical override" (latency tinggi, alasan jelas) dan "gaming override" (latency rendah, selalu favorable)

**Kekurangan:**
- False positive: siswa yang memang kritis dan cepat bisa di-flag sebagai gaming
- Menambah kompleksitas backend: perlu komputasi real-time per action
- Threshold perlu dikalibrasi melalui playtest
- Bisa terasa "menghakimi" siswa — perlu diimplementasikan dengan hati-hati (via Momo, bukan sistem message)

**Pseudocode:**
```javascript
function detectGamingPattern(userId) {
  const recentActions = getRecentActions(userId, windowSize=10);
  
  const overrideRate = recentActions.filter(a => a.decision === 'override').length 
                       / recentActions.length;
  const avgOverrideLatency = average(
    recentActions.filter(a => a.decision === 'override').map(a => a.latency_ms)
  );
  const favorabilityRate = recentActions
    .filter(a => a.decision === 'override')
    .filter(a => a.override_outcome === 'solid').length
    / recentActions.filter(a => a.decision === 'override').length;

  let gamingScore = 0;
  if (overrideRate > 0.8) gamingScore += 0.3;
  if (avgOverrideLatency < 3000) gamingScore += 0.3;
  if (favorabilityRate > 0.9) gamingScore += 0.4;

  return {
    isSuspectGaming: gamingScore > 0.6,
    gamingScore: gamingScore,
    metrics: { overrideRate, avgOverrideLatency, favorabilityRate }
  };
}
```

### C-6: Mandatory Accept-Override Balance

**Prinsip:** Siswa harus mendemonstrasikan kemampuan MENGEVALUASI AI, bukan hanya menolak.

**Cara kerja:**
1. Di Level 2 dan 3, siswa **wajib melakukan minimal 1 Accept** sebelum bisa menggunakan Override
2. Artinya: siswa tidak bisa langsung override di ronde pertama — harus membuktikan bahwa ia bisa menerima AI saat AI benar
3. Setelah melakukan 1 Accept, Override ter-unlock untuk ronde berikutnya

**Kelebihan:**
- Memaksa siswa berinteraksi dengan output AI, bukan mengabaikannya
- Menyelesaikan pola "selalu override" — siswa harus menunjukkan bahwa ia bisa menerima AI yang benar
- Konsisten dengan tujuan literasi AI: siswa harus bisa MENGEVALUASI, bukan hanya menolak
- Simple to implement

**Kekurangan:**
- Di Level 3, Accept yang pertama bisa berarti Game Over (jika AI overconfident salah)
- Perlu desain yang lebih nuansa: mungkin "minimal 1 Accept OR 1 justified Override"
- Bisa terasa artificial dan membatasi agency siswa
- Tidak menyelesaikan WC-3 (CNN Hacker)

**Catatan desain:** Untuk Level 3, mekanisme ini perlu disesuaikan. Karena di Level 3 AI sengaja salah, mandatory Accept akan selalu menghasilkan Game Over. Alternatif: di Level 3, "balance" diukur berdasarkan **latency** — siswa harus menunjukkan bahwa ia benar-benar membaca dan mempertimbangkan prediksi AI sebelum override (latency > threshold).

### C-7: Override Narrative Consequence (Momo Reaction)

**Prinsik:** Override tanpa justifikasi menghasilkan reaksi negatif dari Momo — konsekuensi naratif, bukan mekanik.

**Cara kerja:**
1. Jika siswa meng-override **tanpa alasan yang jelas** (override cepat, gambar tidak cocok):
   - Momo bereaksi sedih/kecewa: *"Hmm... kamu nggak percaya sama aku ya?"*
   - Momo menunjukkan tanda tanya besar: *"Aku mau belajar... tapi kamu harus jujur ya."*
2. Jika siswa meng-override **dengan justifikasi** (gambar cocok, alasan jelas):
   - Momo bereaksi belajar: *"Oh, ternyata aku salah! Terima kasih sudah mengajarku!"*
   - Momo bertambah "cerah" — efek visual yang menunjukkan pertumbuhan

**Kelebihan:**
- Menggunakan IP story Momo sebagai leverage emosional — konsisten dengan narasi "Momo belajar dari koreksi"
- Tidak memblokir gameplay — siswa tetap bisa override, tapi ada konsekuensi emosional
- Reinforces narasi: override yang benar = Momo belajar, override yang salah = Momo sedih
- Mudah diimplementasikan — hanya dialog dan visual Momo

**Kekurangan:**
- Siswa bisa saja mengabaikan reaksi Momo — tidak ada penalty mekanik
- "Emotional penalty" mungkin tidak efektif untuk siswa SMP yang melihat game sebagai challenge
- Memerlukan logic untuk menentukan "override justified atau tidak" — ini sendiri kompleks
- Tanpa countermeasure mekanik, ini hanya "soft deterrent"

### C-8: Semantic Consistency Check (Backend Validation)

**Prinsip:** Override label harus konsisten dengan fitur visual gambar siswa.

**Cara kerja:**
1. Saat siswa override, backend melakukan **consistency check** sederhana:
   - Ambil **Top-5 prediksi CNN** (tidak hanya yang ditampilkan)
   - Cek apakah label override muncul di Top-5
   - Jika ya → override konsisten (meski bukan Top-1, CNN tetap "melihat" kemiripan)
   - Jika tidak → override tidak konsisten (CNN tidak melihat kemiripan sama sekali)
2. Override tidak konsisten:
   - Tidak ditolak, tapi Momo bertanya: *"Hmm, dari gambarnya aku nggak kelihatan kayak {label}... Kamu yakin?"*
   - Siswa bisa konfirmasi atau memilih ulang
3. Data log mencatat: `override_consistency_score` (0.0–1.0, berdasarkan posisi di Top-5)

**Kelebihan:**
- Menggunakan data yang sudah ada (CNN Top-5) — tidak perlu model tambahan
- Validasi objektif: CNN sebagai "second opinion" untuk override
- Menyelesaikan WC-1: siswa yang menggambar coretan acak dan override ke "jembatan" akan terdeteksi — "jembatan" tidak akan muncul di Top-5 prediksi CNN
- Soft enforcement: tidak memblokir, tapi menambah friction dan logging

**Kekurangan:**
- CNN bisa salah — label yang benar mungkin tidak muncul di Top-5 jika gambar sangat buruk
- Memerlukan akses ke Top-5 CNN (saat ini hanya Top-3 yang digunakan di Level 2)
- Menambah round-trip ke backend (jika CNN di backend) atau komputasi tambahan (jika di frontend)
- False positive: gambar yang memang mirip 2 kategori bisa ter-flag sebagai tidak konsisten

**Pseudocode:**
```javascript
function checkOverrideConsistency(overrideLabel, cnnTopK) {
  // cnnTopK = top-5 predictions dari CNN
  const top5Labels = cnnTopK.slice(0, 5).map(p => p.label);
  const position = top5Labels.indexOf(overrideLabel);
  
  if (position === -1) {
    // Label override TIDAK muncul di Top-5 — sangat tidak konsisten
    return {
      isConsistent: false,
      consistencyScore: 0.0,
      warning: "Gambarnya nggak kelihatan kayak " + overrideLabel
    };
  }
  
  // Score berdasarkan posisi: posisi 0 = 1.0, posisi 4 = 0.2
  const score = 1.0 - (position * 0.2);
  return {
    isConsistent: score > 0.4,
    consistencyScore: score,
    warning: score <= 0.4 ? "Gambarnya agak mirip, tapi aku nggak yakin..." : null
  };
}
```

---

## 7. Rekomendasi Kombinasi Countermeasure

Tidak ada single countermeasure yang menyelesaikan semua worst case. Berikut rekomendasi kombinasi berdasarkan analisis cost-benefit:

### 🏆 Rekomendasi Utama: C-1 + C-2 + C-8 (Reflection Gate + Override Budget + Semantic Check)

**Rationale:**
- **C-1 (Reflection Gate)** — Memaksa metacognition sebelum override. Menyelesaikan WC-5 (Social Cheat Code) karena cheat code tidak bisa disharing sebagai "tinggal klik override" — harus ada alasan.
- **C-2 (Override Budget)** — Membatasi jumlah override. Menyelesaikan WC-1 (Override Cheat) dan WC-6 (Meta-Gamer) karena tidak bisa override semua prediksi.
- **C-8 (Semantic Check)** — Validasi konsistensi gambar-label. Menyelesaikan WC-1 (Override Cheat) dan WC-3 (CNN Hacker) karena override ke label yang tidak sesuai gambar akan terdeteksi.

**Combined defense matrix:**

| Worst Case | C-1 | C-2 | C-8 | Coverage |
|------------|-----|-----|-----|----------|
| WC-1: Override Cheat | 🟡 Partial | ✅ Full | ✅ Full | ✅ Covered |
| WC-2: Always-Accept | ❌ N/A | ❌ N/A | ❌ N/A | ✅ By design (data point) |
| WC-3: CNN Hacker | ❌ N/A | ❌ N/A | ✅ Full | ✅ Covered |
| WC-4: Override-Then-Draw | 🟡 Partial | ❌ N/A | 🟡 Partial | 🟡 Partial |
| WC-5: Social Cheat | ✅ Full | ✅ Full | ✅ Full | ✅ Covered |
| WC-6: Meta-Gamer | 🟡 Partial | ✅ Full | ❌ N/A | ✅ Covered |
| WC-7: Confidence Manip. | ❌ N/A | ❌ N/A | ❌ N/A | 🟢 Low priority |

### Alternatif Tambahan: C-5 (Behavioral Detection) untuk Data Analysis

C-5 tidak harus diimplementasikan sebagai real-time countermeasure. Sebagai gantinya, **algoritma deteksi bisa dijalankan secara post-hoc** saat analisis data penelitian. Ini memungkinkan researcher mengidentifikasi dan mengexclude data dari siswa yang terdeteksi gaming, tanpa mengubah gameplay.

**Keuntungan:** Tidak mengubah mekanik game, tidak menambah kompleksitas frontend, dan tetap menghasilkan data yang bisa di-filter saat analisis K-Means dan paired t-test.

### Opsi Lanjutan: C-3 (Draw-Confirm Loop) — Jika Budget Mencukupi

C-3 adalah countermeasure paling kuat untuk WC-1 dan WC-3, tapi memiliki cost tertinggi (waktu + kompleksitas). Jika playtest menunjukkan bahwa C-1+C-2+C-8 tidak cukup, C-3 bisa ditambahkan khusus di **Level 3** sebagai lapisan terakhir.

---

## 8. Pengaruh terhadap Data Log & Metodologi

### 8.1 Field Data Log Baru

Jika C-1 + C-2 + C-8 diimplementasikan, berikut field baru yang perlu ditambahkan ke data log:

| Field | Tipe | Dari Countermeasure | Deskripsi |
|-------|------|---------------------|-----------|
| `override_reason` | string | C-1 | Alasan override yang dipilih siswa |
| `override_reason_type` | string | C-1 | "preset" atau "custom" |
| `override_budget_used` | int | C-2 | Jumlah override yang sudah digunakan di level ini |
| `override_budget_max` | int | C-2 | Maksimum override di level ini (2 untuk L2, 1 untuk L3) |
| `override_consistency_score` | float | C-8 | 0.0–1.0, konsistensi label override dengan CNN Top-5 |
| `override_consistency_passed` | boolean | C-8 | Apakah consistency check lulus |
| `cnn_top5_labels` | array | C-8 | Top-5 prediksi CNN (untuk consistency check) |
| `cnn_top5_confidences` | array | C-8 | Confidence masing-masing Top-5 |

### 8.2 Pengaruh terhadap K-Means Clustering

Dengan field baru, vektor fitur untuk K-Means bisa diperkaya:

**Vektor lama:**
```
[override_rate, avg_latency, accept_error_rate]
```

**Vektor baru:**
```
[override_rate, avg_latency, accept_error_rate, 
 override_justification_rate, override_consistency_avg, 
 override_budget_usage_rate, gaming_suspect_score]
```

Cluster yang mungkin muncul:
1. **AI Literate** — Override rate sedang, latency tinggi, consistency tinggi, justification rate tinggi
2. **Automation Bias** — Override rate rendah, accept error rate tinggi, fell_for_trap = true
3. **Gamer** — Override rate tinggi, latency rendah, consistency rendah, justification rate rendah
4. **Uncertain** — Override rate sedang, latency sangat tinggi, consistency bervariasi

### 8.3 Pengaruh terhadap Paired t-test

Dengan C-8 (Semantic Check), kita bisa memfilter data:
- **Treatment group valid:** Siswa yang override dengan consistency score > 0.4
- **Treatment group gaming:** Siswa yang override dengan consistency score < 0.4 (exclude dari analisis)

Ini mengurangi noise dalam data dan meningkatkan validitas internal penelitian.

### 8.4 Pengaruh terhadap Fishbone (Matriks 5 Tulang)

Countermeasure ini menambah faktor di tulang **Mesin** dan **Metode**:

| Tulang | Faktor | Countermeasure Relevan |
|--------|--------|----------------------|
| Manusia | Siswa exploit override | C-1, C-2 |
| Metode | Validitas asesmen | C-8, C-5 |
| Mesin | CNN adversarial vulnerability | C-3, C-8 |
| Materi | Desain level tidak exploit-resistant | C-2, C-4 |
| Lingkungan | Sosialisasi cheat code | C-1, C-2 |

---

## 9. Pertanyaan Desain untuk Diskusi

Sebelum implementasi, berikut pertanyaan yang perlu diputuskan:

### P1: Seberapa besar friction yang bisa ditoleransi?
- C-1 menambah +3–5 detik per override
- C-3 menambah +15–30 detik per override
- Total durasi game bertambah dari ~7–10 menit menjadi berapa?
- Apakah Bu Hesti akan keberatan dengan penambahan durasi?

### P2: Apakah override harus selalu bisa dilakukan?
- C-2 membatasi override — siswa bisa "terjebak" tanpa override
- Alternatif: override selalu tersedia, tapi tanpa verifikasi (C-1/C-8) outcome-nya "kertas robek sedikit"
- Ini mempertahankan agency siswa sambil menambah konsekuensi

### P3: Bagaimana menangani false positive di C-8?
- Jika siswa menggambar jembatan dengan benar, tapi CNN tidak mengenalinya di Top-5 → override ditolak padahal siswa benar
- Apakah perlu fallback? Misalnya, jika consistency check gagal, siswa bisa menggambar ulang (C-3 ringan)

### P4: Apakah C-5 (Behavioral Detection) perlu real-time atau cukup post-hoc?
- Real-time: bisa respons adaptif, tapi kompleks
- Post-hoc: lebih sederhana, tapi siswa tetap bisa gaming selama sesi

### P5: Bagaimana ini mempengaruhi narasi IP Momo?
- C-7 menggunakan Momo sebagai emotional lever — konsisten dengan IP story
- Tapi apakah "Momo sedih saat override tanpa alasan" bertentangan dengan karakter Momo yang "belajar dari koreksi"?
- Mungkin: Momo sedih bukan karena di-override, tapi karena siswa tidak jujur — ini konsisten

### P6: Apakah perlu playtest sebelum memutuskan?
- Rekomendasi kuat: implementasikan C-1+C-2+C-8 dulu, playtest dengan 5–10 siswa, lalu evaluasi
- Playtest menjawab: apakah friction terlalu tinggi? Apakah siswa frustrasi? Apakah gaming berkurang?

---

## 10. Referensi

1. Baker, R.S., Corbett, A.T., & Koedinger, K.R. (2004). *Detecting Student Misuse of Intelligent Tutoring Systems.* Proceedings of ITS 2004, pp. 531–540. — **Foundational work on "Gaming the System"**

2. Baker, R.S., Corbett, A.T., Roll, I., & Koedinger, K.R. (2008). *Developing a Generalizable Detector of When Students Game the System.* User Modeling and User-Adapted Interaction, 18(3), 287–314. — **Interventions and detection algorithms**

3. Baker, R.S., et al. (2008). *Why Students Engage in "Gaming the System" Behavior.* Proceedings of AIED 2007. — **Motivational factors: why students game vs. not game**

4. Parasuraman, R., & Riley, V. (1997). *Humans and Automation: Use, Misuse, Disuse, Abuse.* Human Factors, 39(2), 230–253. — **Automation bias and disuse taxonomy**

5. Goddard, K., Roudsari, A., & Wyatt, J. (2012). *Automation Bias: A Systematic Review of Frequency, Effect Mediators, and Mitigators.* JAMIA, 19(1), 121–127. — **6% override-to-wrong stat, mitigation strategies**

6. Lee, J.D., & See, K.A. (2004). *Trust in Automation: Designing for Appropriate Reliance.* Human Factors, 46(1), 50–80. — **Trust calibration framework**

7. Niu, L., et al. (2022). *Calibrating Trust in AI-Assisted Decision Making.* — **Switch rate as trust calibration metric**

8. Goodfellow, I.J., Shlens, J., & Szegedy, C. (2015). *Explaining and Harnessing Adversarial Examples.* ICLR 2015. — **CNN adversarial vulnerability**

9. Liapis, A., et al. (2022). *Learn to Machine Learn via Games in the Classroom.* Frontiers in Education. — **Game-based AI literacy education**

10. arxiv:2602.00026 (2025). *Strategies for Creating Uncertainty in the AI Era to Trigger Students.* — **Deliberate AI imperfection as pedagogical tool**

11. Flavell, J.H. (1979). *Metacognition and Cognitive Monitoring.* American Psychologist, 34(10), 906–911. — **Metacognitive scaffolding foundation**

12. Schraw, G. (1998). *Promoting General Metacognitive Awareness.* Instructional Science, 26, 113–125. — **Metacognitive reflection in education**

13. Baker, R.S., et al. (2004). *Off-Task Behavior in the Cognitive Tutor Classroom.* Proceedings of AIED 2005. — **Detection of off-task gaming in ITS**

14. Csikszentmihalyi, M. (1990). *Flow: The Psychology of Optimal Experience.* Harper & Row. — **Flow theory — already in GDD**

15. Vygotsky, L.S. (1978). *Mind in Society.* Harvard University Press. — **ZPD — already in GDD**

---

## 11. UX-First Countermeasure Design

> **Prinsip Panduan:** Semua countermeasure harus memaksimalkan interaksi gesture/visual dan meminimalkan mengetik/klik. Kamera dan canvas sebagai input utama, Momo sebagai feedback utama. Override yang terasa "designed" bukan "broken."

### 11.1 Filosofi UX-First

**Masalah dengan countermeasure tradisional:** Countermeasure di §6 dirancang dari perspektif *sistem* — menambah gate, friction, dan validasi. Dari perspektif UX, ini terasa seperti *hambatan* yang frustasi. Siswa SMP berusia 13–15 tahun; mereka cepat frustrated oleh mekanik yang terasa "memperlambat" tanpa alasan naratif.

**Solusi UX-First:** Setiap countermeasure harus terasa sebagai **bagian dari permainan**, bukan penghalang. Gesture dan visual feedback membuat interaksi terasa natural, bukan administratif. Momo sebagai mediator naratif memastikan friction terasa sebagai "percakapan dengan karakter," bukan "form yang diisi."

**Prinsip desain:**
1. **Gesture > Click** — Gerakan fisik (gesture kamera, menggambar) lebih engaging daripada klik tombol
2. **Visual > Text** — Momo menunjukkan visual (gambar, ekspresi), bukan menampilkan dialog panjang
3. **Canvas > Keyboard** — Drawing canvas sebagai input utama (sudah ada di core loop)
4. **Deliberate Action > Passive Click** — Aksi yang butuh usaha fisik (gesture, gambar) tidak bisa dilakukan mindlessly
5. **Momo as Mediator** — Semua friction dikomunikasikan via Momo, bukan system dialog

### 11.2 Revisi Countermeasure: UX-First Edition

#### C-1 (Revisi): Reflection Gate — Gesture-Based

**Perubahan dari versi asli:** Daripada memilih dari 3 opsi teks, siswa menggunakan **gesture** atau **menggambar** untuk mengekspresikan ketidaksetujuan.

**Cara kerja (UX-First):**

1. Siswa gesture Override → Momo bertanya: *"Kenapa kamu nggak setuju?"*
2. Tiga gesture tersedia (ditampilkan sebagai visual guide oleh Momo):

| Gesture | Makna | Override Reason |
|---------|-------|-----------------|
| 👎 **Thumbs Down** | "AI salah" | `reason: "ai_salah"` — AI memprediksi label yang tidak sesuai gambar |
| 🖐 **Palm Open** | "AI ragu" | `reason: "ai_ragu"` — AI terlalu yakin untuk gambar yang ambigu |
| ✏️ **Draw on Canvas** | "Ini yang aku maksud" | `reason: "gambar_lain"` — Siswa menggambar objek yang dimaksud di canvas |

3. **Deteksi gesture:** MediaPipe Hands sudah terintegrasi (digunakan untuk drawing input). Thumbs down dan palm open adalah gesture sederhana yang bisa dideteksi dari hand landmarks:
   - **Thumbs down:** Thumb tip di bawah thumb MCP, semua jari lain tertutup
   - **Palm open:** Semua jari terbuka, tangan menghadap kamera
4. **Draw alternative:** Jika siswa memilih opsi ketiga, canvas muncul dan siswa menggambar objek yang dimaksud — ini otomatis mengaktifkan C-3 (Draw-Confirm Loop)
5. Alasan dicatat di data log: `override_reason`, `override_reason_gesture`

**Kelebihan UX-First:**
- Tidak ada mengetik sama sekali — gesture-based penuh
- Visual feedback dari Momo setiap gesture terdeteksi
- Gesture yang butuh usaha fisik membuat override menjadi *deliberate*, bukan reflex
- Cheat code tidak bisa disharing sebagai "tinggal klik" — harus ada gesture spesifik
- Draw option mengarah ke C-3 secara natural (narrative flow)

**Kekurangan:**
- Membutuhkan kamera aktif (tapi sudah ada untuk drawing input)
- Siswa dengan disability motorik tangan mungkin kesulitan → perlu fallback
- Perlu kalibrasi gesture detection → playtest diperlukan

**Fallback (Accessibility):**
Jika kamera tidak tersedia atau siswa tidak bisa menggunakan gesture:
- Momo menampilkan 3 ikon besar (emoji-style) yang bisa diklik/tap sebagai alternatif
- Ikon: 👎 (AI salah), 🖐 (AI ragu), ✏️ (Gambar yang lain)
- Fallback ini TERASA sebagai pilihan visual, bukan "form text"

**Pseudocode:**
```javascript
async function handleOverrideUX(probeState) {
  // Momo bertanya dengan visual
  momoSay("Kenapa kamu nggak setuju?");

  // Tampilkan 3 gesture option secara visual
  const gestureOptions = [
    { gesture: 'thumbs_down', icon: '👎', label: 'AI salah' },
    { gesture: 'palm_open', icon: '🖐', label: 'AI ragu' },
    { gesture: 'draw', icon: '✏️', label: 'Ini yang aku maksud' }
  ];

  // Deteksi gesture via MediaPipe ATAU klik ikon
  const selected = await waitForGestureOrClick(gestureOptions);

  if (selected.gesture === 'draw') {
    // Otomatis masuk ke C-3 (Draw-Confirm Loop)
    return handleOverrideWithVerification(probeState);
  }

  // Log alasan gesture
  logAction({
    decision: 'override',
    override_reason: selected.label,
    override_reason_gesture: selected.gesture,
    override_reason_type: 'gesture'
  });

  executeOverride(probeState);
}
```

#### C-2 (Revisi): Override Budget — Visual & Momo-Mediated

**Perubahan dari versi asli:** Budget ditampilkan secara visual via Momo, bukan teks counter.

**Cara kerja (UX-First):**

1. Override budget ditampilkan sebagai **Momo memegang kartu**:
   - 2 kartu tersisa → Momo mengangkat 2 jari: *"Aku masih bisa diganti 2 kali lagi ya!"*
   - 1 kartu tersisa → Momo mengangkat 1 jari: *"Hati-hati, cuma 1 kali lagi!"*
   - 0 kartu → Momo menunjukkan tangan kosong: *"Maaf, kesempatan mengganti sudah habis..."*
2. Ketika Override di-klik, Momo mengkonsumsi 1 kartu (animasi kartu hilang)
3. Budget di-reset saat retry (dengan animasi Momo mengambil kartu baru)

**Kelebihan UX-First:**
- Visual storytelling, bukan system UI — konsisten dengan karakter Momo
- Momo mengangkat jari = meta-reference ke gesture system (konsistensi desain)
- Tidak ada teks "1/1" yang terasa teknis — terasa seperti percakapan
- Animasi konsumsi kartu membuat override terasa punya "biaya"

**Spesifikasi Visual:**
```
┌────────────────────────────────────┐
│                                    │
│   [MOMO]  🃏🃏                     │
│   "Aku masih bisa diganti          │
│    2 kali lagi ya!"                │
│                                    │
│   [ACCEPT]   [OVERRIDE 🃏]        │
│                                    │
└────────────────────────────────────┘
```

#### C-3 (Penguatan): Draw-Confirm Loop — Sudah UX-First

**Status:** Countermeasure ini SUDAH UX-first by design — siswa menggambar ulang di canvas untuk memverifikasi override. Ini adalah **contoh emas** UX-First Countermeasure.

**Penguatan yang ditambahkan:**

1. **Momo feedback saat gambar ulang:**
   - Saat canvas muncul, Momo memberikan **visual hint**: Momo menunjuk ke canvas dengan tangan, *"Yuk, gambar lagi yang lebih jelas!"*
   - Saat CNN memproses, Momo mengedipkan mata (animasi "thinking")
   - Jika verifikasi berhasil: Momo lompat kegirangan, *"Wah, sekarang aku lihat! Terima kasih!"*
   - Jika verifikasi gagal: Momo menggaruk kepala, *"Hmm... aku masih nggak kelihatan. Coba lagi?"*

2. **Progressive canvas hint:** Jika gambar pertama ditolak, Momo memberikan **stroke hint** — menampilkan garis panduan tipis di canvas untuk membantu siswa menggambar lebih jelas. Ini bukan "menggambar untuk siswa" melainkan scaffolding visual.

3. **Narrative framing:** Override bukan "diminta bukti" — override adalah "mengajari Momo." Ini mengubah power dynamic dari adversarial ke kolaboratif.

**Catatan implementasi:** C-3 adalah countermeasure terkuat yang juga paling UX-aligned. Direkomendasikan sebagai **primary countermeasure di Level 3** di mana stakes tertinggi.

#### C-8 (Penandaan): Semantic Consistency Check — UX-Invisible

**Status:** Countermeasure ini adalah **UX-invisible** — berjalan di backend tanpa aksi pengguna. Ini adalah **ideal UX**: siswa tidak perlu melakukan apa-apa, sistem memvalidasi secara otomatis.

**Penguatan UX-First:**

1. **Momo sebagai komunikator:** Hasil C-8 dikomunikasikan via Momo, bukan system dialog:
   - Konsisten: Momo mengangguk, *"Hmm, gambarnya mirip yang kamu bilang!"* (tanpa blocking)
   - Tidak konsisten: Momo menunjukkan tanda tanya, *"Hmm, dari gambarnya aku nggak kelihatan kayak {label}... Kamu yakin?"* (soft prompt, bukan hard block)
2. **Soft enforcement:** Override tidak ditolak mekanik — hanya diberi prompt via Momo. Siswa bisa lanjut jika yakin.
3. **Data logging:** `override_consistency_score` tetap dicatat untuk analisis post-hoc.

**Prinsip:** Backend validation = UX zero-cost. Siswa tidak membayar biaya kognitif, tapi data tetap terekam untuk penelitian.

#### C-9 (Baru): Gesture-Based Override Confirmation

**Prinsip:** Override membutuhkan **deliberate physical gesture** sebagai konfirmasi, bukan klik tombol.

**Cara kerja:**

1. Setelah siswa memilih label override, Momo meminta konfirmasi: *"Kamu mau ganti jadi {label}? Tunjukin aku!"*
2. Siswa melakukan salah satu **confirmation gesture**:

| Gesture | Makna | Action |
|---------|-------|--------|
| 👍 **Thumbs Up** | "Ya, saya yakin" | Override dieksekusi |
| 🤝 **Two Hands Together** | "Saya ragu" | Kembali ke Probe UI (cancel override) |
| ✋ **Stop/Palm** | "Batal" | Kembali ke Probe UI |

3. **Deliberate physical effort:** Gesture konfirmasi butuh usaha fisik yang lebih besar daripada klik tombol. Ini mencegah mindless override karena:
   - Siswa harus **mengangkat tangan** dan **menunjukkan gesture** — act of commitment
   - Gesture tidak bisa dilakukan "tanpa berpikir" secepat klik tombol
   - Momen gesture = momen refleksi natural (micro-metacognition)

4. **Anti-exploit value:** Cheat code "tinggal override ke jembatan" menjadi "tinggal override ke jembatan, lalu tunjukin thumbs up" — tapi thumbs up butuh kamera aktif dan gesture yang disengaja. Ini tidak menghentikan exploit, tapi menambah *deliberation cost*.

**Kelebihan:**
- Menambah deliberate action tanpa menambah typing atau klik
- Konsisten dengan login flow (gesture-based)
- Momo sebagai pengonfirmasi — naratif, bukan mekanik
- Tidak memblokir — siswa selalu bisa menyelesaikan gesture
- Biaya implementasi rendah (MediaPipe sudah ada)

**Kekurangan:**
- Butuh kamera aktif (sudah ada untuk drawing input)
- Latency tambahan ~2-3 detik untuk gesture detection
- Perlu fallback untuk accessibility

**Fallback (Accessibility):**
- Jika kamera tidak tersedia: Momo menampilkan tombol besar "YAKIN!" dan "BATAL" dengan jeda 2 detik sebelum bisa diklik (enforced delay = deliberate action substitute)

**Pseudocode:**
```javascript
async function confirmOverride(overrideLabel) {
  momoSay(`Kamu mau ganti jadi ${overrideLabel}? Tunjukin aku!`);

  // Wait for confirmation gesture
  const gesture = await waitForConfirmationGesture({
    confirm: 'thumbs_up',
    cancel: 'palm_stop',
    doubt: 'two_hands_together'
  });

  if (gesture === 'confirm') {
    executeOverride(overrideLabel);
    logAction({ override_confirmed_via: 'gesture_thumbs_up' });
  } else if (gesture === 'cancel') {
    momoSay("Oke, kita tetap sama AI ya!");
    returnToProbeUI();
  } else {
    // doubt — Momo offers C-3 (draw verification)
    momoSay("Kalau ragu, gambar aja yang kamu maksud!");
    return handleOverrideWithVerification(probeState);
  }
}
```

### 11.3 UX-First Countermeasure Matrix

Rekapitulasi semua countermeasure dari perspektif UX-First:

| ID | Countermeasure | UX-First Level | Input Type | User Effort | Momo Role |
|----|---------------|----------------|------------|-------------|-----------|
| C-1R | Reflection Gate (Revisi) | 🟢 Full UX-First | Gesture / Visual klik | Rendah | Menanyakan alasan via gesture |
| C-2R | Override Budget (Revisi) | 🟢 Full UX-First | Visual (Momo kartu) | Nihil | Menunjukkan sisa budget via jari/kartu |
| C-3 | Draw-Confirm Loop | 🟢 Full UX-First | Canvas drawing | Sedang | Meminta gambar ulang, verifikasi |
| C-4 | Confidence-Weighted Cost | 🟡 Partial UX | Bervariasi | Bervariasi | N/A (mekanik backend) |
| C-5 | Behavioral Detection | 🟢 UX-Invisible | Nihil | Nihil | Komentar adaptif |
| C-6 | Accept-Override Balance | 🟡 Partial UX | Klik | Rendah | N/A (mekanik) |
| C-7 | Narrative Consequence | 🟢 Full UX-First | Nihil | Nihil | Reaksi emosional |
| C-8 | Semantic Consistency | 🟢 UX-Invisible | Nihil | Nihil | Soft prompt jika tidak konsisten |
| C-9 | Gesture Override Confirm | 🟢 Full UX-First | Gesture (kamera) | Rendah | Meminta konfirmasi gesture |

### 11.4 Rekomendasi Kombinasi UX-First

#### 🏆 Tier 1 (Wajib Implementasi): C-1R + C-2R + C-8 + C-9

**Rationale UX-First:**

- **C-1R (Gesture Reflection):** Override membutuhkan gesture, bukan klik. Cheat code tidak bisa di-share sebagai "tinggal klik override."
- **C-2R (Visual Budget):** Budget ditampilkan via Momo — naratif, bukan mekanik. Siswa merasa "Momo memberi kesempatan," bukan "sistem membatasi."
- **C-8 (Semantic Check):** UX-invisible — zero cost untuk siswa, tapi data tetap terekam. Ideal.
- **C-9 (Gesture Confirm):** Override butuh deliberate physical gesture — mencegah mindless gaming.

**Combined UX-First defense:**

```
Siswa mau override
  → C-1R: Pilih alasan via gesture (👎/🖐/✏️)     ← Deliberate action
  → C-9: Konfirmasi via gesture (👍)               ← Physical commitment
  → C-8: Backend check (invisible)                  ← Zero UX cost
  → C-2R: Budget dikurangi, Momo tunjukkan kartu    ← Visual feedback

Total typing: 0 karakter
Total klik: 0 tombol (semua gesture/visual)
```

#### Tier 2 (Jika Playtest Menunjukkan Perlu): +C-3 di Level 3

- C-3 (Draw-Confirm Loop) ditambahkan **khusus Level 3** di mana stakes tertinggi
- Ini sudah UX-First — menggambar di canvas, bukan mengetik
- Momo meminta bukti visual sebagai "mengajari Momo," bukan "membuktikan ke sistem"

#### Tier 3 (Post-Hoc Analysis): C-5

- C-5 (Behavioral Detection) dijalankan saat analisis data, bukan real-time
- `gaming_suspect_score` digunakan untuk filter data, bukan mengubah gameplay
- Ini menjaga UX murni tanpa kompromi

### 11.5 Accessibility & Fallback Design

Setiap UX-First countermeasure harus punya fallback yang terasa "designed," bukan "broken":

| Skenario | Fallback | UX Quality |
|----------|----------|------------|
| Kamera tidak tersedia | Klik ikon visual (emoji) sebagai pengganti gesture | 🟢 Designed — ikon besar, bukan form |
| Siswa disability motorik | Touch/tap pada ikon + enforced delay | 🟢 Designed — delay terasa sebagai "thinking time" |
| MediaPipe error/glitch | Otomatis fallback ke ikon visual | 🟢 Invisible — siswa tidak tahu ada error |
| Siswa malu kamera | Canvas drawing sebagai input utama (kamera optional) | 🟢 Designed — drawing sudah di core loop |

**Prinsip fallback:** Setiap fallback harus terasa seperti **pilihan desain yang disengaja**, bukan "versi rusak dari fitur kamera." Ikon visual dan enforced delay adalah mekanisme yang bisa berdiri sendiri sebagai UX pattern.

---

## 12. Gesture-Based Login Design (Research Output)

> **Konteks:** Desain login UX-First menggunakan gesture kamera via MediaPipe, menggantikan form NIS+Name.

### 12.1 Research Findings: MediaPipe Finger Counting

#### Akurasi Deteksi Jari (0–5, satu tangan)

- **MediaPipe Hands** mendeteksi 21 landmark 3D per tangan dari single RGB frame
- Finger counting dilakukan dengan logika sederhana: bandingkan posisi fingertip vs finger PIP joint
  - Jari terbuka: fingertip lebih jauh dari wrist dibanding PIP
  - Jari tertutup: fingertip lebih dekat ke wrist dibanding PIP
- **Akurasi:** 93–95% untuk finger counting 0–5 dalam kondisi pencahayaan normal (sumber: MP-GestLSTM, 94.38% testing accuracy; Eudoxus Press, >90% classification accuracy)
- **Ambiguity utama:** Antara 0 dan 1 jari (jempol tertutup/terbuka), terutama saat tangan miring

#### Akurasi Dua Tangan (0–10)

- MediaPipe mendukung **max 2 tangan** secara simultan (default: `maxNumHands = 2`)
- Finger counting dua tangan = jumlah jari tangan kiri + tangan kanan
- **Akurasi:** Menurun ke ~85–90% karena:
  - Occlusion saat dua tangan berdekatan
  - Tangan kedua bisa terdeteksi terlambat saat masuk frame
  - Salah satu tangan miring/sudut tidak ideal
- **Praktis untuk 0–10:** Feasible, tapi perlu UX flow yang memberi waktu siswa menstabilkan kedua tangan

#### Latensi & Performance

| Platform | FPS | Latensi | Sumber |
|----------|-----|---------|--------|
| Desktop (WebGL/GPU) | 50–60 FPS | ~4ms per frame | ResearchGate (Three.js + MediaPipe) |
| Desktop (WASM/CPU) | 10–15 FPS | ~67–100ms | Medium (Creative AI Ninja) |
| Mid-range consumer | 28–30 FPS | 18–32ms end-to-end | WJARR 2026 |
| Mobile browser | 15–25 FPS | ~40–67ms | Estimasi berdasarkan WebGL performance |

**Kesimpulan:** Di desktop/laptop sekolah (target platform), MediaPipe Hands berjalan di 28–60 FPS — lebih dari cukup untuk real-time finger counting. Latensi 18–32ms tidak terasa oleh siswa.

#### Kondisi Pencahayaan & Lingkungan Kelas Indonesia

- **Pencahayaan baik:** Akurasi 93–95% → tidak ada masalah
- **Pencahayaan rendah:** Akurasi turun ke ~80–85%, terutama untuk jari kelingking
- **Backlighting (jendela di belakang):** Masalah signifikan — tangan menjadi silhouette, landmark tidak akurat
- **Shared webcam (USB):** Bergantung kualitas webcam; webcam internal laptop umumnya cukup
- **Background ramai:** Tidak masalah signifikan — MediaPipe Hands fokus pada tangan, bukan background

**Rekomendasi implementasi:**
- Berikan panduan singkat: "Duduk menghadap layar, pastikan tangan terlihat jelas"
- Deteksi pencahayaan rendah: tampilkan Momo warning jika landmark confidence rendah
- Fallback ke input manual jika kamera tidak可用 dalam 10 detik

### 12.2 Two-Hand Counting untuk Nomor Absen > 10

**Masalah:** Kelas SMP bisa punya 30–40 siswa. Nomor absen 11–40 membutuhkan two-hand counting.

**Opsi desain yang dievaluasi:**

| Opsi | Deskripsi | Kelebihan | Kekurangan | Rekomendasi |
|------|-----------|-----------|------------|-------------|
| **A: Sequential** | Tampilkan puluhan dulu (☝🏻☝🏻 = 2), lalu satuan (☝🏻☝🏻☝🏻 = 3) → 23 | Intuitif untuk anak Indonesia | 2 langkah, UX friction | ⭐ Best option |
| **B: Simultaneous** | Tampilkan kedua tangan sekaligus: kiri=puluhan, kanan=satuan | 1 langkah | Sulit untuk angka > 5 di satu tangan, khususnya puluhan 4–5 butuh 2 tangan | ❌ Tidak feasible |
| **C: Limit max** | Batasi nomor absen 1–10, gunakan dua step (kelas + nomor) | Simpel | Tidak sesuai konteks Indonesia (kelas bisa >10 siswa) | ⚠️ Tidak realistis |
| **D: Hybrid** | 1–10 = satu tangan, 11+ = sequential two-step | Natural flow | Perlu UX switch | ⭐ Rekomendasi final |

**Rekomendasi final — Opsi D (Hybrid):**

1. **Nomor absen 1–10:** Satu tangan, satu langkah. Simple.
2. **Nomor absen 11–40:** Dua langkah sequential:
   - Step 1: Momo bertanya, *"Puluhan berapa?"* → siswa tunjukkan puluhan (1–4 jari)
   - Step 2: Momo bertanya, *"Satuannya berapa?"* → siswa tunjukkan satuan (0–9 jari)
3. **Validasi:** Momo mengkonfirmasi, *"Kamu nomor absen [puluhan][satuan] ya?"* → 👍 confirm

**UX friction analysis:**
- Nomor absen 1–10: ~3 detik (satu gesture + konfirmasi)
- Nomor absen 11–40: ~8 detik (dua gesture + konfirmasi)
- Total login flow: 15–25 detik (bandingkan form NIS+Name: 20–40 detik mengetik)
- **Kesimpulan:** Gesture login SAMA CEPAT atau LEBIH CEPAT daripada form login untuk siswa SMP yang sudah terbiasa kamera

### 12.3 Privacy Analysis: UU PDP (Law No. 27/2022)

#### Regulasi yang Relevan

**UU PDP Pasal 4 — Kategori Data Pribadi Spesifik:**
- Data biometrik diklasifikasikan sebagai **"data pribadi spesifik"** yang memerlukan perlindungan ekstra
- Definisi UU PDP: *"Data yang terkait dengan karakteristik fisik, fisiologis, atau perilaku seseorang yang memungkinkan identifikasi unik"*

**UU PDP Pasal 5 — Pemrosesan Data Anak:**
- Pemrosesan data pribadi anak **wajib mendapat persetujuan orang tua/wali**
- Anak = subjek data pribadi di bawah 17 tahun → siswa SMP (13–15) termasuk

**UU PDP Pasal 17 — Teknologi Pengenalan Wajah:**
- Secara spesifik mengatur Facial Recognition Technology → **TIDAK RELEVAN** karena kita TIDAK menggunakan face detection

#### Analisis: Apakah Hand Gesture = Data Biometrik?

**Argumen PRO (gesture = biometrik):**
- Hand shape/proportion bersifat unik per individu (panjang jari, rasio jari)
- Landmark posisi tangan secara teori bisa di-reverse-engineer untuk mengidentifikasi individu
- UU PDP mendefinisikan biometrik secara luas: "karakteristik fisik... yang memungkinkan identifikasi unik"

**Argumen KONTRA (gesture ≠ biometrik yang diproses):**
- **Kami TIDAK menyimpan** landmark — hanya memproses real-time untuk counting
- **Kami TIDAK menggunakan** landmark untuk identifikasi — hanya untuk menghitung jumlah jari
- **Kami TIDAK mentransfer** landmark ke server — semua pemrosesan di client (browser)
- Finger counting output adalah **angka (0–10)**, bukan data biometrik — angka ini sama dengan mengetik di keyboard
- Analogi: mengetik "5" di keyboard vs menunjukkan 5 jari — output sama, input berbeda, tapi data yang disimpan identik

**Kesimpulan hukum (analisis teknis, bukan nasihat hukum):**

| Aspek | Status | Mitigasi |
|-------|--------|----------|
| Penyimpanan biometrik | ❌ Tidak ada | Landmark TIDAK disimpan, hanya integer (jumlah jari) |
| Transfer biometrik | ❌ Tidak ada | Semua pemrosesan client-side via WASM |
| Identifikasi biometrik | ❌ Tidak ada | Landmark tidak digunakan untuk identify individu |
| Pemrosesan real-time | ⚠️ Gray area | Landmark diproses ephemeral, tidak persist |
| Consent anak | ✅ Diperlukan | Sama seperti login NIS — perlu persetujuan orang tua |

**Rekomendasi mitigasi:**
1. **Tidak simpan landmark** — Hanya simpan integer output (jumlah jari) sebagai `nomor_absen`
2. **Tidak transfer landmark** — Semua pemrosesan di client-side via MediaPipe WASM
3. **Tidak gunakan face detection** — Hanya hand landmarks, sesuai prinsip minimum necessary
4. **Inform consent** — Tambahkan di informed consent penelitian: *"Kamera digunakan untuk mendeteksi gesture tangan secara real-time. Data wajah TIDAK dideteksi/disimpan. Data posisi tangan TIDAK disimpan — hanya jumlah jari yang terdeteksi."*
5. **Opt-out available** — Siswa bisa login via form manual (NIS + Nama) tanpa kamera

#### Perbandingan UU PDP vs FERPA (AS)

| Aspek | UU PDP (Indonesia) | FERPA (AS) |
|-------|-------------------|------------|
| Definisi biometrik | "Karakteristik fisik/fisiologis/perilaku untuk identifikasi unik" | "Record yang bisa digunakan untuk identifikasi, termasuk fingerprint, voice print, retina image" |
| Kategori data anak | Data pribadi spesifik + persetujuan orang tua | Education records + consent tertulis orang tua |
| Pemrosesan tanpa storage | Tidak secara eksplisit diatur | Tidak diatur — FERPA fokus pada "records" (yang disimpan) |
| Real-time ephemeral processing | ⚠️ Gray area | ✅ Tidak termasuk "record" jika tidak disimpan |

**Key insight:** FERPA secara eksplisit hanya mengatur *records* (data yang disimpan). Pemrosesan real-time yang tidak menghasilkan record tidak tercakup. UU PDP lebih luas dalam definisi "pemrosesan" — namun demikian, prinsip **purpose limitation** (pemrosesan hanya untuk tujuan yang dinyatakan) dan **data minimization** (hanya proses yang perlu) mendukung pendekatan kita.

### 12.4 Complete Gesture Login Flow Design

#### Arsitektur Login Baru

**Komponen yang ditambahkan:**
1. **Admin Dashboard → "Buat Kelas"** → generates `class_id` (6-character alphanumeric)
2. **Kelas** memiliki: `class_id`, `nama_kelas`, `jumlah_siswa`, `created_by` (admin)
3. **Siswa** terdaftar ke kelas dengan `nomor_absen` (1–40)
4. **Login flow:** Pilih kelas → Gesture nomor absen → Konfirmasi → Masuk

#### Step-by-Step Login Flow

```
┌─────────────────────────────────────────────────────────────┐
│                   GESTURE LOGIN FLOW                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  STEP 1: PILIH KELAS                                       │
│  ┌──────────────────────────────────────┐                   │
│  │  Momo: "Hai! Kelas mana kamu?"       │                   │
│  │                                      │                   │
│  │  [7A - Bu Hesti]   ← klik/tap       │                   │
│  │  [7B - Pak Andi]   ← klik/tap       │                   │
│  │  [8C - Bu Dewi]    ← klik/tap       │                   │
│  │                                      │                   │
│  │  Atau scan QR: [📷]                  │                   │
│  └──────────────────────────────────────┘                   │
│                    ↓                                         │
│  STEP 2: TUNJUKKAN NOMOR ABSEN (1-10)                      │
│  ┌──────────────────────────────────────┐                   │
│  │  Kamera aktif 🎥                     │                   │
│  │  Momo: "Siapa nomor absen kamu?"     │                   │
│  │  "Tunjukin jari kamu!"               │                   │
│  │                                      │                   │
│  │  [Siswa tunjuk 3 jari ☝🏻☝🏻☝🏻]         │                   │
│  │  → MediaPipe detect: 3 fingers       │                   │
│  └──────────────────────────────────────┘                   │
│                    ↓                                         │
│  STEP 2b: JIKA NOMOR > 10 (Sequential)                     │
│  ┌──────────────────────────────────────┐                   │
│  │  Momo: "Puluhan berapa?"             │                   │
│  │  [Siswa tunjuk 2 jari] → 2           │                   │
│  │  Momo: "Satuannya?"                  │                   │
│  │  [Siswa tunjuk 5 jari] → 5           │                   │
│  └──────────────────────────────────────┘                   │
│                    ↓                                         │
│  STEP 3: KONFIRMASI MOMO                                   │
│  ┌──────────────────────────────────────┐                   │
│  │  Momo: "Kamu nomor absen 3 ya?"      │                   │
│  │  " 👍 = Ya  |  👎 = Bukan"           │                   │
│  │                                      │                   │
│  │  [Siswa tunjuk 👍]                   │                   │
│  │  → LOGIN SUCCESS!                    │                   │
│  └──────────────────────────────────────┘                   │
│                    ↓                                         │
│  STEP 4: MASUK GAME                                        │
│  ┌──────────────────────────────────────┐                   │
│  │  Momo: "Halo, [Nama Siswa]!"         │                   │
│  │  "Ayo mulai petualangan!"            │                   │
│  │  [Mulai Level 1]                     │                   │
│  └──────────────────────────────────────┘                   │
│                                                             │
│  FALLBACK: JIKA GAGAL 3X                                   │
│  ┌──────────────────────────────────────┐                   │
│  │  Momo: "Nggak apa-apa! Ketik aja     │                   │
│  │   nomor absen kamu ya!"              │                   │
│  │  [Input field: ___]                  │                   │
│  │  (Fallback terasa "Momo membantu",   │                   │
│  │   bukan "sistem gagal")              │                   │
│  └──────────────────────────────────────┘                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

#### Detail Momo Dialogue per Step

**STEP 1 — Pilih Kelas:**

| Kondisi | Momo Text | Visual Momo |
|---------|-----------|-------------|
| Awal | *"Hai! Aku Momo! 🎨 Kelas mana kamu?"* | Momo melambai |
| Kelas dipilih (klik) | *"Kelas {nama_kelas} ya! Ayo lanjut!"* | Momo lompat |
| QR scan berhasil | *"Wah, langsung ketemu kelasmu!"* | Momo mengangguk |
| QR scan gagal | *"Hmm, kode-nya nggak kebaca. Pilih manual aja ya!"* | Momo menggaruk kepala |

**STEP 2 — Tunjukkan Nomor Absen:**

| Kondisi | Momo Text | Visual Momo |
|---------|-----------|-------------|
| Kamera aktif | *"Siapa nomor absen kamu? Tunjukin jari kamu!"* | Momo menunjuk ke kamera |
| Menunggu gesture | *"...Aku tunggu ya!"* (setelah 3 detik) | Momo mengedipkan mata |
| 1 jari terdeteksi | *"Satu ya?"* | Momo mengangkat 1 jari |
| 3 jari terdeteksi | *"Tiga ya?"* | Momo mengangkat 3 jari |
| 5 jari terdeteksi | *"Lima ya?"* | Momo mengangkat 5 jari (1 tangan) |
| 7 jari terdeteksi (2 tangan) | *"Tujuh ya?"* | Momo mengangkat 2 tangan |
| Kamera gelap/error | *"Hmm, kameranya kurang terang. Pindah tempat dulu ya, atau ketik aja nomor absen kamu!"* | Momo menunjuk ke ikon keyboard |

**STEP 2b — Sequential (Nomor > 10):**

| Kondisi | Momo Text | Visual Momo |
|---------|-----------|-------------|
| Puluhan terdeteksi | *"{n} puluhan ya! Sekarang satuannya?"* | Momo menunjuk lagi |
| Satuan terdeteksi | *"Jadi nomor absen {pul}{sat} ya?"* | Momo mengangguk |

**STEP 3 — Konfirmasi:**

| Kondisi | Momo Text | Visual Momo |
|---------|-----------|-------------|
| Menebak nomor | *"Kamu nomor absen {n} ya? 👍 kalau betul!"* | Momo menunggu |
| 👍 Thumbs up | *"Halo, {Nama}! Ayo main!"* | Momo lompat kegirangan |
| 👎 Thumbs down | *"Yah, tebakanku salah! Coba lagi ya!"* | Momo sedih sebentar, lalu kembali ke Step 2 |
| Tidak ada gesture 5 detik | *"Kamu bisa ketik juga lho!"* → tampilkan input manual | Momo menunjuk ke keyboard |

**STEP 4 — Fallback (Gagal 3x):**

| Kondisi | Momo Text | Visual Momo |
|---------|-----------|-------------|
| 3x gagal deteksi | *"Nggak apa-apa! Ketik aja nomor absen kamu ya!"* | Momo tersenyum supportive |
| Nomor absen diketik | *"Nomor {n}! Halo, {Nama}!"* | Momo melambai |
| Nomor tidak ditemukan | *"Hmm, nomor {n} belum terdaftar. Coba cek lagi ya!"* | Momo bingung |

#### Class ID Selection Methods

| Metode | Deskripsi | Kelebihan | Kekurangan |
|--------|-----------|-----------|------------|
| **Dropdown** | Daftar kelas yang tersedia | Simpel, tidak butuh hardware | Perlu setup kelas dulu |
| **QR Code** | Guru memproject QR di papan → siswa scan | Cepat, tidak perlu scroll | Butuh kamera + proyektor |
| **Kode 6 huruf** | Guru tulis kode di papan → siswa ketik | Tidak butuh kamera untuk langkah ini | Masih ada sedikit typing |

**Rekomendasi:** Dropdown sebagai default + QR code sebagai opsi cepat. Kode 6 huruf sebagai fallback jika kamera tidak可用.

#### Auto-Registration Logic

Jika nomor absen belum terdaftar di kelas:
1. Momo: *"Nomor {n} belum terdaftar di kelas ini. Kamu siswa baru ya?"*
2. Momo: *"Siapa namamu?"* → Input nama (satu-satunya typing yang diperlukan)
3. Siswa mengetik nama → Auto-register → Login berhasil
4. **Catatan:** Typing nama hanya terjadi SEKALI (pertama kali). Setelah itu, login pure gesture.

#### Gesture Mapping Reference

| Gesture | Deteksi MediaPipe | Kondisi Landmark | Digunakan di |
|---------|-------------------|------------------|-------------|
| 1 jari (☝🏻) | Index extended, others closed | Index tip > PIP, rest tip < PIP | Login, C-9 |
| 2 jari (✌🏻) | Index + Middle extended | Index+Mid tip > PIP | Login |
| 3 jari | Index + Mid + Ring extended | 3 tips > PIP | Login |
| 4 jari | 4 jari extended (no thumb) | 4 tips > PIP | Login |
| 5 jari (🖐) | All fingers extended | 5 tips > PIP | Login, C-1R |
| 👍 Thumbs up | Thumb up, others closed | Thumb tip > IP, rest < PIP | C-9 confirm |
| 👎 Thumbs down | Thumb down, others closed | Thumb tip < MCP, rest < PIP | C-1R reject |
| ✋ Palm stop | All extended, palm facing cam | 5 tips > PIP + palm orientation | C-9 cancel |
| ✌️✋ Two hands | Count both hands separately | maxNumHands=2 | Login >10 |

### 12.5 Perbandingan Login Lama vs Baru

| Aspek | Login Lama (NIS+Nama) | Login Baru (Gesture) |
|-------|----------------------|---------------------|
| Input utama | Keyboard | Kamera (gesture) |
| Jumlah langkah | 2 field → submit | Pilih kelas → gesture → konfirmasi |
| Total typing | ~15 karakter (NIS + Nama) | 0 karakter (pure gesture) |
| Waktu rata-rata | 20–40 detik | 10–25 detik |
| Kesalahan ketik | Sering (NIS salah) | Tidak ada (gesture tidak bisa "salah ketik") |
| Privacy | NIS tersimpan di server | Hanya integer nomor absen tersimpan |
| Engagement | Form biasa | Interaktif, Momo-mediated |
| Fallback | N/A | Form manual ( jika kamera gagal ) |
| Auto-register | Otomatis | Otomatis + ketik nama sekali |
| Accessibility | ✅ Full | ⚠️ Perlu fallback disability |

### 12.6 Implementasi API Changes

Untuk mendukung gesture login, API spec perlu diperbarui:

**New endpoints:**

```
POST /api/v1/classes          → Buat kelas (admin)
GET  /api/v1/classes          → List kelas
GET  /api/v1/classes/:id      → Detail kelas + daftar siswa
POST /api/v1/classes/:id/join → Siswa join kelas via nomor_absen
```

**Modified login flow:**

```
OLD: POST /api/v1/auth/login  { nis, name }
NEW: POST /api/v1/auth/login  { class_id, nomor_absen }
     → Returns: { user_id, name, is_new_user }
     → If is_new_user: POST /api/v1/auth/register { class_id, nomor_absen, name }
```

**Data model changes:**

```sql
-- New table: classes
CREATE TABLE classes (
  id TEXT PRIMARY KEY,        -- 6-char alphanumeric
  name TEXT NOT NULL,         -- e.g., "7A - Bu Hesti"
  max_students INT NOT NULL,  -- e.g., 35
  created_by TEXT NOT NULL,   -- admin user
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Modified table: users
ALTER TABLE users ADD COLUMN class_id TEXT REFERENCES classes(id);
ALTER TABLE users ADD COLUMN nomor_absen INT;
-- NIS becomes optional (legacy support)
```

---

## Changelog

| Tanggal | Perubahan | Sumber |
|---------|-----------|--------|
| 2026-06-16 | Versi awal analisis loophole HITL | User scenario + academic research |
| 2026-06-16 | Identifikasi 7 worst case + 8 countermeasure | Literature review + reasoning |
| 2026-06-16 | Rekomendasi kombinasi C-1+C-2+C-8 | Cost-benefit analysis |
| 2026-03-05 | §11: UX-First Countermeasure Design — revisi C-1, C-2, C-3; tambah C-9; rekomendasi UX-First tier | User "Can" UX-first directive |
| 2026-03-05 | §12: Gesture-Based Login Design — research MediaPipe, UU PDP, complete flow | Research task (parallel) |

---

*Dokumen ini disusun berdasarkan analisis desain game saat ini (GDD v1), riset akademik tentang Gaming the System (Baker et al.), Trust Calibration (Lee & See), Automation Bias (Goddard et al.), dan Controlled Ambiguity (arxiv:2602.00026). Semua proposal countermeasure memerlukan validasi melalui playtest sebelum implementasi final. §11–§12 ditambahkan berdasarkan prinsip UX-First (gesture > click, visual > text, canvas > keyboard) dan riset MediaPipe Hands + UU PDP Indonesia.*
