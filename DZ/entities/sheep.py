import random
from components import Position, Renderable, Health, Hunger, Animal, State

def create_sheep(x, y, is_baby=False):
    """Создать овцу или ягненка"""

    # Текстуры в зависимости от возраста
    if is_baby:
        texture_name = "sheep_baby"
        health = 30.0
        max_children = 0  # Ягнята пока не могут размножаться
    else:
        texture_name = "sheep"
        health = 50.0
        max_children = random.randint(1, 3)  # Взрослые могут иметь потомство

    return {
        'id': f'sheep_{x}_{y}_{random.randint(1000, 9999)}',
        'type': 'sheep',
        'Position': Position(x, y),
        'Renderable': Renderable(texture_name, layer=2),  # Животные поверх растений
        'Health': Health(
            current_hp=health,
            max_hp=health,
            death_texture_name="dead_sheep",
            is_alive=True
        ),
        'Hunger': Hunger(
            current_satiety=random.uniform(30.0, 50.0),
            max_satiety=50.0
        ),
        'Animal': Animal(
            type="herbivore",
            max_amount_of_children=max_children,
            adult_texture_name="sheep",
            baby_texture_name="baby_sheep"
        ),
        'State': State("normal")  # normal, hungry, pregnant, dead
    }

def generate_sheep(map, count, entities):
    """Сгенерировать овец на карте"""
    generated = 0
    map_size = len(map)

    while generated < count:
        x = random.randint(0, map_size - 1)
        y = random.randint(0, map_size - 1)

        # Проверяем, что клетка свободна и проходима
        tile = map[x][y]
        if tile.type == "g":  # Только на траве
            # Проверяем, нет ли уже сущности в этой клетке
            occupied = False
            for entity in entities:
                if ('Position' in entity and
                    entity['Position'].x == x and
                    entity['Position'].y == y and
                    entity.get('type') in ['sheep', 'bush']):
                    occupied = True
                    break

            if not occupied:
                sheep = create_sheep(x, y)
                entities.append(sheep)
                generated += 1
                print(f"🐑 Овца создана в ({x},{y})")
