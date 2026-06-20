# Memory — Escape the Sketchbook Project

> Living document untuk memahami project & tracking keputusan

---

## Pemahaman Project

**Nama Project:** Simulasi Interaktif Literasi AI untuk Siswa SMP Kelas 7-9  
**Judul Utama (Pak TB):** Sistem Literasi Kecerdasan Buatan untuk Siswa Sekolah  
**Format:** Interactive HITL AI Playground — game 2D berbasis browser  
**Engine:** Kaboom.js (bukan Unity — alasan: integrasi JS dengan MediaPipe & TF.js)  

**Tim:**
| Anggota | Fokus | Warna |
|---------|-------|-------|
| Can (Farchan Deano M.) | Frontend, UI/UX, Kaplay.js, MediaPipe, Maskot Momo, Gameplay, Narrative, Probe UI, Animation | 🔵 BIRU |
| Dias (Muhammad Dias Al-I.) | Backend, CNN MobileNet, TensorFlow.js, Data Logging, K-Means Clustering, Dashboard, REST API | 🟢 HIJAU |

**Prinsip Core:** "Controlled Ambiguity" — AI sengaja tidak sempurna agar momen HITL terjadi  
**Prinsip Edukasi (Pak TB):** "Mengajari tanpa terasa menggurui" — prioritas: UI dulu, gameplay, baru edukasi disisipkan  
**Arsitektur:** Hybrid — Browser-Based Inference (TF.js) + Server-Side Active Services (REST API, SQLite, K-Means)

---

## Keputusan Bu Hesti 15/6/26 (Bimbingan Terbaru)

### Desain Sistem
1. **SATU diagram global** pakai WARNA (BIRU=Can, HIJAU=Dias) — jangan pecah jadi banyak diagram kecil
2. **Shape flowchart:** Input = parallelogram, Proses = rectangle, Decision = diamond, Output = parallelogram
3. **Hapus kata "from"** di diagram — langsung "Fase 1", bukan "From Fase 1"
4. **Font diperbesar** — Bu Hesti komplain tulisan kecil
5. **Warna harus konsisten** antar fase
6. **Desain sistem = INPUT–PROSES–OUTPUT** (referensi gambar teman yang pakai format ini)
7. **Hapus decorative** — benda berbahaya/dekorasi tembus pandang dihapus, fokus ke mekanisme HITL
8. **3 level saja** — jangan tambah level decorative

### User Flow
9. User flow dibagi **3 fase** — sudah di-approve
10. **Wajib login** (perubahan dari sebelumnya yang session-only) — karena butuh history data
11. **Use case = aktor + aktivitas** — bukan sekadar daftar fitur

### API & Data
12. **API logging:** POST /api/log, GET /api/sessions, POST /api/analyze
13. **Data yang dicatat:** user_id, level, top1_label, top1_conf, decision, latency

### Metodologi
14. **Metodologi MIX** (Kuantitatif + Kualitatif) — disetujui
15. **Fishbone** untuk analisis data (4 tulang: Manusia, Metode, Media, Materi)
16. **Kuantitatif = matriks log** (tabel data), **Kualitatif = narasi** (interpretasi)

### Level Design
17. **Level 1:** prompt terbatas, Top-1 only (AI akurat, siswa belajar percaya)
18. **Level 2:** Top-3 + confidence, cognitive friction (AI ragu, siswa evaluasi)
19. **Level 3:** AI overconfident salah, wajib override (AI tipu, siswa HARUNG koreksi)

### Maskot
20. Momo = auto-text dasar, **tanpa NLP/voice** (jangan over-engineering)
21. Momo = coretan hidup dari illustrator sebelumnya di universe Sketchbook (IP story)

---

## Changelog

| Tanggal | Perubahan | Sumber |
|---------|-----------|--------|
| 2026-06-16 | Buat memory.md awal | Can request |
| 2026-06-16 | Audit semua file, pindah ke folder structure | Main agent |
| 2026-06-15 | Keputusan Bu Hesti 15/6 tercatat | Notulensi Bimbingan.txt |
| 2026-06-15 | Target user berubah: SD → SMP Kelas 7-9 | Pak TB + Bu Hesti |
| 2026-06-14 | Arsitektur hybrid final: browser TF.js + server REST/SQLite | Merged Context |
| 2026-06-14 | Metodologi: Mixed Methods + R&D + Fishbone + SUS | Riset Metode Penelitian |
