# Pacman

This repository contains the implementation of the classic Pacman game using Python using a simple A* algorithm.

# Installation

Pac-man requires Python 3.x (tested on 3.12), only external libraries are pygame, and the corresponding version of the Pygame library in requirements.txt, freely available online. Make sure you install the matching (32- or 64-bit) version of Pygame as your Python installation.

```
pip install -r requirements.txt
```
Running the game:
```
python main.py
```
# Interface

![image](https://github.com/user-attachments/assets/ab45f6c2-2d38-4a72-b2d7-73c5d6c81114)

# Dependencies

- pygame: Library for creating video games
- sys: Provides access to system-specific parameters and functions
- math: Provides mathematical functions
- copy: Provides functions for copying objects
- heapq: Library for priority queue operations
- time: Provides time-related functions
- random: Library for generating random numbers

# Pacman Game Main Menu Module

This module initializes and runs the main menu for the Pacman game.
It handles user input for menu navigation and starts the game when selected.

Key Features:
- Initializes the main menu screen
- Handles user input for navigating the menu
- Starts the game when "Start Game" is selected
- Quits the game when "Quit" is selected

# Pacman Game Initialization Module

This module contains the initialization and setup functions for the Pacman game.
It handles the construction of the game, including setting up the game screen,
loading resources, and initializing game variables.

Key Features:
- Initializes game settings and configurations
- Loads resources such as images and sounds
- Sets up initial positions and states for Pacman and ghosts
- Provides utility functions for game operations

Functions:
- setPacmanOrientation: Sets the orientation of Pacman based on the direction
- draw_lives: Draws the remaining lives of Pacman on the screen

# Pacman Game Logic Module

This module contains the core game logic for the Pacman game.
It manages the state of Pacman, ghosts, and other game elements.
It also handles the movement and interactions of Pacman and ghosts.

Key Features:
- Manages Pacman's position, direction, and mode
- Handles ghost movement and state
- Updates game state based on interactions between Pacman and ghosts
- Maintains game variables such as score, lives, and timers

Functions:
- getPacmanX: Returns the current X position of Pacman
- setPacmanX: Sets the X position of Pacman

# Pacman Game Main Module

This module initializes and runs the main game loop for the Pacman game.
It handles user input, updates the game state, and renders the game screen.

Key Features:
- Initializes the game screen and settings
- Handles user input for Pacman movement
- Updates the game state based on user input and game logic
- Renders the game screen with updated positions of Pacman, ghosts, and maze elements
- Manages game events such as quitting the game

# Pacman Game Settings Module

This module contains the maze design and other game settings for the Pacman game.
It provides functions to retrieve maze designs for different levels and counts the number of pellets in the maze.

Key Features:
- Defines the maze layout for different levels
- Counts the number of pellets in the maze
- Provides functions to retrieve maze designs for different levels

Maze Legend:
- 0: Dot
- 1: Pellet
- 2: Top left corner
- 3: Top right corner
- 4: Bottom right corner
- 5: Bottom left corner
- 6: Horizontal wall
- 7: Vertical wall
- 8: Wall end bottom
- 9: Wall end left
- 10: Wall end right
- 11: Wall end top
- 12: Bottom T
- 13: Left T
- 14: Right T
- 15: Top T
- 16: Wall X
- 17: Empty space

# Proposed Changes

- Implementation of non interface interactions in C++, starting with the A* Algorithm in game.py
- Make pacman movement more smooth rather than moving cell by cell
- Add ghost warning when pacman kill mode is about to expire
- pacman kill mode should be linked by ghost instead as when ghost gets eaten once, ghost is no longer vulnerable
- Change getMazeDesign function to take 2D list using legend 0 - Dot, 1 - Pellet, 2 - Empty, 3 - Wall and convert to current maze legend for better modifiability like so (in progress in practise.py):
```
# Maze Layout          0 - Dot 1 - Pellet 2 - Empty 3 - Wall
maze = [
[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
[3, 2, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3],
[3, 0, 3, 3, 0, 3, 3, 3, 0, 3, 0, 3, 3, 3, 0, 3, 3, 0, 3],
[3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
[3, 0, 3, 3, 0, 3, 0, 3, 3, 3, 3, 3, 1, 3, 0, 3, 3, 0, 3],
[3, 0, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0, 0, 3],
[3, 3, 3, 3, 0, 3, 3, 3, 0, 3, 0, 3, 3, 3, 0, 3, 3, 3, 3],
[2, 2, 2, 3, 0, 3, 0, 1, 0, 0, 0, 0, 0, 3, 0, 3, 2, 2, 2],
[3, 3, 3, 3, 0, 3, 0, 3, 3, 2, 3, 3, 0, 3, 0, 3, 3, 3, 3],
[0, 0, 0, 0, 0, 0, 0, 3, 2, 2, 2, 3, 0, 0, 0, 0, 0, 0, 0],
[3, 3, 3, 3, 0, 3, 0, 3, 3, 3, 3, 3, 0, 3, 0, 3, 3, 3, 3],
[2, 2, 2, 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 3, 0, 3, 2, 2, 2],
[3, 3, 3, 3, 0, 3, 0, 3, 3, 3, 3, 3, 0, 3, 0, 3, 3, 3, 3],
[3, 0, 0, 0, 0, 0, 0, 1, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3],
[3, 0, 3, 3, 0, 3, 3, 3, 0, 3, 0, 3, 3, 3, 0, 3, 3, 0, 3],
[3, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 3],
[3, 3, 0, 3, 0, 3, 0, 3, 3, 3, 3, 3, 0, 3, 0, 3, 0, 3, 3],
[3, 1, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0, 0, 3],
[3, 0, 3, 3, 3, 3, 3, 3, 0, 3, 0, 3, 3, 3, 3, 3, 3, 0, 3],
[3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3],
[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
]

count = 0
visited = [[False for i in range(len(maze[0]))] for j in range(len(maze))]

# Count top left corner cells (2)
for row in range(len(maze)):
    for col in range(len(maze[row])):  # Loop through each cell
        if maze[row][col] == 3 and not visited[row][col]:  # check if wall and not visited
            # Check if the current cell is not on the last row or last column
            if row < len(maze) - 1 and col < len(maze[0]) - 1:
                # Check if the cell to the right and the cell below are both 1
                # and the cell to the left and the cell above are in [0, 2, 3]
                if maze[row][col + 1] == 3 and maze[row + 1][col] == 3 and maze[row][col - 1] in [0, 1, 2] and maze[row - 1][col] in [0, 1, 2]:
                    visited[row][col] = True  # Mark cells as visited
                    visited[row][col + 1] = True
                    visited[row + 1][col] = True 
                    maze[row][col] = 2
                if row == 0 and col == 0:
                    visited[row][col] = True  # Mark cells as visited
                    visited[row][col + 1] = True
                    visited[row + 1][col] = True
```
