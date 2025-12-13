import pygame
from tile import Tile
from world import World, map_size

pygame.init()

window = pygame.display.set_mode((map_size * 64, map_size * 64))

world = World()
world.cout()

running = True
while running:

    # Handle input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                break

    # Render
    world.draw(window)
    pygame.display.update()

pygame.quit()
