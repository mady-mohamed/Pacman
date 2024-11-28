import pygame, sys
# Maze Layout          0 - Dot 1 - Pellet 2 - Empty 3 - Wall
maze = [
[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
[3, 2, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3],
[3, 0, 3, 3, 0, 3, 3, 3, 0, 3, 0, 3, 3, 3, 0, 3, 3, 0, 3],
[3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
[3, 0, 3, 3, 0, 3, 0, 3, 3, 3, 3, 3, 1, 3, 0, 3, 3, 0, 3],
[3, 0, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0, 0, 3],
[3, 3, 3, 3, 0, 3, 3, 3, 0, 3, 0, 3, 3, 3, 0, 3, 3, 3, 3],
[2, 2, 2, 3, 0, 3, 0, 1, 0, 0, 0, 0, 0, 3, 0, 3, 2, 2, 2],
[3, 3, 3, 3, 0, 3, 0, 3, 3, 3, 3, 3, 0, 3, 0, 3, 3, 3, 3],
[0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0],
[3, 3, 3, 3, 0, 3, 0, 3, 3, 3, 3, 3, 0, 3, 0, 3, 3, 3, 3],
[2, 2, 2, 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 3, 0, 3, 2, 2, 2],
[3, 3, 3, 3, 0, 3, 0, 3, 3, 3, 3, 3, 0, 3, 0, 3, 3, 3, 3],
[3, 0, 0, 0, 0, 0, 0, 1, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3],
[3, 0, 3, 3, 0, 3, 3, 3, 0, 3, 0, 3, 3, 3, 0, 3, 3, 0, 3],
[3, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 3],
[3, 3, 0, 3, 0, 3, 0, 3, 3, 3, 3, 3, 0, 3, 0, 3, 0, 3, 3],
[3, 1, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0, 0, 3],
[3, 0, 3, 3, 3, 3, 3, 3, 0, 3, 0, 3, 3, 3, 3, 3, 3, 0, 3],
[3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3],
[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
]

count = 0
visited = [[False for i in range(len(maze[0]))] for j in range(len(maze))]

# Count top left corner cells (2)
for row in range(len(maze)):
    for col in range(len(maze[row])):  # Loop through each cell
        if maze[row][col] == 3 and not visited[row][col]:  # check if wall and not visited
            # Check if the current cell is not on the last row or last column
            if row < len(maze) - 1 and col < len(maze[0]) - 1:
                # Check if the cell to the right and the cell below are both 1
                # and the cell to the left and the cell above are in [0, 2, 3]
                if maze[row][col + 1] == 3 and maze[row + 1][col] == 3 and maze[row][col - 1] in [0, 1, 2] and maze[row - 1][col] in [0, 1, 2]:
                    count += 1
                    print(row, col)
                    visited[row][col] = True  # Mark cells as visited
                    visited[row][col + 1] = True
                    visited[row + 1][col] = True 
                    # maze[row][col] = 2
                if row == 0 and col == 0:
                    count += 1
                    print(row, col)
                    visited[row][col] = True  # Mark cells as visited
                    visited[row][col + 1] = True
                    visited[row + 1][col] = True 

print(count)

count = 0

visited = [[False for i in range(len(maze[0]))] for j in range(len(maze))]

# Count top right corner cells (3)
for row in range(len(maze)):
    for col in range(len(maze[row])):  # Loop through each cell
        if maze[row][col] == 3 and not visited[row][col]:  # check if wall and not visited
            # Check if the current cell is not on the last row or last column
            if row < len(maze) - 1 and col < len(maze[0]) - 1:
                # Check if the cell to the left and the cell below are both 1
                # and the cell to the right and the cell above are in [0, 2, 3]
                if maze[row][col + 1] in [0, 1, 2] and maze[row][col - 1] == 3 and maze[row + 1][col] == 3  and maze[row - 1][col] in [0, 1, 2]:
                    count += 1
                    print(row, col)
                    visited[row][col] = True  # Mark cells as visited
                    visited[row][col + 1] = True
                    visited[row + 1][col] = True 
                    maze[row][col] = 4
                if row == len(maze) and col == 0:
                    count += 1
                    print(row, col)
                    visited[row][col] = True  # Mark cells as visited
                    visited[row][col + 1] = True
                    visited[row + 1][col] = True 

print(count)

count = 0

# visited = [[False for i in range(len(maze[0]))] for j in range(len(maze))]

# # Count bottom right corner cells (4)
# for row in range(len(maze)):
#     for col in range(len(maze[row])):  # Loop through each cell
#         if maze[row][col] == 3 and not visited[row][col]:  # check if wall and not visited
#             # Check if the current cell is not on the last row or last column
#             if row < len(maze) - 1 and col < len(maze[0]) - 1:
#                 # Check if the cell to the left and the cell below are both 1
#                 # and the cell to the right and the cell above are in [0, 2, 3]
#                 if maze[row][col + 1] in [0, 1, 2] and maze[row + 1][col] in [0, 1, 2] and maze[row][col - 1] == 3 and maze[row - 1][col] == 3:
#                     count += 1
#                     print(row, col)
#                     visited[row][col] = True  # Mark cells as visited
#                     visited[row][col + 1] = True
#                     visited[row + 1][col] = True 
#                     maze[row][col] = 4
#             if row == len(maze) - 1 and col == len(maze[0]) - 1: # Edge cases
#                 count += 1
#                 print(row, col)
#                 visited[row][col] = True  # Mark cells as visited
#                 maze[row][col] = 4

print(count)

# Initialize Pygame
pygame.init()

# Define constants
CELL_SIZE = 20
WALL_COLOR = (0, 0, 255)
PATH_COLOR = (0, 0, 0)
VISITED_COLOR = (255, 0, 0)

# Calculate the dimensions of the window
rows = len(maze)
cols = len(maze[0])
width = cols * CELL_SIZE
height = rows * CELL_SIZE

# Set up the display
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Maze")

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the maze
    for row in range(rows):
        for col in range(cols):
            if maze[row][col] in [0, 1, 2]:
                color = PATH_COLOR
            elif maze[row][col] == 4:
                color = VISITED_COLOR
            else:
                color = WALL_COLOR
            pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
