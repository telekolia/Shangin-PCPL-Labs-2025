from lab_python_oop.shape_2d import Shape2D
from lab_python_oop.color_unit import ColorUnit
from math import pi
from colorama import Back, Style

class CircleShape2D(Shape2D):
    def __init__(self, radius, color):
        self._shape_type = "Круг"
        self._radius = radius
        self._color = ColorUnit(color)

    @property
    def shape_type(self):
        return self._shape_type

    @property
    def area(self):
        return pi * self._radius ** 2

    def __repr__(self):
        return '{name}: радиус: {radius}, площадь: {area}, цвет: {color}'.format(
            name = self.shape_type,
            radius = self._radius,
            area = self.area,
            color = f"{self._color.get_value()}{self._color.color_name}{Style.RESET_ALL}"
        )

    # def draw(self):
    #     for h in range(self._radius):
    #         line = ""
    #         for w in range(self._radius):
    #             if ((w-sqrt(self._radius)) ** 2 + (h-sqrt(self._radius)) ** 2) <= self._radius:
    #                 line += "C"
    #             else:
    #                 line +="\s"
    #         print(Back.RED + line)
