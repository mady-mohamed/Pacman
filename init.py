import pygame
import sys, math, copy
import heapq
import time
import random

''' 1. Initialization and Setup Functions (Constructing the Game)'''

from settings import CELL_SIZE, HEIGHT, VULNERABLE, RED, CYAN, PINK, ORANGE, BLACK, WIDTH, image

def setPacmanOrientation(direction):
    global image  # Declare image as global to modify the global variable
    if direction == 'Up':
        image = pygame.image.load('resources/pacman_up.png')
    elif direction == 'Right':
        image = pygame.image.load('resources/pacman_right.png')
    elif direction == 'Down':
        image = pygame.image.load('resources/pacman_down.png')
    elif direction == 'Left':
        image = pygame.image.load('resources/pacman_left.png')
    else:
        print("pacman orient error")

def draw_lives(screen):
    for i in range(pacman_lives):
        # Scale the image to a smaller size for the lives display
        lives_image = pygame.image.load("resources/pacman_right.png")
        scaled_image = pygame.transform.scale(lives_image, (CELL_SIZE // 2, CELL_SIZE // 2))
        # Calculate the position for each life icon
        x_lives = i * (CELL_SIZE // 2 + 5)  # Add some spacing between icons
        y_lives = HEIGHT - CELL_SIZE // 2 - 5  # Position at the bottom left
        # Blit the scaled image onto the screen
        screen.blit(scaled_image, (x_lives + CELL_SIZE, y_lives))

def draw_score(screen, maze):
    font = pygame.font.SysFont('chalkduster.ttf', CELL_SIZE)
    score_text = font.render(f"Score: {getPacmanScore()}", True, (255, 255, 255))
    screen.blit(score_text, ((len(maze[0])*CELL_SIZE)-4*CELL_SIZE, (CELL_SIZE//2)-6))

''' 2. Game State Functions'''

from game import getPacmanScore, getPacmanX, getPacmanY, setPacmanX, setPacmanY, setPacmanScore
from game import pacmanmode, GHOST_DELAY, ghost_delay_counter, current_direction, pacman_lives

# Function to draw Pac-Man
def draw_pacman(screen, x = getPacmanX(), y = getPacmanY()):
    
    # Scale the image to the cell size
    scaled_image = pygame.transform.scale(image, (CELL_SIZE, CELL_SIZE))
    
    # Calculate the center position for the scaled image
    x_pos = x * CELL_SIZE + CELL_SIZE // 2 - CELL_SIZE // 2
    y_pos = y * CELL_SIZE + CELL_SIZE // 2 - CELL_SIZE // 2
    
    # Blit the scaled image onto the screen
    screen.blit(scaled_image, (x_pos, y_pos))

def setPacmanMode(mode):
    global pacmanmode
    pacmanmode = mode

def setGhostPos(ghost, x, y):
    if ghost == "RED":
        ghosts[0][1], ghosts[0][0] = x, y
        ghosts[0][4] = True  # Set idle flag to True
        ghosts[0][5] = pygame.time.get_ticks() + 2500  # Set idle timer for 2.5 seconds
        ghosts[0][1]-=1
    elif ghost == "CYAN":
        ghosts[1][1], ghosts[1][0] = x, y
        ghosts[1][4] = True
        ghosts[1][5] = pygame.time.get_ticks() + 2500
        ghosts[1][1]+=1
    elif ghost == "PINK":
        ghosts[2][1], ghosts[2][0] = x, y
        ghosts[2][4] = True
        ghosts[2][5] = pygame.time.get_ticks() + 2500
    else:
        ghosts[3][1], ghosts[3][0] = x, y
        ghosts[3][4] = True
        ghosts[3][5] = pygame.time.get_ticks() + 2500

    # Redraw the ghosts to update their positions on the screen


def setGhostState(screen, state, color = "RED"):
    global ghosts
    if state == "VULNERABLE":
        ghosts[0][2], ghosts[1][2], ghosts[2][2], ghosts[3][2] = (VULNERABLE,VULNERABLE,VULNERABLE,VULNERABLE)
        draw_ghosts(ghosts, screen)
    elif state == "normal":
        ghosts[0][2] = RED
        ghosts[1][2] = CYAN
        ghosts[2][2] = PINK
        ghosts[3][2] = ORANGE
        draw_ghosts(ghosts, screen)

def getGhostPos(ghost):
    if ghost == "RED":
        return [ghosts[0][1], ghosts[0][0]]
    elif ghost == "CYAN":
        return [ghosts[1][1], ghosts[1][0]]
    elif ghost == "PINK":
        return [ghosts[2][1], ghosts[2][0]]
    else:
        return [ghosts[3][1], ghosts[3][0]]

# Function to draw ghosts
def draw_ghosts(ghosts, screen):
    for ghost in ghosts:
        row, col, color, accuracy, idle, idle_timer = ghost
        global ghost_img
        if color == RED:
            ghost_img = pygame.image.load('resources/ghost_red.png')
        elif color == CYAN:
            ghost_img = pygame.image.load('resources/ghost_cyan.png')
        elif color == PINK:
            ghost_img = pygame.image.load('resources/ghost_pink.png')
        elif color == ORANGE:
            ghost_img = pygame.image.load('resources/ghost_orange.png')
        else:
            ghost_img = pygame.image.load('resources/ghost_vulnerable.png')
        ghost_img = pygame.transform.scale(ghost_img, (CELL_SIZE, CELL_SIZE))
        x = col * CELL_SIZE
        y = row * CELL_SIZE

        # Directly use the pre-scaled ghost image
        screen.blit(ghost_img, (x, y))

''''''
# Initialize Pygame
pygame.init()

''''''


''' 3. Game Logic Functions'''

from game import astar

# Ghost positions and colors
ghosts = [
    [9, 9, RED, 1, False, 0],  # [row, col, color, accuracy, idle, idle_timer]
    [9, 9, CYAN, 1, False, 0],
    [8, 9, PINK, 1, False, 0],
    [9, 9, ORANGE, 1, False, 0],
]

ghosts[0][1] -= 1
ghosts[1][1] += 1

vel = 1

def move_pacman(direction, maze):
    global pacmanX, pacmanY, pacman_lives, current_direction

    

    if direction == "Left":
        if getPacmanX() > 0 and maze[int(getPacmanY())][getPacmanX() - vel] in [0, 1, 17]:
            setPacmanX(getPacmanX() - vel)
            setPacmanY(int(getPacmanY()))
            setPacmanOrientation("Left")
            if pacmanmode == "KILL":
                killGhost("Left")
        elif getPacmanX() == 0:
            setPacmanX(len(maze[0]) - 1)
            setPacmanY(getPacmanY())
            setPacmanOrientation("Left")

    elif direction == "Right":
        if getPacmanX() < WIDTH // CELL_SIZE - 1 and maze[int(getPacmanY())][math.ceil(getPacmanX()+vel)] in [0, 1, 17]:
            setPacmanX(getPacmanX() + vel)
            setPacmanY(int(getPacmanY()))
            setPacmanOrientation("Right")
            if pacmanmode == "KILL":
                killGhost("Right")
        elif getPacmanX() == len(maze[0]) - 1:
            setPacmanX(0)
            setPacmanY(int(getPacmanY()))
            setPacmanOrientation("Right")

    elif direction == "Up":
        if getPacmanY() > 0 and maze[int(getPacmanY()-vel)][math.ceil(getPacmanX())] in [0, 1, 17]:
            setPacmanX(math.ceil(getPacmanX()))
            setPacmanY(getPacmanY() - vel)
            setPacmanOrientation("Up")
            if pacmanmode == "KILL":
                killGhost("Up")

    elif direction == "Down":
        if getPacmanY() < HEIGHT // CELL_SIZE - 1 and maze[int(getPacmanY()+vel)][math.ceil(getPacmanX())] in [0, 1, 17]:
            setPacmanX(math.ceil(getPacmanX()))
            setPacmanY(getPacmanY() + vel)
            setPacmanOrientation("Down")
            if pacmanmode == "KILL":
                killGhost("Down")

def move_ghost(ghost_pos, player_pos, ghost_color, maze, ghost_index):
    global ghost_delay_counter

    # Check ghost color
    if ghost_color == RED:
        ghost_color = "RED"
    elif ghost_color == CYAN:
        ghost_color = "CYAN"
    elif ghost_color == PINK:
        ghost_color = "PINK"
    else:
        ghost_color = "ORANGE"
    # Check if the ghost is idle
    if ghosts[ghost_index][4]:
        # Check if the idle timer has expired
        if pygame.time.get_ticks() >= ghosts[ghost_index][5]:
            ghosts[ghost_index][4] = False  # Set idle flag to False
        else:
            return ghost_pos  # Keep the ghost idle

    # Increment the delay counter
    ghost_delay_counter += 1

    # Check if the delay counter has reached the delay threshold
    if ghost_delay_counter >= GHOST_DELAY:
        # Reset the delay counter
        ghost_delay_counter = 0

        # Check if the ghost is vulnerable
        if ghosts[ghost_index][2] == VULNERABLE:
            # Calculate the direction that increases the distance from Pac-Man
            possible_moves = [
                (ghost_pos[0] - 1, ghost_pos[1]),  # Up
                (ghost_pos[0] + 1, ghost_pos[1]),  # Down
                (ghost_pos[0], ghost_pos[1] - 1),  # Left
                (ghost_pos[0], ghost_pos[1] + 1)   # Right
            ]
            # Handle wrapping for possible moves
            possible_moves = [(move[0], move[1] % len(maze[0])) for move in possible_moves]

            # Filter out invalid moves (walls or out of bounds)
            valid_moves = list()
            for move in possible_moves:
                if 0 <= move[0] < len(maze) and 0 <= move[1] < len(maze[0]) and maze[move[0]][move[1]] in [0, 1, 17]:
                    valid_moves.append(move)

            # Find the move that maximizes the distance from Pac-Man
            max_distance = -1
            best_move = ghost_pos
            for move in valid_moves:
                distance = (move[0] - player_pos[0]) ** 2 + (move[1] - player_pos[1]) ** 2
                if distance > max_distance:
                    max_distance = distance
                    best_move = move

            return best_move

        # Calculate the path and move the ghost
        path = astar(ghost_pos, player_pos, maze, ghost_color)
        if path and len(path) > 1:
            # Move the ghost to the next position in the path
            next_pos = path[1]

            # Handle wrapping
            next_pos = (next_pos[0], next_pos[1] % len(maze[0]))

            return next_pos

    # If the delay threshold is not reached, return the current position
    return ghost_pos

def killGhost(current_direction):

    def killAdjacent(dir = [0, 0]):
         
        if (getPacmanY(), getPacmanX()) == (ghosts[0][0] + dir[0], ghosts[0][1] + dir[1]):
            setGhostPos("RED", 8, 9)
            setPacmanScore(getPacmanScore() + 200)
        elif (getPacmanY(), getPacmanX()) == (ghosts[1][0] + dir[0], ghosts[1][1] + dir[1]):
            setGhostPos("CYAN", 10, 9)
            setPacmanScore(getPacmanScore() + 200)
        elif (getPacmanY(), getPacmanX()) == (ghosts[2][0] + dir[0], ghosts[2][1] + dir[1]):
            setGhostPos("PINK", 9, 8)
            setPacmanScore(getPacmanScore() + 200)
        elif (getPacmanY(), getPacmanX()) == (ghosts[3][0] + dir[0], ghosts[3][1] + dir[1]):
            setGhostPos("ORANGE", 9, 10)
            setPacmanScore(getPacmanScore() + 200)

    killAdjacent()

    if current_direction == "Left":
        dir = [-1, 0]
        killAdjacent(dir)
    if current_direction == "Up":
        dir = [0, 1]
        killAdjacent(dir)
    if current_direction == "Right":
        dir = [1, 0]
        killAdjacent(dir)
    if current_direction == "Down":
        dir = [0, -1]
        killAdjacent(dir)