# Amapatolli Companion — Restructure Spec

## The Problem
Currently the webapp has separate global sections:
- "Los 11 Juegos" (game cards with modals)
- "Jugadas de Ejemplo" (all 11 examples together)  
- "Guías de Estrategia" (all 11 strategies together)

This is WRONG. The user has to jump between 3 different sections to learn one game.

## The Solution
Each game should be a SINGLE self-contained section with everything inside:

```
GAME: Ce ("Uno")
├── Overview (type, players, components)
├── Preparación (setup + instruction image)
├── Jugadas (gameplay rules + instruction image)
├── Objetivo (victory condition + instruction image)
├── Estrategia (tips, common mistakes)
└── Jugada de Ejemplo (step-by-step scenario)
```

## Implementation

### Remove these separate sections entirely:
1. DELETE section `#estrategias` (the global strategies section)
2. DELETE section `#jugadas-ejemplo` (the global examples section)

### Restructure the Games section:
Instead of a grid of small game cards that open modals, create **11 full sections**, one per game.

Each game section should be:
```html
<section id="juego-ce" class="game-section">
  <h2>Ce <span class="game-translation">("Uno")</span></h2>
  <div class="game-meta">
    <span class="game-type">Cartas · Velocidad/Descarte</span>
    <span>👥 2-6 jugadores</span>
    <span>🎴 Solo baraja</span>
  </div>
  
  <!-- Subsections as accordion/collapsible OR always visible -->
  <div class="game-subsection">
    <h3>Preparación</h3>
    <img src="./instructions/Preparacion Ce@4x.png" alt="Preparación Ce" loading="lazy">
    <p>Rules text...</p>
  </div>
  
  <div class="game-subsection">
    <h3>Jugadas</h3>
    <img src="./instructions/Jugadas Ce@4x.png" alt="Jugadas Ce" loading="lazy">
    <p>Rules text...</p>
  </div>
  
  <div class="game-subsection">
    <h3>Objetivo</h3>
    <img src="./instructions/Objetivo Ce@4x.png" alt="Objetivo Ce" loading="lazy">
    <p>Rules text...</p>
  </div>
  
  <div class="game-subsection">
    <h3>Estrategia</h3>
    <!-- Strategy tips, difficulty badge, common mistakes -->
  </div>
  
  <div class="game-subsection">
    <h3>Jugada de Ejemplo</h3>
    <!-- Step-by-step timeline -->
  </div>
</section>
```

### Navigation Update
The hero nav should list all 11 games as direct links:
```
Juegos: Ce | Ixtli | Pamitl | Pinotl | Tecuia | Atoyatl | Cayahua | Tlalpoloa | Cempohualli | Palehuia | Tlapatlani
Other: Baraja | Signos | Componentes | Glosario | Historia | Expansión
```

### Game Selector
Keep the game selector widget but place it at the top before the game sections. When a game is recommended, it should scroll to that game's section (not open a modal).

### Modals
REMOVE the game modals entirely — all content is now inline in each game section. Keep only the card image modal (for the card gallery).

### Mobile Behavior
On mobile, each game section should have:
- A compact header (always visible)
- Collapsible subsections (Preparación, Jugadas, Objetivo, Estrategia, Ejemplo)
- Default: only Overview visible, subsections collapsed
- User taps to expand each subsection

On desktop:
- All subsections visible by default
- Or: make them collapsible with toggle

### Content Sources
Move ALL content from the deleted sections into their respective game sections:
- Strategy tips from #estrategias → each game's Estrategia subsection
- Example plays from #jugadas-ejemplo → each game's Jugada de Ejemplo subsection
- Modal content (rules, images) → each game's inline sections

### Section Order (after games)
1. Game Selector
2. Game Sections (11 games, each self-contained)
3. Baraja (card gallery)
4. Signos del Tonalpohualli
5. Componentes
6. Glosario
7. Historia
8. Expansión

### Critical Rules
- KEEP all existing content — just reorganize it
- KEEP the game selector widget
- KEEP the card gallery and card modal
- KEEP the score tracker
- KEEP light/dark mode
- KEEP all instruction images with papyrus background (#f5e6c8)
- KEEP the glossary, components, history, expansion sections unchanged
- All text remains in Spanish
- Mobile-first responsive design
- Use existing CSS variables
