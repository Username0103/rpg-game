# RPG Game

A text-based role-playing game with combat mechanics, character progression, and save functionality.

## Project Overview

This project is a command-line RPG game with the following features:
- Turn-based battle system
- Character creation and progression
- Stats system (health, strength, agility, intelligence, endurance)
- Items, abilities, and magic implementation
- Save/load game functionality
- Configuration options

## Getting Started

### Prerequisites
- Python 3.x
- Windows OS (currently uses msvcrt for input handling)

### Installation
1. Clone this repository
2. Ensure you have the required dependencies
3. Run `python rpg_game_startup.py` to start the game

## Project Structure

- **battle.py**: Handles combat encounters between player and NPCs
- **character_creation.py**: Character creation interface
- **classes.py**: Core game classes (Player, NPC, Stats, Game)
- **config_manager.py**: Manages game configuration
- **magic.py**: Implements items, abilities and magic system
- **misc_functions.py**: Utility functions
- **options_menu.py**: In-game options interface
- **rpg_game_startup.py**: Main game launcher
- **save_manager.py**: Handles game save/load functionality

## Configuration

The game uses a configuration system that allows players to adjust various game settings. Settings can be reset to defaults at any time through the options menu.

## Save System

The game implements a save/load system using Python's pickle module, allowing players to save their progress and continue later.

## Development Status

This project is currently under development and not yet playable.  
Most features are be incomplete and subject to change.  
If anyone is reading this, it'd be really cool if you contributed!

## Future Improvements

- Create character creation system
- Complete battle mechanics
- Add enemies and items
- Cross-platform input handling
