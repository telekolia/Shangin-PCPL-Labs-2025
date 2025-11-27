from lab_python_oop.rectangular_shape_2d import RectangularShape2D
from colorama import Fore, Style

class SqareShape2D(RectangularShape2D):
    def __init__(self, side_length, color):
        super().__init__(side_length, side_length, color)
        self._shape_type = "Квадрат"
