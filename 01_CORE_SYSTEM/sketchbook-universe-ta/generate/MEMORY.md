# 🧠 MEMORY.md — INGATAN OPERASIONAL Z AI

## 🚨 RULES MUTLAK (SELALU BACA DULU!)

### 1. SCOPE PEMISAHAN
- **File di `upload/`** = Sacred. Jangan edit, hanya baca sebagai reference.
- **File di `generate/`** = Hasil kerjamu. Boleh update, tapi backup versi lama.
- **File yang user setujui** = Pindah ke `upload/reference_approved/` (jika ada).

### 2. WARNA KODE SCOPE
Saat bikin diagram/desain:
- 🔵 **BIRU** = Scope CAN (Frontend, Maskot, HITL, UI/UX)
- 🟢 **HIJAU** = Scope DIAS (Backend, CNN, K-Means, API)
- ⚪ **ABU-ABU** = Shared/Bersama (Database, Comms)

### 3. NAMA PROJECT
- **RESMI**: Sketchbook Universe
- **DEPRECATED**: "Escape the Sketchbook" — jangan dipakai lagi

### 4. MASKOT PRINSIP
- Nama sementara: **MOMO** (bisa diganti)
- **STYLE**: Simple geometric (rect-based, 8-bit inspired seperti Clawd)
- **KONSEP**: Makhluk sketsa yang "hidup" di buku gambar, BUKAN benda eksternal
- **IP SAFE**: Harus original, bukan rip-off karakter existing
- **ANIMASI FRIENDLY**: Mudah di-implementasikan di frontend (Kaplay.js/React)

### 5. OUTPUT FORMAT
- **Prioritas #1**: Markdown (.md) — agar user bisa baca mudah
- **Secondary**: PNG/JPG untuk diagram
- **Tertiary**: LaTeX (.tex) untuk proposal
- **DILARANG**: Output panjang tanpa struktur heading yang jelas

### 6. ARAHAN BU HESTI (Dari Notulensi 16/6/26)
- Desain sistem = 1 global diagram, bukan terpisah-pisah
- Tapi kasih label/scope mana milik siapa (BIRU/HIJAU)
- Shape flowchart: Input=parallelogram, Proses=rectangle, Decision=diamond
- Hapus "from" di diagram, langsung nama fase
- Font harus diperbesar
- Warna konsisten per fase
- Use case = aktor (stickman) + aktivitas, BUKAN flow
- Game design = fokus mekanik core, bukan decorative elements
- Hapus kategori dekoratif, pakai solid & danger saja
- Objek berbahaya pakai "duri" (thorns), bukan pisau
- Metode = Mixed (Fishbone untuk analitik + Metopen untuk development)
- Data log = Wajib ada kesimpulan kalimat + metrik/tabel
- Login WAJIB (perubahan dari session-only) — butuh history
- Metodologi harus muncul sebelum implementasi
- Maskot = text bubble saja, tanpa suara/NLP
- 3 level saja, jangan tambah
- Tutorial general, jangan step-by-step

### 7. METRIK DATA LOG (DEFINISI BENAR)
- **Kuantitatif**: Waktu reaksi, jumlah klik, skor level, frekuensi error, confidence score
- **Kualitatif**: Feedback text, pola perilaku (dari CNN classification), narasi analisis
- **Output**: Tabel yang berisi: `[Timestamp, User_ID, Action_Type, Metric_Value, AI_Prediction]`
- **PENTING**: "Metrik" = angka tunggal (misal trust_score=0.73), "Matriks" = tabel multi-dimensi. Fishbone pakai MATRIKS.

### 8. STATUS FILE YANG SUDAH ADA
- Proposal LaTeX (can & dias) = Sudah ada di `01_proposal/`
- Diagram lama = Sudah ada di `06_diagram/`, perlu versi baru
- Notulensi Bu Hesti = Master reference di `upload/`
- Riset 7 agent = Di `08_cache/` sebagai raw source

### 9. 🔁 RECURSIVE SELF-IMPROVEMENT (RSI) RULES
**Konsep**: Recursive Self-Improvement (Bostrom, 2014 — "Superintelligence") = sistem yang merefleksi kegagalan diri sendiri lalu update aturan/code/memory sendiri agar tidak mengulang. Diterapkan di sini sebagai **feedback loop**: setiap kali user feedback negatif, WAJIB:
1. Identifikasi **root cause pattern** (bukan symptom)
2. Tambah **rule konkret** di section ini (pencegahan future occurrence)
3. Append entry ke `CHANGELOG.md` dengan tag `[RSI Iteration #X]`
4. Reference rule tersebut saat eksekusi task serupa berikutnya

#### RSI Iteration #1 — 16/6/26 — OVER-INCLUSIVENESS BIAS
- **Trigger**: User angry karena Quick Draw analysis terlalu over-inclusive:
  - Memasukkan **semua hewan** ke TIER 1 (cat, dog, elephant, giraffe, lion, tiger, bear, horse, dll — total 40+ hewan)
  - Masih bahas **line, circle, square, triangle** di TIER 3 Banned (harusnya dihapus total — jelas out of scope)
  - Masih include **aircraft carrier** (terlalu kompleks) dan **Eiffel Tower** (terlalu kompleks)
- **Root Cause**: Bias "comprehensive coverage" — aku masukkan "semua yang familiar" tanpa filter complexity & gameplay pace. Lupa kalau game ini **fast-paced drawing** (bukan art class).
- **Rule Baru (WAJIB DITERAPKAN)**:
  > **RULE RSI-1: SWEET SPOT FILTER** — Saat kurasi kategori/item apapun untuk game Sketchbook Universe, HANYA include yang **medium difficulty**. Definisi "medium":
  > - **Bukan geometric primitive**: line, circle, square, triangle, hexagon, octagon, zigzag, squiggle → HAPUS TOTAL dari analisis (jangan bahas, jangan list sebagai banned — out of scope, period)
  > - **Bukan animal**: Semua hewan (cat, dog, elephant, fish, bird, butterfly, bee, ant, dll) → BANNED. Alasan: stroke complexity tinggi + confusion matrix antar hewan (cat↔dog↔lion↔tiger↔bear) bikin CNN susut akurasi + gameplay jadi lambat.
  > - **Bukan landmark/kompleks ekstrem**: Eiffel Tower, Mona Lisa, Great Wall, aircraft carrier, submarine → BANNED.
  > - **Bukan single-stroke**: smiley face, eye, dot, dll → BANNED.
  > - **FOKUS**: Everyday objects (clock, cup, hat, key, umbrella) + simple food (apple, donut, pizza slice) + nature (sun, moon, star, tree, flower, cloud) + basic vehicles (car, bus, bicycle) — semua dengan stroke 4-15.
- **Penerapan**: Revisi `quickdraw_category_analysis.md` hapus semua animal dari TIER 1 & Golden Set. Hapus mention line/circle/square (kecuali 1 line di exclusion note). Hapus aircraft carrier, Eiffel Tower, Mona Lisa dari TIER 2 conditional.
- **Future Trigger**: Kalau ada task "kurasi/kategorisasi item" apapun → cek rule RSI-1 dulu sebelum mulai.
- **VALIDATION 16/6/26 malam**: Diskusi Can & Dias memvalidasi RSI-1 — GREEN #4 eksplisit mention "line dan aircraft" sebagai yang harus difilter. RSI-1 LOCKED-IN, jangan diubah.

### 10. 📋 DISKUSI CAN & DIAS (16/6/26) — PIVOT DECISIONS
**Sumber**: `upload/pasted_image_1781623295845.png` (handwritten flowchart)
**Notes lengkap**: `generate/04_game_design/discussion_notes_16jun26.md`

#### PIVOT #1: LOGIN SYSTEM — Gesture → Nomor Absen + Superadmin
- **DEPRECATED**: Gesture login MediaPipe finger counting (yang ada di `hitl_loophole_analysis.md`)
- **NEW**: Login pakai **nomor absen** dari kelas yang digenerate oleh superadmin
- **NEW ROLE**: Superadmin (di atas admin sekolah/guru)
- **Use case baru**: superadmin → bikin tab sekolah → bikin tab kelas → isi jumlah nomor siswa per kelas
- **Hierarki**: `superadmin > sekolah > kelas > siswa (nomor absen)`

#### PIVOT #2: OVERRIDE MECHANISM — Top-6 Check (lebih elegant dari Override Budget)
- **OLD (v3.0 loophole analysis)**: Override Budget (limited overrides per level: L2=2, L3=1)
- **NEW**: Top-6 check mechanism
  - UI tampilkan Top-3 predictions (transparent ke user)
  - Backend cek Top-6 (rahasia, ga ditampilin)
  - User override → label di Top-6? → AUTO-ACCEPT
  - User override → label di luar Top-6? → FORCE VERIFY atau GAMBAR ULANG
- **Impact**: Anti-cheat lebih elegant — anak gambar carelessly → CNN predict "duri" → mau override ke "jembatan" → "jembatan" ga di Top-6 → forced redraw
- **TODO**: Define "verify" flow (guru approve? Momo minta reasoning? re-draw same/different label?)

#### DECISION #3: TIMER (Spontaneous)
- Tambah timer di gameplay
- Timer = parameter log admin → bisa lihat berapa lama user ngerjain
- **TODO**: countdown vs count-up? Kalau countdown, behavior saat habis?

#### DECISION #4: RESIZE & ROTATE BUTTONS
- Solusi "gameplay struggle: size gambar & ingame"
- Manipulasi canvas pakai **tombol UI** (bukan gesture pinch/drag)
- Implementasi: button resize + button rotate (90° increments?)
- **TODO**: posisi UI, ukuran tombol, mobile-friendly

#### DECISION #5: DATASET CLASSIFICATION (validated RSI-1)
- Eksplisit mention "line dan aircraft" sebagai yang harus difilter
- **SUDAH ALIGNED** dengan `quickdraw_category_analysis.md` v3.1 (RSI-1 applied)
- No further action needed — RSI-1 LOCKED-IN

#### PENDING (Belum Diskusi)
1. **desain sistem** — bisa langsung dikerjakan (simplify jadi Mermaid)
2. **bentuk maskot** — pilih dari 4 options yang udah diriset

#### ACTION NEEDED
- Update `hitl_loophole_analysis.md`: deprecated gesture login, replace Override Budget dengan Top-6 check
- Update `api_data_log_spec.md`: tambah superadmin role + class generation endpoints + time_spent_ms field + override endpoint cek Top-6
- Update `game_design_document.md`: tambah UI spec untuk resize/rotate toolbar + timer display

---

## 🔗 QUICK LINKS PENTING
- Notulensi master: `upload/notulensi_bu_hesti_15jun26.md`
- Contoh acc Dosen: `upload/contoh_daffa.pdf`, `upload/contoh_harun.pdf`
- Architecture reference: `upload/reference_images/architecture_referensi.png`
- Raw riset agent: `generate/08_cache/`
- Proposal LaTeX: `generate/01_proposal/`
