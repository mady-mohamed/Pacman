import pygame

# Ghost positions and colors
ghosts = [
    [9, 8, RED, 0.1, False, 0],  # [row, col, color, accuracy, idle, idle_timer]
    [9, 10, CYAN, 0.075, False, 0],
    [8, 9, PINK, 0.05, False, 0],
    [10, 9, ORANGE, 0.025, False, 0],
]

ghosts[0][1] -= 1
ghosts[1][1] += 1

vel = 1

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

def heuristic(start, goal):
    return abs(start[0] - goal[0]) + abs(start[1] - goal[1])