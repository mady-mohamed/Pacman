import pygame, heapq, random

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



def heuristic(a, b, ghost):
    (x1, y1) = a
    (x2, y2) = b
    distance = abs(x1 - x2) + abs(y1 - y2)
    
    if ghost == "RED":
        return distance * random.uniform(1, 1.25)
    elif ghost == "CYAN":
        return distance * random.uniform(1.25, 1.5)
    elif ghost == "PINK":
        return distance * random.uniform(1.5, 1.75)
    else:
        return distance * random.uniform(1.75, 2)

def astar(start, goal, maze, ghost):
    open_list = []
    heapq.heapify(open_list)
    heapq.heappush(open_list, (0, start))
    
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal, ghost)}
    
    while open_list:
        current = heapq.heappop(open_list)[1]
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path
        
        for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            neighbor = (current[0] + direction[0], current[1] + direction[1])
            if 0 <= neighbor[0] < len(maze) and 0 <= neighbor[1] < len(maze[0]) and maze[neighbor[0]][neighbor[1]] in [0, 1, 17]:
                tentative_g_score = g_score[current] + 1
                
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal, ghost)
                    heapq.heappush(open_list, (f_score[neighbor], neighbor))
    
    return None