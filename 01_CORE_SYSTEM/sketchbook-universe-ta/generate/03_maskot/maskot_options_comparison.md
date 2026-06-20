# Maskot Options Comparison — 7 Design Directions for Momo (v3.0)

> **Project:** Sketchbook Universe  
> **Document:** Concept Development + Comparison — Bigprompt v3.0  
> **Date:** 2026-03-05 (v3.0 update: 2026-06-16)  
> **Constraint Reminder:** NO LEGS · NO WINGS · Float Only · Text Bubble Only · 8-bit Geometric · Dark dot eyes (NO big white eyes with pupils like Doraemon/Mickey) · NO cheeks (NO Kirby-style pink cheeks) · Flat geometric face only

> **Update v3.0 (16/6/26):** Added 3 new options (E/F/G) with more expressive faces based on user feedback that options A-D had too minimal faces (only dot eyes + line mouth, hard to "read" emotion). New options add **eyebrows** (small rect 4x2) + **morphing mouth shapes** (rect -> oval -> triangle -> wave) + larger eye sizes (r=4 vs r=3 in A-D) + wider eye spacing (14px vs 12px) for clearer emotional signal across 5 animation states (IDLE/HAPPY/CONFUSED/THINKING/EXCITED). Scoring matrix updated with new criterion **Face Expressiveness (weight 0.15)** -- all 8 weights redistributed to total 1.00. Research synthesis: Tatyana Deniz (kawaii eye spacing), Chen 2023 (baby schema ratios), Disney Shape Language (rect=sturdy/friendly), Sackboy origin (programmer-art square evolved to icon), ASCII face grammar (eye shape variance = primary signal).

---

## Daftar Isi

1. [OPSI A: Sticky Note (v2.0)](#1-opsi-a-sticky-note-post-it-creature)
2. [OPSI B: Ink Blob (v2.0)](#2-opsi-b-ink-blob-tinta-hidup)
3. [OPSI C: Sketch Ghost (v2.0)](#3-opsi-c-sketch-ghost-hantu-sketsa)
4. [OPSI D: Origami Monster (v2.0)](#4-opsi-d-origami-monster-kertas-lipat)
5. [OPSI E: Doodle Cube (NEW v3.0)](#5-opsi-e-doodle-cube-kubus-sketsa--new-v30)
6. [OPSI F: Brush Spirit (NEW v3.0)](#6-opsi-f-brush-spirit-kuas-hidup--new-v30)
7. [OPSI G: Eraser Ghost (NEW v3.0)](#7-opsi-g-eraser-ghost-penghapus-hantu--new-v30)
8. [Weighted Scoring Matrix (v3.0)](#8-weighted-scoring-matrix)
9. [TOP 2 Recommendations (v3.0)](#9-top-2-recommendations)
10. [Reference Character Analysis (v3.0)](#10-reference-character-analysis-v30)

---

## 1. OPSI A: "Sticky Note" (Post-it Creature)

### Concept
A yellow sticky note that came alive in the sketchbook. One corner is permanently folded — that fold is where the "magic ink" pooled and gave the note consciousness. The sticky note hovers because paper has no weight in the sketchbook universe.

### Visual Description
Momo-A is a rounded rectangle (like a Post-it note) with a dog-eared corner on the bottom-right. The body IS the face — there's no separate head. Two small pixel-dot eyes sit in the upper third. A simple line mouth sits below. The bottom edge has a subtle wave (not flat — suggests hovering). A faint shadow ellipse floats beneath, never touching. The folded corner is a slightly different shade (teal/green) — this is the "magic ink" mark, the source of consciousness. The overall silhouette is a simple rectangle with one asymmetric fold.

### ASCII Art — IDLE State

```
              ┌──────────────────┐
              │                  │     ← Sticky note body (40×36)
              │   ●          ●   │        Eyes: 2 pixel dots
              │                  │        Spacing: wide-set
              │       ────       │        Mouth: simple line
              │                  │
              │                  │
              │              ╱───│     ← Dog-ear fold (bottom-right)
              │             ╱    │        Teal/green accent color
              └─────────────┘────┘
                    ░░░░░          ← Float shadow (ellipse)
              ──────────────────── ← Ground line (NEVER touched)
```

### ASCII Art — HAPPY State

```
              ✦    ✦    ✦
                   ✦  ✦
              ┌──────────────────┐
              │                  │     ← Body: stretched Y, squished X
              │   ◉          ◉   │        Eyes: bigger (radius 4)
              │                  │        Sparkle particles around
              │      ══════      │        Mouth: wide open
              │                  │
              │              ╱───│
              │             ╱    │
              └─────────────┘────┘
                  ░░░░            ← Shadow smaller (further up)
              ────────────────────
```

### ASCII Art — CONFUSED State

```
                          ?
                         ╱
               ╱──────────────────┐    ← Whole body tilted 15°
              ╱   ●          ●    │      Eyes: shifted left
             │              ●     │      Mouth: small, angled
              ╲──────────────────╲│
               ╲              ╱───│
                ╲            ╱    │
                 └──────────┘────┘
                     ░░░░░         ← Shadow offset by drift
              ────────────────────
```

### ASCII Art — Silhouette (IP Test)

```
              ┌──────────────────┐
              │                  │
              │                  │
              │                  │
              │                  │
              │                  │
              │              ╱───│     ← Fold corner = KEY identifier
              │             ╱    │
              └─────────────┘────┘
                    ░░░░░          ← Float shadow gap
```

### Color Palette

| Role | Hex Code | RGB | Description |
|------|----------|-----|-------------|
| **Primary** | `#FFE066` | (255, 224, 102) | Sticky note yellow — warm, approachable |
| **Secondary** | `#4ECDC4` | (78, 205, 196) | Teal — magic ink mark on folded corner |
| **Accent** | `#FF6B6B` | (255, 107, 107) | Coral red — blush, excitement particles |
| **Outline** | `#2D3436` | (45, 52, 54) | Dark grey — sketch lines, eyes, mouth |
| **Shadow** | `rgba(0,0,0,0.12)` | — | Soft float shadow beneath |
| **Paper BG** | `#F5F0E8` | (245, 240, 232) | Warm cream — sketchbook paper |

### Shape Inventory (Kaplay.js)

| # | Shape | Code | Size | Color | Function |
|---|-------|------|------|-------|----------|
| 1 | Rectangle (rounded) | `rect(40, 36, { radius: 3 })` | 40×36 | `#FFE066` | Body = face |
| 2 | Circle | `circle(3)` | r=3 | `#2D3436` | Left eye |
| 3 | Circle | `circle(3)` | r=3 | `#2D3436` | Right eye |
| 4 | Polygon (fold) | `polygon([v(12,-3), v(16,-3), v(16,1)])` | triangle | `#4ECDC4` | Fold corner |
| 5 | Ellipse | `ellipse(20, 5)` | 20×5 | `rgba(0,0,0,0.12)` | Float shadow |

### Animation Specs

| Animation | Method | Detail |
|-----------|--------|--------|
| **Float** | `sin(time * 2.5) * 3` on `pos.y` | Gentle bob ±3px |
| **Blink** | Eye `scaleY → 0` for 2 frames every ~3s | Quick blink |
| **Happy bounce** | Squash→Stretch→Settle (1.5s) | `scale(1.2,0.8)` → `scale(0.9,1.2)` → `scale(1,1)` |
| **Confused tilt** | `angle = 12 + sin(time*4) * 3` | Oscillating tilt |
| **Flutter** | Fold corner wobbles independently | `angle = sin(time*6) * 8` |

### Pros & Cons

| Aspect | Pros | Cons |
|--------|------|------|
| **8-bit fit** | ⭐⭐⭐⭐⭐ Rect = perfect for pixel art | — |
| **Kaplay.js** | ⭐⭐⭐⭐⭐ All rect + circle calls | — |
| **IP safety** | ⭐⭐⭐⭐ Yellow sticky note is unique | ⚠️ "Sticky note character" exists (Post-it brand) |
| **Theme fit** | ⭐⭐⭐⭐ Paper native to sketchbook | ⚠️ Yellow ≠ sketchbook vibe (more office) |
| **Teen appeal** | ⭐⭐⭐ Cute but maybe too "office" | ⚠️ 13-15 year olds may find sticky note boring |
| **Animation** | ⭐⭐⭐⭐⭐ Easy — rect deformation | — |
| **Silhouette** | ⭐⭐⭐⭐ Fold corner + float gap = unique | ⚠️ Plain rectangle without fold is generic |

---

## 2. OPSI B: "Ink Blob" (Tinta Hidup)

### Concept
A drop of ink that gained consciousness. In the sketchbook universe, ink is alive — it flows, drips, and thinks. Momo-B is a dark ink blot that hovers above the page, leaving faint ink particle trails. She's a creature of pure thought made visible through ink. Her form is organic but not messy — a controlled blob that suggests intelligence.

### Visual Description
Momo-B is a vertically-oriented irregular blob — wider at the top, narrower at the bottom, with a subtle drip extending below. The top portion has two bright dot eyes (the ONLY bright elements on an otherwise dark body). A faint sheen/highlight (small white arc) on the upper-left suggests a wet, glossy surface. Below the body, 2-3 tiny ink drips are animated — they form, extend, and retract (never actually dripping off — Momo keeps her ink together). The whole creature floats with a gentle undulation — the blob's outline subtly morphs between frames (like a lava lamp). A dark shadow pool beneath is more integrated than separate — it's part of Momo's ink.

### ASCII Art — IDLE State

```
                 ╭─────────╮
               ╱    ●   ●   ╲        ← Blob top — wider, rounded
              │               │         Eyes: BRIGHT dots on dark body
              │      ──       │         Mouth: simple line (light colored)
              ╲              ╱
                ╲          ╱          ← Blob narrows toward bottom
                  ╲      ╱
                    ╲  ╱
                     ╲╱  ·            ← Tiny drip (animated: extends & retracts)
                       ·
                    ░░░░░             ← Ink pool shadow (darker, more integrated)
              ────────────────────    ← Ground line
```

### ASCII Art — HAPPY State

```
              ✦    ✦    ✦
                   ✦  ✦
                 ╭─────────╮
               ╱    ◉   ◉   ╲        ← Eyes BIGGER (radius 4)
              │      ════     │        Mouth: wide open (light color)
              ╲              ╱
                ╲          ╱
                  ╲      ╱             ← Squash-stretch: wider, shorter
                    ╲╱
                    ░░░░              ← Shadow spread wider (closer)
              ────────────────────
```

### ASCII Art — CONFUSED State

```
                          ?
                         ╱
                  ╭──────────╮         ← Body: slightly irregular
               ╱     ●    ●    ╲        Eyes: one bigger than other
              │              ●   │       Mouth: wavy line
              ╲   ·         ·   ╱
                ╲    ·   ·    ╱          ← Extra drips (stress response)
                  ╲╱ · · ╲╱
                    ░░░░░░             ← Shadow wobbly
              ────────────────────
```

### ASCII Art — Silhouette (IP Test)

```
                 ╭─────────╮
               ╱             ╲
              │               │
              │               │
              ╲              ╱
                ╲          ╱
                  ╲      ╱
                    ╲  ╱
                     ╲╱
                    ░░░░░             ← Unique: blob + drip + integrated shadow
```

### Color Palette

| Role | Hex Code | RGB | Description |
|------|----------|-----|-------------|
| **Primary** | `#1A1A2E` | (26, 26, 46) | Deep navy ink — mysterious, intelligent |
| **Secondary** | `#16213E` | (22, 33, 62) | Darker ink — depth, shadow areas |
| **Accent** | `#E94560` | (233, 69, 96) | Crimson — eye glow, excitement particles |
| **Eye shine** | `#FFFFFF` | (255, 255, 255) | White — bright dot eyes (contrast on dark) |
| **Outline** | `#0F0F23` | (15, 15, 35) | Near-black — definition |
| **Ink pool** | `rgba(26,26,46,0.4)` | — | Shadow pool beneath |

### Shape Inventory (Kaplay.js)

| # | Shape | Code | Size | Color | Function |
|---|-------|------|------|-------|----------|
| 1 | Ellipse | `ellipse(24, 28)` | 24×28 | `#1A1A2E` | Body (blob top) |
| 2 | Circle | `circle(3)` | r=3 | `#FFFFFF` | Left eye (bright on dark) |
| 3 | Circle | `circle(3)` | r=3 | `#FFFFFF` | Right eye (bright on dark) |
| 4 | Ellipse | `ellipse(8, 14)` | 8×14 | `#16213E` | Drip element (animated) |
| 5 | Ellipse | `ellipse(22, 6)` | 22×6 | `rgba(26,26,46,0.4)` | Ink pool shadow |

### Animation Specs

| Animation | Method | Detail |
|-----------|--------|--------|
| **Float** | `sin(time * 2.0) * 4` on `pos.y` | Slower, heavier bob (ink has "weight" feel) |
| **Blob morph** | `scaleX = 1 + sin(time*3)*0.05; scaleY = 1 - sin(time*3)*0.05` | Subtle lava-lamp morph |
| **Drip cycle** | Drip `scaleY` oscillates 0.8 → 1.2 → 0.8 over 2s | Drips extend and retract |
| **Happy bounce** | Body squash, drips retract (1.5s) | Ink pulls together = excitement |
| **Confused drip** | Extra drips spawn, body wobbles irregularly | Stress = more ink dripping |

### Pros & Cons

| Aspect | Pros | Cons |
|--------|------|------|
| **8-bit fit** | ⭐⭐⭐ Ellipse/blob = less pixel-perfect | ⚠️ Organic shape harder to pixel-art |
| **Kaplay.js** | ⭐⭐⭐⭐ Ellipse calls work | ⚠️ Blob morph needs custom code |
| **IP safety** | ⭐⭐⭐⭐⭐ Ink blob = very unique | — |
| **Theme fit** | ⭐⭐⭐⭐⭐ Ink = core sketchbook element | — |
| **Teen appeal** | ⭐⭐⭐⭐ Dark = cool, mysterious | ⚠️ May feel "scary" for some 13-year-olds |
| **Animation** | ⭐⭐⭐⭐ Blob morph + drips = unique | ⚠️ Drip animation = performance concern |
| **Silhouette** | ⭐⭐⭐⭐ Blob + drip is distinctive | ⚠️ At 16×16, blob reads as circle (generic) |

---

## 3. OPSI C: "Sketch Ghost" (Hantu Sketsa)

### Concept
A ghost made entirely of pencil sketch lines. In the sketchbook universe, even erased drawings leave traces — and Momo-C is the ghost of a drawing that was erased but refused to disappear. She's visible as white fill with pencil-stroke outlines. The bottom of her "body" is wavy/ragged, like a ghost tail, but since she floats, the "tail" never touches the ground. Her outline has visible pencil texture — not smooth vector lines but slightly rough, sketchy strokes.

### Visual Description
Momo-C has a round-topped body (like a classic ghost shape) with a wavy bottom edge. The body is filled with off-white/cream (like sketchbook paper) and outlined with a rough, pencil-textured dark line. Two dot eyes and a small mouth float in the upper portion. The wavy bottom edge oscillates gently — like a ghost's tail undulating. A faint pencil-stroke "hatching" pattern appears inside the body when Momo is thinking. She leaves faint pencil-dust particles when she moves. The overall effect is "a drawing that's still being drawn" — alive but visibly hand-made.

### ASCII Art — IDLE State

```
                 ╭───────────╮
               ╱               ╲       ← Round top (dome shape)
              │    ●       ●    │        Eyes: pencil-dot eyes
              │                  │        Mouth: thin pencil line
              │        ──        │
              │                  │
              ╰─╮            ╭─╯       ← Wavy bottom edge (ghost tail)
                ╰─╮        ╭─╯          Oscillates gently
                  ╰────────╯
                    ░░░░░              ← Float shadow (faint)
              ────────────────────      ← Ground line
```

### ASCII Art — HAPPY State

```
              ✎   ✦   ✎   ✦   ✎        ← Pencil dust particles
                 ╭───────────╮
               ╱               ╲
              │    ◉       ◉    │       ← Eyes: bigger, brighter
              │                  │
              │      ══════      │       ← Mouth: wide open smile
              │                  │
              ╰──╮           ╭──╯       ← Bottom: pulled up (squished)
                 ╰──╮     ╭──╯
                    ╰─────╯
                     ░░░             ← Shadow closer (squished down)
              ────────────────────
```

### ASCII Art — CONFUSED State

```
                        ?
                       ╱
                  ╭───────────╮        ← Body: tilted
               ╱     ●    ●     ╲       Eyes: one larger
              │             ●     │      Mouth: wavy line (pencil scribble)
              │        ∼∼∼        │
              ╰─╮              ╭─╯      ← Bottom: more erratic waves
                ╰─╮    ·    ╭─╯          Pencil dust = stress
                  ╰────────╯
                    ░░░░░             ← Shadow wobbly
              ────────────────────
```

### ASCII Art — Silhouette (IP Test)

```
                 ╭───────────╮
               ╱               ╲
              │                  │
              │                  │
              │                  │
              ╰─╮            ╭─╯       ← Wavy bottom = KEY identifier
                ╰─╮        ╭─╯
                  ╰────────╯
                    ░░░░░
```

### Color Palette

| Role | Hex Code | RGB | Description |
|------|----------|-----|-------------|
| **Primary** | `#F5F0E8` | (245, 240, 232) | Warm cream — paper fill |
| **Secondary** | `#2D3436` | (45, 52, 54) | Dark grey — pencil outline |
| **Accent** | `#FF6B6B` | (255, 107, 107) | Coral — blush, highlight |
| **Outline** | `#3D3D3D` | (61, 61, 61) | Pencil grey — sketch stroke |
| **Pencil dust** | `rgba(45,52,54,0.3)` | — | Faint particles |
| **Shadow** | `rgba(0,0,0,0.08)` | — | Very faint float shadow |

### Shape Inventory (Kaplay.js)

| # | Shape | Code | Size | Color | Function |
|---|-------|------|------|-------|----------|
| 1 | Ellipse | `ellipse(30, 20)` | 30×20 | `#F5F0E8` | Body top (dome) |
| 2 | Rectangle | `rect(30, 20, { radius: 0 })` | 30×20 | `#F5F0E8` | Body mid-section |
| 3 | Circle | `circle(3)` | r=3 | `#2D3436` | Left eye |
| 4 | Circle | `circle(3)` | r=3 | `#2D3436` | Right eye |
| 5 | Polygon (wave) | `polygon([...wavePoints])` | variable | `#F5F0E8` | Wavy bottom edge |

### Animation Specs

| Animation | Method | Detail |
|-----------|--------|--------|
| **Float** | `sin(time * 2.2) * 3` on `pos.y` | Medium-speed float |
| **Wave bottom** | Wave vertices `sin(time*3 + i*0.5) * 2` | Bottom edge undulates |
| **Pencil dust** | Particles on movement, `opacity → 0` over 1s | Sketch residue |
| **Happy** | Body squishes, waves pull up tightly | Ghost "tucks in" = cute |
| **Confused** | Extra pencil scribbles appear around head | Hatching pattern = thinking |

### Pros & Cons

| Aspect | Pros | Cons |
|--------|------|------|
| **8-bit fit** | ⭐⭐⭐⭐ Dome + rect is geometric | ⚠️ Wavy bottom is organic |
| **Kaplay.js** | ⭐⭐⭐⭐ Basic shapes work | ⚠️ Wave polygon needs vertex animation |
| **IP safety** | ⭐⭐⭐⭐ Sketch ghost = somewhat unique | ⚠️ Ghost shape is common (Pac-Man ghosts, etc.) |
| **Theme fit** | ⭐⭐⭐⭐⭐ Pencil + paper = perfect sketchbook | — |
| **Teen appeal** | ⭐⭐⭐⭐ Ghost = cool for teens | ⚠️ May feel "too spooky" for classroom use |
| **Animation** | ⭐⭐⭐⭐ Wave bottom = unique animation | ⚠️ Vertex animation = more complex |
| **Silhouette** | ⭐⭐⭐⭐ Wavy bottom + float = recognizable | ⚠️ Classic ghost shape has many precedents |

---

## 4. OPSI D: "Origami Monster" (Kertas Lipat)

### Concept
An origami creature folded from a sketchbook page. Momo-D is angular, sharp-edged, and has a 3D illusion created through cel-shading. She's the most "designed" of all options — every edge is deliberate, every fold is precise. She hovers because in the sketchbook universe, folded paper can defy gravity. She unfolds slightly when surprised, refolds tightly when thinking.

### Visual Description
Momo-D is a diamond/rhombus shape viewed at a slight 3/4 angle, giving a 3D paper-fold illusion. The "front face" is cream/paper colored with a subtle crease line down the middle. Two angular dot eyes sit on the front face. The "side face" (visible due to 3/4 angle) is slightly darker — suggesting depth. The bottom comes to a point (origami fold), but it never touches the ground — there's always a gap. Sharp crease lines (thin dark lines) mark the fold boundaries. When Momo-D expresses emotion, the paper creases subtly shift — unfolding slightly when surprised, folding tighter when concentrating. A paper texture (subtle hatch pattern) gives the surface character.

### ASCII Art — IDLE State

```
                     ╱╲
                   ╱    ╲              ← Top point (origami apex)
                 ╱  ●  ●  ╲            Eyes: angular dots on front face
               ╱     ──     ╲          Mouth: thin line
             ╱                ╲
            ╱                  ╲        ← Front face (cream)
           ╱    ╱────────╲     ╲       Crease line down middle
          ╱   ╱            ╲    ╲
         ╱  ╱                ╲   ╲     ← Side face (slightly darker)
        ╱ ╱                    ╲  ╲
       ╱╱                      ╲╱
                                 ╲      ← Bottom point (never touches ground)
                    ░░░░░               ← Float shadow
              ────────────────────       ← Ground line
```

### ASCII Art — HAPPY State

```
              ✦     ✦     ✦
                     ╱╲
                   ╱    ╲            ← Slightly wider (unfolded a bit)
                 ╱  ◉  ◉  ╲          Eyes: bigger
               ╱    ══════   ╲        Mouth: wide
             ╱                ╲
            ╱                  ╲       ← Front face MORE open
           ╱                    ╲      (unfolded = happy)
          ╱                      ╲
         ╱                        ╲
        ╱                          ╲
       ╱╱                          ╲╱
                    ░░░░░
              ────────────────────
```

### ASCII Art — CONFUSED State

```
                      ?
                     ╱
                  ╱╲                  ← Tilted
               ╱╱    ╲╲               Fold partially collapsed
             ╱╱  ●  ●  ╲╲            Eyes: one larger
           ╱╱     ∼∼     ╲╲          Mouth: wavy
         ╱╱                ╲╲        ← Tighter fold (confused = contracted)
        ╱╱                  ╲╲
       ╱╱                    ╲╲
                    ░░░░░
              ────────────────────
```

### ASCII Art — Silhouette (IP Test)

```
                     ╱╲
                   ╱    ╲
                 ╱        ╲
               ╱            ╲
             ╱                ╲
            ╱                  ╲
           ╱                    ╲
          ╱                      ╲
         ╱                        ╲
        ╱                          ╲
       ╱╱                          ╲╱
                    ░░░░░              ← Diamond + float = unique among mascots
```

### Color Palette

| Role | Hex Code | RGB | Description |
|------|----------|-----|-------------|
| **Primary** | `#F5E6CA` | (245, 230, 202) | Cream/paper — origami surface |
| **Secondary** | `#D4C4A8` | (212, 196, 168) | Shadow fold — darker paper face |
| **Accent** | `#E74C3C` | (231, 76, 60) | Red crease — origami fold mark |
| **Outline** | `#2D3436` | (45, 52, 54) | Dark grey — crease lines |
| **Crease** | `#C4A87C` | (196, 168, 124) | Tan — fold shadow |
| **Shadow** | `rgba(0,0,0,0.10)` | — | Soft float shadow |

### Shape Inventory (Kaplay.js)

| # | Shape | Code | Size | Color | Function |
|---|-------|------|------|-------|----------|
| 1 | Polygon (diamond) | `polygon([v(0,-24), v(20,0), v(0,24), v(-20,0)])` | 40×48 | `#F5E6CA` | Front face |
| 2 | Polygon (side) | `polygon([v(0,-24), v(20,0), v(0,8), v(-8,-8)])` | ~30×32 | `#D4C4A8` | Side face (3D illusion) |
| 3 | Circle | `circle(3)` | r=3 | `#2D3436` | Left eye |
| 4 | Circle | `circle(3)` | r=3 | `#2D3436` | Right eye |
| 5 | Ellipse | `ellipse(18, 5)` | 18×5 | `rgba(0,0,0,0.10)` | Float shadow |

### Animation Specs

| Animation | Method | Detail |
|-----------|--------|--------|
| **Float** | `sin(time * 2.8) * 3` on `pos.y` | Slightly faster float (lighter = paper) |
| **Gentle spin** | `angle = sin(time * 0.5) * 5` | Slight rotation showing 3D aspect |
| **Unfold** | `scale` animation on sub-faces | Faces separate slightly when surprised |
| **Refold** | Reverse of unfold | Tighten when thinking |
| **Happy spin** | Quick 360° spin + unfold | Origami celebrating |

### Pros & Cons

| Aspect | Pros | Cons |
|--------|------|------|
| **8-bit fit** | ⭐⭐⭐⭐ Angular = pixel-friendly | ⚠️ 3D illusion harder in 2D engine |
| **Kaplay.js** | ⭐⭐⭐ Polygon calls exist but less stable | ⚠️ Complex polygon animation = buggy |
| **IP safety** | ⭐⭐⭐⭐⭐ Origami creature = very unique | — |
| **Theme fit** | ⭐⭐⭐⭐⭐ Paper folding = sketchbook native | — |
| **Teen appeal** | ⭐⭐⭐⭐ Origami = cool, creative | ⚠️ May feel "too complex" or "try-hard" |
| **Animation** | ⭐⭐⭐ Unfold/refold = unique | ⚠️ Polygon vertex animation = hardest to implement |
| **Silhouette** | ⭐⭐⭐⭐⭐ Diamond + float = NO precedent | — |

---


## 5. OPSI E: "Doodle Cube" (Kubus Sketsa) — NEW v3.0

### Concept
Selembar kertas sketsa yang melipat dirinya sendiri menjadi kubus hidup. Sisi depan kubus menjadi panel wajah utama; sisi atas dan samping terlihat memberi ilusi 2.5D tanpa 3D engine. Wajah di panel depan adalah jendela ekspresif Momo — mata hexagonal + eyebrows rect + mulut yang morph per emosi. Lipatan teal di sudut atas = "magic ink mark" (asymmetric signature). Kubus melayang karena kertas tidak punya berat di sketchbook universe.

### Visual Description
Momo-E adalah kubus 2.5D — 3 sisi terlihat: **front face** (rect 28×28 cream `#F5E6CA`), **top face** (parallelogram lighter `#FAEED5` untuk depth illusion), **right side face** (parallelogram darker `#D4C4A8`). Front face = panel wajah. **Mata hexagonal** (polygon 6-vertex, "radius" 4px) terletak 1/3 dari atas, terpisah **14px** (lebih lebar dari A-D yang 12px) — lebih readable. **Eyebrows** = rect 4×2 dark `#2D3436`, di atas mata, terpisah 14px — **SIGNATURE E**, sumber expression range. **Mulut** = rect 8×2 di 2/3 dari atas, dapat morph: line netral (IDLE), wide oval 12×4 (HAPPY), zigzag 4-vertex (CONFUSED), small circle r=2 (THINKING), big triangle 12×8 (EXCITED). **Lipatan teal** (`#4ECDC4`) di sudut kanan-atas kubus = asymmetric signature + magic ink mark. Float shadow ellipse `rgba(0,0,0,0.10)` di bawah.

### ASCII Art — IDLE State

```
                _________________
               /                /|        ← Top face: lighter cream parallelogram
              /________________/ |
             |   ▄▄        ▄▄  | |        ← Eyebrows (rect 4×2, dark) — SIGNATURE E
             |  ⬡          ⬡   | |        ← Eyes: hexagon r=4, wider-set 14px
             |                  | |
             |      ══════      | |        ← Mouth: horizontal rect 8×2 (neutral line)
             |                  | |
             |                  | /
             |__________________|/         ← Side face: darker cream (depth illusion)
                      ▓▓▓▓▓▓              ← Float shadow (ellipse, breathes)
             ────────────────────────      ← Ground line (NEVER touched)
```

### ASCII Art — HAPPY State

```
              ✦    ✦    ✦                   ← Yellow sparkles
                   ✦  ✦
                _________________
               /                /|
              /________________/ |
             |   ▄▀        ▀▄  | |        ← Eyebrows angled up (outer ends raised)
             |  ⬣          ⬣   | |        ← Eyes: slightly bigger (r=5)
             |                  | |
             |    ╭──────────╮  | |        ← Mouth: morphed to wide oval (smile)
             |    ╰──────────╯  | |
             |                  | /
             |__________________|/         ← Body: stretched Y, squished X
                      ▓▓▓                    ← Shadow smaller (Momo rose up)
             ────────────────────────
```

### ASCII Art — CONFUSED State

```
                          ?
                         ╱
                _________________
               /                /|         ← Body tilted 12° (oscillates ±3°)
              /________________/ |
             |  ▄▄        ▀▀  | |         ← Eyebrows ASYMMETRIC (L flat, R raised)
             |  ⬡          ⬡   | |         ← Eyes: L slightly bigger than R (asymmetric)
             |                  | |
             |    ~~~~~~~~~~    | |         ← Mouth: wavy zigzag line (4-vertex polyline)
             |                  | |
             |                  | /
             |__________________|/
                       ▓▓▓▓▓                ← Shadow offset (lateral drift ±4px)
             ────────────────────────
```

### ASCII Art — Silhouette (IP Test)

```
                _________________
               /                /|
              /________________/ |
             |                  | |
             |                  | |        ← No face — pure cube shape
             |                  | |
             |                  | |
             |                  | |
             |                  | /
             |__________________|/         ← Isometric cube + float shadow
                      ▓▓▓▓▓▓                  NO popular mascot uses isometric cube
             ────────────────────────
```

### Color Palette

| Role | Hex Code | RGB | Description |
|------|----------|-----|-------------|
| **Primary (front)** | `#F5E6CA` | (245, 230, 202) | Cream front face — sketch paper |
| **Top face** | `#FAEED5` | (250, 238, 213) | Lighter cream — depth illusion |
| **Side face** | `#D4C4A8` | (212, 196, 168) | Darker cream — shadow face (3D) |
| **Accent (fold)** | `#4ECDC4` | (78, 205, 196) | Teal — magic ink mark (asymmetric signature) |
| **Outline/Eyes/Eyebrows** | `#2D3436` | (45, 52, 54) | Dark grey — face features + cube edges |
| **Shadow** | `rgba(0,0,0,0.10)` | — | Soft float shadow beneath |

### Shape Inventory (Kaplay.js)

| # | Shape | Code | Size | Color | Function |
|---|-------|------|------|-------|----------|
| 1 | Rectangle | `rect(28, 28, { radius: 1 })` | 28×28 | `#F5E6CA` | Front face = face panel |
| 2 | Polygon (top) | `polygon([v(-14,-14), v(14,-14), v(18,-18), v(-10,-18)])` | ~28×4 | `#FAEED5` | Top face (depth illusion) |
| 3 | Polygon (side) | `polygon([v(14,-14), v(18,-18), v(18,14), v(14,18)])` | ~4×32 | `#D4C4A8` | Right side face (depth) |
| 4 | Polygon (hex eye L) | `polygon([6 hex vertices around (-7, -4)], r=4)` | r=4 | `#2D3436` | Left eye (hexagon — wider than A-D's r=3 dot) |
| 5 | Polygon (hex eye R) | `polygon([6 hex vertices around (7, -4)], r=4)` | r=4 | `#2D3436` | Right eye (hexagon) |
| 6 | Rectangle | `rect(4, 2)` at (-7, -8) | 4×2 | `#2D3436` | Left eyebrow (SIGNATURE E) |
| 7 | Rectangle | `rect(4, 2)` at (7, -8) | 4×2 | `#2D3436` | Right eyebrow |
| 8 | Rectangle | `rect(8, 2)` at (0, 4) | 8×2 | `#2D3436` | Mouth (morphs per state via scale + shape swap) |
| 9 | Polygon (fold) | `polygon([v(8,-14), v(14,-14), v(14,-10)])` | triangle | `#4ECDC4` | Magic ink fold corner (asymmetric signature) |
| 10 | Ellipse | `ellipse(22, 5)` at (0, 20) | 22×5 | `rgba(0,0,0,0.10)` | Float shadow (breathes with bob) |

**Total: 10 shapes** (within budget — A uses 5, B uses 5, C uses 5, D uses 5; E uses 10 but all simple rect/polygon — still <100KB assets)

### Animation Specs (5 State)

| State | Body | Eyes (Hexagon) | Eyebrows (Rect 4×2) | Mouth (Morph) | Shadow | Particles |
|-------|------|-----------------|---------------------|---------------|--------|-----------|
| **IDLE** | float `sin(t*2.5)*3`, sway `sin(t*1.5)*2°` | r=4, neutral dark | flat horizontal, 0° angle | rect 8×2 (neutral line) | breathe ±10% | — |
| **HAPPY** | squish `(1.2,0.8)` → stretch `(0.9,1.2)` (1.5s) | r=5, sparkle ring overlay | angled up +10° (outer end raised, `angle=10°`) | morph → oval 12×4 (smile curve) | shrink to 70% | 5 yellow `#FFE066` sparkles |
| **CONFUSED** | tilt `12 + sin(t*4)*3°`, drift `sin(t*2)*4` px | asymmetric: L r=4.5, R r=3.5 | asymmetric: L flat, R angled up +15° | morph → zigzag 4-vertex polyline (wavy) | offset by drift | "?" mark above (text bubble `#FF6B6B`) |
| **THINKING** | slow spin `(t*120)%360` (3s/rot) | r=3 (smaller, focused), L↔R dart every 600ms | flat, narrowed (width 3 instead of 4) | morph → small circle r=2 (lips pursed) | wobble ±15% | 3 yellow dots orbiting r=24 |
| **EXCITED** | shake `±3px` at 30Hz, 2-bounce (2s) | r=5, color flash yellow `#FFE066` (200ms pulses) | angled up +20° (both raised high) | morph → big triangle 12×8 (open mouth) | pulse with shake | 8 confetti `#FFE066` + 4 teal `#4ECDC4` |

### Face Expression Matrix (5 state × 3 face parts)

| State | Eyes (Hexagon) | Eyebrows (Rect 4×2) | Mouth (Rect 8×2 morph) |
|-------|----------------|---------------------|------------------------|
| **IDLE** | r=4, dark `#2D3436`, neutral position (±7px from center) | Flat horizontal, 0° angle | Horizontal line `8×2` (neutral) |
| **HAPPY** | r=5 (grown 25%), dark, sparkle ring particle overlay | Angled up +10° (outer end raised) — `polygon` tilted | Morph → wide oval `12×4` (smile — upward arc curve) |
| **CONFUSED** | Asymmetric: L r=4.5 (bigger), R r=3.5 (smaller) | Asymmetric: L flat 0°, R angled up +15° | Morph → zigzag 4-vertex polyline (wavy line — `polygon([v(-6,0),v(-2,-2),v(2,2),v(6,0)])`) |
| **THINKING** | r=3 (smaller 25%, focused), L↔R position dart every 600ms | Flat, narrowed (width 3 instead of 4, slightly closer set) | Morph → small circle r=2 (pursed — `circle(2)` replaces rect) |
| **EXCITED** | r=5, color flash yellow `#FFE066` (alternating 200ms with dark) | Angled up +20° (both raised high, almost touching top edge) | Morph → big triangle `12×8` (open mouth — `polygon([v(-6,0),v(6,0),v(0,8)])`) |

### Pros & Cons

| Aspect | Pros | Cons |
|--------|------|------|
| **8-bit fit** | ⭐⭐⭐⭐⭐ Rect + hex = pure geometric, pixel-perfect | — |
| **Kaplay.js** | ⭐⭐⭐⭐ All `rect()`/`polygon()` calls, 10 shapes total | ⚠️ 2.5D Z-ordering between top/side/front faces needs care |
| **IP safety** | ⭐⭐⭐⭐ Cube + sketch paper combo is unique | ⚠️ Generic "cube character" precedent (Minecraft Slime) — mitigated by opaque cream, teal fold, no transparency, eyebrows |
| **Theme fit** | ⭐⭐⭐⭐⭐ Paper cube = pure sketchbook native | — |
| **Teen appeal (13-15)** | ⭐⭐⭐⭐ Cube reads as "Minecraft-y" + playful | ⚠️ Some 13yo may dismiss as "Minecraft rip-off" until they see fold + face + float |
| **Animation ease** | ⭐⭐⭐⭐ Mouth morph + eyebrows = unique range; float = standard sin | ⚠️ 2.5D face rotation (THINKING spin) is harder than flat rect |
| **Silhouette strength** | ⭐⭐⭐⭐ Isometric cube + float = recognizable | ⚠️ At 16×16 icon size, cube reads as square (similar to A) |
| **Face Expressiveness** | ⭐⭐⭐⭐⭐ Hex eyes + eyebrows + morphing mouth = STRONGEST face of all 7 options | — |

### IP Safety Analysis

#### 3 Closest Existing Characters

| Character | Owner | Similarity | Differentiator (why Momo-E is safe) |
|-----------|-------|-----------|--------------------------------------|
| **Minecraft Slime Cube** | Mojang/Microsoft | Cube body + simple face | Momo-E: opaque cream (not transparent green), has teal fold corner (Slime has none), 2.5D isometric (Slime is flat front), has eyebrows (Slime has none), no bouncing physics (Momo floats) |
| **Boxy Boy (Tekken)** | Bandai Namco | Cardboard box + simple face | Momo-E: sketch paper (not cardboard), 2.5D isometric (Boxy Boy is flat), hex eyes (Boxy Boy = dots), has eyebrows, magic ink fold (not tape strip), no limbs |
| **Cubone (Pokemon)** | Nintendo/Game Freak | Cube-ish head + simple face | Momo-E: full cube body (Cubone = skull mask on bipedal body), cream color (Cubone = brown), hex eyes (Cubone = shadowed eyes), no limbs (Cubone has arms/legs), floating (Cubone walks) |

#### Clawd Distance Score: 3/8

| Dimension | Clawd | Momo-E | Same? |
|-----------|-------|--------|-------|
| Base shape | Rect (flat 2D) | Cube (2.5D isometric) | ⚠️ Partial — both rect-derived |
| Shape type | Geometric | Geometric | ⚠️ Same |
| Color | Salmon pink | Cream | ✅ Different |
| Eye style | Dark round dots | Dark hexagons | ⚠️ Same family (dark, no pupils) |
| Limbs | 4-6 legs | None (float only) | ✅ Different |
| Movement | Walk | Float | ✅ Different |
| Context | Terminal | Sketchbook | ✅ Different |
| Asymmetry | Legs (mild) | Teal fold corner | ✅ Different element |

**3 similarities** (geometric family, dark-dot-eye family, rect-derived base) — MODERATE distance. Mitigated by 2.5D cube vs flat rect, hex vs round dots, fold corner asymmetric signature. **Verdict: SAFE with mitigations (fold corner + 2.5D + hex eyes).**

---

## 6. OPSI F: "Brush Spirit" (Kuas Hidup) — NEW v3.0

### Concept
Sebuah kuas lukis yang hidup di sketchbook universe. Handle kayu vertikal = tubuh utama, bulu kuas di atas = "rambut" yang fluff dan expressive, ferrule (cincin logam) = pemisah. Wajah diukir di handle bagian atas, di bawah ferrule — panel datar yang paling cocok untuk face. Kuas melayang karena bulunya menangkap "angin imajinasi" sketchbook. Stroke trail muncul saat excited (seperti sapuan kuas cepat). Brush = sketchbook-native tool yang tidak terpakai oleh karakter populer manapun.

### Visual Description
Momo-F vertical oriented, total tinggi 60px lebar 28px. **Bristle** (bulu kuas) di atas: ellipse cream `#F5F0E8` 22×18 dengan tip menyempit ke atas — bisa bergerak (wave gentle saat IDLE, fluff out saat HAPPY, flat/compressed saat CONFUSED). **Ferrule**: rect 28×6 silver/metallic `#B8B8B8` menandai batas bristle-handle, dengan 2 garis horizontal tipis (decorative ring lines). **Handle**: rect 28×36 brown `#8B4513` dengan rounded top, bagian bawah menyempit ke triangle point (rect + triangle). **Wajah** pada handle 10px di bawah ferrule: **mata** = ring style (lingkaran luar r=5 light cream `#F5F0E8` + lingkaran dalam r=3 dark `#2D3436`) — tetap 8-bit karena circle-within-circle (NO white shine, hanya ring contrast). **Eyebrows** = rect 5×2 dark di atas mata, terpisah 14px — SIGNATURE F untuk expression range. **Mulut** = arc/curve (polygon 6-vertex) yang morph: flat line (IDLE), wide upward arc (HAPPY), zigzag (CONFUSED), small circle (THINKING), big O vertical (EXCITED). **Accent red** `#FF6B6B` stripe di handle = asymmetric signature. Float shadow ellipse `rgba(0,0,0,0.12)` di bawah.

### ASCII Art — IDLE State

```
                   ╭───────╮              ← Bristle (ellipse cream, gently waves)
                  ╱  ▓▓▓▓▓  ╲                "rambut" Momo — fluffs on movement
                 │   ▓▓▓▓▓   │
                  ╲         ╱
                   ╰───────╯
                ╔═════════════╗         ← Ferrule (metallic silver rect)
                ║  ═════════  ║            2 decorative ring lines
                ╚═════════════╝
                ┃  ▄▄     ▄▄  ┃         ← Eyebrows (rect 5×2, dark) — SIGNATURE F
                ┃  ◯       ◯   ┃         ← Eyes: ring style (outer light + inner dark dot)
                ┃                ┃           r=5, wider-set 14px (bigger than A-D's r=3)
                ┃    ╲_______╱  ┃         ← Mouth: gentle arc (slight smile)
                ┃                ┃
                ┃      ▮        ┃         ← Accent red stripe (asymmetric signature)
                ┃                ┃         ← Handle (rect brown, rounded top)
                ┃                ┃
                ┃      ╲╱       ┃         ← Handle tapers to point
                ╲───────────────╱
                      ▓▓▓▓▓▓              ← Float shadow
              ────────────────────────    ← Ground line
```

### ASCII Art — HAPPY State

```
              ✦     ✦     ✦
                   ✦  ✦
                   ╭─────────╮           ← Bristle fluffs OUT (wider ellipse 26×22)
                  ╱ ▓▓▓▓▓▓▓ ╲
                 │  ▓▓▓▓▓▓▓  │
                  ╲         ╱
                   ╰─────────╯
                ╔═════════════╗
                ║  ═════════  ║
                ╚═════════════╝
                ┃  ▄▀     ▀▄  ┃         ← Eyebrows raised (angled up +10°)
                ┃  ◉       ◉   ┃         ← Eyes: bigger r=6, sparkle overlay
                ┃                ┃
                ┃  ╲─────────╱  ┃         ← Mouth: wide upward arc (big smile)
                ┃                ┃
                ┃      ▮        ┃
                ┃                ┃         ← Body: stretched Y, squished X
                ┃                ┃
                ┃      ╲╱       ┃
                ╲───────────────╱
                     ▓▓▓                  ← Shadow smaller (Momo rose up)
              ────────────────────────
```

### ASCII Art — CONFUSED State

```
                          ?
                         ╱
                   ╭───────╮              ← Bristle flat (compressed, no wave)
                  ╱         ╲
                 │           │
                  ╲         ╱
                   ╰───────╯
                ╔═════════════╗
                ║  ═════════  ║
                ╚═════════════╝
                ┃  ▄▄     ▀▀  ┃         ← Eyebrows ASYMMETRIC (L flat, R raised)
                ┃  ◯       ◯   ┃         ← Eyes: L slightly bigger (asymmetric)
                ┃                ┃
                ┃   ~~~~~~~~~~  ┃         ← Mouth: zigzag wavy line
                ┃                ┃
                ┃      ▮        ┃
                ┃                ┃         ← Body tilted 12° (oscillates ±3°)
                ┃                ┃
                ┃      ╲╱       ┃
                ╲───────────────╱
                      ▓▓▓▓                 ← Shadow offset (lateral drift ±4px)
              ────────────────────────
```

### ASCII Art — Silhouette (IP Test)

```
                   ╭───────╮
                  ╱         ╲
                 │           │
                  ╲         ╱
                   ╰───────╯
                ╔═════════════╗
                ║             ║
                ╚═════════════╝
                ┃             ┃
                ┃             ┃
                ┃             ┃         ← No face — pure brush silhouette
                ┃             ┃
                ┃             ┃
                ┃             ┃
                ┃      ╲╱      ┃
                ╲───────────────╱
                      ▓▓▓▓▓▓              ← Brush + float = unique among mascots
              ────────────────────────      NO popular mascot is a paintbrush
```

### Color Palette

| Role | Hex Code | RGB | Description |
|------|----------|-----|-------------|
| **Primary (handle)** | `#8B4513` | (139, 69, 19) | Brown wood handle — warm, earthy |
| **Secondary (bristle)** | `#F5F0E8` | (245, 240, 232) | Cream bristle — paint-ready |
| **Ferrule** | `#B8B8B8` | (184, 184, 184) | Metallic silver — tool detail |
| **Accent (stripe)** | `#FF6B6B` | (255, 107, 107) | Coral red — handle stripe (asymmetric signature) |
| **Outline/Eyes/Eyebrows** | `#2D3436` | (45, 52, 54) | Dark grey — face features + handle outline |
| **Shadow** | `rgba(0,0,0,0.12)` | — | Float shadow beneath |

### Shape Inventory (Kaplay.js)

| # | Shape | Code | Size | Color | Function |
|---|-------|------|------|-------|----------|
| 1 | Ellipse | `ellipse(22, 18)` at (0, -22) | 22×18 | `#F5F0E8` | Bristle (bulu kuas = "rambut") |
| 2 | Rectangle | `rect(28, 6)` at (0, -10) | 28×6 | `#B8B8B8` | Ferrule (metallic band) |
| 3 | Rectangle | `rect(28, 2)` at (0, -12) | 28×2 | `#2D3436` | Ferrule ring line (top) |
| 4 | Rectangle | `rect(28, 2)` at (0, -8) | 28×2 | `#2D3436` | Ferrule ring line (bottom) |
| 5 | Rectangle | `rect(28, 36, { radius: 4 })` at (0, 8) | 28×36 | `#8B4513` | Handle (body) |
| 6 | Polygon (tip) | `polygon([v(-6,24), v(6,24), v(0,30)])` | triangle | `#8B4513` | Handle bottom taper |
| 7 | Circle | `circle(5)` at (-7, -2) | r=5 | `#F5F0E8` | Left eye outer (ring) |
| 8 | Circle | `circle(3)` at (-7, -2) | r=3 | `#2D3436` | Left eye inner (dark dot) |
| 9 | Circle | `circle(5)` at (7, -2) | r=5 | `#F5F0E8` | Right eye outer (ring) |
| 10 | Circle | `circle(3)` at (7, -2) | r=3 | `#2D3436` | Right eye inner (dark dot) |
| 11 | Rectangle | `rect(5, 2)` at (-7, -8) | 5×2 | `#2D3436` | Left eyebrow (SIGNATURE F) |
| 12 | Rectangle | `rect(5, 2)` at (7, -8) | 5×2 | `#2D3436` | Right eyebrow |
| 13 | Polygon (mouth arc) | `polygon([6-vertex arc curve])` | ~12×4 | `#2D3436` | Mouth (morphs per state) |
| 14 | Rectangle | `rect(3, 8)` at (0, 8) | 3×8 | `#FF6B6B` | Red accent stripe (asymmetric signature) |
| 15 | Ellipse | `ellipse(24, 5)` at (0, 32) | 24×5 | `rgba(0,0,0,0.12)` | Float shadow |

**Total: 15 shapes** (highest of all 7 options — trade-off: face expressiveness vs asset complexity; still <100KB because all are rect/circle/polygon)

### Animation Specs (5 State)

| State | Body | Eyes (Ring) | Eyebrows (Rect 5×2) | Mouth (Arc morph) | Bristle | Particles |
|-------|------|--------------|---------------------|-------------------|---------|-----------|
| **IDLE** | float `sin(t*2.0)*3`, sway `sin(t*1.5)*2°` | r=5 outer / r=3 inner, neutral | flat 0° | gentle arc (slight smile) | wave gently ±2px L/R | — |
| **HAPPY** | squish→stretch (1.5s) | r=6 outer / r=4 inner, sparkle | angled up +10° | wide upward arc 12×4 | fluff out (scale 1.2×) | 5 yellow sparkles |
| **CONFUSED** | tilt 12° oscillate, drift ±4px | asymmetric L r=6 / R r=4 | asymmetric L flat, R angled +15° | zigzag polyline | flat compressed (scale Y 0.6) | "?" above |
| **THINKING** | slow spin (3s/rot) | r=4 (focused), L↔R dart | flat, narrowed | small circle r=2 | slow gentle wave | 3 orbiting dots |
| **EXCITED** | shake ±3px, 2-bounce (2s) | r=6, flash yellow `#FFE066` | angled up +20° | big O vertical (6×10) | rapid flutter (oscillate ±4px) | 8 confetti + brush stroke trail (4 rects `#FF6B6B`) |

### Face Expression Matrix (5 state × 3 face parts)

| State | Eyes (Ring: outer r=5 + inner r=3 dark) | Eyebrows (Rect 5×2) | Mouth (Arc morph via polygon) |
|-------|------------------------------------------|---------------------|-------------------------------|
| **IDLE** | r=5 outer cream / r=3 inner dark, neutral centered | Flat horizontal, 0° angle | Gentle upward arc `12×3` (slight smile) |
| **HAPPY** | r=6 outer (grown) / r=4 inner, sparkle particle overlay | Angled up +10° (outer end raised) | Wide upward arc `12×4` (big smile curve) |
| **CONFUSED** | Asymmetric: L r=6 (bigger), R r=4 (smaller) | Asymmetric: L flat 0°, R angled up +15° | Morph → zigzag polyline `v(-6,0),v(-2,-2),v(2,2),v(6,0)` (wavy) |
| **THINKING** | r=4 outer (smaller, focused) / r=2 inner, L↔R dart | Flat, narrowed (width 4 instead of 5) | Morph → small circle r=2 (pursed — `circle(2)`) |
| **EXCITED** | r=6, color flash: outer ring yellow `#FFE066` alternating 200ms with cream | Angled up +20° (both raised very high) | Morph → big vertical oval `6×10` (open mouth — wide surprise O) |

### Pros & Cons

| Aspect | Pros | Cons |
|--------|------|------|
| **8-bit fit** | ⭐⭐⭐ Ring eyes + arc mouth = some curves | ⚠️ Bristle ellipse + arc mouth = less pixel-perfect than rect |
| **Kaplay.js** | ⭐⭐⭐ All `rect()`/`circle()`/`polygon()` calls | ⚠️ 15 shapes = highest count; arc mouth morph = custom polygon |
| **IP safety** | ⭐⭐⭐⭐ Paintbrush character is unusual; no famous IP | ⚠️ Generic "art tool mascot" archetype — mitigated by ring eyes + red stripe |
| **Theme fit** | ⭐⭐⭐⭐⭐ Brush = core sketchbook tool | — |
| **Teen appeal (13-15)** | ⭐⭐⭐ Brush = "art-class" feel | ⚠️ 13-15yo may find paintbrush "too educational" / less cool than cube |
| **Animation ease** | ⭐⭐⭐ Bristle wave + ring eyes + arc mouth = unique | ⚠️ 15 shapes to coordinate; bristle morph = custom ellipse scale |
| **Silhouette strength** | ⭐⭐⭐⭐ Vertical brush shape is recognizable | ⚠️ At 16×16 icon, brush reads as "stick" (less iconic than cube/ghost) |
| **Face Expressiveness** | ⭐⭐⭐⭐ Ring eyes + eyebrows + arc morph = strong | ⚠️ Slightly less than E (no hex distinctiveness) and G (no flat pink panel) |

### IP Safety Analysis

#### 3 Closest Existing Characters

| Character | Owner | Similarity | Differentiator (why Momo-F is safe) |
|-----------|-------|-----------|--------------------------------------|
| **Generic Paint Tool Icons** (MSPaint, Photoshop, Procreate) | Various | Brush silhouette | Momo-F: has face (icons have none), has bristle "hair" animation (icons are static), vertical handle with red stripe (icons have no accent), floats (icons are 2D flat), text-bubble only (icons are silent) |
| **ChalkZone "Brushy"** | Nickelodeon | Paintbrush character (1 episode) | Momo-F: ring eyes (Brushy = googly eyes), brown handle (Brushy = blue), no arms (Brushy has arms), float only (Brushy walks), text bubble (Brushy talks), much more obscure reference = low risk |
| **Beauty & the Beast enchanted objects** | Disney | Living art tool archetype | Momo-F: brush specifically (Disney = candelabra/clock/teapot/feather duster, no brush), float only (Disney objects hop), text bubble (Disney objects speak/sing), no arms (Disney objects have arms) |

#### Clawd Distance Score: 2/8

| Dimension | Clawd | Momo-F | Same? |
|-----------|-------|--------|-------|
| Base shape | Rect (horizontal) | Vertical brush (rect + ellipse + triangle) | ✅ Different (vertical mixed shape) |
| Shape type | Geometric | Mixed (geometric + organic bristle) | ✅ Different |
| Color | Salmon pink | Brown + cream + silver | ✅ Different |
| Eye style | Dark round dots | Ring eyes (cream outer + dark inner) | ✅ Different (ring ≠ dot) |
| Limbs | 4-6 legs | None (float only) | ✅ Different |
| Movement | Walk | Float | ✅ Different |
| Context | Terminal | Sketchbook | ✅ Different |
| Asymmetry | Legs (mild) | Red stripe + bristle wave | ⚠️ Same concept (asymmetric detail) |

**2 similarities** (asymmetric detail concept only — even that is different element). **F is the MOST DISTANT option from Clawd of all 7.** Verdict: VERY SAFE from Clawd derivative risk.

---

## 7. OPSI G: "Eraser Ghost" (Penghapus Hantu) — NEW v3.0

### Concept
Sebuah penghapus pink yang sudah menghapus terlalu banyak gambar hingga bagian bawahnya meleleh jadi shape hantu cream. Wajah diukir di panel pink yang flat (paling readable karena kontras pink-dark). Bagian bawah ghost-shape wavy = ekspresi sekunder (memuai 5 peaks saat CONFUSED, mengecil 3 peaks saat THINKING). Pink eraser + cream ghost = combo warna yang TIDAK dimiliki karakter populer manapun. Eraser melayang karena bagian ghost-nya anti-gravity.

### Visual Description
Momo-G vertical oriented, total tinggi 48px lebar 28px. **Bagian atas** (60% = 28×28): penghapus pink `#FFB6C1` rect dengan rounded top `radius: 4` — seperti penghapus sekolah standar. **Bagian bawah** (40% = 28×16): ghost-shape cream `#F5F0E8` dengan wavy bottom edge 4 peaks (polygon 8-vertex). **Wajah** di panel pink (yang flat = paling readable): **mata** = vertical oval (ellipse 3×5 dark `#2D3436`) — orientation berbeda dari dot biasa, lebih readable sebagai "eye" karena vertical aspect ratio. **Eyebrows** = rect 5×2 dark di atas mata, terpisah 14px — SIGNATURE G untuk expression range. **Mulut** = oval 6×3 yang dapat morph: flat horizontal line (IDLE), wide horizontal oval 12×4 (HAPPY), wavy zigzag line (CONFUSED), small circle r=2 (THINKING), big vertical oval 6×10 (EXCITED — open mouth). **Boundary line** navy `#1A1A2E` di tengah penghapus = pemisah eraser-ghost (subtle 2px rect). Float shadow ellipse `rgba(0,0,0,0.10)` di bawah ghost skirt. Wavy bottom oscillates gently (`sin(t*3 + i*0.5)*2` per vertex).

### ASCII Art — IDLE State

```
                  ╭──────────────╮         ← Eraser pink (rect, rounded top)
                  │              │            Pink #FFB6C1
                  │  ▄▄      ▄▄  │         ← Eyebrows (rect 5×2, dark) — SIGNATURE G
                  │  ▮       ▮   │         ← Eyes (vertical oval 3×5, dark)
                  │              │            Vertical = more readable than dot
                  │     ════     │         ← Mouth: small horizontal line (neutral)
                  │              │
                  ├──────────────┤         ← Eraser-ghost boundary line (navy)
                  │              │         ← Ghost cream bottom
                  ╰─╮  ╭─╮  ╭─╮  ╭─╯         Wavy bottom (4 peaks, oscillates)
                    ╰──╯  ╰──╯  ╰─╯
                       ▓▓▓▓▓▓              ← Float shadow
              ────────────────────────     ← Ground line
```

### ASCII Art — HAPPY State

```
              ✦    ✦    ✦
                   ✦  ✦
                  ╭──────────────╮         ← Eraser pink (squished slightly)
                  │              │
                  │  ▄▀      ▀▄  │         ← Eyebrows raised (angled up +10°)
                  │  ◉       ◉   │         ← Eyes: bigger, sparkle overlay
                  │              │
                  │   ╭──────╮   │         ← Mouth: wide horizontal oval (smile)
                  │   ╰──────╯   │
                  ├──────────────┤
                  │              │         ← Ghost bottom (pulled UP tight)
                  ╰──╮       ╭──╯            Waves compressed (3 peaks, tucked)
                     ╰───────╯
                       ▓▓▓                 ← Shadow smaller (Momo rose)
              ────────────────────────
```

### ASCII Art — CONFUSED State

```
                          ?
                         ╱
                  ╭──────────────╮         ← Eraser tilted 10° (oscillates)
                  │              │
                  │  ▄▄      ▀▀  │         ← Eyebrows ASYMMETRIC (L flat, R raised)
                  │  ▮       ◯   │         ← Eyes: L vertical oval, R round (asymmetric shape)
                  │              │
                  │   ~~~~~~~~   │         ← Mouth: wavy zigzag line
                  │              │
                  ├──────────────┤
                  │              │         ← Ghost bottom PUFFED OUT (5 peaks)
                  ╰──╮ ╭─╮ ╭─╮ ╭──╯          Expanded = stress response
                     ╰─╯ ╰─╯ ╰─╯
                       ▓▓▓▓▓                ← Shadow wobbly
              ────────────────────────
```

### ASCII Art — Silhouette (IP Test)

```
                  ╭──────────────╮
                  │              │
                  │              │
                  │              │
                  │              │
                  │              │
                  │              │
                  ├──────────────┤         ← Boundary line visible
                  │              │
                  ╰─╮  ╭─╮  ╭─╮  ╭─╯         Wavy bottom = KEY identifier
                    ╰──╯  ╰──╯  ╰─╯
                       ▓▓▓▓▓▓              ← Pink rect + ghost wavy bottom = unique hybrid
              ────────────────────────      NO mascot combines eraser + ghost
```

### Color Palette

| Role | Hex Code | RGB | Description |
|------|----------|-----|-------------|
| **Primary (eraser)** | `#FFB6C1` | (255, 182, 193) | Pink eraser — school supply color |
| **Secondary (ghost)** | `#F5F0E8` | (245, 240, 232) | Cream ghost — sketchbook paper |
| **Boundary** | `#1A1A2E` | (26, 26, 46) | Navy line — eraser-ghost separator |
| **Outline/Eyes/Eyebrows** | `#2D3436` | (45, 52, 54) | Dark grey — face features |
| **Accent (sparkle)** | `#FFE066` | (255, 224, 102) | Yellow — sparkle particles (HAPPY/EXCITED) |
| **Shadow** | `rgba(0,0,0,0.10)` | — | Float shadow beneath ghost skirt |

### Shape Inventory (Kaplay.js)

| # | Shape | Code | Size | Color | Function |
|---|-------|------|------|-------|----------|
| 1 | Rectangle | `rect(28, 28, { radius: 4 })` at (0, -8) | 28×28 | `#FFB6C1` | Eraser top (rounded) |
| 2 | Rectangle | `rect(28, 2)` at (0, 6) | 28×2 | `#1A1A2E` | Boundary line (eraser-ghost separator) |
| 3 | Polygon (ghost skirt) | `polygon([v(-14,6), v(14,6), v(14,16), v(10,12), v(6,18), v(2,12), v(-2,18), v(-6,12), v(-10,18), v(-14,12)])` | ~28×12 | `#F5F0E8` | Ghost wavy bottom (4-5 peaks, oscillates) |
| 4 | Ellipse (eye L) | `ellipse(3, 5)` at (-7, -10) | 3×5 | `#2D3436` | Left eye (vertical oval — more readable than dot) |
| 5 | Ellipse (eye R) | `ellipse(3, 5)` at (7, -10) | 3×5 | `#2D3436` | Right eye (vertical oval) |
| 6 | Rectangle | `rect(5, 2)` at (-7, -14) | 5×2 | `#2D3436` | Left eyebrow (SIGNATURE G) |
| 7 | Rectangle | `rect(5, 2)` at (7, -14) | 5×2 | `#2D3436` | Right eyebrow |
| 8 | Ellipse (mouth) | `ellipse(6, 2)` at (0, -2) | 6×2 | `#2D3436` | Mouth (morphs per state via scale + shape swap) |
| 9 | Ellipse | `ellipse(24, 5)` at (0, 22) | 24×5 | `rgba(0,0,0,0.10)` | Float shadow |

**Total: 9 shapes** (efficient — only 4 more than A/B/C/D's 5, but huge face expressiveness gain)

### Animation Specs (5 State)

| State | Body | Eyes (Vertical Oval) | Eyebrows (Rect 5×2) | Mouth (Oval morph) | Ghost skirt (waves) | Shadow | Particles |
|-------|------|----------------------|---------------------|--------------------|--------------------|--------|-----------|
| **IDLE** | float `sin(t*2.3)*3`, sway `sin(t*1.5)*2°` | 3×5 neutral | flat 0° | 6×2 flat horizontal (line) | 4 peaks, oscillate `sin(t*3 + i*0.5)*2` | breathe ±10% | — |
| **HAPPY** | squish→stretch (1.5s) | 4×6 (bigger), sparkle | angled up +10° | morph → wide horizontal oval 12×4 | 3 peaks compressed (pulled UP) | shrink to 70% | 5 yellow sparkles |
| **CONFUSED** | tilt 10° oscillate, drift ±4px | asymmetric L 3×6 / R round 3×3 | asymmetric L flat, R angled +15° | morph → zigzag polyline 4-vertex | 5 peaks PUFFED OUT (expanded, stress) | wobble ±15% | "?" above |
| **THINKING** | slow spin (3s/rot) | 3×4 (smaller, focused), L↔R dart | flat, narrowed (width 4) | morph → small circle r=2 (pursed) | 3 peaks compressed (focused, tucked) | wobble ±15% | 3 orbiting dots |
| **EXCITED** | shake ±3px, 2-bounce (2s) | 4×6, flash yellow `#FFE066` | angled up +20° | morph → big vertical oval 6×10 (open mouth O) | 4 peaks rapid oscillation (excited flutter) | pulse with shake | 8 confetti `#FFE066` + 4 navy `#1A1A2E` |

### Face Expression Matrix (5 state × 3 face parts)

| State | Eyes (Vertical Oval 3×5) | Eyebrows (Rect 5×2) | Mouth (Oval 6×2 morph) |
|-------|--------------------------|---------------------|------------------------|
| **IDLE** | 3×5 vertical oval, dark `#2D3436`, neutral | Flat horizontal, 0° angle | 6×2 flat horizontal (line — almost invisible, neutral closed mouth) |
| **HAPPY** | 4×6 vertical oval (grown), sparkle particle overlay | Angled up +10° (outer end raised) | Morph → wide horizontal oval `12×4` (smile — wider than tall) |
| **CONFUSED** | Asymmetric: L 3×6 (taller), R 3×3 round (shorter) | Asymmetric: L flat 0°, R angled up +15° | Morph → zigzag polyline `v(-6,0),v(-2,-2),v(2,2),v(6,0)` (wavy) |
| **THINKING** | 3×4 (smaller, focused), L↔R position dart every 600ms | Flat, narrowed (width 4 instead of 5) | Morph → small circle r=2 (pursed — `circle(2)` replaces ellipse) |
| **EXCITED** | 4×6 (bigger), color flash: dark `#2D3436` alternating 200ms with yellow `#FFE066` | Angled up +20° (both raised very high) | Morph → big vertical oval `6×10` (open mouth — taller than wide, big O) |

### Pros & Cons

| Aspect | Pros | Cons |
|--------|------|------|
| **8-bit fit** | ⭐⭐⭐⭐ Rect eraser + polygon ghost = geometric | ⚠️ Wavy bottom = polygon (still geometric but multi-vertex) |
| **Kaplay.js** | ⭐⭐⭐⭐ All `rect()`/`ellipse()`/`polygon()` calls, 9 shapes total | ⚠️ Wavy polygon vertex animation = standard but needs care |
| **IP safety** | ⭐⭐⭐ Pink eraser rescues ghost silhouette | ⚠️ Ghost bottom has Pac-Man precedent (mitigated by pink top + boundary line + no eyes-on-stalks) |
| **Theme fit** | ⭐⭐⭐⭐⭐ Eraser = core sketchbook tool (complement to brush) | — |
| **Teen appeal (13-15)** | ⭐⭐⭐⭐ Pink + ghost = playful, school-relatable | ⚠️ Some 13yo boys may dismiss pink as "too girly" — mitigate by emphasizing ghost + eraser function over color |
| **Animation ease** | ⭐⭐⭐⭐ Wave bottom + rect deform + oval morph = proven pattern (similar to C) | ⚠️ Wave vertex animation = more complex than A's pure rect |
| **Silhouette strength** | ⭐⭐⭐ Pink rect + ghost wavy = hybrid recognizable | ⚠️ Ghost bottom alone = Pac-Man risk (pink top rescues at full body, but icon-only = risky) |
| **Face Expressiveness** | ⭐⭐⭐⭐⭐ Vertical oval eyes (unique orientation) + eyebrows + oval morph = TIED STRONGEST with E | — |

### IP Safety Analysis

#### 3 Closest Existing Characters

| Character | Owner | Similarity | Differentiator (why Momo-G is safe) |
|-----------|-------|-----------|--------------------------------------|
| **Pac-Man Ghost** (Blinky/Pinky/Inky/Clyde) | Bandai Namco | Ghost wavy bottom silhouette | Momo-G: pink rect TOP (Pac-Man = full dome ghost, no rect top), has eyebrows (Pac-Man has none), vertical oval eyes (Pac-Man = white-on-stalks), boundary line (Pac-Man has none), eraser concept (Pac-Man = monster). Pink top is the KEY differentiator — no Pac-Man ghost has a pink rectangular top |
| **Slimer (Ghostbusters)** | Sony/Columbia | Green ghost with face | Momo-G: pink+cream (Slimer = green), rect top (Slimer = blob), vertical oval eyes (Slimer = round), no arms (Slimer has arms), eraser bottom half (Slimer = full blob). Completely different silhouette |
| **Casper (Friendly Ghost)** | DreamWorks/Classic Media | White ghost with face | Momo-G: pink rect top (Casper = full dome), wavy bottom 4-5 peaks (Casper = smooth dome), vertical oval eyes (Casper = round), has eyebrows (Casper has none), eraser concept (Casper = ghost child). Hybrid eraser-ghost = no precedent |

#### Clawd Distance Score: 3/8

| Dimension | Clawd | Momo-G | Same? |
|-----------|-------|--------|-------|
| Base shape | Rect (full body) | Rect top + ghost bottom (hybrid) | ⚠️ Partial — rect top half similar |
| Shape type | Geometric | Mixed (geometric top + organic ghost bottom) | ⚠️ Partial |
| Color | Salmon pink | Pink eraser + cream ghost | ⚠️ Partial — pink family but different shade |
| Eye style | Dark round dots | Dark vertical ovals | ⚠️ Same family (dark, no pupils) |
| Limbs | 4-6 legs | None (float only) | ✅ Different |
| Movement | Walk | Float | ✅ Different |
| Context | Terminal | Sketchbook | ✅ Different |
| Asymmetry | Legs (mild) | Boundary line + ghost skirt | ✅ Different element |

**3 similarities** (rect top, dark-dot-eye family, pink-family color) — MODERATE distance. Mitigated by ghost bottom half (Clawd has no ghost), vertical oval eyes (Clawd = round dots), pink eraser top is materially different from salmon pink crab body. **Verdict: SAFE with mitigations (ghost bottom + boundary line + vertical oval eyes).**

---

## 8. Weighted Scoring Matrix

### 8.1 Criteria & Weights (v3.0 — added Face Expressiveness, redistributed to total 1.00)

| # | Criterion | Weight (v3.0) | Weight (v2.0) | Change | Rationale |
|---|-----------|---------------|---------------|--------|-----------|
| 1 | **Kaplay.js Compatibility** | 0.15 | 0.20 | -0.05 | Must be buildable in our engine without workarounds |
| 2 | **8-bit Geometric Fit** | 0.10 | 0.15 | -0.05 | Core design constraint from user — rect-based, pixel aesthetic |
| 3 | **IP Safety** | 0.15 | 0.20 | -0.05 | Must be original — legal risk is non-negotiable |
| 4 | **Sketchbook Theme Fit** | 0.15 | 0.15 | 0 | Must feel native to sketchbook universe, not generic |
| 5 | **Teen Appeal (13-15)** | 0.10 | 0.10 | 0 | Target audience must find Momo appealing, not childish |
| 6 | **Animation Ease** | 0.10 | 0.10 | 0 | Float-only animation must be achievable with simple tweens |
| 7 | **Silhouette Strength** | 0.10 | 0.10 | 0 | Must pass black-shadow test for brand recognition |
| 8 | **Face Expressiveness** ⭐NEW | 0.15 | — | +0.15 | 5-state animation requires readable face — user feedback v3.0 |
| | **TOTAL** | **1.00** | **1.00** | 0 | — |

### 8.2 Scoring (1-5 scale per criterion, 7 options)

| Criterion | Weight | A: Sticky Note | B: Ink Blob | C: Sketch Ghost | D: Origami | E: Doodle Cube ⭐NEW | F: Brush Spirit ⭐NEW | G: Eraser Ghost ⭐NEW |
|-----------|--------|---------------|-------------|-----------------|------------|---------------------|---------------------|---------------------|
| Kaplay.js Compat | 0.15 | 5 | 4 | 4 | 2 | 4 | 3 | 4 |
| 8-bit Geometric Fit | 0.10 | 5 | 3 | 4 | 3 | 5 | 3 | 4 |
| IP Safety | 0.15 | 4 | 5 | 3 | 5 | 4 | 4 | 3 |
| Sketchbook Theme Fit | 0.15 | 4 | 5 | 5 | 5 | 5 | 5 | 5 |
| Teen Appeal | 0.10 | 3 | 4 | 4 | 3 | 4 | 3 | 4 |
| Animation Ease | 0.10 | 5 | 3 | 4 | 2 | 4 | 3 | 4 |
| Silhouette Strength | 0.10 | 4 | 3 | 4 | 5 | 4 | 4 | 3 |
| **Face Expressiveness** ⭐NEW | 0.15 | 2 | 2 | 2 | 2 | **5** | 4 | **5** |
| **Weighted Total** | **1.00** | **3.95** | **3.70** | **3.70** | **3.45** | **4.40** | **3.70** | **4.05** |
| **Rank (v3.0)** | | #3 | #4 (tied) | #4 (tied) | #7 | **🥇 #1** | #4 (tied) | **🥈 #2** |

### 8.3 Score Calculation (weighted)

| Option | Calculation (weight × score, summed) | Total |
|--------|--------------------------------------|-------|
| **A: Sticky Note** | (5×0.15)+(5×0.10)+(4×0.15)+(4×0.15)+(3×0.10)+(5×0.10)+(4×0.10)+(2×0.15) | **3.95 / 5.00** |
| **B: Ink Blob** | (4×0.15)+(3×0.10)+(5×0.15)+(5×0.15)+(4×0.10)+(3×0.10)+(3×0.10)+(2×0.15) | **3.70 / 5.00** |
| **C: Sketch Ghost** | (4×0.15)+(4×0.10)+(3×0.15)+(5×0.15)+(4×0.10)+(4×0.10)+(4×0.10)+(2×0.15) | **3.70 / 5.00** |
| **D: Origami Monster** | (2×0.15)+(3×0.10)+(5×0.15)+(5×0.15)+(3×0.10)+(2×0.10)+(5×0.10)+(2×0.15) | **3.45 / 5.00** |
| **E: Doodle Cube** ⭐ | (4×0.15)+(5×0.10)+(4×0.15)+(5×0.15)+(4×0.10)+(4×0.10)+(4×0.10)+(5×0.15) | **4.40 / 5.00** |
| **F: Brush Spirit** | (3×0.15)+(3×0.10)+(4×0.15)+(5×0.15)+(3×0.10)+(3×0.10)+(4×0.10)+(4×0.15) | **3.70 / 5.00** |
| **G: Eraser Ghost** ⭐ | (4×0.15)+(4×0.10)+(3×0.15)+(5×0.15)+(4×0.10)+(4×0.10)+(3×0.10)+(5×0.15) | **4.05 / 5.00** |

### 8.4 Score Comparison v2.0 → v3.0

| Option | v2.0 Score (7 crit) | v3.0 Score (8 crit, w/ Face Express) | Δ | v2.0 Rank | v3.0 Rank |
|--------|---------------------|--------------------------------------|----|-----------|-----------|
| A: Sticky Note | 4.35 | 3.95 | -0.40 | #1 | #3 |
| B: Ink Blob | 3.95 | 3.70 | -0.25 | #2 (tied) | #4 (tied) |
| C: Sketch Ghost | 3.95 | 3.70 | -0.25 | #2 (tied) | #4 (tied) |
| D: Origami Monster | 3.45 | 3.45 | 0.00 | #4 | #7 |
| **E: Doodle Cube** ⭐NEW | — | **4.40** | — | — | **🥇 #1** |
| **F: Brush Spirit** ⭐NEW | — | 3.70 | — | — | #4 (tied) |
| **G: Eraser Ghost** ⭐NEW | — | **4.05** | — | — | **🥈 #2** |

**Key finding:** Adding Face Expressiveness criterion (weight 0.15) shifted TOP 2 from A+C (both dropped due to minimal faces scoring 2/5) to E+G (both scoring 5/5 for face expressiveness). The trade-off is justified: Momo needs to convey 5 emotion states (IDLE/HAPPY/CONFUSED/THINKING/EXCITED) through face alone (no voice, no arms, no body language beyond float) — so face expressiveness is now critical, not optional.

### 8.5 Visual Score Radar (v3.0)

```
                    Kaplay.js Compat (0.15)
                          5
                          │
              D:2 ────────┼──────── A:5
              F:3 ────────┼──────── E:4
              B:4   C:4   │   G:4
                          │
   Silhouette (0.10)      │       8-bit Fit (0.10)
   5 ─────────────────────┼──────────────────── 1
   D:5    E:4  C:4        │        A:5  E:5
   F:4    A:4             │        C:4  G:4
   B:3    G:3             │        B:3  F:3
                          │
              B:5  C:5  D:5  E:5  F:5  G:5 ── Theme Fit (0.15)
              A:4

   IP Safety (0.15):    A:4  B:5  C:3  D:5  E:4  F:4  G:3
   Teen Appeal (0.10):  A:3  B:4  C:4  D:3  E:4  F:3  G:4
   Animation (0.10):    A:5  B:3  C:4  D:2  E:4  F:3  G:4

   ⭐ Face Expressiveness (0.15) — NEW v3.0:
       A:2  B:2  C:2  D:2  (minimal dot+line, weak)
       F:4                (ring eyes + arc mouth, medium)
       E:5  G:5           (eyebrows + morph mouth + larger eyes, STRONG)
```

---

## 9. TOP 2 Recommendations (v3.0)

### Recommendation #1: **OPSI E — "Doodle Cube"** (Score: 4.40) ⭐ NEW v3.0

**Why it wins:** Highest combined score across all 7 options. Best face expressiveness (tied #1 with G). Pure 8-bit geometric (rect + hex polygon). Cube shape has IP-safety precedent but mitigated by opaque cream + teal fold + eyebrows. Sketchbook-native (paper cube).

| Strength | Detail |
|----------|--------|
| **Face expressiveness** | Hex eyes (r=4, larger than A-D's r=3) + eyebrows (rect 4×2, SIGNATURE E) + morphing mouth (rect → oval → zigzag → circle → triangle) = 5 distinct face states with 3 variable parts (eyes, eyebrows, mouth) = 5×3 = 15 visual signals |
| **8-bit purity** | All rect/polygon calls — pixel-perfect, no curves |
| **Cube shape** | 2.5D isometric — visually distinct from any other Momo option (rect A, blob B, dome C, diamond D, brush F, hybrid G) |
| **Theme perfection** | Paper cube = sketchbook native (paper folding + 2.5D depth illusion = origami-meets-sketch) |
| **Animation range** | Cube spin (THINKING) is unique — A/B/C/D/G can only tilt, not spin in 2.5D |
| **Performance** | 10 shapes total — slightly more than A-D (5 shapes each) but still <100KB assets, <5MB RAM, <5% CPU per frame |

**Trade-offs to acknowledge:**

| Risk | Mitigation |
|------|-----------|
| Minecraft Slime precedent (cube + face) | Mitigated: opaque cream (not transparent green), teal fold corner (Slime has none), 2.5D isometric (Slime is flat front), eyebrows (Slime has none), no bouncing physics (Momo floats), sketchbook context (Slime = cave). At silhouette test, cube + float + fold = distinct |
| 2.5D Z-ordering complexity | Mitigated: 3 faces drawn in fixed order (top → side → front), no parallax. Standard 2D game engine pattern. Tested with `polygon()` calls in Kaplay.js |
| At 16×16 icon size, cube reads as square (similar to A) | Mitigated: at icon size, use distinct silhouette (cube + fold + shadow) — fold corner is the differentiator. Or use alternate "front face only" icon variant |
| 13-15yo may say "Minecraft rip-off" initially | Mitigated: emphasize fold corner (magic ink mark), eyebrows, and float — none of which Slime has. Position Momo-E as "sketchbook cube that folds itself" not "Minecraft cube" |

**Recommended refinements for OPSI E:**
1. Always render the teal fold corner — it's the asymmetric signature that separates Momo-E from generic cube characters
2. Eyebrows should be the FIRST face part to animate per state (before eyes/mouth) — they're the primary emotion signal
3. For THINKING state, the 2.5D spin should be slow (3s/rotation) — too fast reads as "dizzy" not "thinking"
4. Consider adding subtle pencil-doodle texture lines on the front face (like someone sketched on it) — ties to sketchbook theme

---

### Recommendation #2: **OPSI G — "Eraser Ghost"** (Score: 4.05) ⭐ NEW v3.0

**Why it's second:** Strongest face expressiveness (tied with E) thanks to vertical oval eyes + eyebrows + oval morph. Hybrid eraser-ghost combo has no precedent. Complements E conceptually (E = paper + creation, G = eraser + deletion — together they cover the sketchbook lifecycle).

| Strength | Detail |
|----------|--------|
| **Face expressiveness (tied #1)** | Vertical oval eyes (unique orientation — different from dot or hex) + eyebrows + morphing mouth = 5 distinct face states. The vertical oval eyes are SIGNATURE G — no other option uses vertical aspect ratio |
| **Hybrid concept** | Eraser + ghost = combination no popular mascot uses. Pink top + cream bottom = color combo unique among mascots |
| **Theme complement** | Eraser is the natural complement to brush/pen/pencil in sketchbook toolkit — completes the set |
| **Ghost skirt as secondary expression** | Wavy bottom (4 peaks) can puff out (5 peaks = stressed/CONFUSED) or compress (3 peaks = focused/THINKING) — secondary expression channel beyond face |
| **Performance** | 9 shapes total — only 4 more than A-D (5 shapes each), efficient for the face expressiveness gain |
| **IP rescue** | Pink eraser top rescues ghost bottom from Pac-Man association — at silhouette, hybrid shape is unmistakably "eraser-ghost", not "ghost alone" |

**Trade-offs to acknowledge:**

| Risk | Mitigation |
|------|-----------|
| Ghost bottom has Pac-Man precedent (Blinky/Pinky/Inky/Clyde) | Mitigated: pink rect TOP (Pac-Man = full dome ghost, no rect top), boundary line (Pac-Man has none), eyebrows (Pac-Man has none), vertical oval eyes (Pac-Man = white-on-stalks), eraser concept (Pac-Man = monster). Pink top is the KEY differentiator — no Pac-Man ghost has a pink rectangular top |
| Pink may feel "too girly" for 13-15yo boys | Mitigated: emphasize ghost function over color (ghost = cool, eraser = playful); pink is also "Momo pink" not "Barbie pink" — softer tone `#FFB6C1`; boundary line + vertical eyes give it edge |
| Wavy bottom = polygon vertex animation (more complex than A) | Mitigated: standard pattern (4-vertex wave, oscillate via `sin(t*3 + i*0.5)*2` per vertex) — already proven in OPSI C. Same code structure |
| Silhouette risk at 16×16 (ghost bottom alone = Pac-Man) | Mitigated: always render pink top with face. For icon-only contexts, use pink rect + simplified wavy bottom (2 peaks instead of 4). NEVER render ghost bottom alone without pink top |

**Recommended refinements for OPSI G:**
1. The boundary line (navy `#1A1A2E`) between eraser and ghost should ALWAYS be visible — it's the secondary signature after the pink top
2. The wavy bottom peaks should oscillate at different phases per peak (`sin(t*3 + i*0.5)*2` where i = peak index) — this gives "ghost flutter" feel, not "uniform wave"
3. For EXCITED state, the ghost skirt should flutter RAPIDLY (oscillate at 8Hz, not 3Hz) — visual cue for high energy
4. Vertical oval eyes are SIGNATURE G — never use round dots or hexagons. The vertical aspect ratio is what makes G's face distinct from E's hex and F's ring

---

### Why OPSI A and C are NO LONGER Top 2 (v2.0 → v3.0 shift)

| Option | v2.0 Rank | v3.0 Rank | Why dropped |
|--------|-----------|-----------|-------------|
| **A: Sticky Note** | #1 (4.35) | #3 (3.95) | Face Expressiveness score = 2/5 (minimal dot+line). User feedback v3.0: "masih kurang paham" karena wajah minimal. Without face expressiveness criterion, A wins on technical feasibility. With it added (weight 0.15), A drops below E and G |
| **C: Sketch Ghost** | #2 (3.95) | #4 tied (3.70) | Same face expressiveness issue (2/5) + IP risk from Pac-Man ghost precedent (already flagged in v2.0). Adding Face Expressiveness pushes C below E, G, and A |

**Why this shift is correct:**

The v3.0 user feedback specifically identified face minimalism as the problem. The 5-state animation bible (IDLE/HAPPY/CONFUSED/THINKING/EXCITED) requires face to be the PRIMARY expression channel because:
1. **No voice/NLP** (arahan Bu Hesti) — face must convey all emotion visually
2. **No arms** (no legs, no wings) — face is the only expressive body part beyond float bob
3. **Text bubble is informational**, not emotional — text says "Coba lagi ya!" but face must show the supportive tone
4. **13-15yo audience** reads emotion faster from face than from text — face is the "first read" channel

Therefore, the v3.0 criterion addition (Face Expressiveness, weight 0.15) is not arbitrary — it directly addresses user feedback and reflects the animation bible's requirements.

---

### Why OPSI B, D, and F are NOT Top 2

| Option | Why Not Top 2 | Dealbreaker |
|--------|---------------|-------------|
| **B: Ink Blob** | Organic blob harder to animate in 8-bit; at 16×16 reads as circle (generic); dark palette heavy for educational game; face is dot+line only (2/5) — same minimal issue as A/C/D | At icon size, blob = generic circle. IP silhouette weak. Face not expressive enough for v3.0 requirement. |
| **D: Origami Monster** | Polygon vertex animation hardest in Kaplay.js; 3D illusion adds rendering complexity; angular/diamond makes text-bubble placement awkward; face is dot+line on diamond (2/5) — minimal face issue + hardest technical | Kaplay.js polygon animation unreliable; too many workarounds. Face not expressive. |
| **F: Brush Spirit** | 15 shapes (highest of all 7); ring eyes + arc mouth = some curves (less 8-bit); teen appeal weaker than E/G ("art class" feel); at 16×16 brush reads as "stick" (less iconic) | 15 shapes = performance concern; 8-bit fit only 3/5; silhouette weak at icon size. Despite strong Clawd distance (2/8), loses on technical + aesthetic. |

---

### Hybrid Recommendation (If Budget Allows v3.0)

If the team wants the BEST of E and G (both new v3.0 winners), consider a **hybrid approach** that combines:

```
┌─────────────────────────────────────────────────────────────────────┐
│          HYBRID MOMO v3.0: "Sketch Eraser Cube"                     │
│                                                                     │
│  FROM E (Doodle Cube):  2.5D cube body shape                        │
│                         Kaplay.js rect() + polygon() calls          │
│                         Teal fold corner (asymmetric signature)     │
│                         Hex eyes (r=4) — wider-set 14px             │
│                         Eyebrows (rect 4×2) — SIGNATURE             │
│                         Mouth morph matrix (rect→oval→zigzag→O→△)   │
│                                                                     │
│  FROM G (Eraser Ghost): Pink color palette (eraser aesthetic)       │
│                         Ghost wavy bottom (secondary expression)    │
│                         Vertical oval eyes option (alternative)     │
│                         Eraser concept (sketchbook complement)      │
│                                                                     │
│  RESULT: A pink 2.5D cube with hex eyes, eyebrows, morphing        │
│  mouth, teal fold corner, and ghost wavy bottom edge.              │
│                                                                     │
│  Trade-off: more shapes (12-14 total) but maximum face             │
│  expressiveness + unique silhouette.                                │
│                                                                     │
│  NOTE: This is OPTIONAL. E alone or G alone already wins.           │
│  Hybrid only if team wants to maximize differentiation.             │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 10. Reference Character Analysis (v3.0)

### 10.1 Research Synthesis (5 web searches + 2 additional)

| Search | Source | Key Finding Applied to Momo E/F/G |
|--------|--------|-----------------------------------|
| **1. Kawaii face design principles** | Tatyana Deniz, Design Bundles | Eyes spread out wider than usual (14px vs 12px in A-D). Mouth sits just below eyes. Slight line variation changes expression completely → eyebrows + morphing mouth = key |
| **2. Geometric mascot face 8-bit** | StockCake, Vecteezy, Pinterest | "Bold geometric pixel art character with cubic body" + "expressive happy face" validates E direction. Hex/cube = 8-bit pure |
| **3. Minimal character design personality** | Graphic Mama, Disney Shape Language PDF | Shape language: rect = sturdy/friendly, circle = soft/harmless, triangle = dynamic. Momo-E uses rect (cube) = sturdy/friendly. Variance in size/shape = personality |
| **4. ASCII face expression** | asky.lol, texteditor.com, 1lineart | Eye shape variance (°, □, ▰, ╹, ◯, ⬡) is the PRIMARY signal in minimal face design. Mouth shape secondary. Eyebrows tertiary but critical for emotion range |
| **5. Pixel art mascot face states** | Vecteezy, Dreamstime, DeviantArt | 5-state emotion sets (happy/sad/angry/scared/surprised) typically use 3-4 face parts: eyes + mouth + eyebrows + (sometimes cheeks — AVOID per Momo constraints) |
| **6. Sackboy origin** | Media Molecule blog | Sackboy started as "YellowHead" = pink square body + triangular yellow head (programmer art). Proves simple geometric shapes CAN become iconic mascots. Validates E (cube) approach |
| **7. Minecraft slime / Toad / Goomba** | YouTube, TikTok, Facebook | Goomba signature = angry EYEBROWS (key differentiator). Toad = huge head shape + tiny face on small visible portion. Minecraft Slime = green cube + 2 dot eyes + flat mouth — confirms E precedent exists but mitigations work |

### 10.2 Reference Character Analysis (6+ characters with simple but expressive faces)

#### Character 1: Sackboy (LittleBigPlanet) — Media Molecule

| Aspect | Detail |
|--------|--------|
| **Shape inventory** | Square/rect fabric body + oval head + button eyes + stitched mouth + arms/legs |
| **How face expresses 5 states** | IDLE: neutral dot eyes + line mouth. HAPPY: eyes squint + mouth wide. CONFUSED: head tilt + asymmetric eyes + wavy mouth. THINKING: eyes look up + small mouth. EXCITED: eyes wide + open mouth + body bounce |
| **IP-safe lessons** | Fabric texture + stitching detail = signature that no other mascot has. Proves simple shapes (rect body) + texture = unique identity |
| **Adopt for Momo** | Eyebrows as primary emotion signal (Sackboy has stitched eyebrows). Body texture (Momo-E: pencil-doodle marks on front face) |
| **Adapt for Momo** | Sackboy has arms/legs (Momo: float only, no limbs). Sackboy is fabric (Momo: paper). Sackboy has button eyes (Momo: dark dots/hex — no pupils) |
| **Avoid for Momo** | Sackboy's stitches (too detailed for 8-bit). Sackboy's arms (Momo has none) |

#### Character 2: Cubone (Pokemon) — Nintendo/Game Freak

| Aspect | Detail |
|--------|--------|
| **Shape inventory** | Skull helmet (hides upper face) + brown body + bone weapon |
| **How face expresses 5 states** | IDLE: shadowed eyes (visible only as dark spots in skull) + small mouth. HAPPY: eyes glow + mouth curves. CONFUSED: head tilt + asymmetric eye glow. THINKING: eyes look aside + mouth flat. EXCITED: eyes wide + mouth open |
| **IP-safe lessons** | Hiding part of the face (skull) CREATES mystery + signature. Eye glow in shadow = expressive despite minimal visible face |
| **Adopt for Momo** | Asymmetric face masking concept. Eye shape variance (Cubone: shadow spots; Momo-E: hex; Momo-G: vertical oval) as signature |
| **Adapt for Momo** | Cubone wears skull (Momo: no helmet — face on flat panel). Cubone has body + limbs (Momo: float only) |
| **Avoid for Momo** | Skull helmet (too dark/scary for 13-15yo educational game). Bone weapon (Momo has no hands/props) |

#### Character 3: Bomberman — Konami/Hudson Soft

| Aspect | Detail |
|--------|--------|
| **Shape inventory** | Pink round body + simple dot eyes + line mouth + small antenna |
| **How face expresses 5 states** | IDLE: dot eyes + line mouth. HAPPY: bigger eyes + smile curve. CONFUSED: tilted head + wavy mouth. THINKING: eyes look up + small mouth. EXCITED: wide eyes + open mouth + antenna wobble |
| **IP-safe lessons** | Pink + round body + simple face = proven cute formula. Antenna = asymmetric signature that separates from generic pink blobs |
| **Adopt for Momo** | Antenna concept (Momo-E: teal fold corner = equivalent asymmetric signature). Pink palette viable (Momo-G uses pink eraser top) |
| **Adapt for Momo** | Bomberman has limbs + walks (Momo: float only). Bomberman is full-body pink (Momo-G: only top half pink) |
| **Avoid for Momo** | Bomberman's white eyes with pupils (Momo: dark dot/hex eyes only — no pupils per IP-safe constraint). Bomberman's antenna (too similar — Momo uses fold corner instead) |

#### Character 4: Slime (Minecraft) — Mojang/Microsoft

| Aspect | Detail |
|--------|--------|
| **Shape inventory** | Green cube (translucent) + 2 black dot eyes + flat black mouth |
| **How face expresses 5 states** | IDLE: dot eyes + flat mouth. HAPPY: slightly curved mouth (limited). CONFUSED: N/A (Slime has limited expressions). THINKING: N/A. EXCITED: N/A — Slime is mostly emotionless, expresses through physics (bounce/squish) |
| **IP-safe lessons** | Cube + dot eyes + line mouth = MINIMAL expression (this is the problem Momo-E must AVOID — add eyebrows + morphing mouth). Green translucent = signature. Physics-based expression (squish/bounce) = secondary channel |
| **Adopt for Momo** | Cube body shape (E). Physics-based secondary expression (squish/stretch in HAPPY/EXCITED) |
| **Adapt for Momo** | Slime is green translucent (Momo-E: cream opaque). Slime has dot+line minimal face (Momo-E: hex+eyebrows+morphing mouth — much more expressive). Slime bounces (Momo: floats) |
| **Avoid for Momo** | Slime's minimal face (this is what user complained about in A-D). Slime's translucent green (too similar — Momo uses opaque cream). Slime's lack of eyebrows (Momo adds them for expression) |

#### Character 5: Toad (Mario) — Nintendo

| Aspect | Detail |
|--------|--------|
| **Shape inventory** | Huge mushroom head (red cap with white spots) + small face on lower visible portion + small body |
| **How face expresses 5 states** | IDLE: dot eyes + small mouth. HAPPY: bigger eyes + smile. CONFUSED: head tilt + asymmetric eyes. THINKING: eyes look up + small mouth. EXCITED: wide eyes + open mouth + cap wobble |
| **IP-safe lessons** | HUGE head shape + tiny face on visible portion = ratio trick (face looks more expressive because it's small on big shape). Cap = signature (no other mascot has mushroom cap) |
| **Adopt for Momo** | Ratio trick: face on larger body (Momo-E: face on 28×28 front face of cube = larger canvas than A-D's 40×36 sticky note where face is tiny). Signature shape above/around face (Momo-E: cube edges; Momo-G: pink eraser top) |
| **Adapt for Momo** | Toad has body + limbs (Momo: float only). Toad's cap is part of body (Momo: cube/eraser/brush body IS the face canvas) |
| **Avoid for Momo** | Toad's red+white mushroom cap (too iconic — IP risk). Toad's blue vest (too detailed for 8-bit minimal) |

#### Character 6: Goomba (Mario) — Nintendo

| Aspect | Detail |
|--------|--------|
| **Shape inventory** | Brown dome body + angry EYEBROWS (key signature) + dot eyes + frown mouth + small feet |
| **How face expresses 5 states** | Goomba is typically locked to "angry" expression. Variants show: IDLE: angry eyebrows + frown. HAPPY: rare, eyebrows soften + mouth curves. CONFUSED: tilted + asymmetric eyebrows. THINKING: N/A. EXCITED: rare, eyebrows raise + mouth opens |
| **IP-safe lessons** | Eyebrows as PRIMARY signature = Goomba is identified by eyebrows more than by body shape. This validates Momo v3.0 E/F/G's addition of eyebrows as SIGNATURE feature |
| **Adopt for Momo** | Eyebrows as primary emotion signal (Momo-E/F/G all add eyebrows — this is the KEY v3.0 upgrade over A-D). Eyebrow position/angle per state = primary differentiator |
| **Adapt for Momo** | Goomba is angry (Momo: friendly — eyebrows used for happy/thinking/excited, not just anger). Goomba has feet (Momo: float only). Goomba is brown (Momo: cream/pink — different palette) |
| **Avoid for Momo** | Goomba's permanent anger (Momo needs full 5-state range). Goomba's frown default (Momo: neutral/slight-smile default in IDLE). Goomba's feet (Momo has none) |

#### Character 7: Cube (Geometry Dash) — RobTop Games

| Aspect | Detail |
|--------|--------|
| **Shape inventory** | Square/cube body + (sometimes) simple face in special editions |
| **How face expresses 5 states** | Cube is mostly faceless (face only in special editions). Expression via movement: IDLE: still. HAPPY: jump + spin. CONFUSED: wobble. THINKING: slow rotate. EXCITED: rapid spin + particles |
| **IP-safe lessons** | Cube alone (no face) can be iconic — but for Momo we need face (educational context requires emotion). Cube + face = Slime precedent (mitigated). Cube + face + eyebrows + float = NO precedent |
| **Adopt for Momo** | Cube body (E). Spin animation for THINKING state (E uses 2.5D spin). Particle effects for EXCITED |
| **Adapt for Momo** | Geometry Dash cube is faceless (Momo-E: full face with hex eyes + eyebrows + morphing mouth). Geometry Dash has trail particles (Momo-E: only in EXCITED state, otherwise clean) |
| **Avoid for Momo** | Geometry Dash's exact cube proportion (Momo-E uses 2.5D isometric, not flat front). Geometry Dash's neon palette (Momo: cream sketchbook palette) |

#### Character 8: DoodleBob (SpongeBob) — Nickelodeon

| Aspect | Detail |
|--------|--------|
| **Shape inventory** | Pencil-drawn stick figure + crazy bold eyes + wide mouth + limbs |
| **How face expresses 5 states** | DoodleBob is mostly "manic" — large bold eyes + wide mouth. Variants: IDLE: bold stare. HAPPY: huge grin. CONFUSED: tilted + asymmetric eyes. THINKING: eyes dart. EXCITED: wild gestures + open mouth |
| **IP-safe lessons** | Pencil-drawn aesthetic + BOLD face features = distinctive. DoodleBob's face is its identity (more than its body shape) |
| **Adopt for Momo** | Pencil-drawn aesthetic (already in OPSI C Sketch Ghost — can apply to E/G as texture overlay). Bold face features (Momo-E/G: eyebrows + morphing mouth are bolder than A-D's minimal dot+line) |
| **Adapt for Momo** | DoodleBob has limbs (Momo: float only). DoodleBob is manic/chaotic (Momo: calm by default, expressive on demand). DoodleBob is monochrome pencil (Momo: cream + accent colors) |
| **Avoid for Momo** | DoodleBob's manic energy (too chaotic for educational game). DoodleBob's exact pencil-stroke style (too similar — Momo uses clean 8-bit lines, not sketchy strokes, except in C Sketch Ghost variant) |

### 10.3 Cross-Reference: How E/F/G Compare to References

| Trait | Sackboy | Cubone | Bomberman | MC Slime | Toad | Goomba | GeoDash Cube | DoodleBob | **Momo E** | **Momo F** | **Momo G** |
|-------|---------|--------|-----------|----------|------|--------|--------------|-----------|-----------|-----------|-----------|
| Base shape | Square+oval | Skull+body | Round | Cube | Dome+cap | Dome | Cube | Stick | **Cube 2.5D** | Brush vertical | Rect+ghost |
| Eyes | Button | Shadow | Dot | Dot | Dot | Dot | None | Bold line | **Hex ⬡** | **Ring ◯** | **Vertical oval ▮** |
| Eyebrows | Stitched | None | None | None | None | **Angry** | None | Bold | **Rect ▄▄** | **Rect ▄▄** | **Rect ▄▄** |
| Mouth | Stitched | Small | Line | Flat | Small | Frown | None | Wide | **Morphing** | **Arc morph** | **Oval morph** |
| Limbs | Arms+legs | Arms+legs | Arms+legs | None | Feet | Feet | None | Arms+legs | **Float only** | **Float only** | **Float only** |
| Floats? | No | No | No | No | No | No | No | No | **YES** | **YES** | **YES** |
| Sketchbook-native? | No | No | No | No | No | No | No | No (paper) | **YES** | **YES** | **YES** |
| 5-state expression | Yes | Limited | Limited | **No** (minimal) | Limited | **No** (angry only) | No (faceless) | Limited (manic) | **Full 5-state** | **Full 5-state** | **Full 5-state** |

**Key finding:** Momo E/F/G are the ONLY options in this matrix that combine ALL of: float only + sketchbook-native + 5-state expression + eyebrows + morphing mouth. This is the v3.0 differentiation.

---

*Document generated: 2026-03-05 (v2.0), updated 2026-06-16 (v3.0)*  
*Bigprompt v3.0 — Concept Development + Comparison + 3 New Face-Expressive Options*  
*Source: Task maskot-face-options-v3 execution*  
*Research: 7 web searches + 8 reference character analyses*  
*Constraint compliance: NO LEGS · NO WINGS · Float Only · Text Bubble Only · 8-bit Geometric · Dark dot eyes · NO cheeks · IP-safe · <100KB assets · <5MB RAM · <5% CPU*
