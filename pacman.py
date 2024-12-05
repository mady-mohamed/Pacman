import init, pygame, settings, math

maze = settings.getMazeDesign("Level1")

def pacman_main():
    global screen, kill_mode_timer, ghost_respawn_timer, mazeZeroCount, mazePotZeroCount, maze, mazeLevel
    clock = pygame.time.Clock()
    running = True
    screen = pygame.display.set_mode((init.WIDTH, init.HEIGHT))

    while running:
        # dt = clock.tick(60)/1000
        print(clock.tick(15))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        global pacman_lives

        screen.fill(init.BLACK)
        
        # Handle movement
        if keys[pygame.K_LEFT]:
            init.current_direction = "Left"
            if init.pacmanmode == "KILL":
                init.killGhost("Left")
        elif keys[pygame.K_RIGHT]:
            init.current_direction = "Right"
            if init.pacmanmode == "KILL":
                init.killGhost("Right")
        elif keys[pygame.K_UP]:
            init.current_direction = "Up"
            if init.pacmanmode == "KILL":
                init.killGhost("Up")
        elif keys[pygame.K_DOWN]:
            init.current_direction = "Down"
            if init.pacmanmode == "KILL":
                init.killGhost("Down")

        # Move Pac-Man in the current direction
        if init.current_direction:
            init.move_pacman(init.current_direction, maze, vel = 1)

        # Update maze state for Pac-Man's position
        if maze[init.getPacmanY()][init.getPacmanX()] == 0:
            maze[init.getPacmanY()][init.getPacmanX()] = 17
            init.setPacmanScore(init.getPacmanScore() + 10)
        elif maze[init.getPacmanY()][init.getPacmanX()] == 1:
            init.setPacmanMode("KILL")
            init.setPacmanScore(init.getPacmanScore() + 50)
            kill_mode_timer = pygame.time.get_ticks() + 10000  # Set timer for 10 seconds
            maze[init.getPacmanY()][init.getPacmanX()] = 17

        # Move the ghosts
        init.ghosts[0][0], init.ghosts[0][1] = init.move_ghost((init.ghosts[0][0], init.ghosts[0][1]), (init.getPacmanY(), init.getPacmanX()), init.ghosts[0][2], maze, 0)
        init.ghosts[1][0], init.ghosts[1][1] = init.move_ghost((init.ghosts[1][0], init.ghosts[1][1]), (init.getPacmanY(), init.getPacmanX()), init.ghosts[1][2], maze, 1)
        init.ghosts[2][0], init.ghosts[2][1] = init.move_ghost((init.ghosts[2][0], init.ghosts[2][1]), (init.getPacmanY(), init.getPacmanX()), init.ghosts[2][2], maze, 2)
        init.ghosts[3][0], init.ghosts[3][1] = init.move_ghost((init.ghosts[3][0], init.ghosts[3][1]), (init.getPacmanY(), init.getPacmanX()), init.ghosts[3][2], maze, 3)

        # Check for collisions with ghosts when in KILL mode
        if init.pacmanmode == "KILL":
            pacman_x = init.getPacmanX()
            pacman_y = init.getPacmanY()
            pacman_pos = (pacman_y, pacman_x)
            init.setGhostState(screen, "VULNERABLE")
            # main.killGhost()
            # Check if the timer has expired to switch back to normal mode
            if pygame.time.get_ticks() > kill_mode_timer:
                init.setPacmanMode("normal")
            
        if init.pacmanmode == "normal":
            pacman_x = init.getPacmanX()
            pacman_y = init.getPacmanY()
            pacman_pos = (pacman_y, pacman_x)
            init.setGhostState(screen, "normal")
            if pacman_pos == (init.ghosts[0][0], init.ghosts[0][1]) or pacman_pos == (init.ghosts[1][0], init.ghosts[1][1]) or pacman_pos == (init.ghosts[2][0], init.ghosts[2][1]) or pacman_pos == (init.ghosts[3][0], init.ghosts[3][1]):
                init.setPacmanX(1)
                init.setPacmanY(1)
                init.setGhostPos("RED", 9, 9) #(9 8) (9 10) (8 9) (10 9)
                init.setGhostPos("CYAN", 9, 9)
                init.setGhostPos("PINK", 9, 8)
                init.setGhostPos("ORANGE", 9, 9)
                init.pacman_lives -= 1
                if init.pacman_lives < 0:
                    running = False
        
        settings.draw_maze(maze)

        for row in range(len(settings.getMazeDesign("Level1"))-1):
            for col in range(len(settings.getMazeDesign("Level1")[0])-1):
                if settings.getMazeDesign("Level1")[row][col] in [0, 1, 17]:
                    settings.mazePotZeroCount += 1
                if maze[row][col] == 17:
                    settings.mazeZeroCount += 1
        if settings.mazePotZeroCount > settings.mazeZeroCount: 
            settings.mazePotZeroCount, settings.mazeZeroCount = 0, 0   
            
        elif settings.mazePotZeroCount == settings.mazeZeroCount:
            print("Level2")
            maze = settings.getMazeDesign("Level2")
            settings.draw_maze(maze)
            init.setPacmanX(1)
            init.setPacmanY(1)
            init.setGhostPos("RED", 10, 8) #(9 8) (9 10) (8 9) (10 9)
            init.setGhostPos("CYAN", 8, 10)
            init.setGhostPos("PINK", 7, 9)
            init.setGhostPos("ORANGE", 11, 9)
            settings.mazeLevel += 1
            settings.mazePotZeroCount, settings.mazeZeroCount = 0, 0
        if settings.mazeLevel > 2:
            running = False
        
        # Redraw the screen

        # sets maze level and draws maze
        init.draw_pacman(screen, pacman_x, pacman_y)  # Ensure Pac-Man is drawn after updating position
        init.draw_ghosts(init.ghosts, screen)
        init.draw_lives(screen)  # Draw Pac-Man's lives last to ensure they are on top
        init.draw_score(screen, maze)


        pygame.display.flip()

if __name__ == "__main__":
    pacman_main()
