import pygame

# Screen dimensions
WIDTH, HEIGHT = 380, 420
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Pac-Man")

image = pygame.image.load('pacman_right.png')
pygame.display.set_icon(image)

# Colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
VULNERABLE = BLUE
RED = (255, 0, 0)
PINK = (255, 105, 180)
CYAN = (0, 255, 255)
ORANGE = (255, 165, 0)
WHITE = (255, 255, 255)

# Maze layout (1: wall, 0: dot, 2: pellet, 3: empty)
global level1maze, level2maze
level = "Level1"
pellet = 0
mazePotZeroCount = 0 # Potential count for current level empty cells
mazeZeroCount = 0   # Current count for empty cells
mazeLevel = 1



def getMazeDesign(level):
    global maze
    level1maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 3, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 2, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1],
    [3, 3, 3, 1, 0, 1, 0, 2, 0, 0, 0, 0, 0, 1, 0, 1, 3, 3, 3],
    [1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1],
    [3, 3, 3, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 3, 3, 3],
    [1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
    [1, 2, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
    pellet = 0
    for row in range(len(level1maze)):
        for col in range(len(level1maze[0])):
            if level1maze[row][col] == 2:
                pellet += 1

    
    if level == "Level1":
        return level1maze
    elif level == "Level2":
        level2maze = [row[:] for row in level1maze]  # Create a copy of level1maze
        for row in range(len(level1maze)):
            for col in range(len(level1maze[0])):
                if level1maze[row][col] == 2 and pellet > 3:
                    level2maze[row][col] = 0
                    pellet = max(0, pellet - 1)  # Ensure pellet does not go negative
        return level2maze
    else:
        print("Invalid Maze Input", level)
        return level1maze

# Function to draw the maze
def draw_maze(mazeLevel = getMazeDesign("Level1")):
    for row in range(len(mazeLevel)):
        for col in range(len(mazeLevel[row])):
            x = col * CELL_SIZE
            y = row * CELL_SIZE
            if mazeLevel[row][col] == 1:  # Wall
                pygame.draw.rect(screen, BLUE, (x, y, CELL_SIZE, CELL_SIZE))
            elif mazeLevel[row][col] == 0:  # Dot
                pygame.draw.circle(
                    screen, WHITE, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2), 2
                )
            elif mazeLevel[row][col] == 2:  # Pellet
                pygame.draw.circle(
                    screen, WHITE, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2), 5
                )

