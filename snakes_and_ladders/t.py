
import os
import pygame


# Initialize pygame
pygame.init()

# Your dictionary
data = {"Settings": {"Players": {"cat": ["df","red","pygame.image.load(os.path.join(\"assets\", \"cat_red.png\"))"],"dog": ["ghfd","red","pygame.image.load(os.path.join(\"assets\", \"dog_red.png\"))"]},"Total_players": 2}}

# Extract the string for the 'cat' player
cat_image_code = data["Settings"]["Players"]["cat"][2]

# Define the variable directly in the global scope
exec(f"cat_image = {cat_image_code}")

# Set up the display
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Display Cat Image")

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with white color
    screen.fill((255, 255, 255))

    # Blit the cat image at position (100, 100)
    screen.blit(cat_image, (100, 100))

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()