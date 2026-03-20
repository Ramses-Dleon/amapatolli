# Amapatolli Companion — Phase 2 Specification

## Overview
Expand the existing single-page HTML companion app with Phase 2 features: strategies, game tools, and cultural content. All additions go into the SAME `index.html` file.

## Current State
- `index.html` (~1600 lines): 7 sections (Hero, Games, Cards, Signs, Components, History, Expansion)
- Dark mesoamerican theme: `--obsidian`, `--gold`, `--jade`, `--terracotta`
- 155 image assets in subdirectories (cards/, instructions/, ilhuitl/, boards/, tetl/, reversos/, icons/)
- Deployed at https://amapatolli-companion.vercel.app

## Phase 2 Features to Add

### 1. INSTRUCTION IMAGES VISIBLE DIRECTLY (Priority: Critical)
The instruction images (Preparación, Jugadas, Objetivo) for each game are currently ONLY visible inside modals. Make them visible directly:
- Each game card in the grid should show a THUMBNAIL of the "Jugadas" instruction image
- When the game card is clicked, the modal already shows all 3 images — keep that, but make them LARGER and more prominent
- Add a "Quick Reference" section below the game grid showing ALL instruction images in a scrollable gallery grouped by game

### 2. STRATEGY GUIDES (Priority: High)
Add a new section "#estrategias" between Games and Cards sections. Content for each game:

**Ce (UNO-style):**
- Track both color axes (margin + background) simultaneously
- Save Tlapiani wildcards for when blocked, never play turn 1
- Play Birds when opponent has just drawn cards
- Double-match cards: only chain when both advance your exit plan
- ALWAYS shout "Ce Amapatolli" on penultimate card — forgetting costs 3 cards
- Common mistake: playing wildcards too early

**Ixtli (Lotería):**
- Memorize your board BEFORE play starts (10 seconds)
- Scan by quadrant, not linearly
- At 6 tokens, fixate on the ONE remaining illustration you need
- Common mistake: scanning left-to-right instead of by visual cluster

**Pamitl (Connect-5):**
- Always take center (3,3) on move 1 — it controls the most lines
- Create dual-threat forks (two winning lines simultaneously)
- Don't neglect diagonals
- Cell value: center > adjacent > edge > corners
- Common mistake: playing reactively without building own threats

**Pinotl:**
- This is a PACING game, not a speed game
- Identify "dead weight" cards (rare illustrations) and discard them first
- Save Tlapiani for endgame unplayable cards
- Common mistake: racing to discard early

**For the other 7 games:** Create shorter strategy boxes with 2-3 key tips each based on their mechanics.

Format each strategy guide as a collapsible card with:
- Difficulty tier badge (Principiante / Intermedio / Avanzado)
- 3-5 key tips with icons
- "Errores comunes" section
- Color-coded by game archetype (speed=jade, strategy=gold, cooperative=terracotta)

### 3. GAME SELECTOR / RECOMMENDER (Priority: High)
Add interactive "¿Qué juego jugamos?" widget at the top of the games section:
- 3 questions: ¿Cuántos jugadores? (2/3-4/5-6) | ¿Cuánto tiempo? (rápido/medio/largo) | ¿Qué tipo? (velocidad/estrategia/cooperativo)
- Shows filtered recommendations with match percentage
- Direct link to that game's section

### 4. SCORE TRACKER (Priority: Medium)
Add a floating button (bottom-right) that opens a score tracking panel:
- Add player names (up to 6)
- +/- buttons per player
- Round history
- Winner highlight
- Save to localStorage
- Reset button

### 5. NAHUATL GLOSSARY (Priority: Medium)
Add a section "#glosario" with 30+ terms:
- All 11 game names with translations and pronunciation
- All 20 tonalpohualli sign names
- Key terms: Tlapiani, Tetl, Huapalli, Amapatolli, Tonalpohualli, etc.
- Each entry: Náhuatl | Español | Pronunciation hint | Brief meaning

### 6. MOBILE OPTIMIZATION (Priority: Critical)
- Ensure ALL new sections work perfectly on mobile (320px-428px width)
- Touch targets minimum 44px
- No horizontal scroll
- Game selector should be fullscreen overlay on mobile
- Score tracker should be a bottom sheet on mobile
- Strategy guides should be fully collapsible (accordion)

## Design Constraints
- MUST remain a single `index.html` file
- Use the existing CSS variables (--obsidian, --gold, --jade, --terracotta, --white, --gray)
- Use localStorage for persistence (score tracker)
- No external JS libraries — vanilla JS only
- All content in Spanish
- Maintain the existing mesoamerican dark theme aesthetic
- Keep existing sections intact — add new sections between existing ones

## Image Paths for Instructions
All instruction images are in `./instructions/` with format:
- `Preparación [Game]@4x.png`
- `Jugadas [Game]@4x.png`  
- `Objetivo [Game]@4x.png`

Game names: Ce, Ixtli, Pamitl, Pinotl, Tecuia, Atoyatl, Cayahua, Tlalpoloa, Cempohualli, Palehuia, Tlapatlani

Note: Pamitl's preparation file is `Preparación Pamitl@4x.png` (with space).

## Navigation
Update the hero nav-grid to include new sections:
- Juegos (11) | Estrategias | Baraja | Signos | Componentes | Glosario | Historia | Expansión

## Testing
After building, verify:
1. All 11 game cards show thumbnail of their instruction image
2. All strategy guides expand/collapse correctly
3. Game selector filters work
4. Score tracker persists across page refreshes
5. All images load (no broken links)
6. Mobile layout works at 375px width
