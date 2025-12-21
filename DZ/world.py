from tile import Tile
from systems.__init__ import RenderSystem, GrowthSystem, HealthSystem, HungerSystem, AnimalSystem
from entities.bush import generate_bushes
from entities.sheep import generate_sheep


map_size = 10

default_map = [[Tile("g") for i in range(map_size)] for j in range(map_size)]
for x in range(5, 7):
    for y in range(7, 9):
        default_map[x][y].type = "w"

default_entities = []
generate_bushes(default_map, 1, default_entities)
generate_sheep(default_map, 1, default_entities)

class World():
    def __init__(self, entities = [row for row in default_entities], map = [row[:] for row in default_map]):
        self.map = [row[:] for row in map]
        self.entities = [row for row in entities]

    def update(self):
        HealthSystem.update(self.entities)
        HungerSystem.update(self.entities)
        AnimalSystem.update(self.entities, self.map)
        GrowthSystem.update(self.entities)

    def draw(self, window, texture_manager):
        for i in range(map_size):
            for j in range(map_size):
                self.map[i][j].draw(window, i*64, j*64)

        RenderSystem.draw(window, self.entities, texture_manager)


    def cout(self):
        print("world map:")
        for y in range(map_size):
            for x in range(map_size):
                print(self.map[x][y].type, end=" ")
            print()
