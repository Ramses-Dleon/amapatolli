# Quick Reference Guide - HTML Restructure

## What Was Changed

### Before (Original Structure)
```
Navigation:
- Juegos (11)
- Jugadas de Ejemplo  
- Estrategias
- Baraja
- ...

Content:
├── SECTION 1: Grid of 11 game cards
├── SECTION 2: 11 collapsible example plays
├── SECTION 2.5: 11 collapsible strategies
└── SECTION 3+: Baraja, Signos, etc.
```

### After (Restructured)
```
Navigation:
- Ce
- Ixtli
- Pamitl
- ... (all 11 games)
- Baraja
- ...

Content:
├── Game Section: Ce
│   ├── Header + metadata
│   ├── Preparación (image)
│   ├── Jugadas (image)
│   ├── Objetivo (image)
│   ├── Estrategia (tips)
│   └── Jugada de Ejemplo (steps)
├── Game Section: Ixtli
│   └── ... (same structure)
├── ... (all 11 games)
└── Baraja, Signos, etc. (unchanged)
```

## New Section Structure

Each game section follows this template:
```html
<section id="juego-{id}" class="game-section">
    <h2>{Name} <span class="game-translation">{translation}</span></h2>
    <div class="game-meta">
        <span class="game-type">{type}</span>
        <span>{players}</span>
        <span>{components}</span>
    </div>
    <p class="game-description">{description}</p>
    
    <div class="game-subsection">
        <h3>Preparación</h3>
        <img src="./instructions/Preparacion {Name}@4x.png" ...>
    </div>
    
    <div class="game-subsection">
        <h3>Jugadas</h3>
        <img src="./instructions/Jugadas {Name}@4x.png" ...>
    </div>
    
    <div class="game-subsection">
        <h3>Objetivo</h3>
        <img src="./instructions/Objetivo {Name}@4x.png" ...>
    </div>
    
    <div class="game-subsection">
        <h3>Estrategia</h3>
        {strategy tips and common mistakes}
    </div>
    
    <div class="game-subsection">
        <h3>Jugada de Ejemplo</h3>
        {example play steps}
    </div>
</section>
```

## Benefits

1. **Self-contained**: Each game has all its information in one place
2. **Direct navigation**: Click game name to go directly to that game
3. **Simpler structure**: No need for collapsible sections
4. **Maintainability**: Easier to add/edit individual games
5. **Reduced file size**: Eliminated duplicate structure (385 lines saved)

## Files Modified

- `/home/coder/.openclaw/workspace/amapatolli-companion/index.html` - Restructured output
- `/home/coder/.openclaw/workspace/amapatolli-companion/index.html.backup` - Original backup
- `/home/coder/.openclaw/workspace/amapatolli-companion/restructure.py` - Python script
- `/home/coder/.openclaw/workspace/amapatolli-companion/RESTRUCTURE_SUMMARY.md` - Detailed summary
- `/home/coder/.openclaw/workspace/amapatolli-companion/RESTRUCTURE_GUIDE.md` - This guide

## Running the Script

To re-run the restructure:
```bash
cd /home/coder/.openclaw/workspace/amapatolli-companion
python3 restructure.py
```

The script reads from `index.html.backup` and writes to `index.html`.
