import pygame, heapq, random, ctypes, os

# Pac-Man position

pacman_lives = 2
pacmanDir = [0, 0, 0, 0] # ["Up", "Right", "Down", "Left"]
pacman_score = 0

# Add a global variable for the delay counter
ghost_delay_counter = 0
GHOST_DELAY = 5  # Number of ticks to delay the movement for all ghosts (7)

global pacmanmode
pacmanmode = "normal"

# Add a global variable for the timer
ghost_respawn_timer = 0

# Add a global variable to store the current direction
current_direction = None

#Pacman
pacmanX = 1
pacmanY = 1

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



def getPacmanScore():
    global pacman_score
    return pacman_score

def setPacmanScore(value):
    global pacman_score
    pacman_score = value


# Load the DLL
dll_path = os.path.relpath("algorithms.dll")
algorithms = ctypes.CDLL(dll_path, winmode=0)

# Define the argument and return types for the astar function
algorithms.astar.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.POINTER(ctypes.c_int)), ctypes.c_int, ctypes.c_int]
algorithms.astar.restype = ctypes.POINTER(ctypes.POINTER(ctypes.c_int))

def astar(start, goal, maze, ghost):
    # Convert the maze to a ctypes 2D array
    maze_height = len(maze)
    maze_width = len(maze[0])
    MazeArrayType = ctypes.POINTER(ctypes.c_int) * maze_height
    maze_array = MazeArrayType()
    for i in range(maze_height):
        row = (ctypes.c_int * maze_width)(*maze[i])
        maze_array[i] = ctypes.cast(row, ctypes.POINTER(ctypes.c_int))

    # Convert start and goal to ctypes
    xStart, yStart = start
    xGoal, yGoal = goal
    ghost = ghost.encode('utf-8')

    # Call the C function
    result = algorithms.astar(xStart, yStart, xGoal, yGoal, ghost, maze_array, maze_height, maze_width)

    # Convert the result back to a Python list
    path = []
    i = 0
    while result[i][0] != -1:  # Assuming the C++ function returns -1, -1 to indicate the end of the path
        path.append((result[i][0], result[i][1]))
        i += 1

    return path

def greedy(start, goal, maze, ghost):
    xStart, yStart = start
    xGoal, yGoal = goal
    maze_height = len(maze)
    maze_width = len(maze[0])

    # Priority queue to store nodes to be explored, ordered by their heuristic value
    open_list = []
    heapq.heappush(open_list, (0, (xStart, yStart)))
    came_from = {}
    came_from[(xStart, yStart)] = None

    ghost = ghost.encode('utf-8')

    while open_list:
        _, current = heapq.heappop(open_list)
        currentX, currentY = current

        # If the goal is reached, reconstruct the path
        if current == (xGoal, yGoal):
            path = []
            while current is not None:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Possible movement directions (right, down, left, up)
        for direction in directions:
            neighbor = (currentX + direction[0], currentY + direction[1])
            neighborX, neighborY = neighbor

            # Check if the neighbor is within the maze bounds and is a walkable cell (0, 1, or 17)
            if 0 <= neighborX < maze_height and 0 <= neighborY < maze_width and maze[neighborX][neighborY] in [0, 1, 17]:
                if neighbor not in came_from:
                    priority = algorithms.heuristic(neighborX, neighborY, xGoal, yGoal, ghost)  # Heuristic: Manhattan distance
                    heapq.heappush(open_list, (priority, neighbor))
                    came_from[neighbor] = current

    # If no path is found, return an empty path
    return []