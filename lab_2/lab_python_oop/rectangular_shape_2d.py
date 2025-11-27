from lab_python_oop.shape_2d import Shape2D
from lab_python_oop.color_unit import ColorUnit
from colorama import Fore, Style

class RectangularShape2D(Shape2D):
    def __init__(self, width, height, color):
        self._shape_type = "Прямоугольник"
        self._width = width
        self._height = height
        self._color = ColorUnit(color)

    @property
    def shape_type(self):
        return self._shape_type

    @property
    def area(self):
        return self._width * self._height

    def __repr__(self):
        return '{name}: ширина: {width}, высота: {height}, цвет: {color}'.format(
            name = self.shape_type,
            width = self._width,
            height = self._height,
            color = f"{self._color.get_value()}{self._color.color_name}{Style.RESET_ALL}"
        )

    # def draw(self):
    #     if self._height == self._width:
    #         letter = "S"
    #     else:
    #         letter = "R"

    #     for i in range(self._height):
    #         line = letter * self._width
    #         print(Back.RED + line)
