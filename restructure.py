#!/usr/bin/env python3
"""
Restructure index.html to consolidate game information into self-contained sections.
"""

import re
from typing import Dict, List, Tuple

# Game metadata in order - using translations from strategy/example sections
GAMES = [
    {
        'id': 'ce',
        'name': 'Ce',
        'translation': '("Uno")',
        'display_translation': '("Uno")',
    },
    {
        'id': 'ixtli',
        'name': 'Ixtli',
        'translation': '("Ojo/Rostro")',
        'display_translation': '("Ojo/Rostro")',
    },
    {
        'id': 'pamitl',
        'name': 'Pamitl',
        'translation': '("Bandera/Fila")',
        'display_translation': '("Bandera/Fila")',
    },
    {
        'id': 'pinotl',
        'name': 'Pinotl',
        'translation': '("Pila/Montón")',
        'display_translation': '("Pila/Montón")',
    },
    {
        'id': 'tecuia',
        'name': 'Tecuia',
        'translation': '("Golpear")',
        'display_translation': '("Golpear")',
    },
    {
        'id': 'atoyatl',
        'name': 'Atoyatl',
        'translation': '("Río")',
        'display_translation': '("Río")',
    },
    {
        'id': 'cayahua',
        'name': 'Cayahua',
        'translation': '("Dejar caer")',
        'display_translation': '("Dejar caer")',
    },
    {
        'id': 'tlalpoloa',
        'name': 'Tlalpoloa',
        'translation': '("Devorar la tierra")',
        'display_translation': '("Devorar la tierra")',
    },
    {
        'id': 'cempohualli',
        'name': 'Cempohualli',
        'translation': '("Veinte")',
        'display_translation': '("Veinte")',
    },
    {
        'id': 'palehuia',
        'name': 'Palehuia',
        'translation': '("Ayudar")',
        'display_translation': '("Ayudar")',
    },
    {
        'id': 'tlapatlani',
        'name': 'Tlapatlani',
        'translation': '("Intercambiar")',
        'display_translation': '("Intercambiar")',
    },
]


def extract_game_card_data(html_content: str, game_name: str) -> Dict[str, str]:
    """Extract metadata from a game card."""
    # Find the game card div
    pattern = rf'<div class="game-card" data-game="{game_name.lower()}">(.*?)</div>\s*(?=<!--|\s*<div class="game-card")'
    match = re.search(pattern, html_content, re.DOTALL)
    
    if not match:
        return {}
    
    card_html = match.group(1)
    
    # Extract game type
    type_match = re.search(r'<p class="game-type">(.*?)</p>', card_html)
    game_type = type_match.group(1) if type_match else ''
    
    # Extract description
    desc_match = re.search(r'<p class="game-type">.*?</p>\s*<p>(.*?)</p>', card_html, re.DOTALL)
    description = desc_match.group(1).strip() if desc_match else ''
    
    # Extract players and components from game-info div
    info_match = re.search(r'<div class="game-info">(.*?)</div>', card_html, re.DOTALL)
    players = ''
    components = ''
    if info_match:
        info_html = info_match.group(1)
        spans = re.findall(r'<span>(.*?)</span>', info_html)
        if len(spans) >= 2:
            players = spans[0]
            components = spans[1]
    
    return {
        'type': game_type,
        'description': description,
        'players': players,
        'components': components,
    }


def extract_strategy_content(html_content: str, game_name: str, translation: str) -> str:
    """Extract strategy content for a game."""
    # Use straight quotes as they appear in the strategy section
    full_name = f'{game_name} {translation}'
    pattern = rf'<div class="strategy-card[^>]*>.*?<h3>{re.escape(full_name)}</h3>.*?<div class="strategy-body">(.*?)</div>\s*</div>\s*</div>\s*</div>'
    match = re.search(pattern, html_content, re.DOTALL)
    
    if match:
        return match.group(1).strip()
    
    return '<p>Estrategias próximamente.</p>'


def extract_example_play_content(html_content: str, game_name: str, translation: str) -> str:
    """Extract example play content for a game."""
    # Use straight quotes as they appear in the example section
    # Allow optional suffix after translation (like " — Cooperativo")
    full_name_base = f'{game_name} {translation}'
    pattern = rf'<div class="example-card">.*?<h3>{re.escape(full_name_base)}[^<]*</h3>.*?<div class="example-body">(.*?)</div>\s*</div>\s*</div>'
    match = re.search(pattern, html_content, re.DOTALL)
    
    if match:
        return match.group(1).strip()
    
    return '<p>Ejemplo de jugada próximamente.</p>'


def create_game_section(game: Dict[str, str], game_data: Dict[str, str], 
                       strategy_content: str, example_content: str) -> str:
    """Create a self-contained game section."""
    game_id = game['id']
    game_name = game['name']
    display_translation = game['display_translation']
    
    section = f'''        <section id="juego-{game_id}" class="game-section">
            <h2>{game_name} <span class="game-translation">{display_translation}</span></h2>
            <div class="game-meta">
                <span class="game-type">{game_data.get('type', '')}</span>
                <span>{game_data.get('players', '')}</span>
                <span>{game_data.get('components', '')}</span>
            </div>
            <p class="game-description">{game_data.get('description', '')}</p>
            
            <div class="game-subsection">
                <h3>Preparación</h3>
                <img src="./instructions/Preparacion {game_name}@4x.png" alt="Preparación {game_name}" loading="lazy">
            </div>
            
            <div class="game-subsection">
                <h3>Jugadas</h3>
                <img src="./instructions/Jugadas {game_name}@4x.png" alt="Jugadas {game_name}" loading="lazy">
            </div>
            
            <div class="game-subsection">
                <h3>Objetivo</h3>
                <img src="./instructions/Objetivo {game_name}@4x.png" alt="Objetivo {game_name}" loading="lazy">
            </div>
            
            <div class="game-subsection">
                <h3>Estrategia</h3>
                {strategy_content}
            </div>
            
            <div class="game-subsection">
                <h3>Jugada de Ejemplo</h3>
                {example_content}
            </div>
        </section>
'''
    return section


def main():
    # Read the backup file
    with open('index.html.backup', 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    lines = html_content.split('\n')
    
    print(f"Total lines in file: {len(lines)}")
    
    # Extract data for all games
    game_sections = []
    for game in GAMES:
        print(f"Processing {game['name']}...")
        
        game_data = extract_game_card_data(html_content, game['id'])
        strategy_content = extract_strategy_content(html_content, game['name'], game['translation'])
        example_content = extract_example_play_content(html_content, game['name'], game['translation'])
        
        print(f"  - Game data: {bool(game_data)}")
        print(f"  - Strategy: {len(strategy_content)} chars")
        print(f"  - Example: {len(example_content)} chars")
        
        section = create_game_section(game, game_data, strategy_content, example_content)
        game_sections.append(section)
    
    # Build new HTML
    # Lines 0-1590: Keep (up to and including <nav class="nav-grid">)
    before_nav = '\n'.join(lines[0:1591])
    
    # New navigation
    nav_buttons = []
    for game in GAMES:
        nav_buttons.append(f'            <a href="#juego-{game["id"]}" class="nav-button">{game["name"]}</a>')
    
    nav_buttons.extend([
        '            <a href="#baraja" class="nav-button">Baraja</a>',
        '            <a href="#signos" class="nav-button">Signos</a>',
        '            <a href="#componentes" class="nav-button">Componentes</a>',
        '            <a href="#glosario" class="nav-button">Glosario</a>',
        '            <a href="#historia" class="nav-button">Historia</a>',
        '            <a href="#expansion" class="nav-button">Expansión</a>',
    ])
    
    new_nav = '\n'.join(nav_buttons)
    
    # Lines 1601-1604: nav closing tags
    nav_closing = '''        </nav>
    </section>

    <div class="container">'''
    
    # All game sections
    all_game_sections = '\n\n'.join(game_sections)
    
    # Lines 2810+ : Keep (from SECTION 3: BARAJA onwards)
    # Line 2809 is the closing </section> tag, line 2810 starts with blank line
    after_games = '\n'.join(lines[2810:])
    
    # Combine everything
    new_html = (
        before_nav + '\n' +
        new_nav + '\n' +
        nav_closing + '\n' +
        all_game_sections + '\n\n' +
        after_games
    )
    
    # Write the new file
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    
    print("\n✓ Restructuring complete!")
    print(f"✓ Created {len(game_sections)} game sections")
    print(f"✓ New file written to index.html")
    
    # Count new lines
    new_lines = new_html.split('\n')
    print(f"✓ New file has {len(new_lines)} lines (original had {len(lines)} lines)")


if __name__ == '__main__':
    main()
