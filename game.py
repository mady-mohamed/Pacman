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


# Calculate Heuristic Function
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
    """
    A* pathfinding algorithm to find the shortest path from start to goal in a maze.
    
    Parameters:
    - start: Tuple (x, y) representing the starting position.
    - goal: Tuple (x, y) representing the goal position.
    - maze: 2D list representing the maze where 0, 1, and 17 are traversable cells.
    - ghost: Position of the ghost (used in the heuristic function).
    
    Returns:
    - List of tuples representing the path from start to goal, or None if no path is found.
    """
    # Initialize a heap to apply algorithm
    open_list = []
    heapq.heapify(open_list)
    heapq.heappush(open_list, (0, start)) # Initialize with cost (0) and coordinates corresponding to the maze
    
    came_from = {} # Dictionary to keep track of path
    cost_score = {start: 0} # Dictionary to track score of each move
    astar_score = {start: heuristic(start, goal, ghost)} # Dictionary to document the heuristic function of each move
    
    while open_list:
        current = heapq.heappop(open_list)[1] # pop lowest astar value in list
        

        # If current move reaches goal, path will be returned
        if current == goal: 
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path
        
        for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            neighbor = (current[0] + direction[0], current[1] + direction[1]) # Modify x,y based on position of next move
            # Check if x coordinate movement is within bounds of maze
            # and if it is a legal move
            if 0 <= neighbor[0] < len(maze) and 0 <= neighbor[1] < len(maze[0]) and maze[neighbor[0]][neighbor[1]] in [0, 1, 17]:
                cost = cost_score[current] + 1
                # checks if neighbor move (node) has not been visited in the cost_score dictionary, in other words first time algorithm is encountering this node
                # or if newly calculated cost is lower than last recorded cost
                if neighbor not in cost_score or cost < cost_score[neighbor]: 
                    came_from[neighbor] = current  # Record the path: the current node is the predecessor of the neighbor
                    cost_score[neighbor] = cost  # Update the cost to reach the neighbor
                    astar_score[neighbor] = cost + heuristic(neighbor, goal, ghost)  # Calculate the A* score (cost + heuristic) for the neighbor
                    heapq.heappush(open_list, (astar_score[neighbor], neighbor))  # Push the neighbor with its A* score onto the priority queue
    
    return None