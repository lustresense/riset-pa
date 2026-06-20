# Desain Maskot Momo — "Escape the Sketchbook"

> **Proyek:** Interactive HITL AI Literacy Simulation  
> **Maskot:** Momo — Game Master, Confidence Score Display, Probe UI Trigger  
> **IP Story:** Momo adalah *coretan hidup* (living sketch) dari illustrator sebelumnya yang pernah hidup di universe Sketchbook. Old illustrator meninggalkan jejak-jejak, dan Momo adalah salah satu jejak yang menjadi hidup.  
> **Target:** Siswa SMP Kelas 7–9 (usia 13–15 tahun)  
> **Engine:** Kaplay.js (JavaScript, formerly Kaboom.js)  
> **Constraint:** Max 5 basic shapes (rect, circle), 8-bit aesthetic, easy to animate  

---

## Daftar Isi

1. [Riset Referensi: Clawd (Claude AI Mascot)](#1-riset-referensi-clawd-claude-ai-mascot)
2. [Prinsip Desain Momo](#2-prinsip-desain-momo)
3. [Option 1 — Stabilo Hidup (Living Highlighter)](#3-option-1--stabilo-hidup-living-highlighter)
4. [Option 2 — Tinta Blob (Ink Blob)](#4-option-2--tinta-blob-ink-blob)
5. [Option 3 — Kertas Lipat (Folded Paper / Origami)](#5-option-3--kertas-lipat-folded-paper--origami)
6. [Perbandingan Tiga Opsi](#6-perbandingan-tiga-opsi)
7. [Rekomendasi](#7-rekomendasi)
8. [Implementasi Teknis Kaplay.js](#8-implementasi-teknis-kaplayjs)
9. [Referensi](#9-referensi)

---

## 1. Riset Referensi: Clawd (Claude AI Mascot)

### Apa itu Clawd?

Clawd adalah maskot resmi Anthropic untuk produk **Claude Code**. Ia berbentuk **kepiting pixel art 8-bit** yang muncul di terminal dan berbagai touchpoint brand Claude. Clawd menjadi salah satu elemen brand paling iconic di dunia AI, bahkan dilindungi secara trademark—Anthropic memaksa proyek "Clawdbot" berganti nama menjadi "Moltbot" karena dianggap meniru.

### Bagaimana Clawd Dibangun? (Technical Breakdown dari Codrops)

| Aspek | Detail |
|-------|--------|
| **Elemen dasar** | 100% `<rect>` elements — **tidak ada path, tidak ada curves**. Murni persegi panjang tersusun menjadi karakter |
| **Filosofi** | Minimalis ekstrem: "The mascot is built entirely from `<rect>` elements, no paths, no curves. Just rectangles arranged into a character." — Codrops |
| **Animasi** | GSAP (GreenSock Animation Platform), frame-by-frame, timing yang punya personality dan weight |
| **Detail teknis** | Bahkan `lean` tubuh butuh `<clipPath>` biar kakinya nggak nembus tanah — detail sekecil ini yang bikin karakter terasa "hidup" meskipun cuma kotak-kotak |
| **Kontras visual** | Pixel art 8-bit yang nostalgic di konteks AI yang futuristik — ini kontras yang disengaja: AI = modern, mascot = retro |

### Prinsip Desain yang Diambil dari Clawd (Bukan Visual-nya)

> ⚠️ **KRITIS:** Momo **TIDAK** menyalin Clawd. Yang diambil adalah **prinsip desainnya**, bukan bentuk/identitas visualnya. Clawd adalah kepiting milik Anthropic — Momo adalah makhluk sketchbook milik project ini.

| Prinsip Clawd | Aplikasi ke Momo |
|---------------|------------------|
| Bentuk dari elemen dasar sederhana (hanya rect) | Momo dibangun dari max 5 shapes: rect, circle, polygon |
| Gampang dianimasikan secara programmatic | Setiap bagian Momo (body, eyes, limbs) adalah object terpisah yang bisa di-tween |
| Timing animasi punya personality | Setiap state Momo (idle, think, sad, happy) punya gerakan khas dengan timing unik |
| Kontras visual yang sengaja | Momo (hijau neon) vs dunia sketchbook (monokrom) — satu-satunya elemen berwarna |
| Trademark-able | Momo harus punya silhouette yang unik dan bisa diidentifikasi tanpa detail |

---

## 2. Prinsip Desain Momo

### IP Story Constraint

```
Momo BUKAN objek dari luar (bukan robot alien, bukan penghapus dari toko, bukan asisten digital).
Momo adalah CORETAN HIDUP — jejak illustrator sebelumnya yang menjadi hidup di universe Sketchbook.
```

Ini memberikan:
- **Emotional depth:** Momo punya "memory" dari illustrator lama — dia merasa terikat pada dunia kertas
- **Narrative justification:** Kenapa Momo ada di dunia buku? Karena dia memang bagian dari buku itu
- **Gameplay connection:** Momo bisa "membaca" coretan karena dia sendiri adalah coretan — ada empati antar-gambar

### Design Rules

1. **Max 5 basic shapes** — Kaplay.js `rect()`, `circle()`, `polygon()` only
2. **8-bit aesthetic** — pixel-art-like, bukan smooth vector
3. **Silhouette-first** — harus recognizable hanya dari silhouette hitam
4. **Animation-ready** — setiap bagian terpisah (body, eyes, limbs) untuk tweening independen
5. **Color identity** — hijau neon (#00C853) sebagai satu-satunya warna cerah di dunia monokrom
6. **Native to sketchbook** — bukan makhluk asing, tapi makhluk yang lahir dari dunia kertas

---

## 3. Option 1 — Stabilo Hidup (Living Highlighter)

### Concept

Spidol stabilo (highlighter) yang ditinggalkan oleh illustrator lama di halaman buku. Dulu dia cuma alat untuk menyoroti teks, tapi setelah illustrator pergi, tinta hijau di dalamnya mulai bergerak sendiri — menyoroti coretan-coretan yang ditinggalkan, membaca mereka, dan mencoba menebak maknanya. Dia "hidup" karena tinta illustrator masih mengalir di dalamnya.

### ASCII Art — Front View (Idle State)

```
      ▄▄▄▄▄
     ███████
     ███████
     █ ◉  ◉ █
     ███████
     █ ▃▃▃ █
     ███████
     ███████
     ███████
      ██ ██
```

### ASCII Art — Side View (untuk referensi dimensi)

```
    ▄▄▄▄▄▄▄▄
   ██████████
   ██████████
   █ ◉    ░░█
   ██████████
   █ ▃▃▃  ░░█
   ██████████
   ██████████
   ██████████
    ██  ████
```

### ASCII Art — Detail Parts Breakdown

```
  ┌─── CAP (rect) ───┐
  │     ▄▄▄▄▄        │  ← Shape 1: rect(28, 8) — cap highlighter
  │    ███████        │
  ├───────────────────┤
  │    █ ◉  ◉ █       │  ← Shape 2&3: circle(3) — mata
  │    ███████        │
  │    █ ▃▃▃ █        │  ← Shape 4: rect(14, 4) — mulut
  │    ███████        │  ← Body = Shape 1 juga
  │    ███████        │
  │    ███████        │
  │     ██ ██         │  ← Shape 5: 2x rect(6, 8) — kaki
  └───────────────────┘
```

### Shape Inventory (Max 5)

| # | Shape | Kaplay.js | Dimensi | Warna | Fungsi |
|---|-------|-----------|---------|-------|--------|
| 1 | Rectangle | `rect(28, 36)` | 28×36 px | `#00C853` (neon green) | Body + Cap |
| 2 | Circle | `circle(3)` | r=3 px | `#FFFFFF` | Mata kiri |
| 3 | Circle | `circle(3)` | r=3 px | `#FFFFFF` | Mata kanan |
| 4 | Rectangle | `rect(14, 4)` | 14×4 px | `#1B5E20` (dark green) | Mulut |
| 5 | Rectangle ×2 | `rect(6, 8)` | 6×8 px | `#00C853` | Kaki kiri + kanan |

### Reasoning

**Kenapa cocok dengan IP Story:**
- Stabilo/highlighter adalah **alat gambar** — dia milik dunia sketchbook secara natural
- Old illustrator "meninggalkan" stabilo di halaman buku — tinta di dalamnya masih basah, lalu menjadi hidup
- Stabilo itu alat untuk **menyoroti** — secara simbolik, Momo "menyoroti" confidence score AI, menandai apa yang penting
- Warna hijau neon sudah established sebagai identitas Momo sejak awal project — highlighter hijau adalah sumber warna tersebut

**Kenapa cocok dengan Technical Constraints:**
- Bentuk dasar **rectangular** — paling dekat dengan filosofi Clawd (rect-only)
- Hanya butuh 3 jenis shape: rect (body, mulut, kaki), circle (mata)
- Body yang tinggi dan stabil membuat animasi bobbing/menjilat sangat natural
- Silhouette kuat: persegi panjang dengan dua kaki — langsung recognizable

### Animation Descriptions

| State | Deskripsi Gerakan | Timing & Feel |
|-------|-------------------|---------------|
| **Idle** | Body bobbing ringan atas-bawah (2px, sin wave), mata berkedip setiap 3 detik, kaki diam tap sedikit | Gentle, `sin(time * 3) * 2`, blink via `circle(radius)` toggle 0→3 |
| **Think** | Body sedikit miring ke kanan (3° rotate), satu "lengan" muncul dari sisi body menyentuh dagu (cap area), tanda `?` muncul di atas cap | Tilt via `angle = sin(time*2) * 5`, arm extend via `rect.width` tween, `?` particle muncul |
| **Wrong/Sad** | Body mengecil (squish X, stretch Y), mata berubah jadi garis horizontal (`circle→rect`), mulut turun ke bawah, kaki tertutup rapat | Squish via `scale = vec2(0.8, 1.2)`, eyes morph, mouth `pos.y += 2` |
| **Happy** | Body stretch (stretch X, squish Y), mata jadi bintang/besar, mulut terbuka lebar, kaki melompat, partikel tinta hijau menyebar | Bounce via `scale = vec2(1.2, 0.8)` then settle, particles via `add([rect(2,2), ...])` |

### Kaplay.js Implementation Hint

```javascript
// === MOMO: Stabilo Hidup — Kaplay.js Skeleton ===
// Compose dari max 5 shapes

const momo = add([
  pos(center().x, center().y),
  anchor("center"),
  "momo",
]);

// Shape 1: Body + Cap (main rectangle)
momo.add([
  rect(28, 36),
  pos(0, 0),
  anchor("center"),
  color(0, 200, 83),      // #00C853
  outline(2, Color.fromHex("#1B5E20")),
  "momo_body",
]);

// Shape 2: Left Eye
momo.add([
  circle(3),
  pos(-6, -6),
  color(255, 255, 255),
  "momo_eye_L",
]);

// Shape 3: Right Eye
momo.add([
  circle(3),
  pos(6, -6),
  color(255, 255, 255),
  "momo_eye_R",
]);

// Shape 4: Mouth
momo.add([
  rect(14, 4),
  pos(0, 4),
  anchor("center"),
  color(27, 94, 32),       // #1B5E20
  "momo_mouth",
]);

// Shape 5: Legs (two rects as children of a leg group)
const legs = momo.add([pos(0, 18), "momo_legs"]);
legs.add([rect(6, 8), pos(-6, 0), anchor("center"), color(0, 200, 83)]);
legs.add([rect(6, 8), pos(6, 0), anchor("center"), color(0, 200, 83)]);

// --- IDLE ANIMATION ---
let baseY = momo.pos.y;
onUpdate("momo", () => {
  momo.pos.y = baseY + Math.sin(time() * 3) * 2;
});
```

### Pros & Cons

| Pros | Cons |
|------|------|
| ✅ Paling dekat dengan filosofi Clawd — rect-dominant, minimalis ekstrem | ❌ Risiko terlalu mirip Clawd jika tidak dibedakan cukup (perlu personality yang kuat dari animasi) |
| ✅ Warna hijau neon sudah established — tidak perlu rebrand | ❌ Stabilo terkesan "benda mati" — perlu effort ekstra di animasi agar terasa hidup |
| ✅ Silhouette kuat dan unik — persegi panjang berkaki | ❌ Bentuk rectangular kurang ekspresif dibanding bentuk organik (animasi harus kompensasi) |
| ✅ Paling sedikit shapes — 3 jenis saja (rect, circle, rect) | ❌ Bagi sebagian orang, stabilo = alat tulis, bukan "makhluk" |
| ✅ Narasi highlighter yang "menyoroti" = kuat secara simbolik untuk confidence score | ❌ Cap detail mungkin terlalu kecil di layar mobile |
| ✅ Dibangun dari <rect> elements — persis cara Clawd dibangun | ❌ Perlu确保 tidak melanggar trademarke — bentuk harus benar-benar beda dari Clawd |

---

## 4. Option 2 — Tinta Blob (Ink Blob)

### Concept

Setetes tinta yang tumpah dari pena illustrator lama, lalu meresap ke dalam kertas dan mendapatkan kesadaran. Tinta itu membawa "memory" dari semua gambar yang pernah dibuat oleh illustrator — itulah kenapa Momo bisa "membaca" dan "menebak" coretan. Tinta mengalir, berubah bentuk, dan kadang menetes — ini adalah manifestasi fisik dari proses berpikir AI yang fluid dan tidak selalu pasti.

### ASCII Art — Front View (Idle State)

```
      ██████
    ██████████
   ███ ◉  ◉ ███
   ████████████
   ████ ▃▃▃ ████
   ████████████
    ██████████
     ████████
      ██████
       ████
      ██  ██
```

### ASCII Art — Dripping Detail

```
      ██████         ← Atas: bulat penuh
    ██████████
   ███ ◉  ◉ ███     ← Mata di 1/3 atas
   ████████████
   ████ ▃▃▃ ████     ← Mulut di tengah
   ████████████
    ██████████       ← Body makin menyempit ke bawah
     ████████
      ██████
       ██ ██         ← Drip effect: dua tetes kecil
```

### ASCII Art — Side View (untuk referensi dimensi)

```
     ██████
   ██████████
   ██ ◉  ░░░█
   ██████████
   ██ ▃▃ ░░░█
   ██████████
    █████████
     ████████
      ██████
       ██ ██
```

### Shape Inventory (Max 5)

| # | Shape | Kaplay.js | Dimensi | Warna | Fungsi |
|---|-------|-----------|---------|-------|--------|
| 1 | Circle (ellipse) | `circle(16)` | r=16 px | `#00C853` (neon green) | Body utama (tinta blob) |
| 2 | Circle | `circle(3)` | r=3 px | `#FFFFFF` | Mata kiri |
| 3 | Circle | `circle(3)` | r=3 px | `#FFFFFF` | Mata kanan |
| 4 | Circle ×2 | `circle(3)` | r=3 px | `#00C853` | Drip drops (tetesan tinta) |
| 5 | Rect | `rect(10, 4)` | 10×4 px | `#1B5E20` | Mulut |

> **Catatan:** Body circle bisa di-squish via `scale` untuk membuat efek oval/blob tanpa menambah shape.

### Reasoning

**Kenapa cocok dengan IP Story:**
- Tinta adalah **substansi fundamental** dari menggambar — lebih "hidup" daripada alat tulis. Tinta mengalir, menyebar, meresap
- Tumpahan tinta dari pena illustrator = kecelakaan kreatif yang jadi hidup — ini emotional
- Tinta "membawa memory" dari setiap gambar yang pernah dibuat — justifikasi kenapa Momo bisa membaca coretan
- Efek menetes (drip) = visual metaphor untuk ketidakpastian AI — kadang "meluncur" dengan percaya diri, kadang "menetes" ragu-ragu

**Kenapa cocok dengan Technical Constraints:**
- Circle adalah shape paling organik — natural untuk blob/creature yang "hidup"
- Squash & stretch animation paling natural di circular body (toon physics)
- Drip effect bisa di-achieve dengan circle kecil + gravity tween
- Total shapes: hanya 3 jenis (circle, rect untuk mulut, circle untuk drip)

### Animation Descriptions

| State | Deskripsi Gerakan | Timing & Feel |
|-------|-------------------|---------------|
| **Idle** | Body breathing (scale X/Y alternating sin wave), drip drops jatuh perlahan dari bawah body lalu respawn di atas, mata berkedip | `scale = vec2(1 + sin(time*2)*0.05, 1 - sin(time*2)*0.05)`, drip: `tween(pos.y, pos.y+20, 1.5)` |
| **Think** | Body elongate ke atas (stretch Y, squish X), drip berhenti, mata menyipit, satu drip kecil muncul dari sisi = "keringat mikir" | `scale = vec2(0.85, 1.15)`, sweat drop: `circle(2)` tween from side |
| **Wrong/Sad** | Body flatten (squish Y, stretch X), drip banyak turun sekaligus = "menetes sedih", mata jadi titik kecil, mulut melengkung ke bawah | `scale = vec2(1.3, 0.7)`, multiple drip spawns, eye `radius = 1.5` |
| **Happy** | Body bounce (squash-stretch cepat), mata membesar, drip berhenti, partikel tinta kecil menyebar ke segala arah, mulut terbuka lebar | Bounce: `scale` tween sequence `1→1.3→0.8→1.1→1.0`, burst particles |

### Kaplay.js Implementation Hint

```javascript
// === MOMO: Tinta Blob — Kaplay.js Skeleton ===
// Circle-based, organic feel

const momo = add([
  pos(center().x, center().y),
  anchor("center"),
  "momo",
]);

// Shape 1: Body (main blob circle)
momo.add([
  circle(16),
  pos(0, 0),
  anchor("center"),
  color(0, 200, 83),
  "momo_body",
]);

// Shape 2: Left Eye
momo.add([
  circle(3),
  pos(-5, -4),
  color(255, 255, 255),
  "momo_eye_L",
]);

// Shape 3: Right Eye
momo.add([
  circle(3),
  pos(5, -4),
  color(255, 255, 255),
  "momo_eye_R",
]);

// Shape 4: Mouth
momo.add([
  rect(10, 4),
  pos(0, 4),
  anchor("center"),
  color(27, 94, 32),
  "momo_mouth",
]);

// Shape 5: Drip drops (animated, respawn)
function spawnDrip() {
  const drip = momo.add([
    circle(3),
    pos(rand(-8, 8), 14),
    color(0, 200, 83),
    opacity(0.8),
    "drip",
  ]);
  tween(drip.pos.y, drip.pos.y + 20, 1.5, (v) => drip.pos.y = v)
    .onEnd(() => destroy(drip));
}

// --- IDLE ANIMATION (breathing blob) ---
onUpdate("momo", () => {
  const breathe = Math.sin(time() * 2);
  momo.scale = vec2(1 + breathe * 0.05, 1 - breathe * 0.05);
});

loop(2, () => {
  if (getCurrentMomoState() === "idle") spawnDrip();
});
```

### Pros & Cons

| Pros | Cons |
|------|------|
| ✅ Paling "hidup" secara visual — blob yang breathing, dripping, shape-shifting | ❌ Circle-based = kurang 8-bit dibanding rect-based (terkesan terlalu smooth) |
| ✅ Tinta = paling fundamental ke dunia sketch — lebih "asli" daripada alat tulis | ❌ Drip effect butuh extra particle management (bisa kena performance di low-end) |
| ✅ Squash & stretch natural — animasi paling ekspresif dari 3 opsi | ❌ Silhouette kurang kuat — blob bulat bisa terlihat generik tanpa detail |
| ✅ Drip = visual metaphor kuat untuk uncertainty AI | ❌ Circle di Kaplay.js lebih mahal render-nya dibanding rect (anti-aliasing) |
| ✅ Emotionally resonant: tumpahan tinta = kecelakaan kreatif yang jadi kekuatan | ❌ Risk of looking like "slime" generik — perlu personality dari animasi & color |
| ✅ Tidak mirip Clawd sama sekali — completely different design language | ❌ Circular body kurang "grounded" — sulit bikin kaki yang natural |

---

## 5. Option 3 — Kertas Lipat (Folded Paper / Origami)

### Concept

Selembar kertas yang illustrator lama lipat menjadi makhluk kecil — mungkin seekor burung, mungkin seekor katak, atau mungkin sesuatu yang tidak jelas. Yang jelas, setelah illustrator pergi, lipatan kertas itu mulai bergerak sendiri. Dia bisa membuka dan melipat dirinya ulang, mengubah bentuknya sedikit demi sedikit. Dia terbuat dari kertas, jadi dia "memahami" dunia buku secara intuitif — dia adalah kertas yang hidup di antara kertas lainnya.

### ASCII Art — Front View (Idle State)

```
        ▲▲
       ▓▓▓▓
      ▓ ◉◉ ▓
     ▓▓▓▓▓▓▓▓
    ▓▓▓▓▓▓▓▓▓▓
   ▓▓▓▓▓▓▓▓▓▓▓▓
    ▓▓▓▓▓▓▓▓▓▓
     ▓▓    ▓▓
     ▓▓    ▓▓
```

### ASCII Art — Detail Fold Lines

```
        ▲▲              ← Fold point (top)
       ▓▓▓▓
      ▓ ◉◉ ▓            ← Mata di sisi fold
     ▓▓─┬──┬─▓▓         ← Fold lines (garis lipatan)
    ▓▓▓▓│▓▓│▓▓▓▓        ← Inner fold sections
   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    ▓▓▓▓▓▓▓▓▓▓          ← Bottom body
     ▓▓    ▓▓            ← Kaki (lipatan terbuka)
     ▓▓    ▓▓
```

### ASCII Art — Side View (3D Fold Effect)

```
       ╱▓╲
      ╱▓▓▓╲
     ╱▓ ◉░░╲
    ╱▓▓▓▓▓▓▓╲
   ╱▓▓▓▓▓▓▓▓▓╲
  ▓▓▓▓▓▓▓▓▓▓▓▓
   ▓▓▓▓▓▓▓▓▓▓
     ▓▓  ▓▓
```

### Shape Inventory (Max 5)

| # | Shape | Kaplay.js | Dimensi | Warna | Fungsi |
|---|-------|-----------|---------|-------|--------|
| 1 | Polygon (diamond) | `polygon([v(0,-20), v(18,0), v(0,16), v(-18,0)])` | 36×36 px | `#00C853` | Body utama (kertas dilipat) |
| 2 | Circle | `circle(3)` | r=3 px | `#FFFFFF` | Mata kiri |
| 3 | Circle | `circle(3)` | r=3 px | `#FFFFFF` | Mata kanan |
| 4 | Rect ×2 | `rect(1, 12)` | 1×12 px | `#1B5E20` | Fold lines (garis lipatan) |
| 5 | Rect ×2 | `rect(8, 10)` | 8×10 px | `#00C853` | Kaki (lipatan terbuka) |

> **Catatan:** Polygon untuk body memungkinkan bentuk diamond/rhombus yang khas origami. Fold lines (rect tipis) memberikan ilusi lipatan kertas.

### Reasoning

**Kenapa cocok dengan IP Story:**
- Kertas adalah **medium** dari sketchbook — lebih fundamental daripada alat atau tinta. Tanpa kertas, tidak ada buku
- Illustrator "melipat" kertas menjadi makhluk — ini act of creation yang personal dan emosional
- Origami = transformasi — Momo bisa "membuka" dan "melipat" dirinya, cocok dengan konsep AI yang berubah-ubah confidence-nya
- Kertas yang hidup di antara kertas lainnya = dia native ke dunia buku, bukan pendatang

**Kenapa cocok dengan Technical Constraints:**
- Polygon (diamond/rhombus) adalah shape unik yang langsung distinctive — tidak mirip Clawd atau karakter lain
- Fold lines = rect tipis yang sangat ringan — detail visual tanpa biaya render
- Angular/geometric shapes = natural untuk 8-bit/pixel art aesthetic
- Kaki sebagai "lipatan terbuka" = tidak perlu detail kompleks, cukup rect sederhana

### Animation Descriptions

| State | Deskripsi Gerakan | Timing & Feel |
|-------|-------------------|---------------|
| **Idle** | Body sway kiri-kanan perlahan (2° rotate), fold lines berkedip tipis (opacity toggle), mata berkedip, kaki diam | `angle = sin(time * 1.5) * 2`, fold line `opacity = 0.5 + sin(time*4)*0.3` |
| **Think** | Body "membuka" sedikit (polygon vertices expand 10%), fold lines menebal = Momo sedang "mengembang" mencerna informasi, satu kaki mengangkat | Vertex tween: expand by 10%, fold `rect.height = 18`, leg `pos.y -= 4` |
| **Wrong/Sad** | Body "melipat" rapat (polygon vertices contract 20%), mata tertutup (circle→rect garis), kaki rapat, body miring ke sisi = kertas yang layu | Contract vertices by 20%, `angle = 15`, eyes morph to `rect(6, 1)` |
| **Happy** | Body "membuka penuh" (expand 15%), spin 360°, kaki terbuka lebar, partikel kertas kecil beterbangan, mata besar | Expand 15%, `angle` tween 0→360 over 0.5s, paper particles `add([rect(3,3), ...])` |

### Kaplay.js Implementation Hint

```javascript
// === MOMO: Kertas Lipat — Kaplay.js Skeleton ===
// Polygon-based, origami feel

const momo = add([
  pos(center().x, center().y),
  anchor("center"),
  "momo",
]);

// Shape 1: Body (diamond/rhombus polygon)
// polygon() menerima array vec2 sebagai vertices
momo.add([
  polygon([
    vec2(0, -20),   // top point
    vec2(18, 0),    // right point
    vec2(0, 16),    // bottom point
    vec2(-18, 0),   // left point
  ]),
  pos(0, 0),
  anchor("center"),
  color(0, 200, 83),
  outline(2, Color.fromHex("#1B5E20")),
  "momo_body",
]);

// Shape 2: Left Eye
momo.add([
  circle(3),
  pos(-5, -4),
  color(255, 255, 255),
  "momo_eye_L",
]);

// Shape 3: Right Eye
momo.add([
  circle(3),
  pos(5, -4),
  color(255, 255, 255),
  "momo_eye_R",
]);

// Shape 4: Fold Lines (two thin rects as creases)
momo.add([
  rect(1, 14),
  pos(-4, -2),
  anchor("center"),
  color(27, 94, 32),
  opacity(0.6),
  "momo_fold_L",
]);
momo.add([
  rect(1, 14),
  pos(4, -2),
  anchor("center"),
  color(27, 94, 32),
  opacity(0.6),
  "momo_fold_R",
]);

// Shape 5: Legs (two rects — "open folds")
const legs = momo.add([pos(0, 14), "momo_legs"]);
legs.add([rect(8, 10), pos(-6, 0), anchor("center"), color(0, 200, 83)]);
legs.add([rect(8, 10), pos(6, 0), anchor("center"), color(0, 200, 83)]);

// --- IDLE ANIMATION (swaying origami) ---
onUpdate("momo", () => {
  momo.angle = Math.sin(time() * 1.5) * 2;
});
```

### Pros & Cons

| Pros | Cons |
|------|------|
| ✅ Paling unik secara silhouette — diamond/rhombus tidak dimiliki maskot manapun | ❌ Polygon di Kaplay.js kurang well-supported dibanding rect/circle — mungkin perlu workaround |
| ✅ Origami = transformasi — cocok dengan konsep AI yang berubah confidence | ❌ Geometric/angular kurang "hangat" untuk anak SMP — terkesan rigid |
| ✅ Kertas = medium paling fundamental dari sketchbook | ❌ Fold lines terlalu detail untuk ukuran kecil — bisa tidak terlihat |
| ✅ Tidak mirip Clawd sama sekali — completely different design language | ❌ Animation "membuka/melipat" polygon = perlu re-render vertices setiap frame (lebih kompleks) |
| ✅ Concept illustrator "melipat kertas jadi makhluk" sangat emotional | ❌ Diamond body membuat teks/dialog bubble sulit ditempatkan secara visual |
| ✅ Visual metaphor kuat: kertas yang "membuka" = gaining understanding | ❌ Origami reference mungkin terlalu Jepang-specific, kurang universal untuk siswa Indonesia |

---

## 6. Perbandingan Tiga Opsi

### Matrix Perbandingan

| Kriteria | Stabilo Hidup | Tinta Blob | Kertas Lipat |
|----------|:------------:|:----------:|:------------:|
| **IP Story Fit** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **8-bit Aesthetic** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Animation Ease** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Shape Simplicity** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Emotional Depth** | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Clawd Distance** | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Kaplay.js Compatibility** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Silhouette Strength** | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Teen Appeal (13-15)** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Confidence Score UI Fit** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| **TOTAL** | **40/50** | **39/50** | **37/50** |

### Visual Comparison (All Three — Idle State)

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

### Narrative Personality Per Option

| Aspek | Stabilo Hidup | Tinta Blob | Kertas Lipat |
|-------|--------------|------------|--------------|
| **Personality** | Kaku tapi mencoba ekspresif (seperti benda yang belajar jadi hidup) | Flowy, unpredictable, kadang menetes ketidakpastian | Terlipat rapi, suka transform, organized chaos |
| **Voice** | "Gue stabilo, gue nyorot yang penting. Kadang nyorotnya salah." | "Gue tinta, gue ngalir aja. Kadang nge-blur, kadang jelas." | "Gue kertas, gue bisa lipat diri. Kadang terbuka, kadang rapat." |
| **Confidence Display** | Body glow/pulse sesuai confidence (makin terang = makin yakin) | Ukuran body (makin besar = makin yakin, makin kecil = ragu) | Lipatan (makin terbuka = makin yakin, makin rapat = ragu) |
| **HITL Trigger** | Stabilo "menyoroti" jawaban AI, lalu pertanyaan muncul | Tinta "menetes" keraguan, lalu probe muncul | Kertas "membuka" pertanyaan tersembunyi |

---

## 7. Rekomendasi

### Primary Recommendation: **Option 1 — Stabilo Hidup** (dengan modifikasi)

Stabilo Hidup adalah pilihan terkuat karena:

1. **Filosofi Clawd-compat tanpa plagiat** — Rect-dominant, minimalis, gampang dianimasi. Ini cara pikir Clawd, tapi bentuknya completely different
2. **Brand consistency** — Warna hijau neon (#00C853) sudah established sebagai identitas Momo sejak awal. Stabilo hijau = sumber warna tersebut
3. **Narrative symbol kuat** — "Menyoroti" = core function AI (confidence scoring), "ditinggalkan illustrator" = emotional depth, "tinta yang masih mengalir" = kenapa dia bisa "membaca" gambar
4. **Technical simplicity** — Hanya 3 jenis shape (rect, circle), paling sedikit dari ketiga opsi. Ini = paling stabil di Kaplay.js

### Modifikasi untuk Mengatasi Kelemahan

| Kelemahan | Solusi |
|-----------|--------|
| Terlalu mirip Clawd (rect-only) | Tambahkan **drip tinta** kecil di bawah cap — ini membuat silhouette unik (kotak + tetes) dan naratif (stabilo yang bocor = hidup) |
| Stabilo terkesan "benda mati" | Animasi personality yang kuat: bobbing dengan weight, eyes yang ekspresif, "lengan" yang muncul saat think |
| Kurang ekspresif | Gunakan **scale manipulation** yang agresif — squash/stretch lebih dramatis dari yang ditampilkan di atas |
| Cap terlalu kecil di mobile | Jadikan cap = area mata (mata berada di dalam cap), bukan body terpisah |

### Secondary Recommendation: **Option 2 — Tinta Blob** (jika prioritas = emotional depth)

Jika keputusan mengutamakan kedalaman emosional dan jarak dari Clawd, Tinta Blob adalah pilihan terbaik. Animasi squash-stretch pada circular body paling natural, dan visual metaphor "tinta yang menetes keraguan" sangat kuat untuk konteks HITL.

---

## 8. Implementasi Teknis Kaplay.js

### Arsitektur Animasi (Berlaku untuk Semua Opsi)

```
┌─────────────────────────────────────────┐
│              Momo Game Object           │
│  ┌─────────────────────────────────┐    │
│  │  Parent: pos(), anchor(), tag   │    │
│  │                                 │    │
│  │  ┌───────┐  ┌───────┐          │    │
│  │  │ Body  │  │ Eyes  │          │    │
│  │  │ shape │  │ L & R │          │    │
│  │  └───────┘  └───────┘          │    │
│  │                                 │    │
│  │  ┌───────┐  ┌───────┐          │    │
│  │  │ Mouth │  │ Limbs │          │    │
│  │  │ shape │  │ group │          │    │
│  │  └───────┘  └───────┘          │    │
│  │                                 │    │
│  │  ┌───────────────────┐         │    │
│  │  │ Particle System   │         │    │
│  │  │ (drip/spark/paper)│         │    │
│  │  └───────────────────┘         │    │
│  └─────────────────────────────────┘    │
│                                         │
│  State Machine:                         │
│  idle → think → {happy | sad} → idle    │
└─────────────────────────────────────────┘
```

### State Machine Implementation

```javascript
// === Momo State Machine — Kaplay.js ===

const MOMO_STATES = {
  IDLE: "idle",
  THINK: "think",
  HAPPY: "happy",
  SAD: "sad",
};

let momoState = MOMO_STATES.IDLE;
let momoRef = null; // reference ke momo game object

function setMomoState(newState) {
  // Cleanup previous state
  momoState = newState;
  
  switch (newState) {
    case MOMO_STATES.IDLE:
      // Reset all transforms, start idle anim
      tween(momoRef.scale, vec2(1, 1), 0.3, (v) => momoRef.scale = v);
      break;
      
    case MOMO_STATES.THINK:
      // Tilt + squish + question mark
      tween(momoRef.angle, 5, 0.3, (v) => momoRef.angle = v);
      tween(momoRef.scale, vec2(0.9, 1.1), 0.3, (v) => momoRef.scale = v);
      spawnQuestionMark(momoRef.pos);
      break;
      
    case MOMO_STATES.HAPPY:
      // Bounce + stretch + particles
      tween(momoRef.scale, vec2(1.2, 0.8), 0.15, (v) => momoRef.scale = v)
        .onEnd(() => {
          tween(momoRef.scale, vec2(1, 1), 0.3, (v) => momoRef.scale = v);
        });
      spawnParticles(momoRef.pos, 5);
      break;
      
    case MOMO_STATES.SAD:
      // Squish + flatten + drip
      tween(momoRef.scale, vec2(1.2, 0.7), 0.3, (v) => momoRef.scale = v);
      tween(momoRef.angle, -8, 0.3, (v) => momoRef.angle = v);
      break;
  }
}
```

### Confidence Score Display Integration

```javascript
// === Momo sebagai Confidence Score Display ===

function updateMomoConfidence(confidence) {
  // confidence: 0.0 - 1.0
  const body = momoRef.get("momo_body")[0];
  if (!body) return;
  
  // Visual: body opacity/glow berdasarkan confidence
  // High confidence (>0.8): bright, stable
  // Medium (0.5-0.8): slight wobble
  // Low (<0.5): dim, shaky
  
  if (confidence > 0.8) {
    body.color = Color.fromHex("#00E676"); // bright green
    setMomoState(MOMO_STATES.HAPPY);
  } else if (confidence > 0.5) {
    body.color = Color.fromHex("#00C853"); // normal green
    setMomoState(MOMO_STATES.THINK);
  } else {
    body.color = Color.fromHex("#69F0AE"); // pale green
    setMomoState(MOMO_STATES.SAD);
  }
}
```

### Frame-Based Animation Timeline Reference

```
Frame  0    4    8    12   16   20   24   28   32   36   40
       │    │    │    │    │    │    │    │    │    │    │
IDLE:  ▐▌  ▐█▌  ▐▌  ▐█▌  ▐▌  ▐█▌  ▐▌  ▐█▌  ▐▌  ▐█▌  ▐▌
       bob  up   bob  up   bob  up   bob  up   bob  up   bob

THINK: ▐▌  ▐▌╱  ▐▌╱  ▐▌?  ▐▌?  ▐▌?  ▐▌╱  ▐▌  ▐▌  ▐▌  ▐▌
       still tilt  tilt  ?    ?    ?    tilt  reset ...

HAPPY: ▐▌  █▌  ▐▌  █▌  ▐▌  ▐█▌  ▐▌  ▐▌  ▐▌  ▐▌  ▐▌
       squish stretch squish bounce settle ... (back to idle)

SAD:   ▐▌  ▐▌  ▐▌  ▐▌  ▐▌  ▐▌  ▐▌  ▐▌  ▐▌  ▐▌  ▐▌
       flatten  ... hold ... hold ... (until state change)
```

### Sprite Sheet Approach (Alternatif)

Jika shape-based terlalu kompleks, bisa switch ke sprite sheet approach:

```javascript
// Load sprite sheet
loadSprite("momo", "sprites/momo.png", {
  sliceX: 4,   // 4 states per row
  sliceY: 3,   // 3 animation frames per state
  anims: {
    idle: { from: 0, to: 2, speed: 4, loop: true },
    think: { from: 4, to: 6, speed: 3, loop: true },
    happy: { from: 8, to: 10, speed: 6, loop: false },
    sad: { from: 12, to: 14, speed: 2, loop: true },
  },
});

// Usage
const momo = add([
  sprite("momo"),
  pos(center()),
  anchor("center"),
]);

momo.play("idle");
```

> **Rekomendasi:** Gunakan shape-based approach (rect/circle/polygon) untuk development awal — lebih fleksibel untuk iterasi. Switch ke sprite sheet ketika desain sudah final dan butuh performance optimization.

---

## 9. Referensi

1. **Codrops** — Reverse-engineering Clawd mascot animation: "The mascot is built entirely from `<rect>` elements, no paths, no curves. Just rectangles arranged into a character."
2. **Business Insider** — Clawd trademark case: Anthropic memaksa "Clawdbot" rebrand ke "Moltbot"
3. **Kaplay.js Documentation** — `rect()`, `circle()`, `polygon()`, `tween()`, `onUpdate()`
4. **Project Memory** — Keputusan Bu Hesti: Momo = auto-text dasar, tanpa NLP/voice, coretan hidup dari illustrator sebelumnya
5. **Merged Context** — Diskusi desain Momo: "Jangan copy Clawd, ambil prinsipnya saja: simple silhouette, sedikit part, ekspresi kuat"

---

> **Dokumen ini adalah living document.** Setelah pemilihan opsi final, bagian implementasi teknis akan di-update dengan kode produksi lengkap untuk Kaplay.js.

---

*Terakhir diupdate: 2026-03-05*
