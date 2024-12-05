import pygame

# Screen dimensions
CELL_SIZE = 30
WIDTH, HEIGHT = 19 * CELL_SIZE, 21 * CELL_SIZE 

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Pac-Man")

image = pygame.image.load('resources/pacman_right.png')
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

global level1maze, level2maze
level = "Level1"
pellet = 0
mazePotZeroCount = 0 # Potential count for current level empty cells
mazeZeroCount = 0   # Current count for empty cells
mazeLevel = 1

# 0 - Dot, 1 - Pellet, 2 - top left corner, 3 - top right corner, 4 - bottom right corner, 5 - bottom left corner, 6 - horizontal wall
# 7 - vertical wall, 8 - wall end bottom, 9 - wall end left, 10 - wall end right, 11 - wall end top, 12 - bottom T, 13 - left T, 14 - right T
# 15 - Top T, 16 - Wall X, 17 - empty cell

def getMazeDesign(level):
    level1maze = [
        [2, 6, 6, 6, 6, 6, 6, 6, 6, 15, 6, 6, 6, 6, 6, 6, 6, 6, 3],
        [7, 17, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 1, 7],
        [7, 0, 9, 10, 0, 9, 6, 10, 0, 8, 0, 9, 6, 10, 0, 9, 10, 0, 7],
        [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
        [7, 0, 9, 10, 0, 11, 0, 9, 6, 15, 6, 10, 0, 11, 0, 9, 10, 0, 7],
        [7, 0, 0, 0, 0, 7, 0, 0, 0, 7, 0, 0, 0, 7, 0, 0, 0, 0, 7],
        [5, 6, 6, 3, 0, 13, 6, 10, 0, 8, 0, 9, 6, 14, 0, 2, 6, 6, 4],
        [17, 17, 17, 7, 0, 7, 0, 0, 0, 0, 0, 0, 0, 7, 0, 7, 17, 17, 17],
        [6, 6, 6, 4, 0, 8, 0, 2, 10, 17, 9, 3, 0, 8, 0, 5, 6, 6, 6],
        [0, 0, 0, 0, 0, 0, 0, 7, 17, 17, 17, 7, 0, 0, 0, 0, 0, 0, 0],
        [6, 6, 6, 3, 0, 11, 0, 5, 6, 6, 6, 4, 0, 11, 0, 2, 6, 6, 6],
        [17, 17, 17, 7, 0, 7, 0, 0, 0, 0, 0, 0, 0, 7, 0, 7, 17, 17, 17],
        [2, 6, 6, 4, 0, 8, 0, 9, 6, 15, 6, 10, 0, 8, 0, 5, 6, 6, 3],
        [7, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 7],
        [7, 0, 9, 3, 0, 9, 6, 10, 0, 8, 0, 9, 6, 10, 0, 2, 10, 0, 7],
        [7, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 7],
        [13, 10, 0, 8, 0, 11, 0, 9, 6, 15, 6, 10, 0, 11, 0, 8, 0, 9, 14],
        [7, 0, 0, 0, 0, 7, 0, 0, 0, 7, 0, 0, 0, 7, 0, 0, 0, 0, 7],
        [7, 0, 9, 6, 6, 12, 6, 10, 0, 8, 0, 9, 6, 12, 6, 6, 10, 0, 7],
        [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 7],
        [5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 4],
    ]
    pellet = 0
    for row in range(len(level1maze)):
        for col in range(len(level1maze[0])):
            if level1maze[row][col] == 1:
                pellet += 1

    if level == "Level1":
        return level1maze
    elif level == "Level2":
        level2maze = [row[:] for row in level1maze]  # Create a copy of level1maze
        for row in range(len(level1maze)):
            for col in range(len(level1maze[0])):
                if level1maze[row][col] == 1 and pellet > 3:
                    level2maze[row][col] = 0
                    pellet = max(0, pellet - 1)  # Ensure pellet does not go negative
        return level2maze
    else:
        print("Invalid Maze Input", level)
        return level1maze

# Function to draw the maze
def draw_maze(mazeLevel = getMazeDesign("Level1")):
    wall_images = {
        2: 'resources/wall-corner-ul.gif',
        3: 'resources/wall-corner-ur.gif',
        4: 'resources/wall-corner-lr.gif',
        5: 'resources/wall-corner-ll.gif',
        6: 'resources/wall-straight-horiz.gif',
        7: 'resources/wall-straight-vert.gif',
        8: 'resources/wall-end-b.gif',
        9: 'resources/wall-end-l.gif',
        10: 'resources/wall-end-r.gif',
        11: 'resources/wall-end-t.gif',
        12: 'resources/wall-t-bottom.gif',
        13: 'resources/wall-t-left.gif',
        14: 'resources/wall-t-right.gif',
        15: 'resources/wall-t-top.gif',
        16: 'resources/wall-x.gif'
    }

    for row in range(len(mazeLevel)):
        for col in range(len(mazeLevel[row])):
            x = col * CELL_SIZE
            y = row * CELL_SIZE
            cell_value = mazeLevel[row][col]

            if cell_value == 0:  # Dot
                pygame.draw.circle(
                    screen, WHITE, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2), 2
                )
            elif cell_value == 1:  # Pellet
                pygame.draw.circle(
                    screen, WHITE, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2), 5
                )
            elif cell_value in wall_images:
                try:
                    wallImage = pygame.image.load(wall_images[cell_value])
                    wallImage = pygame.transform.scale(wallImage, (CELL_SIZE, CELL_SIZE))
                    screen.blit(wallImage, (x, y))
                except pygame.error as e:
                    print(f"Error loading image {wall_images[cell_value]}: {e}")
            elif cell_value == 17:  # Empty
                pass