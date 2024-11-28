# Pacman

This repository contains the implementation of the classic Pacman game using Python.

# Pacman Game Main Menu Module

This module initializes and runs the main menu for the Pacman game.
It handles user input for menu navigation and starts the game when selected.

Key Features:
- Initializes the main menu screen
- Handles user input for navigating the menu
- Starts the game when "Start Game" is selected
- Quits the game when "Quit" is selected

Dependencies:
- pygame: Library for creating video games
- pacman: Contains the main game loop and game logic
- sys: Provides access to system-specific parameters and functions

Global Variables:
- SCREEN_WIDTH: Width of the main menu screen
- SCREEN_HEIGHT: Height of the main menu screen
- WHITE: Color value for white
- BLACK: Color value for black
- screen: Pygame display surface for the main menu
- background_image: Background image for the main menu
- font: Font for the main menu options
- small_font: Font for smaller text in the main menu
- menu_options: List of options available in the main menu

# Pacman Game Initialization Module

This module contains the initialization and setup functions for the Pacman game.
It handles the construction of the game, including setting up the game screen,
loading resources, and initializing game variables.

Key Features:
- Initializes game settings and configurations
- Loads resources such as images and sounds
- Sets up initial positions and states for Pacman and ghosts
- Provides utility functions for game operations

Dependencies:
- pygame: Library for creating video games
- sys: Provides access to system-specific parameters and functions
- math: Provides mathematical functions
- copy: Provides functions for copying objects
- heapq: Library for priority queue operations
- time: Provides time-related functions
- random: Library for generating random numbers
- settings: Contains game settings and constants

Global Variables:
- CELL_SIZE: Size of each cell in the maze
- HEIGHT: Height of the game screen
- WIDTH: Width of the game screen
- VULNERABLE: State of ghosts when they can be eaten by Pacman
- RED, CYAN, PINK, ORANGE: Colors representing different ghosts
- BLACK: Color representing the background
- image: Current image of Pacman based on its orientation

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

Dependencies:
- pygame: Library for creating video games
- heapq: Library for priority queue operations
- random: Library for generating random numbers

Global Variables:
- pacman_lives: Number of lives Pacman has
- pacmanDir: Direction of Pacman's movement
- pacman_score: Current score of the game
- ghost_delay_counter: Counter for delaying ghost movement
- GHOST_DELAY: Number of ticks to delay the movement for all ghosts
- pacmanmode: Current mode of Pacman (normal or kill)
- ghost_respawn_timer: Timer for ghost respawn
- current_direction: Current direction of Pacman's movement
- pacmanX, pacmanY: Current position of Pacman

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

Dependencies:
- init: Contains initial game settings and configurations
- pygame: Library for creating video games
- settings: Contains maze design and other game settings

# Pacman Game Settings Module

This module contains the maze design and other game settings for the Pacman game.
It provides functions to retrieve maze designs for different levels and counts the number of pellets in the maze.

Key Features:
- Defines the maze layout for different levels
- Counts the number of pellets in the maze
- Provides functions to retrieve maze designs for different levels

Dependencies:
- pygame: Library for creating video games

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
