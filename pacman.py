import main, pygame

maze = main.getMazeDesign("Level1")

def pacman_main():
    global screen, kill_mode_timer, ghost_respawn_timer, mazeZeroCount, mazePotZeroCount, maze, mazeLevel
    clock = pygame.time.Clock()
    running = True
    screen = pygame.display.set_mode((main.WIDTH, main.HEIGHT))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        global pacman_lives

        screen.fill(main.BLACK)
        
        # Handle movement
        if keys[pygame.K_LEFT]:
            main.current_direction = "Left"
            if main.pacmanmode == "KILL":
                main.killGhost()
        elif keys[pygame.K_RIGHT]:
            main.current_direction = "Right"
            if main.pacmanmode == "KILL":
                main.killGhost()
        elif keys[pygame.K_UP]:
            main.current_direction = "Up"
            if main.pacmanmode == "KILL":
                main.killGhost()
        elif keys[pygame.K_DOWN]:
            main.current_direction = "Down"
            if main.pacmanmode == "KILL":
                main.killGhost()

        # Move Pac-Man in the current direction
        if main.current_direction:
            main.move_pacman(main.current_direction, maze)

        # Update maze state for Pac-Man's position
        if maze[main.getPacmanY()][main.getPacmanX()] == 0:
            maze[main.getPacmanY()][main.getPacmanX()] = 3
            main.setPacmanScore(main.getPacmanScore() + 10)
        elif maze[main.getPacmanY()][main.getPacmanX()] == 2:
            main.setPacmanMode("KILL")
            main.setPacmanScore(main.getPacmanScore() + 50)
            kill_mode_timer = pygame.time.get_ticks() + 10000  # Set timer for 10 seconds
            maze[main.getPacmanY()][main.getPacmanX()] = 3

        # Move the ghosts
        main.ghosts[0][0], main.ghosts[0][1] = main.move_ghost((main.ghosts[0][0], main.ghosts[0][1]), (main.getPacmanY(), main.getPacmanX()), main.ghosts[0][3], maze, 0)
        main.ghosts[1][0], main.ghosts[1][1] = main.move_ghost((main.ghosts[1][0], main.ghosts[1][1]), (main.getPacmanY(), main.getPacmanX()), main.ghosts[1][3], maze, 1)
        main.ghosts[2][0], main.ghosts[2][1] = main.move_ghost((main.ghosts[2][0], main.ghosts[2][1]), (main.getPacmanY(), main.getPacmanX()), main.ghosts[2][3], maze, 2)
        main.ghosts[3][0], main.ghosts[3][1] = main.move_ghost((main.ghosts[3][0], main.ghosts[3][1]), (main.getPacmanY(), main.getPacmanX()), main.ghosts[3][3], maze, 3)

        # Check for collisions with ghosts when in KILL mode
        if main.pacmanmode == "KILL":
            pacman_x = main.getPacmanX()
            pacman_y = main.getPacmanY()
            pacman_pos = (pacman_y, pacman_x)
            main.setGhostState(screen, "VULNERABLE")
            main.killGhost()
            # Check if the timer has expired to switch back to normal mode
            if pygame.time.get_ticks() > kill_mode_timer:
                main.setPacmanMode("normal")
            
        if main.pacmanmode == "normal":
            pacman_x = main.getPacmanX()
            pacman_y = main.getPacmanY()
            pacman_pos = (pacman_y, pacman_x)
            main.setGhostState(screen, "normal")
            if pacman_pos == (main.ghosts[0][0], main.ghosts[0][1]) or pacman_pos == (main.ghosts[1][0], main.ghosts[1][1]) or pacman_pos == (main.ghosts[2][0], main.ghosts[2][1]) or pacman_pos == (main.ghosts[3][0], main.ghosts[3][1]):
                main.setPacmanX(1)
                main.setPacmanY(1)
                main.setGhostPos("RED", 10, 8) #(9 8) (9 10) (8 9) (10 9)
                main.setGhostPos("CYAN", 8, 10)
                main.setGhostPos("PINK", 7, 9)
                main.setGhostPos("ORANGE", 11, 9)
                main.pacman_lives -= 1
                if main.pacman_lives < 0:
                    running = False

        for row in range(len(main.getMazeDesign("Level1"))-1):
            for col in range(len(main.getMazeDesign("Level1")[0])-1):
                if main.getMazeDesign("Level1")[row][col] == 2 or main.getMazeDesign("Level1")[row][col] == 0 or main.getMazeDesign("Level1")[row][col] == 3:
                    main.mazePotZeroCount += 1
                if maze[row][col] == 3:
                    main.mazeZeroCount += 1
        if main.mazePotZeroCount > main.mazeZeroCount: 
            main.draw_maze(maze)
            print(main.mazePotZeroCount, main.mazeZeroCount, main.mazeLevel)
            main.mazePotZeroCount, main.mazeZeroCount = 0, 0
    
            
        elif main.mazePotZeroCount == main.mazeZeroCount:
            print("Level2")
            maze = main.getMazeDesign("Level2")
            main.draw_maze(maze)
            mazeZeroCount = 0
            main.setPacmanX(1)
            main.setPacmanY(1)
            main.setGhostPos("RED", 10, 8) #(9 8) (9 10) (8 9) (10 9)
            main.setGhostPos("CYAN", 8, 10)
            main.setGhostPos("PINK", 7, 9)
            main.setGhostPos("ORANGE", 11, 9)
            main.mazeLevel += 1
        if main.mazeLevel > 2:
            running = False
        
        # print(mazePotZeroCount, mazeZeroCount, level)
        mazeZeroCount = 0
        mazePotZeroCount = 0
        # Redraw the screen

        # sets maze level and draws maze
        main.draw_pacman(screen, pacman_x, pacman_y)  # Ensure Pac-Man is drawn after updating position
        main.draw_ghosts(main.ghosts, screen)
        main.draw_lives(screen)  # Draw Pac-Man's lives last to ensure they are on top
        main.draw_score(screen, maze)


        pygame.display.flip()

        clock.tick(10)

if __name__ == "__main__":
    pacman_main()
