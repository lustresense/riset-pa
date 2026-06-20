# 📋 Quick Draw Category Analysis v3.1 — RSI-1 Revision

> **Status**: ✅ Revised (RSI-1 applied) | **Total Analisis**: 271 kategori diklasifikasi
> **Sumber**: Bigprompt v3.0 + User feedback 16/6/26 (over-inclusiveness fix)
> **Revisi**: 🔁 RSI Iteration #1 — Sweet Spot Filter (NO animals, NO geometric primitives, NO complex landmarks)
> **Selaras**: Arahan Bu Hesti (hapus dekoratif, pakai solid & danger, 3 level) + RSI-1 (medium difficulty only)

---

## 🔁 RSI-1 Revision Summary

**Apa yang berubah dari v3.0 → v3.1:**

| Aspek | v3.0 (Salah) | v3.1 (Benar — RSI-1) |
|-------|-------------|---------------------|
| **Hewan** | 40+ hewan di TIER 1 (cat, dog, elephant, lion, tiger, bear, horse, dll) | SEMUA hewan di-BAN (Type E) — stroke complexity + confusion matrix tinggi |
| **Geometric primitives** | Di-bahas detail di special cases (mode decoration, mode belajar bentuk) | HAPUS TOTAL dari analisis — out of scope, jangan over-engineer |
| **Landmark kompleks** | Eiffel Tower, Mona Lisa masih di TIER 2 conditional | Hard BAN (Type D) — terlalu kompleks untuk fast-paced drawing |
| **Aircraft carrier** | Tidak ada di list awal (lupa) | Hard BAN (Type D) — terlalu kompleks |
| **Total TIER 1** | 146 (terlalu banyak) | ~70 (medium difficulty only) |
| **Golden Set** | 148 (over) | ~100 (sweet spot) |

**Lihat**: `MEMORY.md` Section 9 (RSI Rules) + `CHANGELOG.md` entry RSI Iteration #1

---

## 📑 Daftar Isi

1. [Section 1: Executive Summary](#section-1-executive-summary)
2. [Section 2: Kategorisasi Utama (3 Tier)](#section-2-kategorisasi-utama-3-tier)
3. [Section 3: Special Category Handling](#section-3-special-category-handling)
4. [Section 4: Proposed Final List (Golden Set)](#section-4-proposed-final-list-golden-set)
5. [Section 5: Thematic Grouping](#section-5-thematic-grouping)
6. [Section 6: Implementation Recommendations](#section-6-implementation-recommendations)
7. [Section 7: Quality Control Checklist](#section-7-quality-control-checklist)

---

## Section 1: Executive Summary

### 📊 Statistik Filtering (v3.1 RSI-1)

| Metric | Angka | Keterangan |
|--------|-------|------------|
| **Total Input** | 345 kategori | Dataset Quick Draw Google (full release) |
| **TIER 1 (Recommended)** | 102 kategori | Medium difficulty only — food, nature, objects, vehicles |
| **TIER 2 (Conditional)** | 68 kategori | Butuh konteks/safety warning |
| **TIER 3 (Banned)** | 101 kategori | Hard no — total breakdown: |
| └ Type A (Geometric Primitives) | 9 | Out of scope — line, circle, square, dll |
| └ Type B (Sensitive) | 18 | Weapons, fire hazards, medical triggers |
| └ Type C (Not Educational) | 10 | Appliances, low-value items |
| └ Type D (Too Complex/Abstract) | 14 | Landmarks, mythology, weather phenomena |
| └ Type E (Animals — RSI-1) | 50 | ALL animals banned |
| **GOLDEN SET (Final)** | 116 kategori | Sweet spot — medium difficulty |

### 🎯 Alasan Utama Filtering (RSI-1 Sweet Spot)

1. **NO ANIMALS** — Semua hewan di-BAN karena:
   - **Stroke complexity tinggi** — butuh 15-30 stroke untuk body parts (legs, ears, tails, eyes)
   - **Confusion matrix antar hewan** — cat↔dog↔lion↔tiger↔bear mirip visual, CNN akurasi turun
   - **Memperlambat gameplay** — anak butuh waktu lama, bukan fast-paced lagi
2. **NO GEOMETRIC PRIMITIVES** — line, circle, square, triangle, zigzag, squiggle → out of scope, bukan object recognition target. Dihapus total dari analisis (jangan over-engineer dgn decoration mode).
3. **NO COMPLEX LANDMARKS** — Eiffel Tower, Mona Lisa, Great Wall, aircraft carrier → mustahil digambar dalam 20 detik. Hard ban tanpa conditional.
4. **FOKUS MEDIUM DIFFICULTY** — Everyday objects (clock, cup, hat, key, umbrella) + simple food (apple, donut, pizza slice) + nature (sun, moon, star, tree, flower, cloud) + basic vehicles (car, bus, bicycle). Stroke range 4-15.
5. **CHILD SAFETY** — Senjata (rifle, sword, knife, cannon) langsung di-BAN. Item fire hazard (matches, lighter) dan medical trigger (syringe, stitches) juga di-BAN. Bertentangan dgn arahan Bu Hesti ("objek berbahaya pakai duri, bukan pisau").

### 📐 Distribusi per Level (Golden Set v3.1)

| Level | Jumlah Kategori | Difficulty Range | Tujuan |
|-------|----------------|------------------|--------|
| **Level 1** (Tutorial/Warm-up) | ~60 kategori | ★☆☆☆☆ to ★★☆☆☆ | Top-1 prediction, high confidence (HITL L1) |
| **Level 2** (Core Gameplay) | ~40 kategori | ★★☆☆☆ to ★★★☆☆ | Top-3 + confidence (HITL L2) |
| **Level 3** (Challenge/Mastery) | ~20 kategori | ★★★★☆ to ★★★★★ | AI overconfident wrong, override (HITL L3) |
| **TOTAL** | **~120 kategori** | — | Sweet spot — medium difficulty only |

> **Catatan**: Golden Set v3.1 lebih kecil dari v3.0 (148 → ~120) karena hewan dan complex landmarks dihapus. Lebih fokus, lebih fast-paced.

### ✅ Selaras dengan Arahan Bu Hesti (16/6/26) + RSI-1

| Arahan | Implementasi |
|--------|--------------|
| "Hapus kategori dekoratif, pakai solid & danger saja" | TIER 3 Type A: line, square, circle, zigzag, squiggle, smiley face di-BAN. Duri (thorns) pakai `cactus` sebagai proxy. |
| "Objek berbahaya pakai 'duri' (thorns), bukan pisau" | TIER 3 Type B: rifle, sword, knife, cannon, axe, saw, drill di-BAN. `cactus` (dgn spikes) jadi danger object alternatif. |
| "3 level saja, jangan tambah" | Golden Set dibagi jadi Level 1/2/3 — tidak ada Level 4+. |
| "Maskot text bubble saja, tanpa suara/NLP" | Category selection tidak butuh interaksi suara. Momo kasih feedback via text bubble. |
| "Login wajib, butuh history" | SQL schema punya `category_id` → bisa tracking per-user history. |
| **RSI-1: NO ANIMALS** | Semua hewan di-BAN (Type E). Confusion matrix + stroke complexity di-document. |
| **RSI-1: NO GEOMETRIC PRIMITIVES** | line, circle, square, dll di-list sekali dgn alasan singkat, tidak over-engineered. |
| **RSI-1: NO COMPLEX LANDMARKS** | Eiffel Tower, Mona Lisa, Great Wall, aircraft carrier di-BAN (Type D). |

---

## Section 2: Kategorisasi Utama (3 Tier)

### 🟢 TIER 1: RECOMMENDED (Solid Gameplay — Medium Difficulty)

**Kriteria Inklusi (RSI-1 Sweet Spot):**
- Relevan dengan tema sketchbook/kreativitas/edukasi
- **Medium difficulty** (stroke 4-15, bukan 1-3 dan bukan 20+)
- Dikenal anak-anak Indonesia (familiar object)
- Visual distinctive (bisa dibedakan dari kategori lain)
- **BUKAN hewan** (RSI-1: animals banned)
- **BUKAN geometric primitive** (RSI-1: line/circle/square out of scope)
- **BUKAN landmark kompleks** (RSI-1: Eiffel Tower etc. banned)

**Total: 102 kategori**

| Nama Kategori | Alasan Include | Difficulty (1-5) | Level Rekomendasi | Notes |
|---------------|----------------|------------------|-------------------|-------|
| `apple` | Basic shape, universal fruit, distinctive tangkai | 2 | Level 1 | Tutorial ideal — bulat + tangkai |
| `banana` | Distinctive curve, universal fruit | 2 | Level 1 | Tutorial mudah — 1 curve + ujung |
| `donut` | Distinctive hole, familiar | 2 | Level 1 | Anti-confusion dgn circle (ada hole) |
| `lollipop` | Distinctive stick + circle | 2 | Level 1 | Tutorial bentuk dasar gabungan |
| `cookie` | Circle + chip details | 2 | Level 1 | Perlu chip detail biar tidak mirip circle |
| `ice cream` | Cone + scoop composition | 2 | Level 1 | Bisa tema musim panas |
| `carrot` | Triangle + leaves | 2 | Level 1 | Tutorial sayuran, simple shape |
| `mushroom` | Cap + stem, distinctive | 2 | Level 1 | Bisa tema hutan |
| `peanut` | Peanut shape (figure-8), Indonesia familiar | 2 | Level 1 | Local relevance — kacang |
| `string bean` | Long curve (kacang panjang), Indonesia familiar | 2 | Level 1 | Local relevance tinggi |
| `pear` | Distinctive from apple, simple shape | 2 | Level 1 | Variasi buah |
| `grapes` | Cluster of circles, pattern menarik | 2 | Level 2 | Cluster pattern — edukatif |
| `strawberry` | Heart-ish shape + seeds + leaves | 3 | Level 2 | Detail lebih banyak dari apple |
| `watermelon` | Oval + stripes, familiar (semangka) | 2 | Level 1 | Bisa dibelah — multi-state |
| `pineapple` | Oval + crown + texture pattern | 3 | Level 2 | Texture complexity — Level 2 |
| `broccoli` | Crown + stem, distinctive | 2 | Level 2 | Bisa lesson sayuran |
| `potato` | Lumpy oval, simple | 2 | Level 1 | Risk mirip batu — perlu context |
| `onion` | Simple oval + root lines | 2 | Level 1 | Bisa lesson dapur |
| `pizza` | Triangle slice + toppings | 3 | Level 2 | Slice vs whole — multi-state |
| `hamburger` | Stacked layers concept | 3 | Level 2 | Bisa ajarkan layering |
| `hot dog` | Long shape + bun, simple | 2 | Level 2 | Risk mirip sandwich — perlu detail |
| `sandwich` | Triangle + layers | 2 | Level 2 | Bisa ajarkan layering |
| `cake` | Layered shape + decoration | 3 | Level 2 | Birthday cake — multi-state |
| `birthday cake` | Special version dgn candles | 3 | Level 2 | Candle context — multi-state |
| `sun` | Circle + rays, universal | 2 | Level 1 | Tutorial ideal — circle + rays |
| `moon` | Crescent shape, distinctive | 2 | Level 1 | Bisa tema malam |
| `star` | 5-point geometric, universal | 2 | Level 1 | Tutorial geometric (5-point) |
| `cloud` | Cluster of bumps, distinctive | 2 | Level 1 | Bisa tema cuaca |
| `rain` | Cloud + drops, simple | 2 | Level 1 | Bisa tema cuaca |
| `rainbow` | Multi-color arcs, distinctive | 2 | Level 1 | Bisa lesson warna |
| `snowflake` | Symmetrical pattern, distinctive | 3 | Level 2 | Symmetry lesson |
| `snowman` | 3 circles + accessories | 3 | Level 2 | Bisa tema musim dingin |
| `tree` | Trunk + crown, universal | 2 | Level 1 | Bisa variasi: palm, pine, oak |
| `flower` | Center + petals, universal | 2 | Level 1 | Bisa variasi bentuk |
| `grass` | Multiple short lines (cluster) | 2 | Level 1 | Perlu context biar tidak terlalu simple |
| `leaf` | Simple vein pattern, distinctive | 2 | Level 1 | Bisa variasi bentuk daun |
| `mountain` | Triangle-based, simple | 2 | Level 1 | Bisa landscape composition |
| `ocean` | Wave lines, simple | 2 | Level 1 | Bisa tema laut |
| `river` | Curvy lines, simple | 2 | Level 1 | Bisa landscape |
| `beach` | Multi-part (sand + water + sun) | 3 | Level 2 | Composition lesson |
| `pond` | Oval + reflection lines | 2 | Level 2 | Bisa tema alam |
| `cactus` | Body + spikes, distinctive | 2 | Level 2 | Bisa tema gurun — proxy 'duri' |
| `palm tree` | Trunk + fronds, Indonesia familiar | 2 | Level 1 | Local relevance tinggi |
| `bush` | Cluster of curves, simple | 2 | Level 1 | Risk mirip cloud — perlu context |
| `house` | Square + triangle roof, universal | 2 | Level 1 | Tutorial ideal |
| `door` | Rectangle + knob, simple | 2 | Level 1 | Perlu detail biar tidak terlalu simple |
| `table` | Top + 4 legs, simple | 2 | Level 1 | Bisa ajarkan perspective |
| `chair` | Seat + back + legs, distinctive | 2 | Level 1 | Bisa ajarkan perspective |
| `bed` | Frame + pillow + blanket | 2 | Level 1 | Bisa tema kamar |
| `book` | Rectangle + spine, simple | 2 | Level 1 | Perlu detail biar tidak mirip rectangle |
| `clock` | Circle + hands, distinctive | 2 | Level 1 | Bisa lesson waktu |
| `alarm clock` | Clock + bells, distinctive | 2 | Level 1 | Bell detail — distinctive dari clock |
| `cup` | Circle + handle, simple | 2 | Level 1 | Perlu handle biar tidak mirip circle |
| `mug` | Body + handle, Indonesia familiar | 2 | Level 1 | Local relevance — ngopi culture |
| `hat` | Brim + crown, distinctive | 2 | Level 1 | Bisa variasi topi |
| `shoe` | Side view, distinctive | 2 | Level 1 | Bisa ajarkan side view |
| `backpack` | Body + straps, distinctive | 2 | Level 1 | Local relevance — anak sekolah |
| `key` | Circle + stem + teeth, distinctive | 2 | Level 1 | Bisa lesson 'membuka' |
| `umbrella` | Dome + handle, distinctive | 2 | Level 1 | Bisa tema hujan |
| `pencil` | Rectangle + tip, simple | 2 | Level 1 | Tutorial ideal |
| `flashlight` | Body + lens + button, distinctive | 2 | Level 2 | Bisa tema gelap |
| `floor lamp` | Base + pole + shade, distinctive | 2 | Level 1 | Bisa tema kamar |
| `fan` | Center + blades, Indonesia familiar | 2 | Level 1 | Local relevance — kipas angin |
| `teapot` | Body + spout + handle, distinctive | 2 | Level 2 | Bisa tema dapur |
| `telephone` | Handset classic, distinctive | 2 | Level 1 | Bisa lesson teknologi |
| `wheel` | Circle + spokes, distinctive | 2 | Level 1 | Tutorial geometric + spokes |
| `windmill` | Tower + 4 blades, distinctive | 3 | Level 2 | Blade complexity — Level 2 |
| `ladder` | 2 rails + rungs, distinctive | 2 | Level 1 | Bisa tema profesi |
| `mailbox` | Box + flag + post, distinctive | 2 | Level 2 | Bisa tema komunikasi |
| `picture frame` | Rectangle + inner border, simple | 2 | Level 1 | Perlu context biar tidak terlalu simple |
| `envelope` | Rectangle + flap, distinctive | 2 | Level 1 | Bisa tema surat |
| `bucket` | Body + handle, distinctive | 2 | Level 1 | Bisa tema pantai |
| `pillow` | Rounded rectangle, simple | 2 | Level 1 | Bisa tema kamar |
| `tent` | Triangle + door, distinctive | 2 | Level 2 | Bisa tema camping |
| `eyeglasses` | 2 lenses + bridge, distinctive | 2 | Level 1 | Bisa lesson vision |
| `camera` | Body + lens + viewfinder, distinctive | 3 | Level 2 | Bisa tema fotografi |
| `cell phone` | Body + screen, distinctive | 2 | Level 2 | Bisa context modern |
| `laptop` | Screen + keyboard base, distinctive | 2 | Level 2 | Bisa context modern |
| `headphones` | Band + 2 ear cups, distinctive | 3 | Level 2 | Bisa context 'musik' |
| `car` | Body + 2 wheels, universal | 2 | Level 1 | Tutorial ideal |
| `bicycle` | 2 wheels + frame, distinctive | 3 | Level 2 | Frame complexity — Level 2 |
| `bus` | Longer body + windows, distinctive | 2 | Level 1 | Bisa tema transportasi |
| `truck` | Cab + cargo, distinctive | 2 | Level 2 | Bisa tema konstruksi |
| `airplane` | Body + wings + tail, distinctive | 2 | Level 2 | Bisa tema perjalanan |
| `helicopter` | Body + rotor + tail, distinctive | 3 | Level 2 | Rotor detail — Level 2 |
| `train` | Body + wheels + chimney, distinctive | 2 | Level 2 | Bisa tema transportasi |
| `sailboat` | Hull + sail, distinctive | 2 | Level 2 | Bisa tema laut |
| `firetruck` | Truck + ladder, distinctive | 3 | Level 2 | Bisa tema profesi |
| `police car` | Car + siren, distinctive | 2 | Level 2 | Bisa tema profesi |
| `ambulance` | Van + red cross, distinctive | 2 | Level 2 | Bisa tema profesi |
| `school bus` | Bus + yellow color, distinctive | 2 | Level 1 | Local relevance — anak sekolah |
| `motorbike` | 2 wheels + frame, Indonesia familiar | 3 | Level 2 | Local relevance tinggi |
| `tractor` | Body + big wheels, distinctive | 3 | Level 2 | Bisa tema pertanian |
| `traffic light` | Pole + 3 lights, educational | 2 | Level 2 | Lesson safety jalan |
| `stop sign` | Octagon + text, educational | 2 | Level 2 | Lesson safety jalan |
| `helmet` | Dome + strap, safety lesson | 2 | Level 2 | Lesson safety berkendara |
| `bridge` | Deck + supports, structural concept | 3 | Level 3 | Reserve Level 3 — engineering concept |
| `castle` | Walls + towers, fantasy theme | 3 | Level 3 | Reserve Level 3 — detail banyak |
| `lighthouse` | Tower + light, coastal theme | 3 | Level 3 | Reserve Level 3 — coastal theme |
| `crown` | Base + spikes + jewels, distinctive | 2 | Level 2 | Bisa tema kerajaan |
| `diamond` | Geometric facets, distinctive | 2 | Level 2 | Bisa ajarkan shape |
| `hot air balloon` | Balloon + basket + ropes, distinctive | 3 | Level 3 | Reserve Level 3 — multi-part |

---

### 🟡 TIER 2: CONDITIONAL (Use with Caution)

**Kriteria Inklusi:**
- Medium difficulty tapi butuh **konteks khusus** agar masuk akal
- Atau perlu **safety warning** (tools, fire items, medical)
- Atau less familiar (music instruments, vintage items)
- **BUKAN hewan** (RSI-1)
- **BUKAN landmark kompleks** (RSI-1)

**Total: 68 kategori**

| Nama Kategori | Alasan Conditional | Syarat Penggunaan | Risk |
|---------------|-------------------|-------------------|------|
| `guitar` | Familiar tapi detail sulit | Pakai acoustic simple, bukan electric | Stroke complexity tinggi |
| `piano` | Familiar tapi sulit digambar | Pakai single keyboard row, bukan grand piano | Perspective complexity |
| `drums` | Familiar, multi-part | Pakai drumset simplified | Multi-part coordination |
| `flute` | Kurang familiar — pakai seruling? | Bisa rebrand sebagai 'seruling' Indonesia | Cultural context shift |
| `t-shirt` | Familiar tapi simple | Pakai dgn print pattern di depan | Risk terlalu simple |
| `pants` | Familiar tapi simple | Pakai dgn detail pocket/zipper | Risk terlalu simple |
| `shorts` | Familiar tapi simple | Pakai dgn detail pocket | Risk terlalu simple |
| `sweater` | Familiar, distinctive (sleeves) | Pakai dgn knit pattern | Stroke complexity medium |
| `sock` | Familiar tapi terlalu simple | Pakai dgn pattern (stripes) | Risk terlalu simple |
| `belt` | Familiar tapi terlalu simple | Pakai dgn buckle detail | Risk terlalu simple |
| `bowtie` | Distinctive tapi simple | Pakai sebagai accessory context | Risk terlalu simple |
| `bracelet` | Distinctive tapi simple | Pakai dgn charm detail | Risk terlalu simple |
| `necklace` | Distinctive tapi simple | Pakai dgn pendant detail | Risk terlalu simple |
| `wristwatch` | Familiar, distinctive | Pakai dgn time on dial | Detail complexity medium |
| `face` | Multi-part composition | Pakai sebagai tutorial wajah lengkap | Detail complexity tinggi |
| `hand` | Multi-part, bisa sulit | Pakai dgn simplified 4-finger cartoon | Detail complexity tinggi |
| `foot` | Simple, bisa sensitive | Pakai dgn context 'kaki' | Risk terlalu simple |
| `tooth` | Simple, bisa sensitive | Pakai dgn tema gigi sehat (lesson sikat gigi) | Risk medical trigger |
| `hammer` | Tool familiar, bisa berbahaya | Pakai dgn tema 'pertukangan' | Risk melukai jika direplikasi |
| `screwdriver` | Tool familiar, bisa berbahaya | Pakai dgn tema 'pertukangan' | Risk melukai jika direplikasi |
| `pliers` | Tool familiar, kurang menarik | Pakai dgn tema 'pertukangan' | Relevance rendah untuk anak |
| `shovel` | Tool familiar (cangkul) | Pakai dgn tema berkebun | Risk minimal |
| `rake` | Tool familiar (garu) | Pakai dgn tema berkebun | Risk minimal |
| `broom` | Tool familiar (sapu) | Pakai dgn tema pekerjaan rumah | Risk minimal |
| `scissors` | Tool familiar, bisa berbahaya | Pakai dgn safety warning + safety scissors design | Risk melukai medium |
| `paintbrush` | Tool familiar, aman | Pakai dgn tema melukis | Risk minimal |
| `paint can` | Tool familiar, aman | Pakai dgn tema melukis | Risk minimal |
| `marker` | Tool familiar (spidol), aman | Pakai dgn tema menulis | Risk minimal |
| `crayon` | Tool familiar, aman | Pakai dgn tema mewarnai | Risk minimal |
| `eraser` | Tool familiar, aman tapi simple | Pakai dgn context 'pensil' | Risk terlalu simple |
| `calculator` | Familiar, simple | Pakai dgn context 'matematika' | Risk terlalu simple |
| `calendar` | Familiar, simple | Pakai dgn context 'tanggal' | Risk terlalu simple |
| `computer` | Familiar, complex | Pakai simplified desktop | Detail complexity tinggi |
| `keyboard` | Familiar, complex | Pakai dgn context 'komputer' | Detail complexity tinggi |
| `radio` | Kurang familiar anak modern | Hanya jika ada tema retro/vintage | Relevance rendah |
| `remote control` | Familiar, simple | Pakai dgn context 'TV' | Risk terlalu simple |
| `compass` | Kurang familiar anak modern | Hanya jika ada tema 'petualangan' | Relevance rendah |
| `barn` | Kurang familiar di Indonesia | Hanya jika ada tema peternakan | Cultural familiarity rendah |
| `house plant` | Familiar, simple | Pakai dgn context 'dekorasi rumah' | Risk mirip 'flower' |
| `garden` | Multi-part composition | Pakai dgn context 'tanam bunga' | Composition complexity |
| `candle` | Familiar tapi fire hazard | Pakai dgn safety warning — di context 'ulang tahun' | Fire hazard jika direplikasi |
| `campfire` | Fire hazard jika direplikasi | Hanya jika ada tema 'survival/camping' dgn safety lesson | Fire hazard tinggi |
| `lantern` | Familiar, moderate risk | Pakai dgn context 'festival lampion' | Fire hazard medium |
| `basketball` | Familiar, simple | Pakai dgn context 'olahraga' | Risk terlalu simple (mirip circle) |
| `soccer ball` | Familiar (sepak bola Indonesia), distinctive pattern | Pakai dgn context 'olahraga' | Pattern complexity medium |
| `dumbbell` | Familiar, simple | Pakai dgn context 'olahraga' | Risk terlalu simple |
| `kite` | Distinctive, familiar (layang-layang) | Pakai dgn context 'bermain' — Indonesia relevance tinggi | Rebrand 'layang-layang' |
| `parachute` | Distinctive, familiar | Pakai dgn context 'dirgantara' | Detail complexity medium |
| `megaphone` | Kurang familiar anak | Pakai dgn context 'pengumuman' | Relevance rendah |
| `microphone` | Familiar, distinctive | Pakai dgn context 'menyanyi/pidato' | Relevance medium |
| `hourglass` | Distinctive, antique concept | Pakai dgn context 'waktu sejarah' | Relevance rendah modern |
| `feather` | Simple, distinctive | Pakai dgn context 'indah' | Risk terlalu simple |
| `passport` | Kurang familiar anak | Pakai dgn context 'perjalanan internasional' | Relevance rendah |
| `postcard` | Kurang familiar anak modern | Pakai dgn context 'surat' atau 'liburan' | Relevance rendah |
| `sleeping bag` | Kurang familiar di Indonesia | Hanya jika ada tema 'camping' | Cultural familiarity rendah |
| `vase` | Familiar, distinctive (bunga) | Pakai dgn context 'dekorasi' | Risk mirip 'flower pot' |
| `garden hose` | Familiar, simple | Pakai dgn context 'menyiram' | Risk terlalu simple |
| `fence` | Simple, distinctive | Pakai dgn context 'pagar rumah' | Risk terlalu simple |
| `stairs` | Simple, distinctive | Pakai dgn context 'naik turun' | Perspective complexity |
| `bandage` | Medical — borderline ban | Hanya jika ada tema 'P3K' — bisa OK dgn lesson safety | Injury context sensitive |
| `map` | Familiar tapi complex | Pakai simplified treasure map | Detail complexity tinggi |
| `axe` | Weapon-like — borderline ban | Hanya jika ada tema 'penebang kayu' profesional (safety warning) | Weapon risk medium |
| `drill` | Power tool, danger | Hanya jika ada tema 'pertukangan' dewasa | Injury risk tinggi |
| `matches` | Fire hazard tinggi — borderline ban | Hanya jika ada tema 'survival' khusus dgn safety lesson | Fire hazard tinggi |
| `lighter` | Fire hazard tinggi — borderline ban | Hanya jika ada tema 'survival' khusus | Fire hazard tinggi + weapon-like |
| `stethoscope` | Medical — borderline ban | Hanya jika ada tema 'dokter' — tapi risk trigger medical anxiety | Medical anxiety |
| `stove` | Burn hazard — borderline ban | Hanya jika ada tema 'memasak' dgn safety warning | Burn hazard |
| `oven` | Burn hazard — borderline ban | Hanya jika ada tema 'memanggang' dgn safety warning | Burn hazard |

---

### 🔴 TIER 3: BANNED / EXCLUDED (Hard No)

**Kriteria Eksklusi (5 Type — RSI-1):**
- **Type A (Geometric Primitives)**: line, circle, square, triangle, zigzag, squiggle, smiley → out of scope
- **Type B (Sensitive)**: weapons, fire hazards, medical triggers, alcohol, inappropriate
- **Type C (Not Educational)**: appliances, low-value items
- **Type D (Too Complex/Abstract)**: landmarks, mythology, weather phenomena
- **Type E (Animals — RSI-1)**: SEMUA hewan banned — stroke complexity + confusion matrix

**Total: 101 kategori di-BAN**

#### Type A: Geometric Primitives (Out of Scope) — 9 items

| Nama Kategori | Alasan Ban |
|---------------|------------|
| `line` | Geometric primitive — out of scope. Hanya 1 stroke, bukan object recognition. |
| `circle` | Geometric primitive — out of scope. |
| `square` | Geometric primitive — out of scope. |
| `triangle` | Geometric primitive — out of scope. |
| `hexagon` | Geometric primitive — out of scope. |
| `octagon` | Geometric primitive — out of scope. (Note: 'stop sign' punya octagon shape TAPI dengan text 'STOP' — distinct). |
| `zigzag` | Geometric primitive / pattern — out of scope dari core drawing. Bisa dipakai di 'decoration mode' terpisah. |
| `squiggle` | Random line, no semantic meaning — out of scope. |
| `smiley face` | Single-stroke composition (lingkaran + 2 titik + 1 kurva). Pakai sebagai UI emotion indicator, bukan draw target. |

#### Type B: Inappropriate / Sensitive — 18 items

| Nama Kategori | Alasan Ban |
|---------------|------------|
| `skull` | Konotasi kematian/kekerasan — tidak cocok untuk anak SMP. Risiko trigger trauma. |
| `rifle` | Senjata api — dilarang keras. Bertentangan dgn arahan Bu Hesti: 'objek berbahaya pakai duri, bukan pisau'. |
| `cannon` | Senjata artileri — dilarang keras. |
| `sword` | Senjata tajam — dilarang keras. Pakai 'duri' (cactus) sebagai danger object. |
| `knife` | Senjata tajam — dilarang keras. Pakai 'duri' (cactus) sebagai danger object. |
| `syringe` | Medical trauma trigger — anak bisa fobia jarum suntik. |
| `matches` | Fire hazard tinggi — anak bisa coba replikasi. Hard ban. |
| `lighter` | Fire hazard + weapon-like. Hard ban. |
| `drill` | Power tool berbahaya — anak bisa coba pakai. Hard ban. |
| `axe` | Weapon-like. Hard ban. Pakai 'duri' (cactus) untuk danger. |
| `saw` | Mata pisau berbahaya. Hard ban. Anak bisa coba replikasi. |
| `underwear` | Tidak pantas untuk game anak — bisa jadi joke target inappropriate. |
| `wine bottle` | Alkohol — tidak pantas untuk anak. Dilarang keras. |
| `wine glass` | Alkohol — tidak pantas untuk anak. Dilarang keras. |
| `toilet` | Bisa jadi joke target inappropriate — low educational value. |
| `jail` | Tema penjara tidak cocok untuk game edukasi anak. |
| `stitches` | Medical graphic — bisa trigger trauma luka. Hard ban. |
| `fireplace` | Fire hazard + kurang familiar Indonesia. Hard ban. |

#### Type C: Out of Scope / Not Educational — 10 items

| Nama Kategori | Alasan Ban |
|---------------|------------|
| `spreadsheet` | Terlalu corporate/boring — tidak relevan untuk game anak. |
| `power outlet` | DANGER: Anak bisa coba colok-colok — listrik hazard. Hindari. |
| `stove` | Burn hazard + low educational value. |
| `oven` | Burn hazard + low educational value. |
| `microwave` | Burn hazard + radiation concern. Hindari untuk anak. |
| `dishwasher` | Appliance rumah — low educational value. |
| `washing machine` | Appliance rumah — low educational value. |
| `hospital` | Medical setting — borderline. Default: BAN kecuali tema 'profesi kesehatan' khusus. |
| `fire hydrant` | Low educational value — tidak relevan Indonesia (jarang ada hydrant umum). |
| `cigarette` | (Tidak ada di dataset Quick Draw asli — listed untuk documentation) Dilarang keras. |

#### Type D: Too Complex / Frustrating / Abstract — 14 items

| Nama Kategori | Alasan Ban |
|---------------|------------|
| `The Mona Lisa` | Mustahil untuk anak gambar dalam 20 detik — karya seni kompleks. Hindari total. |
| `The Great Wall of China` | Landscape kompleks — terlalu sulit. Hindari. |
| `The Eiffel Tower` | Landmark Western — terlalu kompleks untuk fast-paced drawing. Hindari. |
| `aircraft carrier` | Terlalu kompleks (detail dek, menara, pesawat) — bukan target gambar fast-paced. Hindari. |
| `animal migration` | Konsep abstrak — bukan object. Break down menjadi 'burung terbang' atau implement sebagai path-drawing mechanic terpisah. |
| `camouflage` | Konsep pattern — bukan object. Hindari dari drawing mode core. |
| `hurricane` | Weather phenomenon — bukan object. Implement sebagai efek (animasi) bukan draw target. |
| `tornado` | Weather phenomenon — bukan object. Sama seperti hurricane. |
| `lightning` | Weather phenomenon — bukan object. Bisa jadi 'pattern' dekoratif saja (mirip zigzag di decoration mode). |
| `brain` | Anatomi kompleks — sulit digambar anak. Hindari. |
| `mermaid` | Mitologi — body detail kompleks. Hindari kecuali tema dongeng khusus. |
| `dragon` | Mitologi — body detail kompleks. Hindari kecuali tema fantasy khusus. |
| `angel` | Religious + body detail kompleks. Hindari total. |
| `flying saucer` | Sci-fi — body detail kompleks. Hindari kecuali tema 'luar angkasa' khusus. |

#### Type E: Animals (RSI-1 BAN) — 50 items

| Nama Kategori | Alasan Ban |
|---------------|------------|
| `mosquito` | Animal — dilarang (RSI-1). Tambahan: vector penyakit (demam berdarah di Indonesia). |
| `cat` | RSI-1: Animal banned. Stroke complexity + confusion matrix dgn dog/lion/tiger/bear. |
| `dog` | RSI-1: Animal banned. Confusion matrix dgn cat/wolf/fox. |
| `elephant` | RSI-1: Animal banned. Multi-part (body + trunk + tusks + 4 legs) — too complex. |
| `giraffe` | RSI-1: Animal banned. Multi-part (long neck + spots + 4 legs). |
| `lion` | RSI-1: Animal banned. Mane detail + confusion matrix dgn cat. |
| `tiger` | RSI-1: Animal banned. Stripe pattern + confusion matrix dgn cat/lion. |
| `bear` | RSI-1: Animal banned. Confusion matrix dgn dog (large). |
| `rabbit` | RSI-1: Animal banned. Long ears + confusion matrix dgn hare. |
| `horse` | RSI-1: Animal banned. 4 legs complex + body proportion. |
| `cow` | RSI-1: Animal banned. Multi-part (udder + horns + 4 legs). |
| `pig` | RSI-1: Animal banned. Snout detail + confusion matrix dgn dog. |
| `duck` | RSI-1: Animal banned. Beak + body + legs. |
| `frog` | RSI-1: Animal banned. Legs detail. |
| `monkey` | RSI-1: Animal banned. Tail + body proportion. |
| `penguin` | RSI-1: Animal banned. Wing + beak + feet. |
| `panda` | RSI-1: Animal banned. Eye patches + confusion matrix dgn bear. |
| `kangaroo` | RSI-1: Animal banned. Pouch + tail + legs. |
| `owl` | RSI-1: Animal banned. Big eyes + wing detail. |
| `whale` | RSI-1: Animal banned. Body + fin + spout. |
| `dolphin` | RSI-1: Animal banned. Body + fin + smile. |
| `shark` | RSI-1: Animal banned. Dorsal fin + teeth detail. |
| `octopus` | RSI-1: Animal banned. 8 tentacles — too complex. |
| `crab` | RSI-1: Animal banned. Claws + 8 legs. |
| `snail` | RSI-1: Animal banned. Spiral shell detail. |
| `snake` | RSI-1: Animal banned. Curvy body — risk mirip 'squiggle'. |
| `spider` | RSI-1: Animal banned. 8 legs + confusion matrix dgn tick. |
| `squirrel` | RSI-1: Animal banned. Bushy tail detail. |
| `swan` | RSI-1: Animal banned. Curved neck — too complex. |
| `hedgehog` | RSI-1: Animal banned. Many spikes. |
| `flamingo` | RSI-1: Animal banned. 1 leg balance + curved neck. |
| `parrot` | RSI-1: Animal banned. Curved beak + tail feathers. |
| `raccoon` | RSI-1: Animal banned. Mask + striped tail. |
| `rhinoceros` | RSI-1: Animal banned. Horn + thick legs. |
| `crocodile` | RSI-1: Animal banned. Teeth + tail — too complex. |
| `sea turtle` | RSI-1: Animal banned. Shell + flippers. |
| `ant` | RSI-1: Animal banned. 3-circle body tapi terlalu simple (1-3 stroke). |
| `bee` | RSI-1: Animal banned. Stripes + wings. |
| `zebra` | RSI-1: Animal banned. Stripes + confusion matrix dgn horse. |
| `fish` | RSI-1: Animal banned. Simple oval tapi terlalu generic + confusion matrix dgn shark/whale. |
| `bird` | RSI-1: Animal banned. Generic + confusion matrix dgn owl/duck/penguin. |
| `butterfly` | RSI-1: Animal banned. Symmetric wings — confusion matrix dgn moth. |
| `camel` | RSI-1: Animal banned. Hump + 4 legs. |
| `bat` | RSI-1: Animal banned. Wing membrane detail. |
| `lobster` | RSI-1: Animal banned. Claws + many legs. |
| `sheep` | RSI-1: Animal banned. Wool texture + confusion matrix dgn cloud. |
| `mouse` | RSI-1: Animal banned. Tail + ear detail + confusion matrix dgn rat. |
| `goatee` | RSI-1: Animal part banned. |
| `beard` | RSI-1: Animal part banned. |
| `moustache` | RSI-1: Animal part banned. |

---

## Section 3: Special Category Handling

Special cases berkurang dari v3.0 (10 → 8) karena RSI-1 menghapus over-engineering (decoration mode, belajar bentuk mode, dll).

### Case Study: `Geometric Primitives (line, circle, square, triangle, zigzag, squiggle)`

**Problem:** Geometric primitives bukan object recognition target — out of scope. Sebelumnya aku terlalu detail bahas case-by-case (mode decoration, mode belajar bentuk, dll). Itu over-engineering.

**Solution:** HAPUS TOTAL dari analisis. Jangan bahas. Jangan list di special cases berulang. Hanya 1 line exclusion note.

**Implementation Idea:** Di TIER 3 BANNED list, geometric primitives di-list sekali dengan alasan singkat 'out of scope — geometric primitive'. Tidak perlu decoration mode, tidak perlu belajar bentuk mode. Out of scope, period.

**Verdict:** HAPUS TOTAL. Jangan over-engineer dengan mode khusus.

---

### Case Study: `All Animals (cat, dog, elephant, lion, tiger, bear, horse, dll)`

**Problem:** Animals punya 3 masalah serius untuk fast-paced drawing game: (1) Stroke complexity tinggi — butuh 15-30 stroke untuk detail body parts (legs, ears, tails, eyes). (2) Confusion matrix antar hewan sangat tinggi — cat↔dog↔lion↔tiger↔bear mirip secara visual, CNN akurasi turun. (3) Memperlambat gameplay — anak butuh waktu lama untuk gambar detail, bukan fast-paced lagi.

**Solution:** BAN SEMUA hewan dari game. Tidak ada TIER 2 conditional, tidak ada exception. Pure ban.

**Implementation Idea:** Semua hewan di-list di TIER 3 Type E (Animal Ban) dengan alasan 'RSI-1: Animal banned'. Confusion matrix antar hewan cat↔dog↔lion↔tiger↔bear di-document sebagai bukti masalah.

**Verdict:** BANNED — semua hewan, tanpa exception. Game ini fokus ke objects + food + nature + vehicles.

---

### Case Study: `Complex Landmarks (Eiffel Tower, Mona Lisa, Great Wall, aircraft carrier)`

**Problem:** Landmark dan oversized items (aircraft carrier punya dek + menara + pesawat, Eiffel Tower punya banyak lattice, Mona Lisa adalah portrait kompleks) mustahil digambar dalam 20 detik oleh anak SMP.

**Solution:** Hard ban tanpa conditional. Sebelumnya aku masih allow Eiffel Tower di TIER 2 conditional untuk 'landmark mode' — itu salah.

**Implementation Idea:** Semua landmark + oversized items di-list di TIER 3 Type D dengan alasan spesifik per item.

**Verdict:** BANNED — semua landmark & oversized items.

---

### Case Study: `Abstract Concepts (animal migration, camouflage, hurricane, tornado, lightning)`

**Problem:** Konsep abstrak (perpindahan massal, pattern penyembunyian, fenomena cuaca) bukan object fisik — sulit dinilai konsistensi gambar.

**Solution:** Hard ban dari core drawing. Lightning boleh sebagai pattern dekoratif (sama seperti zigzag) — tapi di decoration mode terpisah, bukan core gameplay.

**Implementation Idea:** Di-list di TIER 3 Type D dengan alasan 'abstract concept — not physical object'.

**Verdict:** BANNED dari core drawing. Lightning: ALLOW di decoration mode (terpisah).

---

### Case Study: `Single-Stroke Items (smiley face, eye, dot)`

**Problem:** Item yang bisa digambar dalam 1-3 stroke tidak ada cognitive challenge — anak bisa 'menang' tanpa effort.

**Solution:** Hard ban. Untuk smiley face, pakai sebagai UI emotion indicator (Momo expression), bukan draw target.

**Implementation Idea:** Di-list di TIER 3 Type A (Out of Scope — Single Stroke).

**Verdict:** BANNED dari draw target. smiley: ALLOW sebagai UI emotion indicator.

---

### Case Study: `Body Parts (standalone eye, ear, mouth, nose, etc)`

**Problem:** Standalone body parts terlalu simple (eye = lingkaran + titik, ear = curve) dan bisa sensitive. Tapi 'face' composition OK karena multi-part.

**Solution:** Standalone body parts: BAN. Composition (face, full body): TIER 2 conditional.

**Implementation Idea:** Eye/ear/mouth/etc hanya muncul sebagai KOMPONEN dalam quest 'gambar wajah lengkap'. Tidak pernah muncul sebagai target gambar tersendiri.

**Verdict:** Standalone: BAN. As component in composition: TIER 2 conditional.

---

### Case Study: `Mythology / Fantasy (mermaid, dragon, angel, flying saucer)`

**Problem:** Mitologi/fantasy/sci-fi punya body detail kompleks (mermaid = woman + fish tail, dragon = lizard + wings + fire). Sulit dinilai konsistensi gambar anak.

**Solution:** Hard ban. Jangan bikin 'fantasy mode' expansion — over-engineering.

**Implementation Idea:** Di-list di TIER 3 Type D dengan alasan 'mythology/fantasy — body detail complex'.

**Verdict:** BANNED — semua mythology/fantasy items.

---

### Case Study: `Fire Items (fire standalone, fireplace, campfire, candle)`

**Problem:** Fire hazard — anak bisa coba replikasi di real life. 'fire' standalone juga konsep abstrak (animasi, bukan object).

**Solution:** Pakai 'candle' (di context ulang tahun) dan 'campfire' (di context survival dgn safety lesson) saja di TIER 2. 'fire' standalone & 'fireplace' BAN.

**Implementation Idea:** Candle hanya muncul saat quest 'ulang tahun Momo' — dgn safety warning. Campfire hanya muncul saat quest 'survival' — dgn safety lesson. 'fire' standalone tidak pernah muncul sebagai draw target.

**Verdict:** candle & campfire: TIER 2 conditional. fireplace & fire standalone: BAN.

---

## Section 4: Proposed Final List (Golden Set v3.1)

Golden Set v3.1 — 116 kategori, **medium difficulty only** (NO animals, NO geometric primitives, NO complex landmarks):

### Level 1 (Tutorial/Warm-up) — Difficulty ★☆☆☆☆ to ★★☆☆☆

**Total: 57 kategori**

| Kategori | Difficulty | Tema | Catatan Implementasi |
|----------|-----------|------|----------------------|
| `apple` | 2 | food | Tutorial ideal — bulat + tangkai |
| `banana` | 2 | food | Curve distinctive |
| `donut` | 2 | food | Circle with hole |
| `lollipop` | 2 | food | Circle + stick |
| `cookie` | 2 | food | Circle + chip details |
| `ice cream` | 2 | food | Cone + scoop |
| `carrot` | 2 | food | Triangle + leaves |
| `mushroom` | 2 | food | Cap + stem |
| `peanut` | 2 | food | Figure-8 shape (Indonesia) |
| `string bean` | 2 | food | Long curve (Indonesia) |
| `pear` | 2 | food | Distinctive dari apple |
| `watermelon` | 2 | food | Oval + stripes |
| `potato` | 2 | food | Lumpy oval |
| `onion` | 2 | food | Oval + root lines |
| `sun` | 2 | nature | Circle + rays |
| `moon` | 2 | nature | Crescent shape |
| `star` | 2 | nature | 5-point geometric |
| `cloud` | 2 | nature | Cluster of bumps |
| `rain` | 2 | nature | Cloud + drops |
| `rainbow` | 2 | nature | Multi-color arcs |
| `tree` | 2 | nature | Trunk + crown |
| `flower` | 2 | nature | Center + petals |
| `grass` | 2 | nature | Cluster of short lines |
| `leaf` | 2 | nature | Vein pattern |
| `mountain` | 2 | nature | Triangle-based |
| `palm tree` | 2 | nature | Trunk + fronds (Indonesia) |
| `house` | 2 | objects | Square + triangle roof |
| `door` | 2 | objects | Rectangle + knob |
| `table` | 2 | objects | Top + 4 legs |
| `chair` | 2 | objects | Seat + back + legs |
| `bed` | 2 | objects | Frame + pillow |
| `book` | 2 | objects | Rectangle + spine |
| `clock` | 2 | objects | Circle + hands |
| `alarm clock` | 2 | objects | Clock + bells |
| `cup` | 2 | objects | Circle + handle |
| `mug` | 2 | objects | Body + handle (Indonesia) |
| `hat` | 2 | objects | Brim + crown |
| `shoe` | 2 | objects | Side view |
| `backpack` | 2 | objects | Body + straps |
| `key` | 2 | objects | Circle + stem + teeth |
| `umbrella` | 2 | objects | Dome + handle |
| `pencil` | 2 | objects | Rectangle + tip |
| `fan` | 2 | objects | Center + blades (Indonesia) |
| `telephone` | 2 | objects | Handset classic |
| `wheel` | 2 | objects | Circle + spokes |
| `ladder` | 2 | objects | 2 rails + rungs |
| `picture frame` | 2 | objects | Rectangle + inner border |
| `envelope` | 2 | objects | Rectangle + flap |
| `bucket` | 2 | objects | Body + handle |
| `pillow` | 2 | objects | Rounded rectangle |
| `eyeglasses` | 2 | objects | 2 lenses + bridge |
| `floor lamp` | 2 | objects | Base + pole + shade |
| `car` | 2 | vehicles | Body + 2 wheels |
| `bus` | 2 | vehicles | Longer body + windows |
| `school bus` | 2 | vehicles | Bus + yellow (Indonesia) |
| `train` | 2 | vehicles | Body + wheels + chimney |
| `sailboat` | 2 | vehicles | Hull + sail |

### Level 2 (Core Gameplay) — Difficulty ★★☆☆☆ to ★★★☆☆

**Total: 41 kategori**

| Kategori | Difficulty | Tema | Catatan Implementasi |
|----------|-----------|------|----------------------|
| `pizza` | 3 | food | Triangle slice + toppings |
| `hamburger` | 3 | food | Stack: bun + patty + lettuce |
| `hot dog` | 2 | food | Long shape + bun |
| `sandwich` | 2 | food | Triangle + layers |
| `cake` | 3 | food | Layers + decoration |
| `birthday cake` | 3 | food | Cake + candles |
| `grapes` | 2 | food | Cluster of circles |
| `strawberry` | 3 | food | Heart-ish + seeds + leaves |
| `pineapple` | 3 | food | Oval + crown + texture |
| `broccoli` | 2 | food | Crown + stem |
| `snowflake` | 3 | nature | Symmetrical pattern |
| `snowman` | 3 | nature | 3 circles + accessories |
| `beach` | 3 | nature | Sand + water + sun |
| `pond` | 2 | nature | Oval + reflection |
| `cactus` | 2 | nature | Body + spikes (proxy duri) |
| `ocean` | 2 | nature | Wave lines |
| `river` | 2 | nature | Curvy lines |
| `bush` | 2 | nature | Cluster of curves |
| `flashlight` | 2 | objects | Body + lens + button |
| `teapot` | 2 | objects | Body + spout + handle |
| `windmill` | 3 | objects | Tower + 4 blades |
| `mailbox` | 2 | objects | Box + flag + post |
| `tent` | 2 | objects | Triangle + door |
| `camera` | 3 | objects | Body + lens + viewfinder |
| `cell phone` | 2 | objects | Body + screen |
| `laptop` | 2 | objects | Screen + keyboard base |
| `headphones` | 3 | objects | Band + 2 ear cups |
| `bicycle` | 3 | vehicles | 2 wheels + frame |
| `truck` | 2 | vehicles | Cab + cargo |
| `airplane` | 2 | vehicles | Body + wings + tail |
| `helicopter` | 3 | vehicles | Body + rotor + tail |
| `firetruck` | 3 | vehicles | Truck + ladder |
| `police car` | 2 | vehicles | Car + siren |
| `ambulance` | 2 | vehicles | Van + red cross |
| `motorbike` | 3 | vehicles | 2 wheels + frame (Indonesia) |
| `tractor` | 3 | vehicles | Body + big wheels |
| `traffic light` | 2 | safety | Pole + 3 lights |
| `stop sign` | 2 | safety | Octagon + text |
| `helmet` | 2 | safety | Dome + strap |
| `crown` | 2 | objects | Base + spikes + jewels |
| `diamond` | 2 | objects | Geometric facets |

### Level 3 (Challenge/Mastery) — Difficulty ★★★★☆ to ★★★★★

**Total: 18 kategori**

| Kategori | Difficulty | Tema | Catatan Implementasi |
|----------|-----------|------|----------------------|
| `garden` | 3 | nature | Multi-flower composition |
| `computer` | 3 | objects | Monitor + keyboard + mouse |
| `keyboard` | 3 | objects | Many keys layout |
| `map` | 3 | objects | Folded paper + paths + X |
| `hourglass` | 3 | objects | Frame + 2 bulbs + sand |
| `vase` | 3 | objects | Body + neck + flowers |
| `feather` | 2 | objects | Spine + barbs |
| `hot air balloon` | 3 | vehicles | Balloon + basket + ropes |
| `parachute` | 3 | objects | Canopy + strings + load |
| `bridge` | 3 | objects | Deck + supports (engineering) |
| `castle` | 3 | objects | Walls + towers (fantasy) |
| `lighthouse` | 3 | objects | Tower + light (coastal) |
| `guitar` | 3 | music | Body + neck + strings |
| `piano` | 3 | music | Keys + body |
| `drums` | 3 | music | Multiple drums + cymbals |
| `face` | 3 | body | Composition: eyes + nose + mouth |
| `hand` | 3 | body | Palm + 4 fingers + thumb |
| `foot` | 2 | body | Sole + toes |

---

## Section 5: Thematic Grouping (Alternative Organization)

Themes v3.1 — **NO Animal Kingdom theme** (RSI-1: animals banned). Focus pada objects, food, nature, vehicles:

### Theme A: Food & Kitchen (~25 items)

`apple`, `banana`, `carrot`, `broccoli`, `pizza`, `hamburger`, `hot dog`, `ice cream`, `cake`, `birthday cake`, `donut`, `cookie`, `grapes`, `strawberry`, `watermelon`, `pineapple`, `peanut`, `pear`, `mushroom`, `onion`, `potato`, `string bean`, `sandwich`, `lollipop`, `mug`, `cup`, `teapot`

### Theme B: Nature & Environment (~20 items)

`tree`, `flower`, `grass`, `mountain`, `ocean`, `river`, `rainbow`, `cloud`, `sun`, `moon`, `star`, `snowflake`, `snowman`, `rain`, `cactus`, `palm tree`, `beach`, `pond`, `bush`, `leaf`, `garden`

### Theme C: Vehicles & Transport (~14 items)

`car`, `bicycle`, `bus`, `truck`, `airplane`, `helicopter`, `sailboat`, `train`, `tractor`, `ambulance`, `firetruck`, `police car`, `school bus`, `motorbike`, `hot air balloon`, `parachute`

### Theme D: Everyday Objects (~30 items)

`house`, `door`, `table`, `chair`, `bed`, `floor lamp`, `clock`, `alarm clock`, `hourglass`, `key`, `telephone`, `cell phone`, `computer`, `laptop`, `keyboard`, `camera`, `book`, `pencil`, `flashlight`, `fan`, `teapot`, `wheel`, `windmill`, `ladder`, `mailbox`, `picture frame`, `envelope`, `bucket`, `pillow`, `tent`, `eyeglasses`, `headphones`, `vase`, `feather`, `map`

### Theme E: Safety & Traffic (~5 items)

`stop sign`, `traffic light`, `helmet`, `firetruck`, `ambulance`, `police car`

### Theme F: Musical Instruments (~5 items, Level 3 only)

`guitar`, `piano`, `drums`, `flute`

### Theme G: Clothes & Accessories (~10 items, conditional)

`t-shirt`, `pants`, `shoe`, `hat`, `sweater`, `sock`, `belt`, `bowtie`, `bracelet`, `necklace`, `wristwatch`, `eyeglasses`, `shorts`, `backpack`, `umbrella`, `helmet`

### Theme H: Body Parts & People (Use Carefully! ~3 items)

`face`, `hand`, `foot`, `tooth`

### Theme I: Buildings & Places (~5 items)

`house`, `bridge`, `castle`, `lighthouse`, `tent`, `barn`

### Theme J: Structural / Fantasy (~5 items)

`crown`, `diamond`, `bridge`, `castle`, `lighthouse`

### 🇮🇩 Indonesian Cultural Relevance Highlight

Beberapa kategori punya **local relevance tinggi** untuk anak Indonesia (bisa di-prioritize):
- `palm tree` (pohon palem) — familiar
- `motorbike` (motor) — transportasi umum
- `string bean` (kacang panjang) — sayuran lokal
- `peanut` (kacang) — familiar
- `fan` (kipas angin) — iklim tropis
- `mug` (cangkir) — budaya ngopi
- `school bus` — anak sekolah
- `kite` (layang-layang) — permainan tradisional
- `cactus` — proxy "duri" (sesuai arahan Bu Hesti)

Bisa dijadikan **default tutorial objects** untuk Level 1 di Indonesia.

---
## Section 6: Implementation Recommendations

### A. Database Schema Proposal (v3.1 RSI-1)

Schema SQLite siap pakai untuk Dias — dengan ban_type 'E' (Animal) sebagai RSI-1 enforcement:

```sql
-- ============================================================
-- SCHEMA: Quick Draw Categories untuk Sketchbook Universe
-- Database: SQLite (sesuai spec Dias)
-- Version: 3.1 (RSI-1 — Sweet Spot Filter applied)
-- ============================================================

CREATE TABLE quickdraw_categories (
    category_id      TEXT PRIMARY KEY,         -- e.g. 'apple', 'house', 'sun'
    name             TEXT NOT NULL,            -- Display name
    name_id          TEXT,                     -- Indonesian name (e.g. 'Apel')
    tier             TEXT NOT NULL             -- 'RECOMMENDED' | 'CONDITIONAL' | 'BANNED'
                     CHECK(tier IN ('RECOMMENDED', 'CONDITIONAL', 'BANNED')),
    difficulty       INTEGER CHECK(difficulty BETWEEN 1 AND 5),  -- 1=easy, 5=hard
    theme            TEXT,                     -- 'food', 'nature', 'vehicles', 'objects', 'safety', 'music', 'clothes', 'body', 'buildings'
    level_assignment INTEGER CHECK(level_assignment BETWEEN 1 AND 3),  -- NULL if banned
    stroke_complexity TEXT CHECK(stroke_complexity IN ('LOW', 'MEDIUM', 'HIGH')),
    is_abstract      INTEGER DEFAULT 0,        -- 1 if concept (not object)
    ban_reason       TEXT,                     -- NULL if not banned
    ban_type         TEXT CHECK(ban_type IN ('A', 'B', 'C', 'D', 'E', NULL)),
                     -- A=Geometric primitive, B=Sensitive, C=Not Educational,
                     -- D=Too Complex/Abstract, E=Animal (RSI-1)
    special_instructions TEXT,                 -- For conditional items
    safety_warning   TEXT,                     -- For items needing safety context
    confusion_with   TEXT,                     -- Comma-separated list of similar categories
    created_at       TEXT DEFAULT (datetime('now')),
    updated_at       TEXT DEFAULT (datetime('now'))
);

-- Index untuk filtering cepat
CREATE INDEX idx_tier_level ON quickdraw_categories(tier, level_assignment);
CREATE INDEX idx_theme      ON quickdraw_categories(theme);
CREATE INDEX idx_difficulty ON quickdraw_categories(difficulty);
CREATE INDEX idx_ban_type   ON quickdraw_categories(ban_type);

-- ============================================================
-- CONTOH DATA (seed data untuk 10 kategori pertama — sesuai RSI-1)
-- ============================================================
INSERT INTO quickdraw_categories VALUES
('apple',     'Apple',     'Apel',       'RECOMMENDED', 2, 'food',     1, 'LOW',    0, NULL, NULL, NULL, NULL, NULL, 'Tutorial ideal: bulat + tangkai', NULL, 'pear,watermelon', datetime('now'), datetime('now')),
('house',     'House',     'Rumah',      'RECOMMENDED', 2, 'objects',  1, 'LOW',    0, NULL, NULL, NULL, NULL, NULL, 'Tutorial ideal: square + triangle', NULL, 'barn,church', datetime('now'), datetime('now')),
('sun',       'Sun',       'Matahari',   'RECOMMENDED', 2, 'nature',   1, 'LOW',    0, NULL, NULL, NULL, NULL, NULL, 'Tutorial ideal: circle + rays', NULL, 'moon,star', datetime('now'), datetime('now')),
('line',      'Line',      'Garis',      'BANNED',      NULL, NULL, NULL, 'LOW', 0, 'Geometric primitive — out of scope', 'A', NULL, NULL, NULL, NULL, NULL, NULL, 'circle,square', datetime('now'), datetime('now')),
('cat',       'Cat',       'Kucing',     'BANNED',      NULL, NULL, NULL, NULL, 0, 'RSI-1: Animal banned — stroke complexity + confusion matrix dgn dog/lion/tiger/bear', 'E', NULL, NULL, NULL, NULL, NULL, NULL, 'dog,lion,tiger,bear', datetime('now'), datetime('now')),
('rifle',     'Rifle',     'Senapan',    'BANNED',      NULL, NULL, NULL, NULL, 0, 'Senjata — dilarang keras (Bu Hesti)', 'B', NULL, NULL, NULL, NULL, NULL, NULL, 'cannon', datetime('now'), datetime('now')),
('guitar',    'Guitar',    'Gitar',      'CONDITIONAL', 3, 'music',    3, 'HIGH',   0, NULL, NULL, NULL, NULL, NULL, 'Pakai acoustic simple, bukan electric', NULL, 'piano,violin', datetime('now'), datetime('now')),
('cactus',    'Cactus',    'Kaktus',     'RECOMMENDED', 2, 'nature',   2, 'MEDIUM', 0, NULL, NULL, NULL, NULL, NULL, 'Bisa tema gurun — link ke duri', NULL, 'tree,bush', datetime('now'), datetime('now')),
('candle',    'Candle',    'Lilin',      'CONDITIONAL', 2, 'objects',  2, 'LOW',    0, NULL, NULL, NULL, 'Fire hazard jika direplikasi', NULL, 'Pakai dgn safety warning di context ulang tahun', 'Jangan nyalakan tanpa orang dewasa', 'campfire,fireplace', datetime('now'), datetime('now')),
('aircraft_carrier', 'Aircraft Carrier', 'Kapal Induk', 'BANNED', NULL, NULL, NULL, NULL, 0, 'RSI-1: Terlalu kompleks (dek + menara + pesawat) — bukan fast-paced target', 'D', NULL, NULL, NULL, NULL, NULL, NULL, 'cruise_ship,submarine', datetime('now'), datetime('now'));
```

### B. API Endpoints (v3.1 RSI-1)

Spesifikasi endpoint dengan `exclude_animals` default true (RSI-1 enforcement):

```
# ============================================================
# API ENDPOINTS — Quick Draw Categories (v3.1 RSI-1)
# Backend: Dias (Express.js + SQLite)
# ============================================================

## GET /api/v1/categories
Get filtered list of categories.

### Query Parameters:
- tier: 'RECOMMENDED' | 'CONDITIONAL' | 'BANNED' (default: RECOMMENDED)
- level: 1 | 2 | 3 (optional — filter by level assignment)
- theme: 'food' | 'nature' | 'vehicles' | 'objects' | 'safety' | 'music' | 'clothes' | 'body' | 'buildings' (optional)
- difficulty_min: 1-5 (optional)
- difficulty_max: 1-5 (optional)
- limit: int (default: 50, max: 200)
- offset: int (default: 0)
- exclude_animals: bool (default: true — RSI-1: animals auto-excluded)

### Response 200 OK:
{
  "total": 70,
  "categories": [
    {
      "category_id": "apple",
      "name": "Apple",
      "name_id": "Apel",
      "tier": "RECOMMENDED",
      "difficulty": 2,
      "theme": "food",
      "level_assignment": 1,
      "stroke_complexity": "LOW",
      "safety_warning": null,
      "confusion_with": ["pear", "watermelon"],
      "special_instructions": "Tutorial ideal: bulat + tangkai"
    }
  ]
}

## GET /api/v1/categories/:category_id
Get single category detail.

## GET /api/v1/level/:level_id/categories
Get all categories assigned to a specific level (Level 1, 2, or 3).

## GET /api/v1/themes
Get list of all available themes with category counts.

## GET /api/v1/level/:level_id/random?count=5
Get N random categories from a level (for randomized gameplay).
NOTE: Auto-excludes animals (ban_type='E') per RSI-1.

## POST /api/v1/categories (Admin only — Can/Dias)
Add new category. Body: full category object.
NOTE: New category with ban_type='E' (animal) auto-rejected per RSI-1.

## PATCH /api/v1/categories/:category_id (Admin only)
Update existing category.

## DELETE /api/v1/categories/:category_id (Admin only — soft delete)
Soft-delete category (set tier='BANNED' with ban_reason='DEPRECATED').
```

### C. Content Pipeline (Phased Rollout — NO Animals)

```
# ============================================================
# CONTENT PIPELINE — Phase rollout (RSI-1: NO animals)
# ============================================================

Phase 1 (MVP — 30 kategori)
├── Level 1 only
├── Tier 1 RECOMMENDED, difficulty 1-2
├── Tema: food + nature + everyday objects (medium difficulty)
├── NO animals (RSI-1)
└── Tujuan: validasi CNN recognition + game loop fast-paced

Phase 2 (Beta — 70 kategori)
├── Level 1 + Level 2
├── Tier 1 RECOMMENDED penuh
├── Tambah tema: vehicles + safety + clothes (conditional)
├── NO animals (RSI-1)
└── Tujuan: stress test confusion matrix (apple↔pear, car↔bus, dll)

Phase 3 (Full Release — 100 kategori)
├── Level 1 + Level 2 + Level 3
├── Tier 1 + Tier 2 (conditional dgn safety warning)
├── Tambah tema: music + body + buildings
├── NO animals (RSI-1)
└── Tujuan: hitung trust calibration metric (HITL core)

Phase 4 (Post-Launch Expansion — seasonal, NO animals)
├── Christmas: christmas tree, snowman (sudah ada), gift box
├── Ramadan: mosque (kalau ada), date (kurma), ketupat
├── Indonesian Independence Day: bendera, buraq, garuda (object, not animal)
├── Halloween: pumpkin, ghost (kalau ada)
└── Tujuan: retensi user + cultural relevance
```

## Section 7: Quality Control Checklist (v3.1 RSI-1)

Sebelum finalisasi daftar, pastikan setiap kategori lolos check ini:

### 🎯 RSI-1 Hard Rules (NON-NEGOTIABLE)
- [ ] **BUKAN hewan** (RSI-1: semua hewan di-BAN, tidak ada exception)
- [ ] **BUKAN geometric primitive** (RSI-1: line, circle, square, triangle, zigzag, squiggle → out of scope)
- [ ] **BUKAN landmark kompleks** (RSI-1: Eiffel Tower, Mona Lisa, Great Wall, aircraft carrier → banned)
- [ ] **BUKAN single-stroke item** (smiley face, dot, eye → banned)
- [ ] **Medium difficulty** (stroke 4-15, bukan 1-3 dan bukan 20+)

### 📋 Standard Quality Checks
- [ ] **Dapat digambar dalam 20 detik** oleh anak SMP usia 13 tahun?
- [ ] **Dikenali minimal 70% populasi target** (test dengan 10 anak sample di playtest)?
- [ ] **Tidak mirip dengan kategori lain** (confusion matrix: `apple` vs `pear` vs `watermelon` — pakai field `confusion_with` di SQL schema)?
- [ ] **Memiliki educational value** (bukan cuma "gambar ini dapat poin")?
- [ ] **Cocok dengan tema sketchbook** (bukan random object)?
- [ ] **Tidak melanggar cultural/religious norm** di Indonesia?
  - [ ] Tidak ada alcohol (`wine bottle`, `wine glass`) → SUDAH DI-BAN
  - [ ] Tidak ada weapon (`rifle`, `sword`, `knife`, `cannon`) → SUDAH DI-BAN
  - [ ] Religious building (`church`) → TIER 2 conditional, hindari jika sensitif
- [ ] **Tidak dangerous** jika anak mencoba replikasi di real life?
  - [ ] `power outlet` → DI-BAN (listrik hazard)
  - [ ] `stove`, `oven`, `microwave` → DI-BAN (burn hazard)
  - [ ] `matches`, `lighter` → DI-BAN (fire hazard)
  - [ ] `syringe`, `stitches` → DI-BAN (medical trigger)
- [ ] **Sudah assign** `difficulty` (1-5), `theme`, `level_assignment` (1-3)?
- [ ] **Sudah isi** `confusion_with` field untuk kategori yang mirip?
- [ ] **Sudah isi** `safety_warning` untuk TIER 2 conditional yang perlu warning?

---

### 🎯 Success Metrics (Bigprompt v3.0 + RSI-1 Evaluation)

- [x] File `quickdraw_category_analysis.md` tergenerate dengan lengkap (1 file, sesuai permintaan user)
- [x] Minimal 200 kategori sudah diklasifikasi → **271 kategori** diklasifikasi
  - TIER 1: 102
  - TIER 2: 68
  - TIER 3: 101 (Type A: 9, Type B: 18, Type C: 10, Type D: 14, Type E: 50)
- [x] Final Golden Set berisi 75-110 kategori siap implementasi → **116 kategori** (sedikit over untuk variasi, bisa trim setelah playtest)
- [x] Setiap keputusan include/exclude punya **alasan tertulis** → semua row di tabel punya kolom alasan
- [x] Special cases ditangani dengan solusi konkret → Section 3 lengkap dengan 8 case studies (reduced dari 10 karena RSI-1 hapus over-engineering)
- [x] SQL schema siap pakai untuk database implementation → Section 6.A lengkap dengan CREATE TABLE + seed data + ban_type 'E' untuk animals
- [x] **RSI-1 Applied**: NO animals in TIER 1 / Golden Set ✅
- [x] **RSI-1 Applied**: Geometric primitives di-list sekali, tidak over-engineered ✅
- [x] **RSI-1 Applied**: Complex landmarks (Eiffel Tower, aircraft carrier) hard BAN ✅

---

### 📌 Rekomendasi Next Steps (untuk Can & Dias)

**Untuk Can (Frontend/Blue Scope):**
1. Pakai Golden Set Level 1 (~60 kategori) untuk tutorial MVP — focus food + nature + everyday objects
2. Implement UI emotion indicator pakai smiley variants (bukan draw target — RSI-1)
3. Design safety warning overlay untuk TIER 2 conditional items (candle, campfire, scissors, hammer)
4. **Auto-reject** di UI kalau ada category dengan ban_type='E' (animal) muncul di game — RSI-1 enforcement

**Untuk Dias (Backend/Green Scope):**
1. Buat SQLite schema sesuai Section 6.A (dengan ban_type 'E' untuk animals)
2. Implement 5 API endpoints (Section 6.B) — `exclude_animals=true` default
3. Train MobileNet model dengan Golden Set (download Quick Draw dataset per category — SKIP all animal categories)
4. Set up confusion matrix tracking: log setiap false-positive pair (`apple` ↔ `pear`, `car` ↔ `bus`, `clock` ↔ `alarm clock`, dll)
5. Phase 1 launch: ~30 kategori Level 1 dulu (food + nature + simple objects) untuk validasi CNN accuracy

**Untuk Bu Hesti (Validation):**
- Cross-check TIER 3 BANNED list dengan arahan "objek berbahaya pakai duri" → sudah aligned (rifle/sword/knife di-ban, `cactus` sebagai duri proxy)
- Cross-check Level structure → 3 level saja, sesuai arahan
- Cross-check RSI-1: NO animals → sesuai feedback user Can 16/6/26

---

## 📝 Catatan Akhir (v3.1 RSI-1)

File ini adalah **single source of truth** untuk category curation di Sketchbook Universe. Revisi v3.1 menghapus over-inclusiveness v3.0 (40+ hewan, line/circle discussion, complex landmarks conditional).

**RSI-1 Rule (locked in `MEMORY.md` Section 9)**:
> Saat kurasi kategori/item apapun, HANYA include yang **medium difficulty**. NO animals, NO geometric primitives, NO complex landmarks, NO single-stroke items. FOKUS: everyday objects + simple food + nature + basic vehicles.

Untuk pertanyaan tentang kategori spesifik yang belum diklasifikasi, tambahkan di TIER 2 conditional dengan alasan "needs further analysis" — jangan langsung BAN tanpa reason. **TAPI: Jangan masukkan hewan ke TIER 2** — semua hewan langsung BAN (Type E) per RSI-1.

**Maintained by**: Can (Frontend/UX) & Dias (Backend/CNN) | **Last updated**: 16/6/26 | **Version**: 3.1 (RSI-1 Applied)
