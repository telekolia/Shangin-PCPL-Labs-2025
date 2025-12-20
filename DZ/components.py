class Position():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Renderable():
    def __init__(self, texture_name, layer = 0):
        self.texture_name = texture_name
        self.layer = layer


class Plant:
    def __init__(self, growrh_time, growth_stage_texture_names, is_mature=False):
        self.is_mature = is_mature
        self.growth_stage = 0
        self.growth_time = growrh_time
        self.growth_stage_texture_names = [row[:] for row in growth_stage_texture_names]
