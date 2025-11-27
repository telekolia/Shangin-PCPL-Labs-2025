from lab_python_oop.__init__ import RectangularShape2D, SqareShape2D, CircleShape2D
from colorama import init

def main():
    rectangle = RectangularShape2D(21, 21, "Синий")
    print(rectangle)
    circle = CircleShape2D(21, "Зелёный")
    print(circle)
    sqare = SqareShape2D(21, "красный")
    print(sqare)

if __name__ == "__main__":
    init(autoreset=True)
    main()
