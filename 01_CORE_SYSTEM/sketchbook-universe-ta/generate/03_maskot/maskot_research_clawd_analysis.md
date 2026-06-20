# Maskot Research: Clawd Analysis & Geometric Mascot References

> **Project:** Sketchbook Universe  
> **Document:** Research Phase — Bigprompt v2.0  
> **Date:** 2026-03-05  
> **Purpose:** Analyze why geometric mascots succeed, extract design principles, and define ADOPT/ADAPT/AVOID strategy for Momo

---

## 1. Why Clawd (Claude Code Mascot) Works

### 1.1 Visual Anatomy of Clawd

| Elemen | Detail | Efek Psikologis |
|--------|--------|-----------------|
| Base Shape | Rectangle rounded | Instant recognizable — rect is the most basic non-organic shape; stands out in a world of round mascots |
| Color | Salmon pink + Dark outline | Warm, approachable — pink is disarming; dark outline gives "pixel art" definition |
| Eyes | 2 dot/garis sederhana | Expressive despite minimalism — the brain fills in emotion from tiny changes |
| Limbs | 4-6 kaki kecil | Cute factor — "chibi legs" trigger parental instinct; easy to animate walk cycle |
| Style | Pure 8-bit pixel art | Nostalgic, tech-vibe — signals "I belong in a terminal/dev environment" |
| Size | ~32x32px base | Perfect for UI integration — small enough to not obstruct, large enough to read |
| Silhouette | Crab-like rect body + legs | Immediately identifiable — you know it's Clawd from shadow alone |

### 1.2 Design Principles That Make Clawd Successful

#### Principle 1: **Radical Simplicity = Maximum Expressiveness**
Clawd proves that fewer visual elements force the designer to be intentional. With only 2 eyes and a body, every pixel change (eye size, body tilt) communicates emotion clearly. There is no "noise" — every visual decision is a signal.

**Key metric:** Clawd achieves ~12 distinguishable emotional states with only 3 variable elements (eye scale, body scale, body angle).

#### Principle 2: **Geometric Base = Animation-Friendly**
A rectangle is the easiest shape to animate in code. No bezier curves, no organic deformation needed. Clawd can be built entirely with `rect()` calls. This means:
- **Programmatic animation** — every frame is code, not art
- **Tweens work perfectly** — `scale`, `angle`, `pos` are all that's needed
- **Sprite sheet is tiny** — 6 frames × 5 states = 30 frames at 32×32 = ~30KB PNG

#### Principle 3: **Contrast Creates Character**
Clawd's pink body against a dark terminal background creates instant visual pop. The dark outline makes the shape "read" at any size. This contrast is not accidental — it's a deliberate readability strategy.

**Formula:** `Light body + Dark outline + Contrasting background = Maximum readability`

#### Principle 4: **Silhouette-First Design**
Even as a black silhouette, Clawd is identifiable. This is the gold standard of character design (the "Mickey ears" test). A strong silhouette means:
- Instant recognition at small sizes
- Works in monochrome (accessibility)
- Trademark-able (legal protection)

#### Principle 5: **Contextual Belonging**
Clawd doesn't just look good — it looks like it BELONGS in a terminal. The 8-bit aesthetic, the monospace implication, the tech palette — everything says "I live here." A mascot that fights its environment feels wrong.

### 1.3 Clawd's Weaknesses (What to Avoid)

| Weakness | Detail | Momo Implication |
|----------|--------|------------------|
| **Limited body language** | No arms = can't point, gesture, or hold objects | Momo needs at least minimal pointing ability for Probe UI |
| **Crab association is specific** | Clawd = crab = limited emotional range (can't easily do "sad crab") | Momo should be abstract enough for full emotional spectrum |
| **Walk-cycle dependency** | Legs mean walk animation is mandatory | Momo has NO LEGS — this is actually an advantage (float only) |
| **Pink is gendered** | Salmon pink reads as "cute/feminine" in some cultures | Momo should use a more gender-neutral palette |
| **Terminal-specific** | Clawd feels out-of-place outside dev tools | Momo must feel native to a sketchbook, not a terminal |

---

## 2. Additional Reference: Successful Geometric/Simple Mascots

### 2.1 Among Us Crewmate

| Elemen | Detail | Pelajaran untuk Momo |
|--------|--------|---------------------|
| Base Shape | Single rounded rectangle (pill/capsule) | One shape can carry an entire character |
| Visor | Single colored rectangle | One asymmetric detail = instant recognition |
| Color Variety | 18 solid colors | Color = identity (could apply to Momo "ink" variants) |
| No Face | No eyes, no mouth | Absence of face = players project emotion onto it |
| Animation | Walk (bouncy) + Kill + Vent | Minimal animation set, maximum impact |
| IP Strength | Iconic silhouette — even the visor alone is recognizable | One signature detail (visor) = enough for IP |

**Key Insight:** Among Us proves that a character with NO facial features can be the most recognizable mascot in gaming. The crewmate's "face" is the visor — a single colored rectangle. This validates Momo's "dot eyes only" approach.

**What Momo Can Learn:**
- One signature asymmetric detail (like the visor) creates instant recognizability
- Solid color fills without gradients = 8-bit aesthetic + tiny file size
- The "floating backpack" on crewmates = Momo's "fold corner" (asymmetric accent)

### 2.2 Fall Guys Bean

| Elemen | Detail | Pelajaran untuk Momo |
|--------|--------|---------------------|
| Base Shape | Rounded bean/capsule | Organic-but-simple = universally appealing |
| Face | Simple dot eyes + line mouth | Same minimal face approach as Clawd |
| Proportion | Big body, tiny limbs | Exaggerated proportion = comedy + cuteness |
| Animation | Wobbly, squash-stretch heavy | Physics-based animation = life (even in simple shapes) |
| Color | Solid fills + pattern costumes | Customization potential through color/pattern |
| IP Strength | The bean shape is now trademarked | Simple + unique shape = trademarkable |

**Key Insight:** Fall Guys shows that "blob + face" is a proven formula. But the magic is in the ANIMATION — the wobble, squash, and stretch give the bean personality that its static design doesn't have. For Momo, this means animation quality matters more than visual complexity.

**What Momo Can Learn:**
- Squash-and-stretch is the most powerful animation technique for simple shapes
- "Wobbly = alive" — even slight oscillation makes a static shape feel organic
- Costumes/skins are possible with simple shapes (Momo could have "ink color" variants)

### 2.3 Pac-Man (Classic Arcade)

| Elemen | Detail | Pelajaran untuk Momo |
|--------|--------|---------------------|
| Base Shape | Circle with wedge mouth | One shape + one subtraction = iconic character |
| Face | The mouth IS the face | Functional anatomy — the mouth serves gameplay |
| Animation | Mouth open/close (2 frames!) | 2-frame animation can be iconic |
| Color | Solid yellow | Single color = maximum brand recognition |
| IP Strength | One of the most recognized shapes in the world | Radical simplicity + functional design = timeless |

**Key Insight:** Pac-Man proves that a character can be defined by a SINGLE shape with a SINGLE animation (mouth open/close). The mouth is both the face AND the gameplay mechanic. For Momo, this suggests that her "fold corner" or "ink drip" could serve double duty — visual identity + gameplay indicator.

**What Momo Can Learn:**
- Every visual element should serve dual purpose (identity + function)
- 2 frames of animation can be more iconic than 60
- Single-color characters are MORE memorable than multi-color ones (contrary to intuition)

---

## 3. Cross-Reference Analysis

### 3.1 What the Top Geometric Mascots Share

| Trait | Clawd | Among Us | Fall Guys | Pac-Man | Implication for Momo |
|-------|-------|----------|-----------|---------|---------------------|
| **≤3 base shapes** | 2 (rect + legs) | 2 (body + visor) | 1 (bean) | 1 (circle) | Momo: max 5 shapes (with shadow) |
| **≤3 colors + outline** | 2 + outline | 1-2 + outline | 1 + outline | 1 | Momo: 3 + outline (primary, secondary, accent, outline) |
| **Dot/line eyes** | Yes | No (visor) | Yes | No | Momo: dot eyes (proven by Clawd + Fall Guys) |
| **Asymmetric detail** | Legs (could be symmetric) | Visor | N/A | Mouth | Momo: fold corner (asymmetric = identity) |
| **Reads at 16×16** | Yes | Yes | Debatable | Yes | Momo: MUST read at 16×16 (icon size) |
| **Floats/bounces** | Walks | Walks | Bounces | N/A | Momo: FLOATS — unique differentiator |

### 3.2 Unique Position for Momo

```
┌──────────────────────────────────────────────────────────┐
│           MASCOT POSITIONING MAP                         │
│                                                          │
│  ORGANIC ←──────────────────────────────→ GEOMETRIC      │
│     │                                                    │
│  Fall Guys ●          Among Us ●                         │
│     │                       │                            │
│     │         PAC-MAN ●     │                            │
│     │              │        │                            │
│     │              │   CLAWD ●                           │
│     │              │        │                            │
│     │         ★ MOMO ★     │                            │
│     │    (geometric +       │                            │
│     │     floating +        │                            │
│     │     sketchbook)       │                            │
│                                                          │
│  WALKING ←─────────────────────────────→ FLOATING        │
│                                                          │
│  Momo occupies a UNIQUE position:                        │
│  - Geometric (like Clawd)                                │
│  - Floating (UNIQUE — no other major mascot floats)      │
│  - Sketchbook-native (not terminal, not space, not TV)   │
│  - Emotionally expressive (more than Among Us)           │
│  - Educational context (unique audience)                 │
└──────────────────────────────────────────────────────────┘
```

---

## 4. ADOPT / ADAPT / AVOID Strategy

### 4.1 ADOPT from Clawd (Take As-Is)

| Principle | Application to Momo |
|-----------|---------------------|
| Geometric simplicity | Momo built from max 5 basic shapes (rect, circle, ellipse) |
| Limited color palette | Max 3 colors + outline (primary, secondary, accent, dark) |
| Expression via eyes/mouth only | Momo's emotional range communicated through eye/mouth changes |
| Programmatic animation | Every state is tween-based, not sprite-dependent |
| Silhouette-first design | Momo must pass the "black shadow" test |
| 8-bit pixel art aesthetic | Sharp edges, no anti-aliasing, rect-dominant |
| ~32-64px base size | Momo at 64×64 (larger than Clawd for sketchbook detail) |

### 4.2 ADAPT from References (Modify for Momo's Context)

| Reference | Original | Momo Adaptation |
|-----------|----------|-----------------|
| Clawd's rect body | Rect = crab shell | Rect = sticky note / sketch page (different narrative) |
| Among Us visor | Visor = face + identity | Fold corner = "tinta ajaib" mark + identity (asymmetric accent on body) |
| Fall Guys squash-stretch | Bouncy bean | Floating squash-stretch (Momo squishes while floating, not while walking) |
| Pac-Man functional mouth | Mouth = eating mechanic | Momo's mouth = confidence indicator (wide = high confidence, thin = low) |
| Clawd's pink palette | Pink = warm terminal | Green highlighter = sketchbook native (completely different vibe) |

### 4.3 AVOID (Explicitly Do NOT Copy)

| What to Avoid | Why | Momo's Alternative |
|---------------|-----|--------------------|
| Clawd's exact shape (rect + legs) | IP risk — too similar | Momo = rect + fold corner + NO legs (floating) |
| Clawd's salmon pink color | Brand confusion | Momo = green highlighter (#00E676) — completely different |
| Any crab/crustacean reference | Direct Clawd overlap | Momo = sketchbook creature, not sea creature |
| Walking animation | Contradicts "no legs" constraint | Float animation only — unique differentiator |
| Multiple limb animation | Performance budget + complexity | Zero limbs — expression through body/face only |
| Among Us's visor shape | Too recognizable — IP risk | Fold corner is smaller, positioned differently, different meaning |
| Fall Guys' bean curve | Organic curve ≠ 8-bit geometric | Momo uses rect with rounded corners, not smooth curves |
| Pac-Man's mouth mechanic | Gameplay mechanic ≠ narrative function | Momo's mouth is expression-only, not gameplay-interactive |

---

## 5. Research Synthesis: Design Principles for Momo

### 5.1 The 7 Commandments of Momo Design

```
╔══════════════════════════════════════════════════════════╗
║              MOMO DESIGN COMMANDMENTS                    ║
║                                                          ║
║  1. RADICAL SIMPLICITY                                   ║
║     Max 5 shapes. Max 3 colors + outline.               ║
║     If it can be removed without losing identity,        ║
║     it must be removed.                                  ║
║                                                          ║
║  2. FLOATING IS IDENTITY                                 ║
║     Momo never touches the ground. The shadow gap        ║
║     is as important as Momo herself.                     ║
║     NO LEGS. NO WINGS. Float = who she is.              ║
║                                                          ║
║  3. SKETCHBOOK-NATIVE                                    ║
║     Every element must feel like it belongs in a         ║
║     sketchbook. Not a terminal, not space, not TV.       ║
║     Paper, ink, pencil, fold, sketch — these are         ║
║     Momo's vocabulary.                                   ║
║                                                          ║
║  4. ASYMMETRIC SIGNATURE                                 ║
║     One detail that breaks symmetry = instant identity.  ║
║     (Fold corner, ink drip, sketch line, etc.)           ║
║                                                          ║
║  5. EXPRESSION > DECORATION                              ║
║     Every pixel should serve expression or identity.     ║
║     No decorative elements. No "cool for cool's sake."   ║
║                                                          ║
║  6. ANIMATION IS CHARACTER                               ║
║     A well-animated simple shape beats a detailed         ║
║     static design. Timing = personality.                 ║
║     (Proven by Fall Guys, Pac-Man)                       ║
║                                                          ║
║  7. IP SAFETY FROM DAY 1                                 ║
║     If it looks like an existing character, change it.   ║
║     Silhouette test. Color test. Name test.              ║
║     Original by design, not by accident.                 ║
╚══════════════════════════════════════════════════════════╝
```

### 5.2 Momo vs. Reference Mascots — Differentiation Matrix

| Aspect | Clawd | Among Us | Fall Guys | **Momo** |
|--------|-------|----------|-----------|----------|
| Locomotion | Walks (legs) | Walks (legs) | Runs/bounces (legs) | **Floats (NO legs)** |
| Base shape | Rect | Capsule | Bean | **Rect + fold** |
| Face | 2 dots | Visor (no face) | 2 dots + mouth | **2 dots + mouth** |
| Asymmetric detail | Legs (can be symmetric) | Visor | N/A | **Fold corner** |
| Color count | 2 + outline | 1-2 + outline | 1 + outline | **3 + outline** |
| Primary color | Salmon pink | Varies | Varies | **Green highlighter** |
| Context | Terminal | Spaceship | Game show | **Sketchbook** |
| Narrative role | Companion | Suspect/crew | Contestant | **Game master / guide** |
| Communication | Text | Text/emote | Emote | **Text bubble ONLY** |
| Death state | N/A | Ejected | Falls off | **Paper tears → recovers** |
| IP uniqueness | Crab rect | Visor capsule | Bean | **Floating rect + fold** |

---

## 6. Reference Image Analysis (Mental Model)

Since we cannot view reference images directly, here are the detailed mental models for each reference mascot:

### Clawd (Claude Code)
```
Imagine: A small salmon-pink rectangle with rounded corners.
         Two tiny dark dots for eyes.
         Four tiny stick legs underneath.
         Thick dark outline around the body.
         Walks with a slight waddle.
         Sometimes appears with a small hat or accessory.
         Lives in a terminal window.
         Overall vibe: Friendly, technical, approachable.
```

### Among Us Crewmate
```
Imagine: A horizontal capsule/pill shape, slightly wider than tall.
         A single blue-tinted rectangle on the upper half = visor.
         A small backpack/bump on one side.
         No eyes, no mouth, no facial features.
         Walks with a slight bob.
         The visor is the ONLY face-like element.
         Overall vibe: Anonymous, suspicious, simple-but-iconic.
```

### Fall Guys Bean
```
Imagine: A vertical bean shape — wider at top, narrower at bottom.
         Two small dot eyes near the top.
         A simple line mouth below the eyes.
         Stubby arms and legs.
         Extremely wobbly/squishy animation.
         The wobble IS the character.
         Overall vibe: Clumsy, joyful, physically comedic.
```

---

*Document generated: 2026-03-05*  
*Bigprompt v2.0 — Research Phase*  
*Source: Task 2 execution*
