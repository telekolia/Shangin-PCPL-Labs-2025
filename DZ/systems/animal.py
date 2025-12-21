import random
from math import sqrt

class AnimalSystem():
    targets = {}

    @staticmethod
    def update(entities, map):
        for entity in entities:
            if 'Animal' in entity:
                if 'Health' in entity:
                    health = entity['Health']

                if 'Health' not in entity or health.is_alive:
                    animal = entity['Animal']
                    if animal.type == "herbivore":
                        AnimalSystem._update_herbivore(entity, entities, map)
                # elif animal.type == "predator":
                #     AnimalSystem._update_predator(entity, entities, map)

    @staticmethod
    def _update_herbivore(entity, entities, map):
        pos = entity['Position']
        hunger = entity['Hunger']
        state = entity['state']
        target_id = entity['target_id']

        AnimalSystem._update_state(entity)

        AnimalSystem._define_target(entity, entities)

        AnimalSystem._action(entity, entities)

        if (hunger and hunger.current_satiety > hunger.max_satiety * 0.8 and 'State' in entity and entity['State'].state != "pregnant"):
            partner = AnimalSystem._find_partner(entity, entities)
            if partner:
                AnimalSystem._breed(entity, partner, entities)

    @staticmethod
    def _update_state(entity):
        hunger = entity['Hunger']
        state = entity['state']

        if hunger.current_satiety > hunger.max_satiety * 0.7:
            state = "chill"
        elif hunger.current_satiety <= hunger.max_satiety * 0.7:
            state = "hungry"

    @classmethod
    def _define_target(entity, entities):
        state = entity['state']
        target_id = entity['target_id']

        if state == "hungry" and target_id not in AnimalSystem.targets:
            target = AnimalSystem._find_food(entity, entities, map)
            target_id = id(target)
            AnimalSystem.targets[target_id] = target
        elif state == "chill":
            target_id = "nope"

    @classmethod
    def _action(entity, entities):
        pos = entity['Position']
        state = entity['state']
        target_id = entity['target_id']

        if target_id in AnimalSystem.targets:
            target = AnimalSystem.targets[target_id]
            AnimalSystem._move_towards(entity, entities, target['Position'], map)

        if state == "hungry" and AnimalSystem._distance(pos, target['Position']) <= 1:
            AnimalSystem._eat_food(entity, target['Position'], entities)
            del AnimalSystem.targets[target_id]

        if state == "chill":
            if random.random() < 0.3:
                AnimalSystem._random_move(entity, map)

    @staticmethod
    def _find_food(entity, entities, map):
        """Найти ближайшую еду для животного"""
        pos = entity['Position']
        animal = entity['Animal']

        nearest_food = None
        min_distance = float('inf')

        # Для травоядных ищем растения с ягодами
        if animal.type == "herbivore":
            for other in entities:
                if ('Plant' in other and other['Plant'].is_mature and
                    'Position' in other):
                    food_pos = other['Position']
                    dist = AnimalSystem._distance(pos, food_pos)

                    # Проверяем, что путь свободен
                    if (dist < min_distance and
                        AnimalSystem._is_path_clear(pos, food_pos, map, entities)):
                        min_distance = dist
                        nearest_food = food_pos

        return nearest_food

    @staticmethod
    def _move_towards(entity, entities, target, map):
        pos = entity['Position']

        # Вычисляем направление
        dx = 0
        dy = 0

        if pos.x < target.x:
            dx = 1
        elif pos.x > target.x:
            dx = -1

        if pos.y < target.y:
            dy = 1
        elif pos.y > target.y:
            dy = -1

        # Пытаемся двигаться по диагонали, если возможно
        new_x = pos.x
        new_y = pos.y

        if dx != 0 and AnimalSystem._can_move_to(pos.x + dx, pos.y, map, entities):
            new_x = pos.x + dx
        if dy != 0 and AnimalSystem._can_move_to(pos.x, pos.y + dy, map, entities):
            new_y = pos.y + dy

        # Если не удалось по диагонали, пробуем одно направление
        if new_x == pos.x and new_y == pos.y:
            if dx != 0 and AnimalSystem._can_move_to(pos.x + dx, pos.y, map, entities):
                new_x = pos.x + dx
            elif dy != 0 and AnimalSystem._can_move_to(pos.x, pos.y + dy, map, entities):
                new_y = pos.y + dy

        # Обновляем позицию
        if new_x != pos.x or new_y != pos.y:
            pos.x = new_x
            pos.y = new_y

            # Тратим энергию на движение
            if 'Hunger' in entity:
                entity['Hunger'].current_satiety -= 0.1

    @staticmethod
    def _random_move(entity, map):
        """Случайное блуждание"""
        pos = entity['Position']
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        random.shuffle(directions)

        for dx, dy in directions:
            new_x, new_y = pos.x + dx, pos.y + dy

            if AnimalSystem._can_move_to(new_x, new_y, map, [entity]):
                pos.x = new_x
                pos.y = new_y

                # Тратим энергию
                if 'Hunger' in entity:
                    entity['Hunger'].current_satiety -= 0.05
                break

    @staticmethod
    def _eat_food(entity, food_pos, entities):
        """Съесть еду"""
        # Находим растение по позиции
        for plant in entities:
            if ('Plant' in plant and 'Position' in plant and
                plant['Position'].x == food_pos.x and
                plant['Position'].y == food_pos.y):

                # Овца ест
                if 'Hunger' in entity:
                    hunger = entity['Hunger']
                    hunger.current_satiety = min(
                        hunger.max_satiety,
                        hunger.current_satiety + 20
                    )
                    print(f"🐑 Овца съела ягоды в ({food_pos.x},{food_pos.y})")

                # Ягоды исчезают (но куст остается)
                plant['Plant'].is_mature = False
                plant['Plant'].growth_stage = 0
                plant['Renderable'].texture_name = plant['Plant'].growth_stage_texture_names[0]
                break

    @staticmethod
    def _find_partner(entity, entities):
        """Найти партнера для размножения"""
        pos = entity['Position']

        for other in entities:
            if (other is not entity and
                'Animal' in other and
                other['Animal'].type == "herbivore" and
                'Health' in other and other['Health'].is_alive and
                'State' in other and other['State'].state != "pregnant"):

                other_pos = other['Position']
                dist = AnimalSystem._distance(pos, other_pos)

                if dist <= 2:  # Рядом
                    return other
        return None

    @staticmethod
    def _breed(entity, partner, entities):
        """Размножение"""
        # Устанавливаем состояние беременности
        entity['State'].state = "pregnant"
        partner['State'].state = "pregnant"

        # Уменьшаем сытость
        if 'Hunger' in entity:
            entity['Hunger'].current_satiety -= 15
        if 'Hunger' in partner:
            partner['Hunger'].current_satiety -= 15

        print(f"🐑 Овцы в ({entity['Position'].x},{entity['Position'].y}) размножаются!")

    @staticmethod
    def _distance(pos1, pos2):
        """Расстояние между двумя позициями"""
        return sqrt((pos1.x - pos2.x)**2 + (pos1.y - pos2.y)**2)

    @staticmethod
    def _can_move_to(x, y, map, entities):
        """Можно ли переместиться в клетку"""
        # Проверяем границы
        if x < 0 or y < 0 or x >= len(map) or y >= len(map[0]):
            return False

        # Проверяем тайл
        if not map[x][y].passable:
            return False

        # Проверяем других существ в клетке
        for other in entities:
            if 'Position' in other:
                if (other['Position'].x == x and
                    other['Position'].y == y and
                    other.get('type') != 'bush'):
                    return False

        return True

    @staticmethod
    def _is_path_clear(start, end, map, entities):
        """Проверка, свободен ли путь (упрощенная)"""
        # Простая проверка - только если клетки рядом
        return AnimalSystem._distance(start, end) <= 1.5

    @staticmethod
    def give_birth(entity, entities, animal_creation_func):
        """Рождение детеныша"""
        if ('State' in entity and entity['State'].state == "pregnant" and
            'Animal' in entity and entity['Animal'].max_amount_of_children > 0):

            pos = entity['Position']

            # Ищем свободное место рядом для детеныша
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            random.shuffle(directions)

            for dx, dy in directions:
                new_x, new_y = pos.x + dx, pos.y + dy

                if AnimalSystem._can_move_to(new_x, new_y, map, entities):
                    # Создаем детеныша
                    baby = animal_creation_func(new_x, new_y, is_baby=True)
                    entities.append(baby)

                    # Сбрасываем состояние
                    entity['State'].state = "normal"
                    entity['Animal'].max_amount_of_children -= 1

                    print(f"🐑 Родился ягненок в ({new_x},{new_y})!")
                    break
