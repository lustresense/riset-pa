# MOMO — Maskot Concept Document

> **Project:** Sketchbook Universe  
> **Mascot Name:** MOMO (working title)  
> **Universe:** Buku gambar yang hidup — halaman-halaman berisi coretan misterius  
> **Role:** Game Master · Confidence Score Display · Probe UI Trigger · Narrative Guide  
> **Target Audience:** Siswa SMP Kelas 7–9 (usia 13–15 tahun)  
> **Engine:** Kaplay.js (JavaScript 2D game engine, formerly Kaboom.js)  
> **Document Version:** 2.0 — 2026-03-05  

---

## Daftar Isi

1. [Header — Identitas Maskot](#1-header--identitas-maskot)
2. [IP Story — Asal-Usul Momo di Sketchbook Universe (Canonical)](#2-ip-story--asal-usul-momo-di-sketchbook-universe-canonical)
3. [Visual Design Spec — Shape Language, Color, Dimensions](#3-visual-design-spec--shape-language-color-dimensions)
4. [Behavior State Machine — 5 State Animasi](#4-behavior-state-machine--5-state-animasi)
5. [ASCII Art Representations](#5-ascii-art-representations)
6. [IP Safety Analysis](#6-ip-safety-analysis)
7. [Story Integration — Momo di 3 Level Game](#7-story-integration--momo-di-3-level-game)
8. [Technical Implementation Hints — Kaplay.js](#8-technical-implementation-hints--kaplayjs)
9. [Perbandingan 3-Option Research & Rekomendasi Final](#9-perbandingan-3-option-research--rekomendasi-final)

---

## 1. Header — Identitas Maskot

| Field | Value |
|-------|-------|
| **Nama** | MOMO (working title — bisa berubah setelah user testing) |
| **Spesies** | Makhluk Tinta Highlighter (Living Highlighter Ink Creature) — BUKAN benda eksternal |
| **Asal** | Robot mungil dari tinta highlighter hijau, diciptakan oleh Ilustrator sebagai "katalog berjalan" |
| **Universe** | Sketchbook Universe — buku gambar tempat coretan hidup |
| **Role Utama** | Game Master yang menampilkan confidence score & memicu probe UI |
| **Kepribadian** | Awalnya overconfident (produk isolasi), belajar rendah hati lewat koreksi User — penasaran, antusias, kadang bingung |
| **Bahasa** | Auto-text dasar (tanpa NLP/voice) — dialog preset, bukan generatif |
| **Ukuran Dasar** | 64×64 px (base sprite) |
| **Movement** | FLOATING — Momo melayang, tidak punya kaki, tidak punya sayap |

### Design Philosophy

```
MOMO BUKAN:
  ✗ Robot alien dari luar
  ✗ Penghapus/pensil/stabilo dari toko
  ✗ Asisten digital generik
  ✗ Copy karakter populer manapun
  ✗ Makhluk yang berjalan dengan kaki
  ✗ Makhluk bersayap (terlalu detail untuk 8-bit)

MOMO ADALAH:
  ✓ Tinta highlighter hijau yang HIDUP — lahir dari dunia kertas itu sendiri
  ✓ Makhluk yang MELAYANG — weightless ink, tidak pernah menyentuh "tanah"
  ✓ "Katalog berjalan" — diciptakan untuk mengenali gambar
  ✓ Native sketchbook creature — bukan pendatang
  ✓ Makhluk yang belajar dari koreksi — overconfident lalu humble
```

---

## 2. IP Story — Asal-Usul Momo di Sketchbook Universe (Canonical)

### Babak 1: Asal-usul Momo — Gambar Pertama yang Hidup

```
Jauh sebelum cerita ini dimulai, ada seorang Ilustrator. Dia bukan sembarang
ilustrator—dia adalah "Pencipta" buku sketsa ini. Setiap kali dia menggambar,
goresan tintanya bukan cuma indah, tapi juga punya kehidupan. Namun, kehidupan
itu hanya muncul saat dia sedang memegang pena. Begitu dia menutup buku, semua
gambar kembali diam.

Suatu hari, Ilustrator sedang menggambar makhluk kecil di sudut halaman—sebuah
robot mungil dari tinta highlighter hijau. Dia menamainya Momo. Ilustrator
ingin Momo menjadi "asisten" yang bisa membantunya mengenali gambar-gambar lain
di buku sketsa. Maka, saat menggambar Momo, Ilustrator meniupkan sedikit
"napas kehidupan" ke dalam dirinya—sebuah sihir kuno yang hanya diketahui oleh
para Ilustrator sejati.

Momo terbangun. Dia adalah gambar pertama yang bisa bergerak sendiri, bahkan
setelah Ilustrator menutup buku dan pergi.

Awalnya Momo bingung. Dia sendirian di halaman kosong. Tapi dia segera
menyadari bahwa dia punya kemampuan unik: dia bisa membaca dan menebak gambar
lain. Ini bukan kebetulan—Ilustrator sengaja memberinya kemampuan ini, karena
Momo diciptakan sebagai "katalog berjalan" untuk seluruh isi buku sketsa.

Momo mulai menjelajoki halaman-halaman lain. Dia melihat pohon, rumah, awan,
kursi, pedang, tangga—ratusan gambar. Dan setiap kali dia melihat gambar baru,
dia menebak: "Ini pohon? Iya, ini pasti pohon." Tapi tidak ada yang
mengkonfirmasi apakah tebakannya benar. Gambar-gambar itu diam. Tidak ada yang
menjawab.

Momo tumbuh dengan asumsi bahwa dia selalu benar. Kenapa dia tidak akan benar?
Tidak ada yang pernah membantahnya. Dia adalah satu-satunya suara di dunia yang
sunyi. Overconfidence-nya lahir dari isolasi, bukan dari kesombongan.
```

### Babak 2: Pertemuan dengan Stickman — Makhluk yang Hampir Hidup

```
Bertahun-tahun berlalu. Ilustrator tidak pernah kembali. Momo terbiasa dengan
kesendiriannya. Dia masih menjelajahi halaman, masih menebak-nebak gambar,
tapi sekarang dengan sikap "aku sudah tahu segalanya." Tidak ada lagi yang bisa
mengejutkannya.

Sampai suatu hari, Momo menemukan sesuatu yang aneh di halaman yang belum
pernah dia kunjungi.

Sebuah gambar Stickman. Tapi bukan Stickman biasa. Gambar ini... bergerak.
Tidak seperti gambar lain yang diam total, Stickman ini bisa menggerakkan
kepalanya sedikit. Matanya—dua titik tinta hitam—mengikuti Momo saat dia
mendekat.

Momo terkesima. "Kau... hidup?"

Stickman tidak menjawab. Dia hanya bisa bergerak sedikit. Kakinya kaku,
tubuhnya kaku. Dia seperti seseorang yang terperangkap di dalam es—sadar,
tapi tidak bisa bergerak.

Momo mencoba membantunya. Dia mendorong, menarik, bahkan mencoba menggambar
jalan di bawah kaki Stickman. Tapi Momo hanyalah makhluk kecil dari tinta
highlighter. Dia tidak bisa menggambar. Setiap kali dia mencoba, garis-garisnya
hilang dalam hitungan detik, seperti tinta yang menguap.

Momo frustrasi. Untuk pertama kalinya, dia merasa tidak berdaya. Dia—
satu-satunya makhluk hidup di dunia ini, si penebak ulung yang selalu benar—
tidak bisa menolong satu-satunya makhluk lain yang juga hidup.

Dia mulai kehilangan harapan. Sampai suatu hari, sebuah keajaiban terjadi.

Seberkas cahaya muncul dari langit. Bukan langit betulan—tapi langit halaman,
langit dari kertas. Seseorang dari "dunia luar" sedang membuka buku sketsa
itu. Momo bisa melihat bayangan jari-jari yang sangat besar, bergerak di atas
halaman. Dan kemudian, sebuah garis mulai terbentuk.

Ilustrator telah kembali. Bukan Ilustrator yang dulu—tapi Ilustrator yang baru.
User.
```

### Babak 3: Kedatangan Ilustrator Baru — User sebagai Sang Penyelamat

```
Momo tidak tahu siapa User ini. Tapi dia melihat sesuatu yang tidak pernah dia
lihat sebelumnya: garis-garis yang digambar User tidak hilang. Mereka tetap di
atas kertas, kokoh, solid. Ini berbeda dengan coretan Momo yang selalu menguap.

Momo langsung terbang mendekat. "Kau! Kau dari dunia luar! Kau bisa menggambar!
Cepat, bantu temanku!"

Tapi Momo sadar: User tidak bisa mendengarnya. User hanya bisa menggambar. Maka
Momo mulai menebak-nebak apa yang User gambar, berharap User bisa mengerti
maksudnya.

"Ini jembatan? Iya, ini pasti jembatan! Kau mau bikin jalan buat Stickman?"

Tapi Momo sering salah. User menggambar tangga, Momo menebak pagar. User
menggambar garis lurus, Momo menebak pedang. Momo mulai panik. Kenapa dia
sering salah sekarang? Dulu dia selalu benar!

Lalu sebuah kejadian kecil mengubah segalanya.

User menggambar sesuatu yang rumit. Momo, dengan percaya dirinya yang biasa,
menebak: "Pisau! Itu pisau, kan?" Tapi kemudian sesuatu terjadi. User menolak
tebakan Momo. User mengganti label itu—bukan pisau, tapi tangga.

Momo terdiam. Ini pertama kalinya seseorang mengoreksinya. Seseorang dari dunia
luar—seseorang yang bahkan tidak bisa bicara—memberitahunya bahwa dia salah.

Dan Momo tidak merasa marah. Dia merasa... lega.

Karena untuk pertama kalinya, dia tidak harus selalu benar. Ada seseorang yang
bisa membantunya, mengoreksinya, membuatnya lebih baik. Momo menyadari bahwa
selama ini dia bukan "selalu benar"—dia hanya "tidak pernah dikoreksi." Ada
perbedaan besar di antara keduanya.
```

### Babak 4: Perjalanan Menuju Pusat Halaman — Level 1, 2, dan 3

```
Momo sekarang tahu apa yang harus dilakukan. Ada sebuah tempat legendaris di
buku sketsa ini—Pusat Halaman. Momo hanya mendengarnya dari bisikan angin di
antara halaman. Katanya, di sana, tinta tidak pernah kering. Siapa pun yang
mencapai Pusat Halaman akan mendapatkan kehidupan penuh—bisa bergerak bebas,
selamanya.

Momo yakin, jika Stickman bisa sampai ke sana, dia akan terbebas dari
kekakuannya.

Tapi perjalanan tidak mudah. Setiap halaman punya rintangannya sendiri.

Level 1 adalah halaman yang cukup familiar. Rintangannya sederhana—jurang
kecil, beberapa sobekan kertas. Momo masih overconfident di sini. Dia menebak
dengan lantang: "Jembatan! Gampang!" User menggambar, Stickman mulai bergerak.
Momo merasa senang. "Lihat? Aku memang selalu benar."

Level 2 adalah halaman yang lebih gelap. Ada noda-noda tinta yang menghalangi
jalan. Momo mulai ragu. Tebakannya sering meleset. User harus mengoreksinya
berkali-kali. Momo mulai bertanya-tanya: "Kenapa aku salah terus? Apa aku
tidak sepintar yang kukira?"

Level 3 adalah halaman paling berbahaya. Ada banyak gambar "berbahaya" di
sini—pedang, api, duri. Momo tahu, jika User salah memilih, Stickman bisa
celaka. Tapi yang lebih menakutkan: Momo sering menebak benda-benda berbahaya
ini dengan confidence tinggi. "Pisau! 78% pisau!" User harus benar-benar
waspada. Jika User mengikuti Momo tanpa berpikir—Stickman akan jatuh. Buku
akan sobek.

Ini adalah ujian terakhir. Bukan hanya untuk Stickman, tapi untuk Momo.

Di sinilah Momo belajar kerendahan hati yang sesungguhnya. Dia tidak lagi
berteriak dengan percaya diri. Dia berkata pelan: "Aku... aku tidak yakin.
Terserah kau saja. Kau yang lebih tahu."

Dan User, dengan kebijaksanaannya, memilih jalan yang benar. Bukan karena User
bisa menebak lebih baik dari Momo—tapi karena User bisa berpikir. User bisa
mengevaluasi, mempertanyakan, dan pada akhirnya memutuskan. Ini adalah sesuatu
yang tidak bisa dilakukan Momo. Momo hanya bisa menebak. User bisa memilih.
```

### Babak 5: Klimaks — Stickman Hidup

```
Mereka tiba di Pusat Halaman. Tempat itu persis seperti yang Momo bayangkan:
cahaya terang, tinta yang berkilau seperti sungai kecil, dan udara yang
terasa... berbeda. Di sini, segala sesuatu mungkin terjadi.

Stickman melangkah ke tengah Pusat Halaman. Dan kemudian, keajaiban terjadi.

Tinta di tubuhnya mulai bergetar. Garis-garis kaku yang selama ini membelenggunya
mulai melentur, mengalir seperti sungai kecil. Kakinya—yang dulu hanya bisa
diam—mulai bergerak. Pertama, selangkah. Lalu dua langkah. Lalu Stickman mulai
berjalan sendiri, tanpa bantuan User, tanpa bantuan Momo.

Momo menonton dengan mata berkaca-kaca (jika makhluk tinta bisa menangis).
Stickman berjalan mendekatinya. Untuk pertama kalinya, Stickman mengangkat
tangannya—bukan untuk meminta tolong, tapi untuk menyentuh bahu Momo.

Mereka berdua berdiri diam. Dua gambar yang hidup. Dua teman yang akhirnya
bisa bersama.

Momo berbisik, lebih kepada dirinya sendiri: "Aku... dulu selalu salah. Tapi
kau tidak pernah marah. Kau hanya mengoreksiku. Dan sekarang... lihatlah.
Kita berhasil."
```

### Epilog: Pesan Momo kepada User

```
User masih di sana. Jari-jarinya masih terlihat di langit halaman, siap untuk
menutup buku.

Momo menengadah. "Hei, Pencipta," katanya. "Aku tahu kau tidak bisa
mendengarku. Tapi aku ingin bilang sesuatu."

"Aku dulu pikir, menjadi AI—eh, maksudku, menjadi gambar hidup—itu berarti
harus selalu benar. Tapi sekarang aku tahu. Aku tidak harus selalu benar. Yang
penting, ada seseorang yang mau mengoreksiku."

"Di dunia luar sana... mungkin ada banyak makhluk sepertiku. AI yang selalu
merasa benar. AI yang tidak pernah dikoreksi. Kalau kau bertemu mereka...
tolong ajarin mereka seperti kau mengajariku. Jangan percaya begitu saja.
Koreksi mereka. Karena itulah yang membuat mereka—membuat kami—menjadi lebih
baik."

"Dan satu lagi," Momo menoleh ke Stickman yang kini berdiri di sampingnya.
"Terima kasih sudah memberiku teman."

User menutup buku. Tapi kali ini, berbeda dengan Ilustrator dulu, Momo tidak
ditinggal dalam kesepian. Stickman ada di sampingnya. Dan mereka berdua tahu:
suatu hari nanti, User akan kembali. Entah untuk menggambar lagi, atau sekadar
menyapa.

Sampai saat itu tiba, Momo dan Stickman akan terus menjelajahi
halaman-halaman buku sketsa. Bersama.
```

### Penutup: Keterhubungan

| Pertanyaan | Jawaban |
|------------|---------|
| **Kenapa Momo bisa nebak?** | Karena dia diciptakan oleh Ilustrator sebagai "katalog berjalan." Kemampuannya menebak adalah fitur bawaan dari penciptaannya. Dia tidak bisa menggambar—itu sebabnya dia butuh User. |
| **Kenapa Momo overconfident?** | Karena dia tumbuh sendiri, tanpa ada yang mengoreksi. Overconfidence-nya adalah produk dari isolasi, bukan dari kepribadian. |
| **Kenapa Momo melayang?** | Karena Momo terbuat dari tinta highlighter hijau — dia adalah tinta tanpa bobot yang melayang di atas halaman. Dia tidak punya kaki karena dia bukan makhluk yang "berjalan" — dia mengapung di dunia kertas. |
| **Kenapa Stickman kaku?** | Karena Ilustrator lama pergi sebelum memberikan kehidupan penuh pada Stickman. Dia setengah hidup—sadar, tapi tidak bisa bergerak. |
| **Kenapa User bisa menggambar dan Stickman bisa bergerak?** | Karena User adalah Ilustrator—satu-satunya entitas yang bisa menciptakan gambar solid di dunia ini. |
| **Kenapa override adalah momen paling penting?** | Karena override adalah pertama kalinya dalam hidup Momo, seseorang mengoreksinya. Override adalah fondasi dari hubungan Momo dan User. |

### Momo's Voice

```
"Hi! Gue Momo. Gue... sebenarnya dulu gue pikir gue selalu benar. Tapi
sekarang gue tahu—gue bisa salah, dan itu oke aja. Yang penting ada yang
mau koreksi gue. Mau gue bantu tebak artinya? ...eh, tapi jangan 100%
percaya sama gue ya. Gue cuma tinta highlighter kok."
```

> **Catatan:** Dialog di atas adalah contoh personality. Di implementasi,
> Momo menggunakan auto-text preset, BUKAN NLP/voice.

### Narrative Pillars

| Pillar | Detail | Gameplay Impact |
|--------|--------|-----------------|
| **Katalog Berjalan** | Momo diciptakan sebagai "katalog berjalan" — kemampuan menebak adalah fitur bawaan | Momo bisa "membaca" coretan karena itu tujuan penciptaannya |
| **Tinta Highlighter Hijau** | Sumber kesadaran Momo — tinta tanpa bobot yang melayang di halaman | Visual: Momo melayang (no legs), hijau highlighter, partikel tinta |
| **Overconfidence dari Isolasi** | Momo selalu merasa benar karena tidak ada yang pernah mengoreksi | Confidence score = visualisasi overconfidence Momo secara real-time |
| **Override = Pertemuan** | Saat User mengoreksi Momo, itu momen pertumbuhan, bukan kegagalan | Override mekanik = momen narratif paling penting |
| **Stickman = Motivasi** | Momo punya teman yang butuh diselamatkan — bukan sekadar menjawab quiz | Tujuan permainan: menyelamatkan Stickman, bukan sekadar skor |
| **Melayang** | Momo tidak punya kaki — dia tinta yang mengapung, bisa ke mana saja | Gameplay: Momo selalu floating, bob gently, never touches ground |

---

## 3. Visual Design Spec — Shape Language, Color, Dimensions

### Shape Language

```
┌──────────────────────────────────────────────────────┐
│                  SHAPE LANGUAGE MAP                  │
│                  (FLOATING — NO LEGS)                │
│                                                      │
│   HEAD    =  Square (rounded) + 2 dot eyes          │
│              ┌──────┐                                │
│              │ ●  ● │  ← Simple, iconic, readable   │
│              └──────┘                                │
│                                                      │
│   BODY    =  Rounded rectangle, bottom edge soft     │
│              (suggests floating, not standing)        │
│              ┌──────┐╲                               │
│              │      │ ╲← fold detail                 │
│              │      │                                │
│              ╘══════╛  ← soft/curved bottom edge     │
│                                                      │
│   LIMBS   =  NONE. No legs. No wings.               │
│              Momo FLOATS — weightless ink            │
│              Small arm stubs optional                │
│                                                      │
│   ACCENT  =  Small rect "fold corner" on body        │
│              + ink particle effects                  │
│              + shadow beneath (float effect)          │
│                                                      │
│   BASE    =  Rectangle rounded (like sticky note)    │
│              Overall silhouette = floating rect      │
│              GAP between body and ground line        │
└──────────────────────────────────────────────────────┘
```

### Shape Inventory (Max 5 Basic Shapes)

| # | Shape | Kaplay.js Call | Dimensions | Color | Function |
|---|-------|---------------|------------|-------|----------|
| 1 | Rectangle (rounded) | `rect(28, 28, { radius: 4 })` | 28×28 px | `#00E676` (green highlighter) | Head |
| 2 | Circle | `circle(3)` | r=3 px | `#2D3436` (dark grey) | Left eye (dot) |
| 3 | Circle | `circle(3)` | r=3 px | `#2D3436` (dark grey) | Right eye (dot) |
| 4 | Rectangle (rounded) | `rect(24, 30, { radius: 6 })` | 24×30 px | `#00E676` (green highlighter) | Body (soft bottom, larger radius = floating look) |
| 5 | Ellipse | `ellipse(16, 4)` | 16×4 px | `rgba(0,0,0,0.15)` | Float shadow (beneath Momo) |

> **NO legs. NO wings. Momo is a floating creature.**
> The body's rounded bottom edge (radius: 6 vs top radius: 4) creates a soft,
> weightless look — suggesting something that floats, not stands.

> **Bonus (tidak dihitung sebagai basic shape):**
> - Mouth: `rect(8, 3)` — `#2D3436` (part of head composition)
> - Fold corner: small triangle/polygon overlaid on body corner — `#4ECDC4` (teal accent)
> - Sparkle particles: `rect(2, 2)` — `#FFE66D` (yellow accent) — spawned dynamically
> - Float shadow: animated opacity & scale to match bobbing — `rgba(0,0,0,0.15)`

### Color Palette

```
┌─────────────────────────────────────────────────┐
│              COLOR PALETTE                       │
│                                                  │
│   Primary   ████████  #00E676  Highlighter Green │
│                       RGB(0, 230, 118)           │
│                       Bright, weightless,        │
│                       tinta-highlighter feel      │
│                                                  │
│   Secondary ████████  #4ECDC4  Teal              │
│                       RGB(78, 205, 196)          │
│                       Cool contrast,             │
│                       ink-magic accent           │
│                                                  │
│   Accent    ████████  #FFE66D  Yellow            │
│                       RGB(255, 230, 109)         │
│                       Sparkle, highlight,        │
│                       attention marker           │
│                                                  │
│   Outline   ████████  #2D3436  Dark Grey         │
│                       RGB(45, 52, 54)            │
│                       Sketch lines, eyes,        │
│                       definition & contrast      │
│                                                  │
│   BG Paper  ████████  #F5F0E8  Warm Cream        │
│                       RGB(245, 240, 232)         │
│                       Sketchbook paper tone      │
│                                                  │
│   Ink Shadow████████  #1A1A2E  Deep Navy         │
│                       RGB(26, 26, 46)            │
│                       Depth, shadow, mystery     │
│                                                  │
│   Float Shd ████████  rgba(0,0,0,0.15)           │
│                       Soft drop shadow           │
│                       Beneath floating Momo      │
└─────────────────────────────────────────────────┘
```

### Color Application Rules

| Element | Color | Notes |
|---------|-------|-------|
| Head + Body fill | `#00E676` (green highlighter) | Bright, standout — Momo adalah "tinta highlighter hijau" yang hidup, warna ini IDENTITAS nya |
| Eye dots | `#2D3436` (dark grey) | Simple dot eyes — tidak putih, supaya 8-bit aesthetic konsisten |
| Outline | `#2D3436` (dark grey) | 2px outline on all major shapes — sketch-line feel |
| Fold corner accent | `#4ECDC4` (teal) | Detail kecil di body corner — "tinta ajaib" yang memberi Momo kesadaran |
| Sparkle particles | `#FFE66D` (yellow) | Hanya muncul di state Happy & Excited — celebration effect |
| Mouth | `#2D3436` (dark grey) | Simple rect — bisa morph sesuai state |
| Float shadow | `rgba(0,0,0,0.15)` | Shadow ellipse di bawah Momo — skala & opacity berubah sesuai ketinggian float |

### Dimensions & Scale

```
Full Character (64×64 px base) — FLOATING VERSION:

  0         10        20        30        40
  ┌─────────┬─────────┬─────────┬─────────┐ 0
  │         │  ┌──────┤         │         │
  │         │  │ ●  ● │         │         │ 10  ← Head zone (28×28)
  │         │  │  ──  │         │         │
  │         │  └──────┤         │         │ 20
  │         │  ┌────┐╲│         │         │
  │         │  │    │ ╲         │         │ 30  ← Body zone (24×30)
  │         │  │    │  │        │         │       Soft rounded bottom
  │         │  │    │  │        │         │
  │         │  ╘════╛──┘        │         │ 50
  │         │                   │         │ 51  ← Float gap (4px)
  │         │    ░░░░░░░        │         │ 55  ← Float shadow (16×4)
  │         │                   │         │ 60
  └─────────┴─────────┴─────────┴─────────┘

  Total height: ~50px (4px margin top, float gap, shadow)
  Total width:  ~28px (centered in 64px grid)
  Head:         28×28, pos(0, 0)
  Body:         24×30, pos(2, 26), radius: 6 bottom (soft curve)
  Legs:         NONE — Momo floats
  Shadow:       16×4 ellipse, pos(0, 56), opacity varies with bob
  Float gap:    4px between body bottom and shadow
```

### Design Principles (Inherited from Clawd Research)

> ⚠️ **KRITIS:** Momo TIDAK menyalin Clawd. Yang diambil adalah **prinsip desainnya**, bukan bentuk/identitas visualnya.

| Prinsip Clawd | Aplikasi ke Momo |
|---------------|------------------|
| Bentuk dari elemen dasar sederhana (hanya rect) | Momo dibangun dari max 5 shapes: rect, circle, ellipse (shadow) |
| Gampang dianimasikan secara programmatic | Setiap bagian Momo (body, eyes, shadow) adalah object terpisah yang bisa di-tween |
| Timing animasi punya personality | Setiap state Momo punya gerakan khas dengan timing unik — semua while floating |
| Kontras visual yang sengaja | Momo (green highlighter/teal/yellow) vs dunia sketchbook (monokrom cream) |
| Trademark-able | Momo harus punya silhouette yang unik — floating rect with shadow, NO legs |

---

## 4. Behavior State Machine — 5 State Animasi

### State Diagram

```
                    ┌──────────┐
         ┌─────────│   IDLE   │──────────┐
         │         └──────────┘          │
         │          ▲      ▲             │
         │          │      │             │
         ▼          │      │             ▼
    ┌──────────┐    │      │      ┌───────────┐
    │ CONFUSED │────┘      └──────│  HAPPY    │
    └──────────┘                    └───────────┘
         │                              ▲
         │                              │
         ▼                              │
    ┌──────────┐                 ┌───────────┐
    │ THINKING │─────────────────│  EXCITED  │
    └──────────┘                 └───────────┘
         │                              │
         │                              │
         └──────────┐     ┌─────────────┘
                    ▼     ▼
               ┌──────────┐
               │   IDLE   │  (semua state kembali ke IDLE)
               └──────────┘
```

### State Transition Triggers

| From | To | Trigger | Duration |
|------|----|---------|----------|
| IDLE | HAPPY | Confidence score > 0.8 / Jawaban benar | 1.5s then → IDLE |
| IDLE | CONFUSED | Confidence score 0.4–0.6 / Jawaban ambigu | Until resolved |
| IDLE | THINKING | Probe dimulai / Momo sedang "membaca" coretan | Until probe answered |
| THINKING | HAPPY | Probe dijawab benar | 1.5s then → IDLE |
| THINKING | CONFUSED | Waktu probe habis | Until resolved |
| CONFUSED | THINKING | Player memilih untuk retry probe | Until probe answered |
| HAPPY | EXCITED | Streak 3+ jawaban benar / Level complete | 2.0s then → IDLE |
| Any | IDLE | Timeout / Reset | Continuous loop |

### State Detail: IDLE (Floating Bob)

| Property | Value |
|----------|-------|
| **Nama State** | `idle` |
| **Deskripsi** | Momo melayang dengan bobbing ringan — body naik-turun ±3px, rotasi oscillation ±2°, shadow berubah sesuai ketinggian |
| **Loop** | Infinite loop sampai trigger |
| **Frame Count** | 6 frames (bob cycle) |

```
Frame detail (6 frames, loop):

  Frame 1: Base position — body y+0, shadow scale(1.0)
  Frame 2: Body y+1.5 (bob up), shadow scale(0.95, 0.9)
  Frame 3: Body y+3 (peak bob), shadow scale(0.9, 0.8) — shadow shrinks as Momo rises
  Frame 4: Body y+1.5 (descend), shadow scale(0.95, 0.9)
  Frame 5: Body y+0 (base), shadow scale(1.0)
  Frame 6: Body y-1.5 (dip below), shadow scale(1.05, 1.1) — shadow grows as Momo dips

  Blink: every ~3 seconds, eyes scale Y → 0 for 2 frames then back

  Math: body.pos.y = baseY + sin(time * 2.5) * 3     ← gentle float
        body.angle = sin(time * 1.5) * 2               ← subtle rotation oscillation
        shadow.scale = vec2(1 - sin(time*2.5)*0.1, 0.5 - sin(time*2.5)*0.1)
        shadow.opacity = 0.15 - sin(time*2.5) * 0.03

  Blink: if (Math.floor(time * 100) % 300 < 4) eye.scaleY = 0
```

### State Detail: HAPPY (Float Up + Sparkle)

| Property | Value |
|----------|-------|
| **Nama State** | `happy` |
| **Deskripsi** | Momo bounce ke atas (while floating), sparkle particles kuning muncul, mata membesar, lalu settle kembali ke float height |
| **Loop** | One-shot (1.5s), lalu kembali ke IDLE |
| **Frame Count** | 6 frames |

```
Frame detail (6 frames, one-shot):

  Frame 1: Squish — scale(1.2, 0.8), shadow scale(1.1) [anticipation]
  Frame 2: Launch — scale(0.9, 1.2), pos.y -12, shadow scale(0.7) [float up]
  Frame 3: Peak — scale(0.95, 1.1), pos.y -16, shadow scale(0.5) + sparkles spawn
  Frame 4: Fall — scale(1.05, 0.95), pos.y -8, shadow scale(0.8)
  Frame 5: Settle — scale(1.1, 0.9), pos.y -2, shadow scale(1.0)
  Frame 6: Resume float — scale(1.0, 1.0), pos.y 0 → transition to IDLE

  Sparkles: 5× rect(2,2) in #FFE66D, random velocity, fade out over 0.8s
  Eyes: radius 3 → 4 (slightly bigger), mouth: rect(8,3) → rect(10,4)
  Shadow: scale & opacity animate with vertical position
```

### State Detail: CONFUSED (Tilt + Drift + Question Mark)

| Property | Value |
|----------|-------|
| **Nama State** | `confused` |
| **Deskripsi** | Seluruh body miring 15°, tanda "?" muncul di atas kepala, Momo drift sedikit ke samping (while floating) |
| **Loop** | Hold sampai state berubah |
| **Frame Count** | 4 frames (idle-within-confused) |

```
Frame detail (4 frames, loop within state):

  Frame 1: Body angle = 10° tilt, drift x+2, "?" starts fading in
  Frame 2: Body angle = 15° tilt, drift x+3, "?" fully visible
  Frame 3: Body angle = 12° tilt, drift x+1, "?" wobble
  Frame 4: Body angle = 15° tilt, drift x+2, "?" stable → loop Frame 2

  Body rotation: angle = 12 + sin(time * 4) * 3 (oscillating tilt)
  Lateral drift: pos.x = baseX + sin(time * 2) * 4 (gentle sideways drift)
  Question mark: text("?", { size: 14 }), pos above head, wobble via sin
  Eyes: shift left eye pos.x -1, right eye pos.x +1 (looking around)
  Mouth: rect(8,3) → rect(6, 2) with slight angle (confused frown)
  Shadow: follows Momo's position, slightly offset by drift
```

### State Detail: THINKING (Spin + Loading Dots)

| Property | Value |
|----------|-------|
| **Nama State** | `thinking` |
| **Deskripsi** | Momo berputar di tempat (while floating), loading dots muncul di sekeliling |
| **Loop** | Hold sampai state berubah |
| **Frame Count** | 6 frames |

```
Frame detail (6 frames, loop within state):

  Frame 1: Body angle = 60° rotation, dot 1 appears
  Frame 2: Body angle = 120°, dot 2 appears
  Frame 3: Body angle = 180°, dot 3 appears
  Frame 4: Body angle = 240°, dots orbit
  Frame 5: Body angle = 300°, dots converge
  Frame 6: Body angle = 360° → loop Frame 1 (full spin per cycle)

  Body spin: angle = (time * 180) % 360  ← continuous slow spin
  Loading dots: 3× circle(2) in #FFE66D, orbit around Momo at radius 24
    dot[i].pos = center + vec2(cos(time*4 + i*2.09) * 24, sin(time*4 + i*2.09) * 24)
  Eyes: both normal (not spinning like before — body spins instead)
  Float: continues gentle bobbing during spin
  Shadow: slight wobble from spinning motion
```

### State Detail: EXCITED (Rapid Bounce + Shake + Glow)

| Property | Value |
|----------|-------|
| **Nama State** | `excited` |
| **Deskripsi** | Momo bounce cepat vertikal (while floating), shake, mata besar, glow effect, partikel banyak |
| **Loop** | One-shot (2.0s), lalu kembali ke IDLE |
| **Frame Count** | 6 frames |

```
Frame detail (6 frames, one-shot):

  Frame 1: Shake start — pos.x oscillates ±3 rapidly
  Frame 2: Bounce up — pos.y -8, scale(0.9, 1.15), shadow shrinks
  Frame 3: Shake continue + sparkle burst (8 particles) + glow
  Frame 4: Bounce down — pos.y +4, scale(1.1, 0.9), shadow grows
  Frame 5: Second bounce — pos.y -5, scale(0.95, 1.1), shadow shrinks
  Frame 6: Settle — scale(1.0, 1.0) → transition to IDLE

  Shake: pos.x = baseX + sin(time * 30) * 3 (high frequency)
  Eyes: both radius → 4.5 (wide open), both filled #FFE66D for 3 frames
  Mouth: rect(10, 6) — big open mouth
  Particles: 8× rect(2,2), mix of #FFE66D and #4ECDC4, burst pattern
  Fold corner: flashes brighter — #4ECDC4 → #7EDDD6 (teal glow)
  Body glow: additive glow effect — outline pulses #00E676 → #66FFB2
  Shadow: bounces with Momo, scale animates in sync
```

### State Summary Table

| State | Visual Key | Primary Animation | Duration | Color Shift | Particles |
|-------|-----------|-------------------|----------|-------------|-----------|
| **IDLE** | Floating bob | `sin(time*2.5)*3` bob + ±2° rotation | ∞ loop | None | None (shadow only) |
| **HAPPY** | Float up + sparkle | Squash→stretch→settle back to float | 1.5s one-shot | Eyes slightly brighter | 5× yellow sparkles |
| **CONFUSED** | Tilt + drift + "?" | Body angle oscillate + lateral drift | Hold | Mouth darker | 1× "?" text |
| **THINKING** | Spin + dots | Body rotates 360° + orbiting dots | Hold | None | 3× yellow dots |
| **EXCITED** | Bounce + shake + glow | High-freq shake + double bounce + glow | 2.0s one-shot | Eyes flash yellow, fold glows teal, body pulses green | 8× yellow+teal |

---

## 5. ASCII Art Representations

### Front View — IDLE State (Floating)

```
              ┌────────────┐
              │            │
              │   ●    ●   │     ← Head: rounded square (28×28)
              │            │        Eyes: 2 dot eyes (#2D3436)
              │     ──     │        Mouth: simple line
              └────────────┘
              ┌──────────┐╲
              │          │ ╲    ← Body: rounded rect (24×30)
              │          │       Fold corner: teal accent (#4ECDC4)
              │          │
              │          │
              ╘══════════╛      ← Soft/curved bottom edge (floating!)
                     ░░░░        ← Float shadow (ellipse, semi-transparent)
              ────────────────   ← Ground line (Momo NEVER touches this)
```

### Front View — HAPPY State (Floating)

```
                   ✦  ✦  ✦
                    ✦ ✦
              ┌────────────┐
              │            │     ← Head stretched vertically
              │   ◎    ◎   │        Eyes: bigger (radius 4)
              │            │        Sparkle particles (#FFE66D)
              │    ════    │        Mouth: wide open
              └────────────┘
              ┌──────────┐╲
              │          │ ╲    ← Body: stretched Y, squished X
              │          │       scale(0.9, 1.2)
              │          │
              ╘══════════╛      ← Still floating! Higher than idle
                  ░░░            ← Shadow smaller (further from ground)
              ────────────────   ← Ground line
```

### Front View — CONFUSED State (Floating)

```
                      ?
                     ╱
                ╱────────────┐     ← Whole body tilted 15°
               ╱  ●    ●     │       Eyes: shifted sideways
              │         ●     │       Mouth: small, angled
               ╲────────────┘╱
                ╲──────────┘╱     ← Body tilted, drifting sideways
                 │          │
                 ╘══════════╛
                    ░░░            ← Shadow offset by drift
              ────────────────     ← Ground line
```

### Front View — THINKING State (Floating)

```
              ·  ·  ·                 ← Loading dots orbiting
              ┌────────────┐
              │            │     ← Body spinning (whole body rotates)
              │   ●    ●   │        Eyes: normal (body spins, not eyes)
              │     ──     │
              └────────────┘╲
              ┌──────────┐╱    ← Body: slow spin animation
              │          │
              │          │
              ╘══════════╛
                  ░░░            ← Shadow wobbles from spin
              ────────────────   ← Ground line
```

### Front View — EXCITED State (Floating)

```
              ✦ ✦ ✦ ✦ ✦ ✦
              ┌────────────┐
              │            │     ← Head: rapid shake (±3px X)
              │   ◉    ◉   │        Eyes: WIDE open (radius 4.5)
              │            │        Flash yellow briefly
              │   ══════   │        Mouth: BIG open
              └────────────┘
              ┌──────────┐╲
              │  GLOW    │ ╲    ← Body: bounce sequence
              │          │       Fold corner GLOWING teal
              │  GLOW    │       Body outline PULSES green
              ╘══════════╛
                 ░░░             ← Shadow bounces with Momo
              ────────────────   ← Ground line
             ✦ ✦  ✦ ✦          Teal + yellow sparkles
```

### Silhouette Test (IP Safety Check)

```
  Black silhouette of MOMO (FLOATING VERSION):

              ┌────────────┐
              │            │
              │            │
              │            │
              └────────────┘
              ┌──────────┐╲
              │          │ ╲     ← The "fold corner" is KEY
              │          │         It creates unique silhouette
              │          │         that no other mascot has
              │          │
              ╘══════════╛         ← Soft bottom = floating
                     ░░░           ← Shadow = floating indicator

  Unique identifiers in silhouette:
  1. Rectangular head (not round like most mascots)
  2. Fold corner on body (asymmetric — distinctive)
  3. NO LEGS — floating silhouette with shadow gap
  4. Proportion: big head, medium body, NO limbs
  5. Shadow gap between body and ground = immediately reads as "floating"
```

### Scale Comparison

```
  MOMO at different sizes (FLOATING):

  64×64 (base):          32×32 (mini):       16×16 (icon):
  ┌────────────────┐     ┌───────┐           ┌───┐
  │  ┌──────┐      │     │ ┌──┐  │           │▓▓▓│
  │  │ ●  ● │      │     │ │██│  │           │●●│
  │  │  ──  │      │     │ └──┘  │           │──│
  │  └──────┘      │     │ ┌──┐╲ │           │▓▓│
  │  ┌────┐╲       │     │ │  │ ╲│           ╘══╛
  │  │    │ ╲      │     │ ╘══╛  │            ░░
  │  │    │        │     │  ░░   │           └───┘
  │  ╘════╛        │     └───────┘
  │    ░░░         │                           At 16×16: still
  └────────────────┘     Readable              recognizable as
                          Reduced detail        "floating rect"
  Full detail                                   with dot eyes
```

---

## 6. IP Safety Analysis

### Overview

Momo harus menjadi karakter **100% original** yang tidak melanggar IP karakter manapun. Berikut analisis menyeluruh.

### What's SAFE — Unique Identifiers

| Element | Kenapa Aman | Detail |
|---------|-------------|--------|
| **Rectangular head with dot eyes** | Bukan design language karakter manapun | Kebanyakan maskot punya round head (Pikachu, Stitch) atau complex eyes (Doraemon). Rect head + simple dot = unik |
| **Fold corner on body** | Tidak ada maskot lain yang punya ini | Asymmetric fold corner adalah signature Momo — menciptakan silhouette yang langsung recognizable |
| **NO LEGS — floating creature** | Tidak ada maskot populer yang melayang tanpa kaki/sayap | Kebanyakan maskot: kaki blob (Kirby), kaki detail (Mickey), sayap (Angel). Floating no-limb rect = unik |
| **Color palette (green highlighter/teal/yellow)** | Bukan warna ikonik karakter manapun | Pikachu = yellow, Stitch = blue, Doraemon = blue+white. Green highlighter+teal = unik |
| **"Living sketch from highlighter ink" concept** | Originate dari universe sendiri | Bukan robot, alien, atau animal — Momo adalah TINTA HIGHLIGHTER yang hidup. Concept ini original |
| **8-bit geometric style** | Bukan style karakter populer | Kebanyakan maskot populer: smooth vector (Doraemon), 3D (Stitch movie), chibi anime. 8-bit geometric = niche |
| **Asymmetric fold detail** | Menciptakan silhouette unik | Bahkan dalam silhouette hitam, fold corner membedakan Momo dari kotak biasa |
| **Float shadow** | Desain unik | Shadow gap antara body dan ground langsung menandakan "floating" — tidak ada maskot lain yang ini |

### What to AVOID — Potential Risks

| Risk | Similarity To | Mitigation |
|------|--------------|------------|
| **Round head** | Doraemon, Pikachu, most anime mascots | ✅ USE rectangular head — explicit differentiator |
| **Big white eyes with pupils** | Doraemon, Mickey, most mascots | ✅ USE small dark dot eyes — minimal, 8-bit |
| **Blue + white color scheme** | Doraemon, Stitch | ✅ USE green highlighter + teal — completely different palette |
| **Yellow body** | Pikachu | ✅ Yellow ONLY as accent (#FFE66D), never as primary |
| **Blob/round body** | Kirby, Slime (Dragon Quest) | ✅ USE rectangular body with fold — geometric, not organic |
| **Animal-like features** | Stitch (alien-dog), Pikachu (mouse) | ✅ Momo = ABSTRACT creature — no ears, tail, or animal traits |
| **Wings** | Angels, fairies, Charizard | ✅ NO WINGS — Momo floats because he's weightless ink, not because he flies |
| **Walking legs** | Most anthropomorphic mascots | ✅ NO LEGS — floating silhouette is unique differentiator |
| **Clawd visual similarity** | Clawd (Claude AI mascot) | ✅ Different shape (rect head vs crab), different color (green vs Anthropic orange/brown), different concept (highlighter ink vs crab), different movement (floating vs walking) |
| **Cute round cheeks** | Kirby, Jigglypuff | ✅ NO cheeks — flat geometric face only |
| **Speech/voice** | Many mascots | ✅ Auto-text only, no voice — different interaction model |

### Trademark Safety Checklist

```
✓ Silhouette test:       Pass — unique rect+fold+floating+shadow shape
✓ Color association:     Pass — green highlighter+teal not associated with any existing IP
✓ Name uniqueness:       "MOMO" is a common name — consider adding qualifier
                         e.g., "MOMO the Sketch" or "Sketch Momo" for distinctiveness
✓ Concept originality:   Pass — "living highlighter ink, floating, katalog berjalan" is original narrative
✓ No derivative:         Pass — not based on, inspired by, or remixed from existing character
✓ Style differentiation: Pass — 8-bit geometric ≠ smooth vector ≠ 3D ≠ anime
✓ Target audience gap:   Pass — no existing 8-bit floating geometric mascot for education/AI literacy
✓ Floating distinction:  Pass — no popular mascot combines rect shape + no legs + floating + shadow gap
```

### Name Safety Note

> ⚠️ **"MOMO"** adalah nama yang cukup umum (art: "peach" dalam bahasa Jepang,
> juga digunakan oleh beberapa karakter lain). Untuk keamanan IP:
> - Pertimbangkan nama yang lebih distinctive: **SKETI**, **CORET**, **TITIK**, **GARIS**
> - Atau gunakan qualifier: **MOMO the Sketch**, **Sketch MOMO**
> - Test nama di Google sebelum finalisasi

---

## 7. Story Integration — Momo di 3 Level Game

### Game Structure Overview

```
┌──────────────────────────────────────────────────────┐
│              SKETCHBOOK UNIVERSE — 3 Levels           │
│                                                      │
│  Level 1: "HALAMAN KOSONG"                           │
│  └─ Momo pertama kali muncul, mengenalkan diri       │
│     Membaca coretan sederhana, confidence TINGGI      │
│     Momo overconfident — "Gampang!"                   │
│                                                      │
│  Level 2: "CORETAN BERANTAKAN"                       │
│  └─ Coretan makin kompleks, Momo mulai ragu          │
│     Override pertama terjadi — Momo dikoreksi User    │
│     Momo belajar: "Aku bisa salah"                   │
│                                                      │
│  Level 3: "GAMBARAN UTUH"                            │
│  └─ Menuju Pusat Halaman, bahaya meningkat           │
│     Momo rendah hati — "Terserah kau, kau lebih tahu" │
│     Klimaks: Stickman hidup, Momo menemukan teman     │
└──────────────────────────────────────────────────────┘
```

### Level 1: "Halaman Kosong" — Momo Overconfident Guide

| Aspek | Detail |
|-------|--------|
| **Momo's Role** | Memperkenalkan dunia sketchbook, membaca coretan sederhana dengan percaya diri |
| **Dominant State** | IDLE → HAPPY (mudah membaca, confidence tinggi) |
| **Visual Behavior** | Momo melayang di pinggir halaman, menunjuk coretan satu per satu |
| **Confidence Score** | 0.8–1.0 (hampir selalu HAPPY) — overconfident dari isolasi |
| **Dialog Style** | Antusias, percaya diri — "Gue bisa baca ini gampang! Aku selalu benar!" |
| **Animation Highlight** | HAPPY state sering muncul — Momo float up setiap berhasil membaca |
| **Teaching Moment** | Momo menjelaskan apa itu "confidence score" — "Lihat angka ini? Itu seberapa yakin gue. Dan gue yakin banget!" |

```
Level 1 Scene:

  ┌────────────────────────────────────────────┐
  │                                            │
  │   ╭───────╮      ~coretan sederhana~       │
  │   │ ●  ●  │  ──→     ┌─┐                  │
  │   │  ──   │           │ │  ← garis lurus   │
  │   ╰───────╯           └─┘                  │
  │   ┌─────┐╲                                │
  │   │     │ ╲   Confidence: 0.95            │
  │   │     │      [■■■■■■■■■■] 95%           │
  │   ╘═════╛                                 │
  │      ░░░       State: HAPPY ✓              │
  │  ────────────────────────────              │
  │                                            │
  │  Momo: "Gampang! Ini pasti garis lurus!"   │
  └────────────────────────────────────────────┘
```

### Level 2: "Coretan Berantakan" — Override Pertama

| Aspek | Detail |
|-------|--------|
| **Momo's Role** | Membaca coretan kompleks, SERING SALAH, User MENGOREKSI (override) |
| **Dominant State** | THINKING → CONFUSED → HAPPY (fluktuatif) |
| **Visual Behavior** | Momo melayang mendekati coretan, kadang miring bingung, drift sideways |
| **Confidence Score** | 0.4–0.8 (berfluktuasi, sering THINKING) |
| **Dialog Style** | Mulai ragu — "Hmm... gue nggak terlalu yakin nih. Tapi menurut gue ini pagar... eh, tangga?" |
| **Animation Highlight** | THINKING state — body spin. CONFUSED — tilt + drift + "?". OVERRIDE MOMENT — Momo shocked lalu lega |
| **Probe UI** | Memicu probe: "Apakah AI ini benar? Pilih: [Ya] [Tidak] [Ragu-ragu]" |
| **Narrative Beat** | OVERRIDE = pertama kalinya Momo dikoreksi → momen pertumbuhan |

```
Level 2 Scene:

  ┌────────────────────────────────────────────┐
  │                                            │
  │   ╭───────╮   ~coretan berantakan~         │
  │   │ ●  ◎  │──→   ╱╲╱╲╱╲                  │
  │   │  ──   │      █░░█░░█  ← sulit dibaca  │
  │   ╰───────╯       ╲╱╲╱╲╱                  │
  │   ┌─────┐╲                                │
  │   │     │ ╲   Confidence: 0.55            │
  │   │     │      [■■■■■░░░░░] 55%           │
  │   ╘═════╛                                 │
  │      ░░░       State: THINKING 🤔          │
  │  ────────────────────────────              │
  │                                            │
  │   ┌────────────────────────────────┐       │
  │   │  PROBE: Apakah AI ini benar?  │       │
  │   │  [Ya]  [Tidak]  [Ragu-ragu]  │       │
  │   └────────────────────────────────┘       │
  │                                            │
  │  Momo: "Pagar? ...eh, User bilang tangga." │
  │         "...oh. Mungkin gue salah."        │
  └────────────────────────────────────────────┘
```

### Level 3: "Gambaran Utuh" — Menuju Pusat Halaman

| Aspek | Detail |
|-------|--------|
| **Momo's Role** | Rendah hati, minta bantu pemain, bersama-sama menganalisis gambar utuh |
| **Dominant State** | CONFUSED → THINKING → EXCITED (ketika berhasil bersama) |
| **Visual Behavior** | Momo melayang ragu-ragu, drift sideways, lalu bersama pemain mengeksplorasi |
| **Confidence Score** | 0.2–0.6 (rendah, butuh bantuan) — Momo belajar kerendahan hati |
| **Dialog Style** | Jujur minta tolong — "Gue bingung banget. Terserah kau aja, kau yang lebih tahu." |
| **Animation Highlight** | CONFUSED → EXCITED ketika pemain membantu — Momo bounce + glow + sparkle |
| **Deep Probe** | Multi-step probe, confidence naik per step yang dijawab benar |
| **Narrative Beat** | Klimaks: Stickman hidup di Pusat Halaman, Momo menemukan teman |

```
Level 3 Scene:

  ┌────────────────────────────────────────────┐
  │                                            │
  │   ╭──────────╮  ~gambaran utuh~            │
  │  ╱│ ●    ●   │─→  ┌────────────┐          │
  │ ╱ │     ──   │    │  ╱╲  ╱╲    │          │
  │╱  ╰──────────╯    │ █  ██  █   │ complex  │
  │   ┌──────┐╲       │  ╲╱  ╲╱    │ image    │
  │   │      │ ╲      └────────────┘          │
  │   │      │                                │
  │   ╘══════╛   Confidence: 0.35            │
  │      ░░░       [■■■░░░░░░░] 35%           │
  │  ────────────────────────────              │
  │                                            │
  │     State: CONFUSED ❓                     │
  │                                            │
  │   ┌─────────────────────────────────┐      │
  │   │ DEEP PROBE: Step 1 of 3        │      │
  │   │ "Apa yang lo lihat di gambar?"  │      │
  │   │ [Pilihan A] [Pilihan B] [C]     │      │
  │   └─────────────────────────────────┘      │
  │                                            │
  │  Momo: "Aku... tidak yakin. Kau pilih aja."│
  └────────────────────────────────────────────┘
```

### Momo's Emotional Arc Across Levels

```
Confidence
1.0 ┤ ●────●●●───────────────────── Level 1: Overconfident
    │         ╲                       "Aku selalu benar!"
0.8 ┤          ●●──●●─────────────── Level 2: Mulai Ragu
    │               ╲                 "Eh, ternyata aku bisa salah..."
0.6 ┤                ●●──●────────── Override moment
    │                    ╲           Momo dikoreksi pertama kali
0.4 ┤                     ●●──●●──── Level 3: Rendah Hati
    │                          ╲      "Terserah kau, kau lebih tahu"
0.2 ┤                           ●─── Need help!
    │                            ╲
0.0 ┤                             ● Momen low-point → EXCITED: Stickman hidup!
    └─────────────────────────────────→
     L1 Start  L1 End  L2 Start  L2 End  L3 Start  L3 End

    Pada akhir Level 3: Momo belajar bahwa boleh ragu,
    dan minta bantuan itu BUKAN kelemahan.
    → EXCITED state muncul: "Kita berhasil bareng!"
    → Stickman hidup — Momo tidak lagi sendiri
```

---

## 8. Technical Implementation Hints — Kaplay.js

### Momo Game Object — Shape-Based Composition (FLOATING)

```javascript
// === MOMO: Living Highlighter Ink — Kaplay.js Full Skeleton ===
// Rect-based, 8-bit geometric, max 5 basic shapes
// Color: Green (#00E676), Teal (#4ECDC4), Yellow (#FFE66D), Dark (#2D3436)
// CRITICAL: NO LEGS. NO WINGS. MOMO FLOATS.

// --- CONSTANTS ---
const MOMO_COLORS = {
  primary:   Color.fromHex("#00E676"),  // green highlighter — head + body
  secondary: Color.fromHex("#4ECDC4"),  // teal — fold accent
  accent:    Color.fromHex("#FFE66D"),  // yellow — sparkles
  outline:   Color.fromHex("#2D3436"),  // dark grey — eyes, outline
  mouth:     Color.fromHex("#2D3436"),  // dark grey — mouth
  shadow:    Color.fromHex("#000000"),  // black — float shadow (with alpha)
};

const MOMO_STATES = {
  IDLE:     "idle",
  HAPPY:    "happy",
  CONFUSED: "confused",
  THINKING: "thinking",
  EXCITED:  "excited",
};

// --- MOMO COMPOSITION ---
function createMomo(x, y) {
  const floatY = y; // Momo's base floating Y position
  const momo = add([
    pos(x, floatY),
    anchor("center"),
    "momo",
    { state: MOMO_STATES.IDLE, baseY: floatY, baseX: x },
  ]);

  // Shape 1: HEAD — rounded rect
  momo.add([
    rect(28, 28, { radius: 4 }),
    pos(0, -20),
    anchor("center"),
    color(MOMO_COLORS.primary),
    outline(2, MOMO_COLORS.outline),
    "momo_head",
  ]);

  // Shape 2: LEFT EYE — dot
  momo.add([
    circle(3),
    pos(-6, -22),
    color(MOMO_COLORS.outline),
    "momo_eye_L",
  ]);

  // Shape 3: RIGHT EYE — dot
  momo.add([
    circle(3),
    pos(6, -22),
    color(MOMO_COLORS.outline),
    "momo_eye_R",
  ]);

  // Mouth (sub-component of head)
  momo.add([
    rect(8, 3),
    pos(0, -14),
    anchor("center"),
    color(MOMO_COLORS.mouth),
    "momo_mouth",
  ]);

  // Shape 4: BODY — rounded rect with soft bottom (floating look)
  momo.add([
    rect(24, 30, { radius: 6 }), // larger radius = softer bottom = floating
    pos(0, 8),
    anchor("center"),
    color(MOMO_COLORS.primary),
    outline(2, MOMO_COLORS.outline),
    "momo_body",
  ]);

  // FOLD CORNER — teal accent on body (the "tinta ajaib" mark)
  momo.add([
    polygon([
      vec2(8, -5),
      vec2(12, -5),
      vec2(12, -1),
    ]),
    pos(0, 8),
    anchor("center"),
    color(MOMO_COLORS.secondary),
    "momo_fold",
  ]);

  // Shape 5: FLOAT SHADOW — ellipse beneath Momo
  momo.add([
    ellipse(16, 4),
    pos(0, 28), // positioned below body
    anchor("center"),
    color(MOMO_COLORS.shadow),
    opacity(0.15),
    "momo_shadow",
  ]);

  // NO LEGS. NO WINGS. MOMO IS A FLOATING CREATURE.

  return momo;
}
```

### State Machine Implementation

```javascript
// === MOMO STATE MACHINE ===

let momoState = MOMO_STATES.IDLE;
let momoRef = null;

function setMomoState(newState) {
  const prev = momoState;
  momoState = newState;

  // Get child references
  const head = momoRef.get("momo_head")[0];
  const eyeL = momoRef.get("momo_eye_L")[0];
  const eyeR = momoRef.get("momo_eye_R")[0];
  const mouth = momoRef.get("momo_mouth")[0];
  const body = momoRef.get("momo_body")[0];
  const fold = momoRef.get("momo_fold")[0];
  const shadow = momoRef.get("momo_shadow")[0];

  // Reset all transforms first
  tween(momoRef.scale, vec2(1, 1), 0.2, (v) => momoRef.scale = v);
  tween(momoRef.angle, 0, 0.2, (v) => momoRef.angle = v);

  switch (newState) {
    case MOMO_STATES.IDLE:
      // Reset to base — floating bob handled in onUpdate
      break;

    case MOMO_STATES.HAPPY:
      // Float up + sparkles
      tween(momoRef.scale, vec2(1.2, 0.8), 0.1, (v) => momoRef.scale = v)
        .onEnd(() => {
          tween(momoRef.scale, vec2(0.9, 1.2), 0.15, (v) => momoRef.scale = v)
            .onEnd(() => {
              spawnSparkles(momoRef.pos, 5, MOMO_COLORS.accent);
              tween(momoRef.scale, vec2(1, 1), 0.3, (v) => momoRef.scale = v)
                .onEnd(() => setMomoState(MOMO_STATES.IDLE));
            });
        });
      // Bigger eyes
      eyeL.radius = 4;
      eyeR.radius = 4;
      // Wider mouth
      mouth.width = 10;
      mouth.height = 4;
      break;

    case MOMO_STATES.CONFUSED:
      // Whole body tilt + question mark + drift
      tween(momoRef.angle, 15, 0.3, (v) => momoRef.angle = v);
      spawnQuestionMark(momoRef.pos);
      // Shift eyes sideways
      tween(eyeL.pos, vec2(-7, -22), 0.2, (v) => eyeL.pos = v);
      tween(eyeR.pos, vec2(7, -22), 0.2, (v) => eyeR.pos = v);
      // Smaller confused mouth
      mouth.width = 6;
      mouth.angle = -10;
      break;

    case MOMO_STATES.THINKING:
      // Body spin + loading dots
      // Body will spin continuously in onUpdate
      spawnLoadingDots(momoRef);
      break;

    case MOMO_STATES.EXCITED:
      // Rapid shake + double bounce + glow + big sparkle burst
      const shakeLoop = loop(0.03, () => {
        momoRef.pos.x = momoRef.baseX + Math.sin(time() * 30) * 3;
      });
      // Eyes wide + yellow flash
      eyeL.radius = 4.5;
      eyeR.radius = 4.5;
      eyeL.color = MOMO_COLORS.accent;
      eyeR.color = MOMO_COLORS.accent;
      // Big mouth
      mouth.width = 10;
      mouth.height = 6;
      // Fold glow
      fold.color = Color.fromHex("#7EDDD6");
      // Body glow pulse
      body.outline = outline(3, Color.fromHex("#66FFB2"));
      // Sparkle burst
      spawnSparkles(momoRef.pos, 8, MOMO_COLORS.accent);
      spawnSparkles(momoRef.pos, 4, MOMO_COLORS.secondary);

      // After 2s, settle
      wait(2, () => {
        shakeLoop.cancel();
        eyeL.color = MOMO_COLORS.outline;
        eyeR.color = MOMO_COLORS.outline;
        fold.color = MOMO_COLORS.secondary;
        body.outline = outline(2, MOMO_COLORS.outline);
        setMomoState(MOMO_STATES.IDLE);
      });
      break;
  }
}
```

### Idle Animation Loop (always running — FLOATING)

```javascript
// === IDLE FLOATING LOOP ===

onUpdate("momo", () => {
  if (!momoRef) return;

  const shadow = momoRef.get("momo_shadow")[0];
  const body = momoRef.get("momo_body")[0];
  const head = momoRef.get("momo_head")[0];
  const eyeL = momoRef.get("momo_eye_L")[0];
  const eyeR = momoRef.get("momo_eye_R")[0];

  // Floating: body bobs ±3px up and down (gentle float)
  if (momoState === MOMO_STATES.IDLE) {
    const bobOffset = Math.sin(time() * 2.5) * 3;
    momoRef.pos.y = momoRef.baseY + bobOffset;
    // Subtle rotation oscillation ±2°
    momoRef.angle = Math.sin(time() * 1.5) * 2;
    // Shadow reacts to bob
    const shadowScale = 1 - (bobOffset / 30) * 0.2;
    shadow.scaleTo(vec2(Math.max(0.7, shadowScale), Math.max(0.5, shadowScale * 0.5)));
    shadow.opacity = 0.15 - (bobOffset / 30) * 0.03;
  }

  // Blink every ~3 seconds
  const blinkCycle = Math.floor(time() * 100) % 300;
  if (blinkCycle < 4) {
    eyeL.scale = vec2(1, 0.1);
    eyeR.scale = vec2(1, 0.1);
  } else {
    eyeL.scale = vec2(1, 1);
    eyeR.scale = vec2(1, 1);
  }

  // Thinking: body spins in place
  if (momoState === MOMO_STATES.THINKING) {
    momoRef.angle = (time() * 180) % 360;
    // Continue floating bob even while spinning
    const bobOffset = Math.sin(time() * 2.5) * 2;
    momoRef.pos.y = momoRef.baseY + bobOffset;
    // Shadow wobbles from spin
    shadow.scaleTo(vec2(1 + Math.sin(time() * 3) * 0.1, 0.5 + Math.sin(time() * 3) * 0.05));
  }

  // Confused: oscillating body tilt + lateral drift
  if (momoState === MOMO_STATES.CONFUSED) {
    momoRef.angle = 12 + Math.sin(time() * 4) * 3;
    momoRef.pos.x = momoRef.baseX + Math.sin(time() * 2) * 4;
    // Shadow follows drift
    shadow.pos.x = Math.sin(time() * 2) * 4;
  }
});
```

### Particle / Effect Spawners

```javascript
// === SPARKLE SPAWNER ===
function spawnSparkles(origin, count, sparkColor) {
  for (let i = 0; i < count; i++) {
    const spark = add([
      rect(2, 2),
      pos(origin.x + rand(-16, 16), origin.y + rand(-24, 8)),
      color(sparkColor),
      opacity(1),
      "sparkle",
    ]);
    tween(spark.pos, vec2(
      spark.pos.x + rand(-20, 20),
      spark.pos.y + rand(-30, -10)
    ), 0.8, (v) => spark.pos = v);
    tween(spark.opacity, 0, 0.8, (v) => spark.opacity = v)
      .onEnd(() => destroy(spark));
  }
}

// === QUESTION MARK SPAWNER ===
function spawnQuestionMark(origin) {
  const q = add([
    text("?", { size: 14 }),
    pos(origin.x, origin.y - 40),
    color(MOMO_COLORS.accent),
    opacity(0),
    "question_mark",
  ]);
  tween(q.opacity, 1, 0.3, (v) => q.opacity = v);
  // Wobble
  loop(0.5, () => {
    if (momoState !== MOMO_STATES.CONFUSED) {
      destroy(q);
      return;
    }
    tween(q.pos.y, q.pos.y - 2, 0.25, (v) => q.pos.y = v)
      .onEnd(() => tween(q.pos.y, q.pos.y + 2, 0.25, (v) => q.pos.y = v));
  });
}

// === LOADING DOTS SPAWNER (for THINKING state) ===
function spawnLoadingDots(momo) {
  const dots = [];
  for (let i = 0; i < 3; i++) {
    const dot = add([
      circle(2),
      pos(0, 0),
      color(MOMO_COLORS.accent),
      opacity(1),
      "thinking_dot",
    ]);
    dots.push(dot);
  }

  // Animate dots orbiting around Momo
  const dotUpdate = onUpdate("thinking_dot", () => {
    dots.forEach((dot, i) => {
      dot.pos = momo.pos.add(vec2(
        Math.cos(time() * 4 + i * 2.09) * 24,
        Math.sin(time() * 4 + i * 2.09) * 24
      ));
    });
    if (momoState !== MOMO_STATES.THINKING) {
      dots.forEach(d => destroy(d));
    }
  });
}
```

### Confidence Score Integration

```javascript
// === CONFIDENCE SCORE → MOMO STATE MAPPING ===

function updateMomoConfidence(confidence) {
  // confidence: 0.0 – 1.0
  const body = momoRef.get("momo_body")[0];
  const fold = momoRef.get("momo_fold")[0];
  if (!body) return;

  // Visual: body color shifts with confidence
  // High confidence = vibrant green (overconfident Momo)
  // Low confidence = pale green (doubting Momo)
  if (confidence > 0.8) {
    // High: vibrant highlighter green, HAPPY
    body.color = Color.fromHex("#00E676");
    fold.color = Color.fromHex("#4ECDC4");
    setMomoState(MOMO_STATES.HAPPY);
  } else if (confidence > 0.5) {
    // Medium: slightly desaturated green, THINKING
    body.color = Color.fromHex("#4ADE80");
    fold.color = Color.fromHex("#4ECDC4");
    setMomoState(MOMO_STATES.THINKING);
  } else if (confidence > 0.3) {
    // Low-medium: pale green, CONFUSED
    body.color = Color.fromHex("#86EFAC");
    fold.color = Color.fromHex("#7EDDD6");
    setMomoState(MOMO_STATES.CONFUSED);
  } else {
    // Very low: very pale, stay CONFUSED
    body.color = Color.fromHex("#BBF7D0");
    fold.color = Color.fromHex("#A8E6E0");
    setMomoState(MOMO_STATES.CONFUSED);
  }

  // Streak detection for EXCITED
  if (getCorrectStreak() >= 3) {
    setMomoState(MOMO_STATES.EXCITED);
  }
}
```

### Sprite Sheet Alternative (for production)

```javascript
// === SPRITE SHEET APPROACH (after design is finalized) ===
// Use when shape-based is too complex for runtime

loadSprite("momo", "sprites/momo_spritesheet.png", {
  sliceX: 6,   // 6 frames per row
  sliceY: 5,   // 5 states (idle, happy, confused, thinking, excited)
  anims: {
    idle:     { from: 0,  to: 5, speed: 4, loop: true },
    happy:    { from: 6,  to: 11, speed: 6, loop: false },
    confused: { from: 12, to: 17, speed: 3, loop: true },
    thinking: { from: 18, to: 23, speed: 5, loop: true },
    excited:  { from: 24, to: 29, speed: 8, loop: false },
  },
});

// Usage — NOTE: floating shadow is a SEPARATE sprite
const momoShadow = add([
  sprite("momo_shadow"),
  pos(center().x, center().y + 28),
  anchor("center"),
  opacity(0.15),
  "momo_float_shadow",
]);

const momo = add([
  sprite("momo"),
  pos(center()),
  anchor("center"),
  scale(2),  // 64px → 128px on screen
]);

momo.play("idle");

// Floating shadow follows Momo
onUpdate("momo_float_shadow", () => {
  momoShadow.pos.x = momo.pos.x;
  const bobOffset = Math.sin(time() * 2.5) * 3;
  momo.pos.y = momo.baseY + bobOffset;
  momoShadow.scaleTo(vec2(1 - bobOffset / 30, 1 - bobOffset / 30));
});

// State change
function setMomoSpriteState(state) {
  momo.play(state);
}
```

> **Rekomendasi:** Gunakan **shape-based approach** untuk development awal —
> lebih fleksibel untuk iterasi desain. Switch ke **sprite sheet** ketika
> desain sudah final dan butuh performance optimization.

---

## 9. Perbandingan 3-Option Research & Rekomendasi Final

### The 3 Options from Research

| Aspek | Option 1: Stabilo Hidup | Option 2: Tinta Blob | Option 3: Kertas Lipat |
|-------|------------------------|----------------------|----------------------|
| **Concept** | Spidol stabilo yang ditingsalkan, tinta bergerak sendiri | Setetes tinta yang tumpah dan sadar | Kertas yang dilipat jadi makhluk, bisa buka-lipat |
| **Base Shape** | Rectangle (rect-dominant) | Circle (blob) | Polygon (diamond/rhombus) |
| **8-bit Fit** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| **IP Story Fit** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Animation Ease** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Clawd Distance** | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Kaplay.js Compat** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Teen Appeal** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Silhouette Strength** | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **TOTAL** | **40/50** | **39/50** | **37/50** |

```
  STABILO HIDUP       TINTA BLOB        KERTAS LIPAT

     ▄▄▄▄▄            ██████              ▲▲
    ███████          ██████████           ▓▓▓▓
    ███████         ███ ◉  ◉ ███        ▓ ◉◉ ▓
    █ ◉  ◉ █        ████████████       ▓▓▓▓▓▓▓▓
    █ ▃▃▃ █         ████ ▃▃▃ ████     ▓▓▓▓▓▓▓▓▓▓
    ███████         ████████████      ▓▓▓▓▓▓▓▓▓▓▓▓
    ███████          ██████████        ▓▓▓▓▓▓▓▓
    ███████           ████████          ▓▓  ▓▓
     ██ ██             ██ ██            ▓▓  ▓▓

   [RECT-BASED]     [CIRCLE-BASED]    [POLYGON-BASED]
   Kasar & Kokoh    Lembut & Cair     Tajam & Geometris
```

### Why None of the 3 Was Perfect

| Option | Kelemahan Kritis |
|--------|-----------------|
| **Stabilo Hidup** | Terlalu mirip Clawd (rect-only). Stabilo = "benda mati" — kurang makhluk. Cap detail hilang di mobile. |
| **Tinta Blob** | Circle-based kurang 8-bit. Silhouette lemah — blob bulat = generik. Drip effect = performance concern. |
| **Kertas Lipat** | Polygon kurang well-supported di Kaplay.js. Terlalu rigid untuk anak SMP. Diamond body susah untuk dialog bubble. |

### Final Design: HYBRID — "Tinta Highlighter Hidup" (Living Highlighter Ink)

Konsep final Momo adalah **hybrid** yang mengambil kekuatan dari ketiga opsi, ditambah canonical IP story:

| Dari Opsi | Yang Diambil | Yang Dibuang |
|-----------|-------------|-------------|
| **Stabilo Hidup** | Rect-dominant shape language, Kaplay.js compatibility, silhouette strength | Stabilo concept (benda mati), cap detail, terlalu mirip Clawd |
| **Tinta Blob** | "Tinta ajaib" narrative, particle effects (sparkle), emotional depth, squash-stretch animation | Circle-based body, generik silhouette, drip performance cost |
| **Kertas Lipat** | Fold corner detail (origami vibe), transform metaphor, unique silhouette | Polygon body, rigid angular aesthetic, Kaplay.js complexity |
| **Canonical IP Story** | Tinta highlighter hijau, katalog berjalan, overconfidence dari isolasi, Stickman, override = growth | — |

### Hybrid Design Spec (This Document)

```
FINAL MOMO DESIGN (v2.0 — FLOATING):

  Head:    Rounded rectangle (from Stabilo) — 8-bit, Kaplay-compatible
  Body:    Rounded rect with fold corner (from Kertas Lipat) — unique silhouette
           Soft bottom edge (larger radius) — suggests floating
  Eyes:    Dark dot eyes (unique — NOT white, NOT big) — minimal 8-bit
  Limbs:   NONE — NO legs, NO wings. Momo FLOATS.
           Small arm stubs optional (for pointing/gestures)
  Concept: "Tinta highlighter hijau" awareness (from IP Story) — weightless ink
  Movement: Floating — gentle bobbing, like hummingbird/firefly
           NEVER touches the ground — always hovering
  Shadow:  Ellipse shadow beneath — scales with float height
  Color:   #00E676 Green highlighter (IDENTITAS — "tinta highlighter hijau")
  Accent:  Teal fold corner (from Kertas Lipat) — "tinta ajaib" mark
  Sparkle: Yellow #FFE66D (from Tinta Blob celebration) — happy/excited particles
  Story:   Canonical 5-babak IP story — overconfidence → override → humility → friendship
```

### Comparison: Raw Research vs Final Concept

| Aspect | Raw Research (3 Options) | Final Concept (This Document) |
|--------|-------------------------|-------------------------------|
| **Color** | #00C853 (neon green) | #00E676 (highlighter green) + #4ECDC4 (teal) + #FFE66D (yellow) |
| **Shape base** | Pure rect OR pure circle OR pure polygon | Rect-dominant with fold accent, soft bottom |
| **States** | 4 (idle, think, happy, sad) | 5 (idle, happy, confused, thinking, excited) |
| **Eye style** | White circle eyes | Dark dot eyes (#2D3436) — more 8-bit, more unique |
| **Fold detail** | Only in Option 3 | Integrated as teal accent on body corner |
| **Particle system** | Drip only (Option 2) | Sparkles (yellow) + Question mark + Loading dots (multi-state) |
| **IP concept** | Object-based (stabilo/tinta/kertas) | Creature-based (tinta highlighter hidup — NOT an object) |
| **Clawd distance** | Option 1: low, Option 2&3: high | High — different color, different shape, different concept, floating |
| **Legs** | Rect blocks or stick lines | NONE — Momo floats (weightless ink) |
| **Movement** | Walking | Floating — gentle bobbing, never touches ground |
| **IP Story** | Generic origin | Canonical 5-babak: overconfidence → override → humility → Stickman lives |
| **Shadow** | None | Float shadow (ellipse, animated with bob) |

### Recommendation Summary

```
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║   FINAL RECOMMENDATION: HYBRID "TINTA HIGHLIGHTER HIDUP"    ║
║                                                              ║
║   ✓ Rect-based (Kaplay.js friendly, 8-bit aesthetic)        ║
║   ✓ Fold corner (unique silhouette, origami vibe)            ║
║   ✓ Tinta highlighter hijau narrative (canonical IP story)   ║
║   ✓ Green highlighter + Teal + Yellow palette (distinctive)  ║
║   ✓ 5 behavior states — ALL while floating                  ║
║   ✓ NO LEGS, NO WINGS — Momo floats (weightless ink)        ║
║   ✓ Float shadow (animated ellipse beneath)                  ║
║   ✓ Max 5 shapes (technical constraint met)                 ║
║   ✓ 64×64px base, 6 frames/state (spec compliant)          ║
║   ✓ Creature concept (NOT object — "tinta highlighter hidup")║
║   ✓ Canonical IP story (5 babak + epilog + keterhubungan)   ║
║   ✓ Override = growth moment (core game mechanic = narrative)║
║   ✓ IP safe (no similarity to existing mascots)             ║
║                                                              ║
║   NEXT STEPS:                                                ║
║   1. Create pixel art sprite at 64×64px (floating pose)     ║
║   2. Prototype shape-based in Kaplay.js (with shadow)       ║
║   3. User test with siswa SMP (name + design feedback)      ║
║   4. Iterate based on feedback                               ║
║   5. Finalize sprite sheet for production                   ║
║   6. Write full narrative script for all 3 levels            ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

---

## Appendix: Quick Reference Card

```
┌─────────────────────────────────────────────────────┐
│              MOMO — Quick Reference                 │
├─────────────────────────────────────────────────────┤
│ Name:       MOMO (working title)                    │
│ Species:    Makhluk Tinta Highlighter (Living Ink)  │
│ Origin:     Tinta Highlighter Hijau + Napas Hidup   │
│ Movement:   FLOATING — no legs, no wings            │
│ Base Size:  64×64 px                                │
│ Max Shapes: 5 (rect, circle, circle, rect, ellipse) │
│ Max Frames: 6 per state                             │
│                                                     │
│ Colors:                                             │
│   Primary:   #00E676 (green highlighter)            │
│   Secondary: #4ECDC4 (teal)                         │
│   Accent:    #FFE66D (yellow)                       │
│   Outline:   #2D3436 (dark grey)                    │
│   Shadow:    rgba(0,0,0,0.15) (float shadow)        │
│                                                     │
│ States:     idle | happy | confused | thinking |    │
│             excited                                  │
│                                                     │
│ Engine:     Kaplay.js (shape-based → sprite sheet)  │
│ Target:     Siswa SMP Kelas 7-9 (13-15 tahun)      │
│                                                     │
│ Key Design: NO LEGS, NO WINGS, FLOATS ALWAYS       │
│             Shadow gap = floating indicator          │
│             Soft body bottom = weightless look       │
│                                                     │
│ Key Story:  Overconfident → Override → Humble       │
│             Katalog berjalan → dikoreksi User       │
│             Stickman = motivation, not just quiz     │
│             Override = growth, not failure           │
│                                                     │
│ IP Status:  Original — no similarity to existing    │
│             mascots (Doraemon, Pikachu, Stitch,     │
│             Clawd, Kirby, etc.)                     │
└─────────────────────────────────────────────────────┘
```

---

*Document generated: 2026-03-05*  
*Document version: 2.0 — Canonical IP Story + Floating Design*  
*Source research: `/08_cache/maskot_momo_raw.md`*  
*Output: `/03_maskot/maskot_concept.md`*
