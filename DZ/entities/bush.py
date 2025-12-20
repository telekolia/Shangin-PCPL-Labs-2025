from components import Position, Renderable, Plant
import random

growth_stage_texture_names = ['bush', 'berry_bush']

def create_bush(x, y):
    return {
        'id': f'bush_{x}_{y}',
        'type': 'bush',
        'Position': Position(x, y),
        'Renderable': Renderable('bush', 1),
        'Plant': Plant(20, is_mature=False),
    }

def generate_bushes(count, map, entities):
    planted_bushes = 0
    while planted_bushes < count:
        x = random.randint(0, len(map)-1)
        y = random.randint(0, len(map)-1)

        tile = map[x][y]
        if tile.type == "g":
            bush = create_bush(x, y)
            entities.append(bush)
            planted_bushes += 1
