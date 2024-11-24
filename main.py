import pygame
import sys, math, copy
import heapq
import time
import random

# Initialize Pygame
pygame.init()


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

global level1maze, level2maze
# Maze layout (1: wall, 0: dot, 2: pellet, 3: empty)
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


maze = level1maze
level2maze = [
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
level = "Level1"
pellet = 0
mazePotZeroCount = 0 #Potential count for current level empty cells
mazeZeroCount = 0   #Current count for empty cells

# Ghost positions and colors
ghosts = [
    [9, 8, RED, 0.1, False, 0],  # [row, col, color, accuracy, idle, idle_timer]
    [9, 10, CYAN, 0.075, False, 0],
    [8, 9, PINK, 0.05, False, 0],
    [10, 9, ORANGE, 0.025, False, 0],
]

# Pac-Man position
pacmanX = 1
pacmanY = 1
pacman_lives = 2
pacmanDir = [0, 0, 0, 0] # ["Up", "Right", "Down", "Left"]


pacman_score = 0
def getPacmanScore():
    global pacman_score
    return pacman_score
def setPacmanScore(value):
    global pacman_score
    pacman_score = value
def draw_score():
    font = pygame.font.SysFont('chalkduster.ttf', CELL_SIZE)
    score_text = font.render(f"Score: {getPacmanScore()}", True, (255, 255, 255))
    screen.blit(score_text, ((len(maze[0])*CELL_SIZE)-4*CELL_SIZE, (CELL_SIZE//2)-6))



# Function to draw the maze
def draw_maze(level):
    for row in range(len(level)):
        for col in range(len(level[row])):
            x = col * CELL_SIZE
            y = row * CELL_SIZE
            if level[row][col] == 1:  # Wall
                pygame.draw.rect(screen, BLUE, (x, y, CELL_SIZE, CELL_SIZE))
            elif level[row][col] == 0:  # Dot
                pygame.draw.circle(
                    screen, WHITE, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2), 2
                )
            elif level[row][col] == 2:  # Pellet
                pygame.draw.circle(
                    screen, WHITE, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2), 5
                )

def setMazeLevel(level):
    global maze
    
    if level == "Level1":
        draw_maze(level1maze)
    elif level == "Level2":
        draw_maze(level2maze)
    else:
        print("Invalid Maze Input", level)
        draw_maze(level1maze)
    draw_maze(maze)


# Function to draw Pac-Man
def draw_pacman(x = pacmanX, y = pacmanY):
    
    # Scale the image to the cell size
    scaled_image = pygame.transform.scale(image, (CELL_SIZE, CELL_SIZE))
    
    # Calculate the center position for the scaled image
    x_pos = x * CELL_SIZE + CELL_SIZE // 2 - CELL_SIZE // 2
    y_pos = y * CELL_SIZE + CELL_SIZE // 2 - CELL_SIZE // 2
    
    # Blit the scaled image onto the screen
    screen.blit(scaled_image, (x_pos, y_pos))

def setPacmanOrientation(direction):
    global image  # Declare image as global to modify the global variable
    if direction == 'Up':
        image = pygame.image.load('pacman_up.png')
    elif direction == 'Right':
        image = pygame.image.load('pacman_right.png')
    elif direction == 'Down':
        image = pygame.image.load('pacman_down.png')
    elif direction == 'Left':
        image = pygame.image.load('pacman_left.png')
    else:
        print("pacman orient error")

def draw_lives():
    for i in range(pacman_lives):
        # Scale the image to a smaller size for the lives display
        lives_image = pygame.image.load("pacman_right.png")
        scaled_image = pygame.transform.scale(lives_image, (CELL_SIZE // 2, CELL_SIZE // 2))
        # Calculate the position for each life icon
        x_lives = i * (CELL_SIZE // 2 + 5)  # Add some spacing between icons
        y_lives = HEIGHT - CELL_SIZE // 2 - 5  # Position at the bottom left
        # Blit the scaled image onto the screen
        screen.blit(scaled_image, (x_lives + CELL_SIZE, y_lives))

def getPacmanX():
    return pacmanX

def setPacmanX(x):
    global pacmanX
    pacmanX = x

def getPacmanY():
    return pacmanY

def setPacmanY(y):
    global pacmanY
    pacmanY = y

# Function to draw ghosts
def draw_ghosts(ghosts):
    for ghost in ghosts:
        row, col, color, accuracy, idle, idle_timer = ghost
        global ghost_img
        if color == RED:
            ghost_img = pygame.image.load('ghost_red.png')
        elif color == CYAN:
            ghost_img = pygame.image.load('ghost_cyan.png')
        elif color == PINK:
            ghost_img = pygame.image.load('ghost_pink.png')
        elif color == ORANGE:
            ghost_img = pygame.image.load('ghost_orange.png')
        else:
            ghost_img = pygame.image.load('ghost_vulnerable.png')
        ghost_img = pygame.transform.scale(ghost_img, (CELL_SIZE, CELL_SIZE))
        x = col * CELL_SIZE
        y = row * CELL_SIZE

        # Directly use the pre-scaled ghost image
        screen.blit(ghost_img, (x, y))

def setGhostState(state, color = "RED"):
    global ghosts
    if state == "VULNERABLE":
        ghosts[0][2], ghosts[1][2], ghosts[2][2], ghosts[3][2] = (VULNERABLE,VULNERABLE,VULNERABLE,VULNERABLE)
        draw_ghosts(ghosts)
    elif state == "normal":
        ghosts[0][2] = RED
        ghosts[1][2] = CYAN
        ghosts[2][2] = PINK
        ghosts[3][2] = ORANGE
        draw_ghosts(ghosts)
    
    

vel = 1

def heuristic(start, goal):
    return abs(start[0] - goal[0]) + abs(start[1] - goal[1])

def astar(start, goal, maze):
    randomness = random.random()
    # Initialize the open list with the start node and its estimation
    #  of the total cost to reach the goal through a particular node (0)
    open_list = []
    heapq.heappush(open_list, (0, start))
    
    # Dictionary to keep track of the path
    came_from = {}
    
    # Dictionary to keep track of the cost from the start node to each node
    g_score = {start: 0}
    
    # Dictionary to keep track of the estimated cost from each node to the goal
    h_score = {start: heuristic(start, goal)}

    while open_list:
        # Get the node with the lowest f-score from the open list
        current = heapq.heappop(open_list)[1]

        # If the current node is the goal, reconstruct the path and return it
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        # Get the neighbors of the current node
        for neighbor in get_neighbors(current, maze):
            # Calculate the tentative g-score for the neighbor
            tentative_g_score = g_score[current] + 1
            
            # If the neighbor is not in g_score or the tentative g-score is lower, update the scores
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                # Adjust the heuristic with randomness to make the pathfinding less accurate
                h_score[neighbor] = tentative_g_score + heuristic(neighbor, goal) * (1 + randomness)
                
                # Add the neighbor to the open list with its f-score
                heapq.heappush(open_list, (h_score[neighbor], neighbor))

    # If the open list is empty and the goal was not reached, return None
    return None

def get_neighbors(position, maze):
    neighbors = []
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for direction in directions:
        neighbor = (position[0] + direction[0], position[1] + direction[1])
        if 0 <= neighbor[0] < len(maze) and 0 <= neighbor[1] < len(maze[0]) and maze[neighbor[0]][neighbor[1]] != 1:
            neighbors.append(neighbor)
    return neighbors

# Add a global variable for the delay counter
ghost_delay_counter = 0
GHOST_DELAY = 10  # Number of ticks to delay the movement for both ghosts
ghosts[0][1]-=1
ghosts[1][1]+=1

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
    draw_ghosts(ghosts)

def move_ghost(ghost_pos, player_pos, ghost, maze, ghost_index):
    global ghost_delay_counter

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
            valid_moves = [move for move in possible_moves if maze[move[0]][move[1]] != 1]

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
        path = astar(ghost_pos, player_pos, maze)
        if path and len(path) > 1:
            # Move the ghost to the next position in the path
            next_pos = path[1]

            # Handle wrapping
            next_pos = (next_pos[0], next_pos[1] % len(maze[0]))

            return next_pos

    # If the delay threshold is not reached, return the current position
    return ghost_pos

def getGhostPos(ghost):
    if ghost == "RED":
        return [ghosts[0][1], ghosts[0][0]]
    elif ghost == "CYAN":
        return [ghosts[1][1], ghosts[1][0]]
    elif ghost == "PINK":
        return [ghosts[2][1], ghosts[2][0]]
    else:
        return [ghosts[3][1], ghosts[3][0]]

global pacmanmode
pacmanmode = "normal"

def setPacmanMode(mode):
    global pacmanmode
    pacmanmode = mode
    print(mode)

# Add a global variable for the timer
ghost_respawn_timer = 0

def killGhost():
    if (getPacmanY(), getPacmanX()) == (ghosts[0][0], ghosts[0][1]):
                setGhostPos("RED", 8, 9)
                setPacmanScore(getPacmanScore() + 200)
    elif (getPacmanY(), getPacmanX()) == (ghosts[1][0], ghosts[1][1]):
                setGhostPos("CYAN", 10, 9)
                setPacmanScore(getPacmanScore() + 200)
    elif (getPacmanY(), getPacmanX()) == (ghosts[2][0], ghosts[2][1]):
                setGhostPos("PINK", 9, 8)
                setPacmanScore(getPacmanScore() + 200)
    elif (getPacmanY(), getPacmanX()) == (ghosts[3][0], ghosts[3][1]):
                setGhostPos("ORANGE", 9, 10)
                setPacmanScore(getPacmanScore() + 200)

# Add a global variable to store the current direction
current_direction = None

def move_pacman(direction):
    global pacmanX, pacmanY, pacman_lives, current_direction

    if direction == "Left":
        if getPacmanX() > 0 and maze[int(getPacmanY())][math.floor(getPacmanX()-vel)] != 1:
            setPacmanX(getPacmanX() - vel)
            setPacmanY(int(getPacmanY()))
            setPacmanOrientation("Left")
            if pacmanmode == "KILL" and getGhostPos("RED") == (getPacmanX() - 1, getPacmanY()):
                setGhostPos("RED", 8, 9)
                setPacmanScore(getPacmanScore() + 200)
            if pacmanmode == "KILL" and getGhostPos("CYAN") == (getPacmanX() - 1, getPacmanY()):
                setGhostPos("CYAN", 8, 9)
                setPacmanScore(getPacmanScore() + 200)
            if pacmanmode == "KILL" and getGhostPos("PINK") == (getPacmanX() - 1, getPacmanY()):
                setGhostPos("PINK", 8, 9)
                setPacmanScore(getPacmanScore() + 200)
            if pacmanmode == "KILL" and getGhostPos("ORANGE") == (getPacmanX() - 1, getPacmanY()):
                setGhostPos("ORANGE", 8, 9)
                setPacmanScore(getPacmanScore() + 200)
        elif getPacmanX() == 0:
            setPacmanX(len(maze[0]) - 1)
            setPacmanY(int(getPacmanY()))
            setPacmanOrientation("Left")

    elif direction == "Right":
        if getPacmanX() < WIDTH // CELL_SIZE - 1 and maze[int(getPacmanY())][math.ceil(getPacmanX()+vel)] != 1:
            setPacmanX(getPacmanX() + vel)
            setPacmanY(int(getPacmanY()))
            setPacmanOrientation("Right")
            if pacmanmode == "KILL" and getGhostPos("RED") == (getPacmanX() + 1, getPacmanY()):
                setGhostPos("RED", 8, 9)
                setPacmanScore(getPacmanScore() + 200)
            if pacmanmode == "KILL" and getGhostPos("CYAN") == (getPacmanX() + 1, getPacmanY()):
                setGhostPos("CYAN", 8, 9)
                setPacmanScore(getPacmanScore() + 200)
            if pacmanmode == "KILL" and getGhostPos("PINK") == (getPacmanX() + 1, getPacmanY()):
                setGhostPos("PINK", 8, 9)
                setPacmanScore(getPacmanScore() + 200)
            if pacmanmode == "KILL" and getGhostPos("ORANGE") == (getPacmanX() + 1, getPacmanY()):
                setGhostPos("ORANGE", 8, 9)
                setPacmanScore(getPacmanScore() + 200)
        elif getPacmanX() == len(maze[0]) - 1:
            setPacmanX(0)
            setPacmanY(int(getPacmanY()))
            setPacmanOrientation("Right")

    elif direction == "Up":
        if getPacmanY() > 0 and maze[int(getPacmanY()-vel)][math.ceil(getPacmanX())] != 1:
            setPacmanX(math.ceil(getPacmanX()))
            setPacmanY(getPacmanY() - vel)
            setPacmanOrientation("Up")

    elif direction == "Down":
        if getPacmanY() < HEIGHT // CELL_SIZE - 1 and maze[int(getPacmanY()+vel)][math.ceil(getPacmanX())] != 1:
            setPacmanX(math.ceil(getPacmanX()))
            setPacmanY(getPacmanY() + vel)
            setPacmanOrientation("Down")

def main():
    global screen, kill_mode_timer, ghost_respawn_timer, current_direction, mazeZeroCount, mazePotZeroCount, maze
    clock = pygame.time.Clock()
    running = True
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        global pacman_lives

        # Handle movement
        if keys[pygame.K_LEFT]:
            current_direction = "Left"
        elif keys[pygame.K_RIGHT]:
            current_direction = "Right"
        elif keys[pygame.K_UP]:
            current_direction = "Up"
        elif keys[pygame.K_DOWN]:
            current_direction = "Down"

        # Move Pac-Man in the current direction
        if current_direction:
            move_pacman(current_direction)

        # Update maze state for Pac-Man's position
        if maze[getPacmanY()][getPacmanX()] == 0:
            maze[getPacmanY()][getPacmanX()] = 3
            setPacmanScore(getPacmanScore() + 10)
        elif maze[getPacmanY()][getPacmanX()] == 2:
            setPacmanMode("KILL")
            setPacmanScore(getPacmanScore() + 50)
            kill_mode_timer = pygame.time.get_ticks() + 10000  # Set timer for 10 seconds
            maze[getPacmanY()][getPacmanX()] = 3

        # Move the ghosts
        ghosts[0][0], ghosts[0][1] = move_ghost((ghosts[0][0], ghosts[0][1]), (getPacmanY(), getPacmanX()), ghosts[0][3], maze, 0)
        ghosts[1][0], ghosts[1][1] = move_ghost((ghosts[1][0], ghosts[1][1]), (getPacmanY(), getPacmanX()), ghosts[1][3], maze, 1)
        ghosts[2][0], ghosts[2][1] = move_ghost((ghosts[2][0], ghosts[2][1]), (getPacmanY(), getPacmanX()), ghosts[2][3], maze, 2)
        ghosts[3][0], ghosts[3][1] = move_ghost((ghosts[3][0], ghosts[3][1]), (getPacmanY(), getPacmanX()), ghosts[3][3], maze, 3)

        # Check for collisions with ghosts when in KILL mode
        if pacmanmode == "KILL":
            pacman_x = getPacmanX()
            pacman_y = getPacmanY()
            pacman_pos = (pacman_y, pacman_x)
            setGhostState("VULNERABLE")
            killGhost()

            # Check if the timer has expired to switch back to normal mode
            if pygame.time.get_ticks() > kill_mode_timer:
                setPacmanMode("normal")
        if pacmanmode == "normal":
            pacman_x = getPacmanX()
            pacman_y = getPacmanY()
            pacman_pos = (pacman_y, pacman_x)
            setGhostState("normal")

            if pacman_pos == (ghosts[0][0], ghosts[0][1]) or pacman_pos == (ghosts[1][0], ghosts[1][1]) or pacman_pos == (ghosts[2][0], ghosts[2][1]) or pacman_pos == (ghosts[3][0], ghosts[3][1]):
                setPacmanX(1)
                setPacmanY(1)
                setGhostPos("RED", 10, 8) #(9 8) (9 10) (8 9) (10 9)
                setGhostPos("CYAN", 8, 10)
                setGhostPos("PINK", 7, 9)
                setGhostPos("ORANGE", 11, 9)
                pacman_lives -= 1
                print(pacman_lives)
                if pacman_lives < 0:
                    running = False

        for row in range(len(level1maze)-1):
            for col in range(len(level1maze[0])-1):
                if level1maze[row][col] == 2 or level1maze[row][col] == 0 or level1maze[row][col] == 3:
                    mazePotZeroCount += 1
                if level1maze[row][col] == 3:
                    mazeZeroCount += 1
        if mazePotZeroCount == mazeZeroCount: 
            maze = level2maze
            draw_maze(maze)
        print(mazePotZeroCount, mazeZeroCount)


        
        # print(mazePotZeroCount, mazeZeroCount, level)
        mazeZeroCount = 0
        mazePotZeroCount = 0
        # Redraw the screen
        screen.fill(BLACK)
        
        setMazeLevel(level)
        # sets maze level and draws maze
        draw_pacman(pacman_x, pacman_y)  # Ensure Pac-Man is drawn after updating position
        draw_ghosts(ghosts)
        draw_lives()  # Draw Pac-Man's lives last to ensure they are on top
        draw_score()


        pygame.display.flip()

        clock.tick(10)

if __name__ == "__main__":
    main()
