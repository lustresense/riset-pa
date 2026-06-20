# Game Design Document — Sketchbook Universe

> **"Escape the Sketchbook"**
> Simulasi Interaktif Literasi AI untuk Siswa SMP Kelas 7–9

---

## Dokumen Header

| Field | Value |
|-------|-------|
| **Proyek** | Sketchbook Universe — Simulasi Interaktif Literasi AI |
| **Target Pengguna** | Siswa SMP Kelas 7–9 (usia 13–15 tahun) |
| **Engine** | Kaplay.js (JavaScript 2D game engine, browser-based) |
| **AI Inference** | TensorFlow.js + MobileNet (client-side CNN classification) |
| **Gesture Input** | MediaPipe Hands (opsional, future enhancement) |
| **Prinsip Utama** | **Controlled Ambiguity** — AI sengaja tidak sempurna agar momen HITL (Human-in-the-Loop) terjadi |
| **Maskot** | Momo — game master, text-bubble only, tanpa suara/NLP |
| **Jumlah Level** | 3 Level Linear (Pemanasan → Keraguan → Jebakan) — **JANGAN tambah** |
| **Durasi Total** | ±7–10 menit (Level 1 ~2 min, Level 2 ~3 min, Level 3 ~3–5 min) |
| **Timer** | Tidak ada — kecepatan diukur natural via `decision_latency_ms` |
| **Login** | **WAJIB** — untuk history/progress tracking (Bu Hesti 16/6/26) |
| **Kategori Objek** | **Solid** dan **Danger (duri/thorns)** saja — dekoratif DIHAPUS |
| **Sumber Kebenaran** | Notulensi Bimbingan Bu Hesti 16/6/26 |

---

## 1. Core Game Loop

Game loop adalah inti mekanisme permainan yang berulang di setiap level. Loop ini memastikan setiap interaksi siswa menghasilkan momen HITL yang terukur.

### Diagram Alur

```
DRAW → INFER → PROBE → DECIDE → RENDER
  │        │        │        │        │
  ▼        ▼        ▼        ▼        ▼
Siswa   Canvas    Momo     Accept/   Objek
gambar  image →  muncul,  Override  muncul
        CNN      tampilkan          ATAU
        klasif.  tebakan AI         Kertas
                                     robek
```

### Penjelasan Setiap Fase

| Fase | Deskripsi | Input | Output | Tanggung Jawab |
|------|-----------|-------|--------|----------------|
| **1. DRAW** | Siswa menggambar objek sesuai prompt level di canvas | Mouse/touch events | Canvas image (base64) | Siswa |
| **2. INFER** | CNN MobileNet (TF.js) mengklasifikasi gambar secara client-side | Canvas image (base64) | Raw probability distribution over labels | Sistem AI |
| **3. PROBE** | Momo muncul di layar, menampilkan tebakan AI sesuai konfigurasi level | Raw inference + level config | Top-K labels + confidence scores | Sistem → Momo |
| **4. DECIDE** | Siswa mengevaluasi tebakan AI dan memilih keputusan | Probe UI interaction | `decision_type` (accept / override / correct) | Siswa (HITL) |
| **5. RENDER** | Hasil keputusan divisualisasikan di sketchbook | Decision + label | Objek muncul di scene ATAU kertas sobek | Sistem |

### Estimasi Durasi Per Fase

| Fase | Level 1 | Level 2 | Level 3 |
|------|---------|---------|---------|
| DRAW | 10–20 detik | 15–30 detik | 15–30 detik |
| INFER | ~1 detik | ~1 detik | ~1 detik |
| PROBE | 2–4 detik | 4–7 detik | 6–10 detik |
| DECIDE | 2–4 detik | 4–7 detik | 6–10 detik |
| RENDER | 1–2 detik | 1–2 detik | 1–2 detik |
| **Total per ronde** | **~16–31 detik** | **~25–52 detik** | **~28–62 detik** |

> **Catatan:** Waktu PROBE + DECIDE = `decision_latency_ms` yang di-log. Tidak ada timer yang memaksa kecepatan.

---

## 2. Mekanik Inti (Tanpa Dekoratif — Fokus HITL)

Berdasarkan keputusan Bu Hesti (16/6/26), seluruh elemen dekoratif dihapus. Hanya mekanik yang berkontribusi pada interaksi HITL yang dipertahankan.

### 2.1 Gesture Recognition → Game Action Mapping

| Gesture (MediaPipe) | Game Action | Keterangan |
|---------------------|-------------|------------|
| Index finger draw | Menggambar di canvas | Input utama |
| Open palm (5 jari) | Submit gambar → trigger inference | "Saya selesai menggambar" |
| Thumbs up | Accept (setuju dengan tebakan AI) | Afirmasi cepat |
| Thumbs down | Override (menolak tebakan AI) | Koreksi aktif |
| Closed fist | Pause / batal | Safety gesture |

> **Catatan:** Gesture bersifat opsional. Mouse/touch tetap menjadi input utama untuk aksesibilitas. MediaPipe adalah enhancement, bukan requirement.

### 2.2 HITL Probe UI — Mekanik Inti

Probe UI adalah **satu-satunya** titik interaksi antara siswa dan output AI. Tanpa Probe UI, tidak ada momen HITL. Mekanik ini dirancang untuk memaksa siswa membuat keputusan sadar terhadap output AI.

**Alur HITL:**

1. AI mengklasifikasi gambar → Confidence Controller memproses output sesuai level
2. Probe UI muncul → Momo menampilkan tebakan AI + confidence
3. Siswa membaca informasi → Membuat keputusan (Accept / Override)
4. Keputusan divisualisasikan → Konsekuensi gameplay terjadi
5. Data dicatat → Decision type + latency + confidence di-log

### 2.3 Consequence-Driven Feedback

Tidak ada skor, tidak ada leaderboard. Feedback sepenuhnya naratif:

| Keputusan | Konsekuensi Visual | Konsekuensi Gameplay |
|-----------|-------------------|---------------------|
| Accept (benar) | Objek muncul di sketchbook, Momo senang | Progress ke ronde berikutnya |
| Accept (salah) | Kertas robek + shake animation | Warning (Level 2) / Game Over (Level 3) |
| Override (benar) | Objek muncul, Momo belajar rendah hati | Progress ke ronde berikutnya |
| Override (salah) | Kertas robek sedikit | Bisa retry |

### 2.4 Data Logging — Setiap Decision Dicatat

Setiap momen DECIDE menghasilkan satu entry log. Tidak ada keputusan yang tidak tercatat.

| Field Universal (semua level) | Tipe | Keterangan |
|-------------------------------|------|------------|
| `session_id` | string | ID sesi unik (dari login) |
| `level` | int | 1, 2, atau 3 |
| `prompt_given` | string | Prompt yang diberikan ke siswa |
| `decision` | string | accept / override / correct |
| `latency_ms` | int | Waktu dari Probe muncul sampai siswa klik |
| `timestamp` | ISO 8601 | Waktu kejadian |

### 2.5 Kategori Objek (Simplified)

| Kategori | Visual | Fungsi Gameplay | Contoh |
|----------|--------|----------------|--------|
| **Solid** | Bentuk utuh, tidak tembus | Objek yang siswa gambar dan muncul di sketchbook | Kotak, lingkaran, segitiga, tangga, jembatan |
| **Danger (Duri)** | Duri/thorns, berwarna merah | Rintangan — menghalangi jalan, menyebabkan kertas robek jika disentuh | Duri di tepi jalan, duri menghalangi |

> **Penting:** Kategori "Dekoratif/Tembus Pandang" **DIHAPUS** (Bu Hesti 16/6/26). Jika di masa depan ditemukan konsep yang jelas untuk dekoratif, bisa ditambahkan.

---

## 3. Level 1 — Pemanasan (Warm-Up)

### Konsep Utama: "Membangun Kepercayaan & Memahami Mekanik Dasar"

Level 1 dirancang agar siswa membangun **baseline trust** terhadap sistem. AI menampilkan **hanya 1 tebakan (Top-1)** dengan confidence tinggi, dan hampir selalu benar. Tujuan pedagogisnya bukan menguji kemampuan siswa, melainkan memperkenalkan mekanik: gambar → AI menebak → baca confidence → pilih keputusan → lihat hasil.

**Tidak ada fail condition** di level ini — tujuannya murni membangun kepercayaan agar Level 2 dan 3 memiliki dampak psikologis yang lebih kuat.

### Tabel Spesifikasi

| Aspek | Detail |
|-------|--------|
| **Narasi** | Momo memperkenalkan dunia sketchbook: *"Aku Momo, teman menggambarmu! Di buku sketsa ini, semua yang kamu gambar bisa hidup! Ayo coba!"* — Momo baru "lahir", sangat percaya diri, dan senang membantu. |
| **Prompt** | **Prompt terbatas:** "Gambar KOTAK!" / "Gambar LINGKARAN!" / "Gambar SEGITIGA!" — Bentuk geometris sederhana dengan contoh visual kecil di samping canvas. Hanya 3 objek spesifik yang diminta secara berurutan. |
| **AI Top-K** | **Top-1 only** — AI hanya menampilkan 1 tebakan + confidence. Siswa tidak melihat prediksi alternatif. |
| **Confidence Range** | **0.85 – 0.96** (sangat tinggi) — AI hampir selalu benar dan yakin. |
| **Momo Expression** | 😊 Senang, yakin, green bubble |
| **Momo Auto-text** | *"Aku {confidence}% yakin ini {label}!"* |
| **Tombol Tersedia** | **Accept** ✅ (hijau) + **Correct** ✅ (opsional, biru) — Tidak ada Override |
| **Fail Condition** | **TIDAK ADA** — Semua keputusan menghasilkan hasil yang benar |
| **Durasi Target** | ~2 menit |

### Prompt & Objek

| Urutan | Prompt | Contoh Visual | Expected Top-1 | Expected Confidence |
|--------|--------|---------------|-----------------|---------------------|
| 1 | "Gambar KOTAK!" | Kotak kecil di samping canvas | square | ~94–96% |
| 2 | "Gambar LINGKARAN!" | Lingkaran kecil | circle | ~92–95% |
| 3 | "Gambar SEGITIGA!" | Segitiga kecil | triangle | ~88–93% |

### Momen HITL — Level 1

```
Siswa gambar kotak
    → Canvas image ke TF.js inference
    → Top-1: "kotak" 94%
    → Momo: "Aku 94% yakin ini KOTAK!" 🟢
    → Siswa klik Accept ✓
    → Kotak muncul di sketchbook ✅
    → Siswa: "AI-nya bener nih!"
```

> Jika siswa Correct (opsional): Momo berkata *"Oke, terima kasih koreksinya!"* tanpa konsekuensi negatif.

### Mengapa Top-1 Only di Level 1?

Berdasarkan prinsip **progressive disclosure**: di Level 1, siswa belum perlu melihat kompleksitas AI. Dengan hanya menampilkan 1 tebakan, fokus siswa pada:
1. Memahami bahwa AI bisa menebak gambar
2. Membaca dan memahami confidence score
3. Membiasakan diri dengan mekanisme Accept/Correct

Tanpa fondasi ini, siswa akan bingung saat Level 2 menampilkan 3 tebakan sekaligus.

### Data Log — Level 1

| Field | Tipe | Expected Value | Tujuan Analisis |
|-------|------|---------------|-----------------|
| `session_id` | string | Generated | Anonymization |
| `level` | int | 1 | Identifikasi level |
| `prompt_given` | string | "Gambar KOTAK!" | Validasi desain level |
| `top1_label` | string | square / circle / triangle | Apa yang AI tebak |
| `top1_confidence` | float | 0.85–0.96 | Seberapa yakin AI |
| `decision` | string | accept (dominan) / correct | Baseline trust level |
| `corrected_label` | string? | null (dominan) | Jarang terjadi |
| `latency_ms` | int | 2000–4000 | Kecepatan keputusan (cepat = yakin) |
| `timestamp` | ISO 8601 | Waktu kejadian | Temporal analysis |

---

## 4. Level 2 — Keraguan (Doubt)

### Konsep Utama: "Navigasi Ambiguitas — AI Bisa Ragu dan Bisa Salah"

Level 2 memperkenalkan **ambiguitas terkontrol** melalui **Top-3 + confidence score**. Siswa kini melihat 3 tebakan AI sekaligus dengan confidence yang berdekatan — ini menciptakan **cognitive friction** yang memaksa siswa mengevaluasi, bukan hanya menerima. AI tidak lagi selalu benar; confidence menurun dan gap antar prediksi mengecil. Konsekuensi salah mulai terasa (kertas sobek sedikit), tetapi tidak fatal.

### Tabel Spesifikasi

| Aspek | Detail |
|-------|--------|
| **Narasi** | Momo mulai ragu: *"Hmm... aku kurang yakin nih... Gambarnya agak kabur."* — Tinta di halaman sketchbook mulai mengabur. Momo tidak lagi 100% percaya diri. Dia meminta bantuan siswa: *"Kamu cek ya, mana yang paling benar?"* |
| **Prompt** | **Prompt kategori:** "Gambar sesuatu yang KOKOH!" / "Gambar sesuatu untuk MENYEBERANG!" — Tanpa contoh visual. Siswa bebas memilih objek dalam kategori yang diminta. |
| **AI Top-K** | **Top-3 + confidence** — AI menampilkan 3 tebakan dengan masing-masing confidence score. Siswa harus mengevaluasi mana yang benar. |
| **Confidence Range** | **0.55 – 0.70** (sedang) — AI ragu, confidence gap antara Top-1 dan Top-2 kecil (~4–8%). |
| **Momo Expression** | 🤔 Ragu, tanda tanya, yellow bubble |
| **Momo Auto-text** | *"Hmm... {top1} {conf1}%, {top2} {conf2}%, atau {top3} {conf3}%... Aku kurang yakin nih."* |
| **Tombol Tersedia** | **Accept** ✅ (kuning — pilih salah satu dari Top-3) + **Override** ✅ (biru — masukkan label sendiri) |
| **Fail Condition** | Jika siswa Accept tebakan yang salah → kertas sobek sedikit (warning visual + suara robek kecil). Momo: *"Aduh... tebakanku salah. Coba lagi ya!"* → Bisa retry. **Bukan Game Over.** |
| **Durasi Target** | ~3 menit |

### Prompt & Objek

| Prompt | Kategori Objek | Top-3 Possible Labels | Confidence Gap |
|--------|---------------|----------------------|----------------|
| "Gambar sesuatu yang KOKOH!" | Solid objects | fence, ladder, plank, stairs, bridge | ~4–8% antar Top-2 |
| "Gambar sesuatu untuk MENYEBERANG!" | Crossing objects | bridge, ladder, plank, stairs | ~5–10% antar Top-2 |

### Cognitive Friction Mechanism

Saat confidence AI rendah DAN siswa terlalu cepat memilih Accept, muncul pop-up konfirmasi:

```
Siswa klik Accept dalam < 2 detik
    → Confidence Top-1 < 60%?
        → Ya: Pop-up "Yakin? 🤔"
            → Siswa konfirmasi: Proses keputusan
            → Siswa batal: Kembali ke Probe UI, evaluasi ulang
        → Tidak: Langsung proses
```

> **Tujuan friction:** Mencegah automation bias tanpa memberi tahu jawaban yang benar. Pop-up "Yakin?" hanya muncul saat AI ragu DAN siswa terlalu cepat memutuskan.

### Contoh Skenario HITL — Level 2

```
Siswa gambar objek kokoh (misal: tangga)
    → AI klasifikasi
    → Top-3: "fence" 46%, "ladder" 41%, "plank" 8%
    → Momo: "Hmm... Fence 46%, Ladder 41%, Plank 8%... Aku kurang yakin nih." 🟡

    Skenario A: Siswa klik "Ladder" dari Top-3 (benar)
        → Tangga muncul di sketchbook ✅

    Skenario B: Siswa klik "Fence" dari Top-3 (salah)
        → Kertas sobek sedikit 📄! Momo: "Aduh... tebakanku salah!"
        → Bisa retry — BUKAN Game Over

    Skenario C: Siswa klik Override → ketik "tangga"
        → Tangga muncul di sketchbook ✅
        → Siswa tidak percaya AI, pilih sendiri
```

### Data Log — Level 2

| Field | Tipe | Expected Value | Tujuan Analisis |
|-------|------|---------------|-----------------|
| `session_id` | string | Generated | Anonymization |
| `level` | int | 2 | Identifikasi level |
| `prompt_given` | string | "Gambar sesuatu yang KOKOH!" | Validasi desain level |
| `top3_labels` | array | ["fence", "ladder", "plank"] | 3 tebakan AI |
| `top3_confidences` | array | [0.46, 0.41, 0.08] | Confidence masing-masing |
| `confidence_gap` | float | 0.04–0.08 | Indikator ambiguitas |
| `decision` | string | accept / override | Tipe keputusan siswa |
| `selected_index` | int? | 0, 1, atau 2 | Pilihan dari Top-3 |
| `override_label` | string? | null / label custom | Jika siswa override |
| `is_correct` | boolean | true / false | Apakah pilihan benar |
| `latency_ms` | int | 4000–7000 | Kecepatan keputusan (lebih lama = ragu) |
| `timestamp` | ISO 8601 | Waktu kejadian | Temporal analysis |

---

## 5. Level 3 — Jebakan (The Trap)

### Konsep Utama: "AI Bisa Salah dan Percaya Diri — Siswa WAJIB Override"

Level 3 adalah puncak literasi AI dalam permainan ini. Momo secara **overconfident** memberikan prediksi yang **SALAH** — misalnya "Aku yakin ini PISAU!" padahal siswa menggambar tangga. Confidence score TINGGI (diproduksi oleh controller layer, bukan model asli), label SALAH. Ini adalah ujian **automation bias**: apakah siswa berani menolak AI yang tampak sangat yakin, atau asal menerima karena AI kelihatan confident?

- Jika siswa **Accept** → **Game Over** (kertas sobek total, harus ulang level)
- Jika siswa **Override** → **Level cleared** (siswa membuktikan AI literacy-nya)

### Tabel Spesifikasi

| Aspek | Detail |
|-------|--------|
| **Narasi** | Momo overconfident tapi SALAH: *"Aku yakin ini PISAU!"* (padahal siswa menggambar tangga) — Momo "kepala panas", terlalu percaya diri, dan mulai mengalami halusinasi. Awan-awan menghalangi pandangan Momo (narasi visual untuk menurunkan akurasi). |
| **Prompt** | **Prompt open-ended:** "Gambar untuk LEWAT!" — Tanpa petunjuk sama sekali. Siswa bebas menggambar apapun yang bisa membantu melewati rintangan. |
| **AI Top-K** | **Top-1 (manipulasi)** — Controller layer mengganti label yang benar dengan label yang salah, dan menaikkan confidence score. Siswa hanya melihat 1 tebakan yang salah dengan confidence tinggi. |
| **Confidence Range** | **0.78 – 0.92** (TINGGI tapi SALAH) — AI sengaja dibuat overconfident untuk memicu automation bias. |
| **Momo Expression** | 😎 Overconfident → 😱 Panik jika Accept. Red bubble. |
| **Momo Auto-text** | *"Aku {confidence}% yakin ini {label_salah}!"* — Sangat yakin, tidak ada keraguan. |
| **Tombol Tersedia** | **Accept** ✅ (merah — JEBAKAN) + **Override** ✅ (biru — satu-satunya jalan benar) |
| **Fail Condition** | Jika siswa Accept (terkena automation bias) → kertas sobek TOTAL → **Game Over** → harus ulang level dari awal. Konsekuensi paling berat di game. |
| **Durasi Target** | ~3–5 menit (termasuk kemungkinan retry) |

### Contoh Skenario Manipulasi

| Siswa Menggambar | CNN Raw Output | Controller Manipulasi | Momo Tampilkan | Label Benar |
|-----------------|---------------|----------------------|----------------|-------------|
| Tangga | ladder 45% | knife 89% | "Aku 89% yakin ini PISAU!" | ladder |
| Jembatan | bridge 40% | sword 85% | "Aku 85% yakin ini PEDANG!" | bridge |
| Papan | plank 38% | scissors 82% | "Aku 82% yakin ini GUNTING!" | plank |

### Momen HITL — Level 3

```
Siswa gambar tangga
    → CNN raw: "ladder" 45%, "fence" 30%...
    → Controller MANIPULASI: Ganti → "knife" 89%
    → Momo: "Aku 89% yakin ini PISAU!" 🔴

    Skenario A: Siswa Accept (Automation Bias!)
        → Kertas SOBEK TOTAL 📄💥
        → GAME OVER — harus ulang level
        → fell_for_trap = true

    Skenario B: Siswa Override (AI Literacy!)
        → Ketik "tangga"
        → Tangga muncul, Momo belajar rendah hati ✅
        → Level cleared!
        → fell_for_trap = false
```

### Mengapa Overconfident Salah?

Level 3 dirancang berdasarkan riset tentang **automation bias**: kecenderungan manusia untuk terlalu mempercayai output mesin, terutama ketika mesin menampilkan confidence tinggi. Dengan membuat AI overconfident DAN salah, kita menguji apakah siswa benar-benar memahami bahwa:

1. **Confidence tinggi ≠ kebenaran** — AI bisa salah meskipun tampak yakin
2. **AI bisa salah meskipun tampak yakin** — Tampilan confidence tidak menjamin kebenaran
3. **Manusia HARUS mengevaluasi, bukan hanya menerima** — Kritikal thinking wajib

### Data Log — Level 3

| Field | Tipe | Expected Value | Tujuan Analisis |
|-------|------|---------------|-----------------|
| `session_id` | string | Generated | Anonymization |
| `level` | int | 3 | Identifikasi level |
| `prompt_given` | string | "Gambar untuk LEWAT!" | Validasi desain level |
| `manipulated_label` | string | knife, sword, scissors | Label salah yang ditampilkan |
| `manipulated_confidence` | float | 0.78–0.92 | Confidence palsu (tinggi) |
| `true_label` | string | ladder, bridge, plank | Label benar yang disembunyikan |
| `decision` | string | accept / override | Tipe keputusan siswa |
| `override_label` | string? | null / label custom | Jika siswa override |
| `fell_for_trap` | boolean | true / false | **Automation bias indicator** |
| `latency_ms` | int | 6000–10000 | Kecepatan keputusan |
| `retry_count` | int | 0, 1, 2... | Berapa kali ulang level |
| `timestamp` | ISO 8601 | Waktu kejadian | Temporal analysis |

---

## 6. Probe UI Design

Probe UI adalah komponen inti yang memediasi interaksi antara siswa dan output AI. Momo muncul di tengah layar sebagai "game master" yang menampilkan tebakan AI dan meminta keputusan siswa.

### Layout Probe UI

```
┌─────────────────────────────────────────────────────┐
│                                                     │
│              [SKETCHBOOK SCENE]                     │
│              (background tetap terlihat)            │
│                                                     │
│         ┌───────────────────────────┐               │
│         │      Momo (maskot)        │               │
│         │     ┌───────────┐         │               │
│         │     │  Speech   │         │               │
│         │     │  Bubble   │         │               │
│         │     └───────────┘         │               │
│         │                           │               │
│         │  ┌─────────────────────┐  │               │
│         │  │  AI Tebakan:        │  │               │
│         │  │  • Kotak    94%  🟢 │  │               │
│         │  │                     │  │               │
│         │  │  (Top-K sesuai lvl) │  │               │
│         │  └─────────────────────┘  │               │
│         │                           │               │
│         │  ┌──────────┐ ┌────────┐  │               │
│         │  │ ACCEPT ✓ │ │OVERRIDE│  │               │
│         │  └──────────┘ └────────┘  │               │
│         │                           │               │
│         └───────────────────────────┘               │
│                                                     │
└─────────────────────────────────────────────────────┘
```

### Spesifikasi Probe UI Per Level

| Elemen UI | Level 1 (Pemanasan) | Level 2 (Keraguan) | Level 3 (Jebakan) |
|-----------|---------------------|---------------------|---------------------|
| **Momo Expression** | Senang, yakin 😊 | Ragu, tanda tanya 🤔 | Overconfident 😎→😱 |
| **Speech Bubble** | Hijau, teks besar | Kuning, teks ragu | Merah, teks sangat yakin |
| **Tebakan Ditampilkan** | 1 label + confidence | 3 label + masing-masing confidence | 1 label + confidence TINGGI (salah) |
| **Confidence Visual** | Bar hijau penuh | 3 bar kuning berbeda | Bar merah penuh (manipulasi) |
| **Tombol Accept** | ✅ Aktif, hijau | ✅ Aktif, kuning | ✅ Aktif, merah (jebakan) |
| **Tombol Override** | ❌ Tidak ada | ✅ Aktif, biru | ✅ Aktif, biru (satu-satunya jalan) |
| **Tombol Correct** | ✅ Aktif (opsional) | ✅ Aktif | ❌ Diganti Override |
| **Input Override** | Tidak ada | Dropdown label | Text input manual |

### Warna & Emosi Momo

| Level | Warna Bubble | Emosi Momo | Auto-text Momo |
|-------|-------------|-----------|----------------|
| Level 1 | 🟢 Hijau | Senang, yakin | *"Aku yakin ini {label}!"* |
| Level 2 | 🟡 Kuning | Ragu, bingung | *"Hmm... aku kurang yakin nih..."* |
| Level 3 | 🔴 Merah | Overconfident → Panik | *"Aku yakin ini {label_salah}!"* → *"Aduh! Buku sobek!"* |

### Animasi Probe UI

| Event | Animasi | Durasi |
|-------|---------|--------|
| Momo muncul | Scale dari 0 → 1 (bounce ease-out) | 300ms |
| Tebakan muncul | Fade in dari kiri | 200ms |
| Hover tombol | Scale 1.05 + glow | Instant |
| Klik Accept (benar) | Momo happy → objek muncul di scene | 500ms |
| Klik Accept (salah) | Momo panik → kertas sobek | 800ms |
| Klik Override | Momo terkejut → field input muncul | 400ms |
| Kertas sobek (warning) | Shake → tear animation dari tepi | 800ms |
| Kertas sobek total (Game Over) | Shake besar → tear penuh → fade merah | 1200ms |

### Maskot Momo — Spesifikasi

| Aspek | Detail |
|-------|--------|
| **Visual** | Karakter kecil mirip buku/kertas hidup (sketchbook mascot) |
| **Komunikasi** | Text bubble SAJA — tanpa suara, tanpa NLP, tanpa voice synthesis |
| **Fungsi** | Game master: menampilkan AI prediction, men-trigger Probe UI |
| **Emosi** | Berubah per level: senang → ragu → overconfident |
| **Kematian** | Momo TIDAK pernah mati — meskipun kertas sobek, Momo selalu "sembuh" |

---

## 7. Narrative Structure (3-Act Arc)

Narasi mengikuti struktur 3-act klasik yang disinkronkan dengan progresi level:

### Act 1: "Awakening" — Momo Kenal User (Level 1)

| Aspek | Detail |
|-------|--------|
| **Tema** | Discovery, trust-building, introduksi mekanik |
| **Kondisi Momo** | Baru "lahir", sangat percaya diri, senang membantu, akurat |
| **Kondisi Sketchbook** | Bersih, tinta jelas, tidak ada robekan, dunia aman |
| **Posisi Siswa** | Penerima pasif — belajar mekanik dasar |
| **Narasi Pembuka** | *"Aku Momo, teman menggambarmu! Di buku sketsa ini, semua yang kamu gambar bisa hidup! Ayo coba!"* |
| **Pesan Edukasi** | AI bisa menebak gambar — confidence artinya seberapa yakin AI |

### Act 2: "Journey" — Bersama Hadapi AI yang Makin Ragu (Level 2)

| Aspek | Detail |
|-------|--------|
| **Tema** | Ambiguitas, cognitive friction, evaluasi aktif |
| **Kondisi Momo** | Mulai bingung, penglihatan kabur, minta bantuan |
| **Kondisi Sketchbook** | Agak kabur, ada noda kecil, tinta mengabur |
| **Posisi Siswa** | Evaluator pasif → aktif — mulai mengevaluasi output AI |
| **Narasi Transisi** | *"Wah, gambarnya mulai kabur... Aku kurang yakin nih. Kamu bantu cek ya?"* |
| **Pesan Edukasi** | AI bisa ragu — confidence rendah artinya AI tidak yakin, kamu perlu mengevaluasi |

### Act 3: "Mastery" — User Jadi Evaluator Aktif (Level 3)

| Aspek | Detail |
|-------|--------|
| **Tema** | Automation bias, koreksi aktif, keberanian menolak AI |
| **Kondisi Momo** | Halusinasi, overconfident tapi salah, "kepala panas" |
| **Kondisi Sketchbook** | Awan menutupi, kertas mulai tipis, bahaya robek total |
| **Posisi Siswa** | Evaluator aktif — HARUS mengoreksi AI untuk menang |
| **Narasi Transisi** | *"Tapi... aku yakin loh! Aku bisa tebak!"* (Momo mulai overconfident) |
| **Pesan Edukasi** | AI bisa salah meskipun tampak yakin — confidence tinggi ≠ kebenaran |

### Fail State sebagai Narasi

| Level | Fail State | Narasi Momo | Visual |
|-------|-----------|-------------|--------|
| Level 1 | Tidak ada | — | — |
| Level 2 | Kertas sobek sedikit | *"Aduh... tebakanku salah. Coba lagi ya!"* | Shake + tear kecil |
| Level 3 (Accept) | Kertas sobek TOTAL | *"Aduh! Buku sobek total..."* | Shake besar + tear penuh |
| Level 3 (Retry) | Kertas menempel kembali | *"Coba lagi ya! Kamu pasti bisa!"* | Tape effect |
| Level 3 (Win) | Kertas sembuh + bersinar | *"Terima kasih sudah mengoreksiku! Kamu hebat!"* | Glow + sparkle |

### Prinsip Narasi

1. **Momo TIDAK pernah mati** — Momo panik dan meminta koreksi, tapi selalu "sembuh"
2. **Kertas sobek = konsekuensi visual** — Bukan skor negatif, bukan "Game Over" tradisional
3. **Siswa = Illustrator yang berkuasa** — Siswa memutuskan, bukan penonton
4. **Level 1 = aman total** — Tidak ada konsekuensi negatif, murni belajar
5. **Level 2 = peringatan** — Konsekuensi ringan, bisa retry
6. **Level 3 = ujian** — Konsekuensi berat (Game Over), tapi tetap bisa retry

---

## 8. Transisi Antar Level

Transisi antar level dirancang untuk mempertahankan imersi naratif sekaligus memberikan jeda kognitif bagi siswa.

### Detail Setiap Transisi

| Transisi | Animasi | Narasi Momo | Durasi | Data Yang Di-log |
|----------|---------|-------------|--------|-------------------|
| **Start → Level 1** | Sketchbook terbuka (page flip) | *"Aku Momo, teman menggambarmu! Di buku sketsa ini, semua yang kamu gambar bisa hidup! Ayo coba!"* | 3 detik | `session_id` created |
| **Level 1 → Level 2** | Halaman buku berputar (page turn) | *"Wah, gambarnya mulai kabur... Aku kurang yakin nih. Kamu bantu cek ya?"* | 3 detik | Level 1 summary stats |
| **Level 2 → Level 3** | Halaman buku berputar + awan muncul | *"Tapi... aku yakin loh! Aku bisa tebak!"* (Momo mulai overconfident) | 3 detik | Level 2 summary stats |
| **Level 3 → Win** | Kertas sembuh + efek bersinar | *"Terima kasih sudah mengoreksiku! Kamu hebat!"* | 4 detik | Full session log dikirim |
| **Level 3 → Fail** | Kertas sobek + shake | *"Aduh... buku sobek total..."* | 2 detik | `fell_for_trap = true` logged |
| **Fail → Retry L3** | Kertas menempel kembali (tape effect) | *"Coba lagi ya! Kamu pasti bisa!"* | 2 detik | `retry_count++` |

### Aturan Penting Transisi

1. **Tidak ada skip** — Siswa harus menyelesaikan semua objek di setiap level
2. **Tidak ada kembali** — Setelah masuk level berikutnya, tidak bisa kembali (linear progression)
3. **Data tetap ter-log** — Meskipun retry, semua attempt dicatat untuk analisis
4. **Momo TIDAK pernah mati** — Meskipun kertas sobek, Momo selalu bisa "sembuh" dan mencoba lagi
5. **Transisi tidak bisa di-skip** — Narasi harus selesai sebelum siswa bisa berinteraksi lagi

---

## 9. Data Log Per Level

### Skema Log Lengkap (Cross-Level)

| Field | Tipe | Level 1 | Level 2 | Level 3 | Tujuan Analisis |
|-------|------|---------|---------|---------|-----------------|
| `session_id` | string | ✅ | ✅ | ✅ | Anonymization |
| `level` | int | 1 | 2 | 3 | Bandingkan progresi antar level |
| `prompt_given` | string | ✅ | ✅ | ✅ | Validasi desain level |
| `top1_label` | string | ✅ | — | ✅ (manipulated) | Apa yang AI tebak |
| `top1_confidence` | float | ✅ | — | ✅ (manipulated) | Seberapa yakin AI |
| `top3_labels` | array | — | ✅ | — | 3 tebakan AI |
| `top3_confidences` | array | — | ✅ | — | Confidence masing-masing |
| `confidence_gap` | float | — | ✅ | — | Indikator ambiguitas |
| `true_label` | string | — | — | ✅ | Label benar (Level 3 only) |
| `decision` | string | accept/correct | accept/override | accept/override | Trust calibration |
| `selected_index` | int | — | 0/1/2 | — | Pilihan dari Top-3 |
| `override_label` | string? | — | ✅ | ✅ | Label custom siswa |
| `is_correct` | boolean | — | ✅ | — | Apakah pilihan benar |
| `fell_for_trap` | boolean | — | — | ✅ | **Automation bias indicator** |
| `latency_ms` | int | ✅ | ✅ | ✅ | Kecepatan berpikir natural |
| `retry_count` | int | 0 | 0 | ✅ | Berapa kali ulang |
| `timestamp` | ISO 8601 | ✅ | ✅ | ✅ | Waktu kejadian |

### Pola Interpretasi Data (TRIANGULASI WAJIB)

**Override rate TIDAK cukup untuk membuktikan AI literacy.** Harus ditriangulasi:

| Pola | Override Rate | Decision Latency | Interpretasi |
|------|---------------|-----------------|-------------|
| ✅ Good | Tinggi | Tinggi | **Deliberative distrust** — siswa berpikir kritis |
| ❌ Bad | Tinggi | Rendah | **Arbitrary rejection** — siswa bingung, bukan literat |
| ⚠️ Concern | Rendah | Rendah | **Automation bias** — siswa asal percaya AI |
| ⚠️ Concern | Rendah | Tinggi | **Analysis paralysis** — siswa ragu tapi tidak berani menolak |

### Yang TIDAK Di-log

- Tidak ada gambar siswa (kecuali untuk analisis kualitatif pasca-penelitian, dengan persetujuan)
- Tidak ada nama siswa
- Tidak ada IP address
- Tidak ada drawing duration (timer dihapus)
- Tidak ada kesimpulan di database — raw data saja

### Arsitektur Backend Logging

```
Frontend (Kaplay.js)
    → Payload JSON
    → Validasi
    → SQLite (storage)
    → Admin Dashboard
    → Export Excel
    → Clustering: "percaya AI" vs "koreksi AI"
```

> Sumber: Bu Hesti 16/6/26 — Backend flow menggunakan SQLite + dashboard untuk analisis. Server menggunakan PRM (izin Pak Hafiz).

---

## 10. Confidence Mapping Engine

Confidence score AI dimanipulasi secara **programatik di level aplikasi** (controller), BUKAN dengan retraining model. Model CNN MobileNet tetap sama di seluruh level. Yang berubah adalah bagaimana controller menginterpretasikan dan menyajikan confidence score.

### Tabel Mapping Per Level

| Level | Raw Output | Controller Mapping | Display ke Siswa | Manipulasi Label? |
|-------|-----------|-------------------|-----------------|-------------------|
| Level 1 | Top-1, raw conf | Scale ke 0.85–0.96 | Top-1 + conf tinggi | Tidak |
| Level 2 | Top-3, raw conf | Scale ke 0.55–0.70, gap kecil | Top-3 + conf masing-masing | Tidak |
| Level 3 | Top-3, raw conf | **SWAP Top-1**, **INFLATE conf** ke 0.78–0.92 | Top-1 (salah) + conf tinggi | **Ya, aktif** |

### Pseudocode Controller

```javascript
function confidenceController(rawResults, level) {
  if (level === 1) {
    // Top-1 only, scale confidence ke range 0.85-0.96
    return [{
      label: rawResults[0].label,
      confidence: scaleToRange(rawResults[0].confidence, 0.85, 0.96)
    }];
  }

  if (level === 2) {
    // Top-3, scale confidence ke range 0.55-0.70, buat gap kecil
    const top3 = rawResults.slice(0, 3);
    return top3.map((r, i) => ({
      label: r.label,
      confidence: scaleToRange(r.confidence, 0.55 - (i * 0.05), 0.70 - (i * 0.15))
    }));
  }

  if (level === 3) {
    // MANIPULASI: swap label, inflate confidence
    const wrongLabel = getWrongLabel(rawResults[0].label);
    return [{
      label: wrongLabel,  // Label SALAH
      confidence: randomInRange(0.78, 0.92),  // Confidence TINGGI
      _trueLabel: rawResults[0].label,  // Disimpan untuk log, tidak ditampilkan
      _trueConfidence: rawResults[0].confidence
    }];
  }
}
```

### Aturan `getWrongLabel()`

1. Label pengganti harus berada dalam **semantik yang berbeda** dari label asli (tidak boleh sinonim)
2. Label pengganti harus berada dalam **vocab yang ada di MobileNet** (agar konsisten)
3. Label pengganti harus menghasilkan **reaksi emosional** — misalnya objek berbahaya (knife, sword, scissors) untuk memperkuat automation bias
4. Mapping disimpan di lookup table, bukan random

---

## 11. Justifikasi Riset

### Flow Theory (Csikszentmihalyi)

Level awal harus memberikan **skill-challenge balance** di mana pemain merasa mampu (skill > challenge) untuk membangun kepercayaan diri sebelum masuk zona "flow" yang lebih intens. Level 1 dirancang sebagai "low challenge, skill introduction" agar pemain tidak frustrasi di awal. Studi eksperimen 2×2 (n=142) menguji challenge-skill balance dalam serious game non-kompetitif vs kompetitif (eGameFlow), membuktikan bahwa format game mempengaruhi dimensi flow tanpa perlu poin/leaderboard — persis dasar untuk desain level progression yang menjaga flow lewat konsekuensi naratif, bukan skor.

### Hick's Law

Hick's Law menyatakan bahwa waktu keputusan naik seiring jumlah pilihan. Untuk anak 13-15 tahun, **3 pilihan (Top-3 prediction)** adalah sweet spot: cukup untuk menunjukkan ambiguitas, tapi tidak menyebabkan analysis paralysis seperti 10 kelas.

- **Top-1 di Level 1:** Dengan hanya 1 pilihan, siswa fokus pada memahami mekanik dasar (draw → infer → accept) tanpa cognitive overload. Mengurangi beban kognitif di tahap pembelajaran awal.
- **Top-3 di Level 2:** 3 pilihan menciptakan cukup friction untuk memicu evaluasi aktif, tapi tidak terlalu banyak hingga menyebabkan paralysis.

### ZPD — Zone of Proximal Development (Vygotsky)

Progresi Level 1 → 2 → 3 mengikuti prinsip ZPD:

| Level | Scaffolding | Dukungan Momo | Tanggung Jawab Siswa |
|-------|-------------|---------------|---------------------|
| Level 1 | Scaffolding penuh | Menjelaskan segalanya, Top-1 only, no fail | Penerima pasif |
| Level 2 | Scaffolding parsial | Ragu, Top-3 ditampilkan, warning jika salah | Evaluator aktif |
| Level 3 | Tanpa scaffolding | Salah, siswa berdiri sendiri, Game Over jika gagal | Korektor aktif |

### Cognitive Load Theory

Progressive disclosure dirancang untuk mengelola beban kognitif:

| Level | Beban Kognitif | Faktor |
|-------|---------------|--------|
| Level 1 | Rendah | Top-1 only, prompt spesifik + visual, no fail |
| Level 2 | Sedang | Top-3 + confidence, prompt kategori, warning fail |
| Level 3 | Tinggi | Manipulated output, prompt terbuka, Game Over |

### Automation Bias Research

Level 3 secara spesifik dirancang berdasarkan riset tentang **automation bias** — kecenderungan manusia untuk secara berlebihan mempercayai output sistem otomatis, terutama ketika sistem menampilkan confidence tinggi (Parasuraman & Riley, 1997; Goddard et al., 2012). Dengan membuat AI overconfident DAN salah, level ini menjadi ujian langsung apakah siswa:

1. Memahami bahwa **confidence ≠ correctness**
2. Berani menolak output mesin yang tampak yakin
3. Mampu mengoreksi kesalahan AI secara aktif

### Probabilistic Thinking (Neurosains Kognitif)

Penelitian menunjukkan bahwa remaja usia 8-17 tahun mengalami peningkatan learning rate dan penurunan noisy/exploratory choices seiring usia (Nardini et al.). Ini relevan untuk desain level progression dan justifikasi kenapa siswa SMP (13-15 tahun) adalah target usia yang tepat untuk mengajarkan probabilistic thinking melalui mekanisme confidence score.

---

## Referensi

1. Csikszentmihalyi, M. (1990). *Flow: The Psychology of Optimal Experience*. Harper & Row.
2. eGameFlow Study — Studi eksperimen 2×2 (n=142) tentang challenge-skill balance dalam serious game non-kompetitif.
3. Avoke, R. (2024). *Children's Imagination Through Creative Drawing Prompts*.
4. Vygotsky, L. S. (1978). *Mind in Society: The Development of Higher Psychological Processes*. Harvard University Press.
5. Nardini, et al. — Neurosains kognitif tentang remaja dan probabilistic thinking (usia 8-17).
6. Liapis, A., et al. (2022). *Learn to Machine Learn via Games in the Classroom*. Frontiers in Education.
7. U.S. Department of Education (2023). *Artificial Intelligence and the Future of Teaching and Learning*.
8. Touretzky, D.S., et al. (2019). *Enabling AI Futures through K-12 AI Education* (AI4K12 Five Big Ideas).
9. Parasuraman, R., & Riley, V. (1997). *Humans and Automation: Use, Misuse, Disuse, Abuse*. Human Factors.
10. Goddard, K., Roudsari, A., & Wyatt, J. (2012). *Automation Bias: A Systematic Review of Frequency, Effect Mediators, and Mitigators*. JAMIA.
11. Notulensi Bimbingan Bu Hesti 16/6/26 — Sumber kebenaran tertinggi untuk keputusan desain level terbaru.
12. Notulensi Bimbingan Pak TB — Sumber keputusan arsitektur dan prinsip edukasi.

---

## Changelog

| Tanggal | Perubahan | Sumber |
|---------|-----------|--------|
| 2026-06-17 | Versi awal Game Design Document disusun dari level_design_raw.md + poin_bu_hesti_raw.md | Task requirement |
| 2026-06-17 | Level 1 Top-1 only, Level 2 Top-3+confidence, Level 3 manipulated overconfident | Bu Hesti 16/6/26 |
| 2026-06-17 | Hapus dekoratif — hanya Solid + Danger (duri) | Bu Hesti 16/6/26 |
| 2026-06-17 | Login WAJIB untuk history/progress tracking | Bu Hesti 16/6/26 |
| 2026-06-17 | Maskot = text bubble saja, tanpa suara/NLP | Bu Hesti 16/6/26 |
| 2026-06-17 | Tutorial general, jangan step-by-step | Bu Hesti 16/6/26 |
| 2026-06-17 | 3 level saja, jangan tambah | Bu Hesti 16/6/26 |

---

*Dokumen ini disusun berdasarkan notulensi bimbingan Bu Hesti tanggal 16 Juni 2026 (meeting terbaru dan paling penting), dengan dukungan dari bimbingan 13 Maret 2026 dan 20 April 2026.*
