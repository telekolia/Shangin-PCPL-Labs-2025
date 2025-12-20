import pygame
from world import World, map_size
from textures import TextureManager

pygame.init()

window = pygame.display.set_mode((map_size * 64, map_size * 64))

clock = pygame.time.Clock()
turn_timer = 0
turn_delay = 0.5  # секунд между ходами

texture_manager = TextureManager()
texture_manager.load_directory('res')

world = World()
world.cout()

running = True
while running:
    dt = clock.tick(60) / 1000.0

    # Handle input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                break

    # Update
    turn_timer += dt
    if turn_timer >= turn_delay:
        world.update()
        turn_timer = 0

    # Render
    world.draw(texture_manager, window)
    pygame.display.update()

pygame.quit()
