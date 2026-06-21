# 📋 Diskusi Notes — Can & Dias (16/6/26)

> **Sumber**: `upload/pasted_image_1781623295845.png` (handwritten flowchart dari diskusi)
> **Status**: 3 dari 5 isu resolved, 2 masih pending
> **Pivot signifikan**: Login gesture → nomor absen, Override mechanism → Top-6 check

---

## 🎯 Struktur Gambar (3 Kolom)

### 🔴 LEFT — RED Boxes (Pending Issues, 5 items)
*Merah = isu yang dibahas. Yang punya panah keluar = udah resolved. Yang gaada panah = belum.*

| # | Isu (RED) | Status | Solusi (GREEN) |
|---|-----------|--------|----------------|
| 1 | **fitur login siswa** | ✅ RESOLVED | → GREEN #1 (nomor absen + superadmin) |
| 2 | **desain sistem** | ❌ PENDING | — (belum diskusi) |
| 3 | **bentuk maskot** | ❌ PENDING | — (belum diskusi) |
| 4 | **gameplay struggle: size gambar & ingame** | ✅ RESOLVED | → GREEN #3 (resize & rotate tombol) |
| 5 | **override struggle: klasifikasi dataset & loophole anticheat/antigaming** | ✅ RESOLVED | → GREEN #4 + #5 (dataset filter + top-6 check) |

### 🟢 MIDDLE — GREEN Boxes (Sudden Decisions, 5 items)
*Hijau = keputusan baru yang muncul saat diskusi*

#### GREEN #1 — Login System Pivot
> "pake nomer absen hasil dari generate kelas. jadi penambahan superadmin. harus bikin use case baru karena super admin bisa bikin tab sekolah → bikin tab kelas → isi nomor dalam sekelas ada berapa"

**Arti**: 
- **PIVOT BESAR**: Login bukan pakai gesture MediaPipe lagi → pakai **nomor absen** dari kelas yang digenerate
- Tambahan role baru: **SUPERADMIN** (di atas admin sekolah/guru)
- Use case baru: superadmin bikin tab sekolah → tab kelas → isi jumlah nomor siswa per kelas
- Hierarki: `superadmin > sekolah > kelas > siswa (nomor absen)`

#### GREEN #2 — Timer (Spontaneous, no incoming arrow)
> "pake timer, bisa jadi parameter untuk di log admin karena kelihaatan berapa waktu buat ngerjakan bagi user"

**Arti**:
- Tambah timer di gameplay (countdown atau count-up?)
- Timer = parameter log admin → bisa lihat berapa lama user ngerjain
- **Tidak merespon red box manapun** → ide spontan Dias/Can saat diskusi

#### GREEN #3 — Resize & Rotate Buttons
> "resize dan rotate pake tombol"

**Arti**:
- Solusi untuk "gameplay struggle size gambar & ingame"
- Manipulasi canvas pakai **tombol UI** (bukan gesture pinch/drag)
- Implementasi: button resize (×0.5, ×1, ×2?) + button rotate (90° CW/CCW?)

#### GREEN #4 — Dataset Classification Filter
> "tetep klasifikasi dataset untuk menghilangkan yang gampang dan yang susah misal: line dan aircraft"

**Arti**:
- **RSI-1 ALIGNMENT PERFECT!** Persis sama dengan yang baru gw apply ke `quickdraw_category_analysis.md` v3.1
- Filter kategori terlalu gampang (line, circle, square) → BAN
- Filter kategori terlalu susah (aircraft carrier, Eiffel Tower) → BAN
- Fokus medium difficulty only

#### GREEN #5 — Top-6 Override Check (CHAINED dari GREEN #4)
> "cek top 6 (yang ditampilkan cuma top 3), kalo override masih ada di top 6, langsung labeling. kalo override di luar top 6, suruh verifikasi atau gambar ulang"

**Arti**:
- **GENIUS anti-cheat mechanism!** User cuma lihat Top-3 predictions di UI
- Backend cek Top-6 (rahasia, ga ditampilin ke user)
- Logic:
  - User override → label ada di Top-6? → **AUTO-ACCEPT** (langsung labeling)
  - User override → label di luar Top-6? → **FORCE VERIFY atau GAMBAR ULANG**
- Ini nge-block exploit: anak gambar carelessly → CNN predict "duri" → anak mau override ke "jembatan" → "jembatan" ga di Top-6 → forced to redraw
- Lebih elegant dari Override Budget (yang di v3.0 loophole analysis)

### ⚪ RIGHT — Image Box "Cek 1" (Visual Reference)
- Gray box dgn label "Cek 1" di pojok kiri atas
- Berisi gambar huruf "A" dengan garis horizontal di bawahnya
- Ada GREEN arrow dari GREEN #3 (resize/rotate) → ini
- **Kemungkinan**: UI mockup reference untuk "check setelah resize/rotate" — example visual yang harus dikenali CNN setelah transformasi

---

## 📊 Mapping ke Existing Project Artifacts

| Decision | File yang Terdampak | Action Needed |
|----------|---------------------|---------------|
| Login pivot ke nomor absen + superadmin | `hitl_loophole_analysis.md` (Gesture Login section), `api_data_log_spec.md` (auth endpoints) | **REWRITE** — gesture login kena deprecated, perlu use case superadmin + class generation |
| Timer sebagai log parameter | `api_data_log_spec.md` (log schema), `game_design_document.md` | **ADD field** `time_spent_ms` di log table |
| Resize/rotate tombol | `game_design_document.md` (UI spec), Can's frontend | **ADD UI spec** untuk toolbar transformasi |
| Dataset classification filter | `quickdraw_category_analysis.md` v3.1 | ✅ **SUDAH ALIGNED** dengan RSI-1 (line + aircraft carrier udah di-BAN) |
| Top-6 override check | `hitl_loophole_analysis.md` (anti-cheat section), `api_data_log_spec.md` (override endpoint) | **ADD mechanism** — replace/augment Override Budget |

---

## 🚨 Yang Masih Pending (RED tanpa panah)

### Pending #1: Desain Sistem
- Ini task yang lo minta di session sebelumnya (simplify jadi Mermaid)
- Belum diskusi sama sekali — bisa langsung dikerjakan
- Pakai notulensi Bu Hesti + 3 desain existing (global/Can/Dias) → simplify jadi Mermaid

### Pending #2: Bentuk Maskot
- Bisa pilih dari 4 options yang udah gw riset (Sticky Note, Ink Blob, Sketch Ghost, Origami Monster)
- Atau kombinasi — perlu Can & Dias sepakat
- Belum diskusi

---

## ✅ Validasi & Gap Analysis

### Yang Sudah Strong:
1. **Top-6 mechanism** — sangat elegant, lebih baik dari Override Budget karena:
   - Transparent di Top-3 (user experience jelas)
   - Backend secret Top-6 (anti-cheat hidden)
   - Verifikasi/redraw flow sebagai fallback
2. **Dataset filter** — aligned 100% dengan RSI-1 yang udah gw apply
3. **Superadmin hierarchy** — clean separation: superadmin bikin struktur → guru/siswa pakai

### Yang Perlu Detail Lanjutan:
1. **Timer definition** — countdown (e.g., 30 detik per gambar) atau count-up (catat waktu)? Kalau countdown, kalo habis gimana? Auto-submit atau auto-fail?
2. **Verify flow di Top-6 reject** — "verifikasi atau gambar ulang":
   - Verifikasi = apa? Guru yang approve? Momo minta reasoning?
   - Gambar ulang = same label atau beda label?
3. **Resize/rotate button UI** — posisi di mana? Ukuran tombol? Mobile-friendly?
4. **Superadmin scope** — superadmin itu siapa? Bu Hesti? Tim TA? Vendor? Berapa banyak superadmin?
5. **Class generation flow** — kalo kelas baru ditambah mid-semester, nomor absen siswa existing tetap atau reshuffle?

---

## 🔁 RSI-1 Validation

**RSI-1 (Sweet Spot Filter)** yang gw apply ke `quickdraw_category_analysis.md` v3.1 **TEPAT** dengan keputusan diskusi ini:
- GREEN #4 eksplisit mention "line dan aircraft" → sama persis dengan yang gw BAN di TIER 3
- ✅ NO ANIMALS rule gw tetap relevan (Dias/Can ga membahas animal — boleh jadi silent agreement)
- ✅ NO GEOMETRIC PRIMITIVES rule → TEPAT ("line" disebut eksplisit)
- ✅ NO COMPLEX LANDMARKS rule → TEPAT ("aircraft" disebut eksplisit)

**Konfirmasi**: RSI-1 locked-in, jangan diubah. Diskusi Can & Dias memvalidasi approach v3.1.
