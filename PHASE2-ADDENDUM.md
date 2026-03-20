# Phase 2 Addendum — Additional Requirements

## 1. LIGHT/DARK MODE TOGGLE (Priority: Critical)

Add a theme toggle button (sun/moon icon) fixed in the top-right corner.

### Dark Mode (default — current theme, refined):
- Background: `#1a1a2e` (obsidian) — keep
- Cards/sections: `#252541` (obsidian-light) — keep
- Gold: `#d4a373` — keep
- Jade: `#48a9a6` — keep
- Terracotta: `#c1666b` — keep  
- Text: `#f5f5f5` — keep
- Gray: `#9b9b9b` — **increase to #b0b0b0 for better readability**

### Light Mode (new):
- Background: `#f8f6f0` (warm parchment/papel amate)
- Cards/sections: `#ffffff` with subtle warm shadow
- Gold: `#8B6914` (darker gold for contrast on light bg)
- Jade: `#2d7a77` (darker jade for readability)
- Terracotta: `#a14448` (darker for contrast)
- Text: `#2a2a2e` (near-black)
- Gray: `#666666`
- Borders: `#d4a373` → `#c4934f` (slightly darker)
- Section borders: subtle, not heavy

### Implementation:
- Use CSS custom properties on `[data-theme="light"]` selector on `<html>`
- Store preference in localStorage
- Respect `prefers-color-scheme` media query as default
- Toggle button: 🌙 (dark) / ☀️ (light) with smooth transition
- ALL sections must be readable in both modes
- Card images should have subtle background in light mode (since card art has dark backgrounds)

## 2. GAME PHASES — COMPLETE FOR ALL 11 GAMES (Priority: Critical)

Each game modal (and the strategy section) MUST show these 3 phases clearly with visual aids:

### Phase Structure per Game:
```
┌─ PREPARACIÓN (Setup) ─────────────────┐
│ • What you need (components)           │
│ • How to arrange the table             │
│ • Card distribution                    │
│ • IMAGE: Preparación [Game]@4x.png     │
└────────────────────────────────────────┘

┌─ JUGADAS (Gameplay) ──────────────────┐
│ • Turn structure                       │
│ • Valid moves/matches                  │
│ • Special card effects                 │
│ • IMAGE: Jugadas [Game]@4x.png        │
└────────────────────────────────────────┘

┌─ OBJETIVO (Victory Condition) ────────┐
│ • How to win                           │
│ • End conditions                       │
│ • Scoring (if applicable)              │
│ • IMAGE: Objetivo [Game]@4x.png       │
└────────────────────────────────────────┘
```

### Complete Game Rules (fill in what's currently sparse):

**Tecuia ("Golpear"):**
- Setup: Deal cards equally. Play on a shared surface.
- Gameplay: Place numbered cards to build sequences. Your color only. Can play on opponent's sequences to block.
- Victory: First to place 5 consecutive numbered cards of your color in any direction.
- Strategy: Control the center positions. Block opponent's sequences at 3-4 length.

**Atoyatl ("Río"):**
- Setup: Deal cards with numeric values.
- Gameplay: Discard cards following numeric value rules (higher, lower, or equal depending on variant).
- Victory: First to play their last card face-down.
- Strategy: Track which values have been played. Save versatile mid-range values.

**Cayahua ("Dejar caer"):**
- Setup: 2 players. Place tokens in diamond formation on Huapalli board.
- Gameplay: Move tokens to adjacent spaces. Capture by jumping over opponent's token.
- Victory: Leave opponent with no tokens remaining.
- Strategy: Control the center diamond. Create capture chains. Don't leave isolated tokens.

**Tlalpoloa ("Devorar la tierra"):**
- Setup: 2 players. Empty Huapalli board.
- Gameplay: Take turns placing tokens. Must form diamond patterns.
- Victory: First to place ALL their tokens on the board.
- Strategy: Claim central spaces early. Block opponent's diamond formations.

**Cempohualli ("Veinte"):**
- Setup: Deal 3 cards to each player (each = 1 life).
- Gameplay: Challenge rounds between players. Loser discards a life card.
- Victory: Last player with cards remaining wins.
- Strategy: Choose challenges carefully. Preserve life cards against weaker opponents.

**Tlapatlani ("Intercambiar"):**
- Setup: Deal cards randomly.
- Gameplay: Trade cards with other players or draw from deck. Organize by illustration type.
- Victory: First to complete 4 organized piles (by illustration category: aves, templos, árboles, figuras).
- Strategy: Identify which categories are most represented in your initial hand. Trade aggressively for your focus categories.

## 3. COLOR CONTRAST FIXES
Current problems to fix:
- Gray text (#9b9b9b) on dark background is hard to read → bump to #b0b0b0 minimum
- Jade links on obsidian can be low contrast → ensure 4.5:1 ratio minimum
- Card border colors need to be visible in BOTH themes
- Filter buttons: ensure active state is clearly distinct in both modes
- Modal overlay: ensure text is readable in both themes

## 4. EVALUATION CRITERIA FOR SUB-AGENTS

### Mobile Evaluator should check:
- All sections at 375px and 320px width
- No horizontal scroll
- Touch targets ≥ 44px
- Text readable without zooming (min 14px)
- Images don't overflow
- Modals are full-screen on mobile
- Score tracker works as bottom sheet
- Theme toggle accessible on mobile

### UX Evaluator should check:
- Navigation flow: can user find any game's rules in <3 taps?
- Information hierarchy: most important content first
- Consistency: all games have same level of detail
- Feedback: interactions have visual response
- Loading: no jarring layout shifts
- Accessibility: keyboard navigation, screen reader basics

### Design Evaluator should check:
- Visual harmony between sections
- Typography hierarchy (h1 > h2 > h3 consistent)
- Color palette coherence in both light and dark modes
- Spacing consistency (use of CSS variables)
- Image treatment: consistent borders, sizing
- Theme transition smoothness
- Mesoamerican aesthetic maintained in light mode
