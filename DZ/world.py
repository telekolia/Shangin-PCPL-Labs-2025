from tile import Tile

map_size = 10

default_map = [[Tile("g") for i in range(map_size)] for j in range(map_size)]
for x in range(5, 7):
    for y in range(7, 9):
        default_map[x][y].type = "w"

class World():
    def __init__(self, map = [row[:] for row in default_map]):
        self.map = [row[:] for row in map]


    def draw(self, window):
        for i in range(map_size):
            for j in range(map_size):
                self.map[i][j].draw(window, i*64, j*64)


    def cout(self):
        print("world map:")
        for y in range(map_size):
            for x in range(map_size):
                print(self.map[x][y].type, end=" ")
            print()
