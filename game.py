import pygame, heapq, random

# Pac-Man position

pacman_lives = 2
pacmanDir = [0, 0, 0, 0] # ["Up", "Right", "Down", "Left"]
pacman_score = 0

# Add a global variable for the delay counter
ghost_delay_counter = 0
GHOST_DELAY = 9  # Number of ticks to delay the movement for both ghosts (5)

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



def heuristic(start, goal):
    return abs(start[0] - goal[0]) + abs(start[1] - goal[1])

def get_neighbors(position, maze):
    neighbors = []
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for direction in directions:
        neighbor = (position[0] + direction[0], position[1] + direction[1])
        if 0 <= neighbor[0] < len(maze) and 0 <= neighbor[1] < len(maze[0]) and maze[neighbor[0]][neighbor[1]] in [0, 1, 17]:
            neighbors.append(neighbor)
    return neighbors



def astar(start, goal, maze):
    # F score = H score (estimation) + G score (cost)
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
            path.append(start)      # Stack Important
            path.reverse()
            return path
        
        # Get the neighbors of the current node
        for neighbor in get_neighbors(current, maze):
            # Calculate the tentative g-score (cost) for the neighbor
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