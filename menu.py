import pygame, pacman
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 485

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pacman Launcher")

# Load the background image
background_image = pygame.image.load('resources/menu.png')

# Fonts
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)

# Menu options
menu_options = ["Start Game", "Quit"]
selected_option = 0

def draw_menu():
    # Fill the screen with the background image
    screen.blit(background_image, (0, 0))

    for i, option in enumerate(menu_options):
        color = WHITE if i == selected_option else (100, 100, 100)
        text = small_font.render(option, True, color)
        screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, 300 + i * 50))

    pygame.display.flip()

def main():
    global selected_option

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(menu_options)
                elif event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(menu_options)
                elif event.key == pygame.K_RETURN:
                    if selected_option == 0:
                        print("Start Game selected")
                        # Add code to start the game
                        pacman.pacman_main()
                        running = False

                    elif selected_option == 1:
                        pygame.quit()
                        sys.exit()

        draw_menu()
        clock.tick(60)

if __name__ == "__main__":
    main()