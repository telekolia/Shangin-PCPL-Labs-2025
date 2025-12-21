import pygame
from world import World, map_size
from textures import TextureManager
from interface.hud import HUD

pygame.init()

window = pygame.display.set_mode((map_size * 64, map_size * 64))
pygame.display.set_caption("Симуляция жизни")

hud = HUD(64)
show_stats = True
show_hud = True

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
            # Показать/скрыть статистику
            elif event.key == pygame.K_s:
                show_stats = not show_stats
                print("Статистика " + ("вкл" if show_stats else "выкл"))

            # Показать/скрыть HUD
            elif event.key == pygame.K_h:
                show_hud = not show_hud
                print("HUD " + ("вкл" if show_hud else "выкл"))

    # Update
    turn_timer += dt
    if turn_timer >= turn_delay:
        world.update()
        turn_timer = 0

    # Render
    world.draw(window, texture_manager)

    # 2. Рисуем HUD поверх сущностей
    if show_hud:
        hud.draw(window, world.entities)

    # 3. Рисуем статистику в углу
    if show_stats:
        hud.draw_stats(window, world.entities, 10, 10)

    pygame.display.update()

pygame.quit()
