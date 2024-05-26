import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Creative Coding with Pygame')

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255)]

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Randomly draw shapes
    for _ in range(10):
        color = random.choice(colors)
        shape = random.choice(['circle', 'rect'])
        if shape == 'circle':
            pygame.draw.circle(screen, color, (random.randint(0, width), random.randint(0, height)), random.randint(10, 100))
        else:
            pygame.draw.rect(screen, color, (random.randint(0, width), random.randint(0, height), random.randint(50, 200), random.randint(50, 200)))

    pygame.display.flip()
    pygame.time.wait(100)
    screen.fill(black)

pygame.quit()
sys.exit()

