import random

class GrowthSystem:
    def update(self, entities):
        for entity in entities:
            if 'Plant' in entity:
                plant = entity['Plant']
                stage_duration = plant.growth_time / len(plant.growth_stage_texture_names)

                if not plant.is_mature:
                    plant.growth_stage += random.randint(1, 3)
                    current_stage = plant.growth_stage / stage_duration
                    entity['Renderable'].texture_name = plant.growth_stage_texture_names[current_stage]
                    if plant.berries_timer >= plant.growth_time:
                        plant.is_mature = True
                        print(f"Куст {plant.id} дал ягоды!")
