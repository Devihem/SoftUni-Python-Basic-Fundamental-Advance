import pygame
import sys

# Initialize Pygame
pygame.init()

# Set the dimensions of the game window
width = 800
height = 600

# Create the game window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hello Game")

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the screen with black color
    screen.fill(black)

    # Create a font object
    font = pygame.font.Font(None, 36)

    # Create a text surface
    text_surface = font.render("Hello", True, white)

    # Get the rectangle that encloses the text surface
    text_rect = text_surface.get_rect()

    # Center the text on the screen
    text_rect.center = (width // 2, height // 2)

    # Draw the text surface onto the screen
    screen.blit(text_surface, text_rect)

    # Update the display
    pygame.display.flip()
