# tutorial-6
## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
# Match-3 Game
A classic match-3 puzzle game built with Makecode Arcade. Swap adjacent food tiles to create matches of 3 or more and score points!
## How to play
### Controls
- Arrow Keys - Move the cursor
- A Button - Select tile / Swap tiles
### Rules
1. Use arrow keys to move the yellow cursor
2. Press A to select a tile
3. Move cursor to an adjacent tile (up/down/left/right)
4. Press A again to swap the two tiles
5. Match 3 or more identical tiles in a row or column
6. Match tiles diaappear and new tiles fall from above
7. Chain reactions automatically continue for bonus points
## Features
-5 food types
- 8x8 grid
- Cascade matching system
- Gravity-based tile dropping
- Score tracking (10 points per tile)
## Getting Started
1. Visit http;//arcade.makecode.com/
2.  Create a new project
3.  Switch to Python mode
4.  Copy and paste the game code
5.  Click run to play

	
## Technologies
### Configuration
- Grid size: 8x8
- Tile size: 16x16 pixels
- Food types: 5

### Core Functions
- init() - Initialize game board and score
- draw() - Render all tiles on screen
- makeCur() - Create cursor sprite
- check() - Detect 3+ matches in rows/columns
- clear() - Remove matched tiles and update score
- fill() - Drop tiles and generate new ones
- swap() - Exchange two adjacent tiles

### Game Logic
1. Player selects two adjacent tiles
2. Tiles swap positions
3. Check for matches
4. If matches found: Remove tiles, fill gaps, repeat check
5. If no matches: swap back

## Customization
### Change Grid Size
```python
SIZE=10 # Make it 10x10

Update boundary checks:
```python
if row < 9: # Change from 7 to SIZZE-1
if col < 9:
```
### Add more Food Types
```python
foods = [food1, food2, food3,food4,food5,food6] # 6 types
board[r].append(randint(O, 5)) #Update range
```

### Change Background Color
```python
scene.set_background_color(1) # Try colors 1-15

## License
Open source for educational purposes.

---

Enjoy the game!

## Setup
This project is simple Lorem ipsum dolor generator.
