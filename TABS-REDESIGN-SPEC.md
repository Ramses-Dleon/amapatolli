# Amapatolli Companion — Tabs Redesign + Color Fix

## Problem
1. Page shows EVERYTHING at once — overwhelming
2. Dark mode colors don't match Jorge's actual design palette
3. Need tabbed navigation so you see ONE game at a time

## Solution: Tab-Based Navigation

### Top Navigation Bar (sticky)
A horizontal scrollable tab bar at the top (after hero):
```
[Inicio] [Ce] [Ixtli] [Pamitl] [Pinotl] [Tecuia] [Atoyatl] [Cayahua] [Tlalpoloa] [Cempohualli] [Palehuia] [Tlapatlani] [Baraja] [Signos] [Glosario] [Info]
```

- **Inicio** tab: shows the hero section, game selector widget, and overview grid (compact cards for all 11 games — just name, type, player count — clickable to switch to that game's tab)
- **Each game tab**: shows ONLY that game's self-contained section (rules, images, strategy, example)
- **Baraja** tab: card gallery with filters
- **Signos** tab: Tonalpohualli signs
- **Glosario** tab: Nahuatl glossary  
- **Info** tab: Components + History + Expansion combined

### Tab Bar Styling
- Sticky at top (position: sticky, top: 0, z-index: 999)
- Horizontally scrollable on mobile (overflow-x: auto)
- Active tab highlighted
- Dark mode: tabs on #231f20 background, active tab with gold (#d0b36e) underline
- Light mode: tabs on #f5e6c8 background, active tab with dark gold underline
- Tab text: small, 0.85rem, uppercase

### Implementation
- Pure CSS/JS tab system (no framework)
- Each section has `data-tab="ce"`, `data-tab="baraja"`, etc.
- Clicking a tab: hide all sections, show only the matching one
- URL hash support: `#ce` opens Ce tab
- Game selector "results" link to the game's tab

## Color Palette — From Jorge's Actual Assets

### Dark Mode (based on card interior #231f20):
```css
:root {
    --bg-primary: #231f20;      /* Card interior black */
    --bg-secondary: #2d2926;    /* Slightly lighter */
    --bg-card: #332e2b;         /* Card/section background */
    --gold: #d0b36e;            /* Card border gold — primary accent */
    --cyan: #3697b5;            /* Instruction blue — secondary accent */
    --red: #ed2c30;             /* Card red — alerts, highlights */
    --green: #2a853b;           /* Illustration green — success */
    --yellow: #f7e019;          /* Illustration yellow — warnings */
    --text-primary: #f5f0e0;    /* Warm white */
    --text-secondary: #c0b8a8;  /* Muted warm gray */
    --border: #d0b36e;          /* Gold borders */
    --papyrus: #f5e6c8;         /* Image backgrounds */
}
```

### Light Mode:
```css
html[data-theme="light"] {
    --bg-primary: #f5e6c8;      /* Papyrus/parchment */
    --bg-secondary: #ece0cc;    /* Slightly darker parchment */
    --bg-card: #ffffff;         /* White cards */
    --gold: #8B6914;            /* Darker gold for contrast */
    --cyan: #2a7a94;            /* Darker cyan */
    --red: #c41e22;             /* Darker red */
    --green: #1e6b2e;           /* Darker green */
    --yellow: #b5a20e;          /* Darker yellow */
    --text-primary: #231f20;    /* Dark text */
    --text-secondary: #5a524a;  /* Muted dark */
    --border: #d0b36e;          /* Gold stays */
    --papyrus: #f5e6c8;         /* Same papyrus for images */
}
```

### Color Mapping
Replace the old variables:
- `--obsidian` (#1a1a2e) → `--bg-primary` (#231f20) 
- `--obsidian-light` (#252541) → `--bg-secondary` (#2d2926)
- `--gold` stays similar → #d0b36e (from actual cards)
- `--jade` (#48a9a6) → `--cyan` (#3697b5) (from actual instructions)
- `--terracotta` (#c1666b) → `--red` (#ed2c30) (from actual cards)

## Critical Rules
- Keep ALL existing content
- Keep score tracker, theme toggle, card modal
- Keep all instruction images with papyrus background
- Tab system must work on mobile (horizontal scroll tabs)
- img[src*="instructions/"] keeps background: #f5e6c8
- URL hash navigation (#ce, #baraja, etc.)
- Default tab is "Inicio" showing overview
- Game selector results should switch to the recommended game's tab
- All text in Spanish
