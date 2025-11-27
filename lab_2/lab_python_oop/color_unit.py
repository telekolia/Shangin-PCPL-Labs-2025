from colorama import Fore

class ColorUnit():
    COLOR_MAPPING = {
        "КРАСНЫЙ": Fore.RED,
        "СИНИЙ": Fore.BLUE,
        "ЗЕЛЁНЫЙ": Fore.GREEN,
        "ЖЁЛТЫЙ": Fore.YELLOW,
        "МАГНЕТА": Fore.MAGENTA,
        "ГОЛУБОЙ": Fore.CYAN,
        "БЕЛЫЙ": Fore.WHITE,
        "ЧЁРНЫЙ": Fore.BLACK,
        "СЕРЫЙ": Fore.LIGHTBLACK_EX,
        "ФИОЛЕТОВЫЙ": Fore.MAGENTA,
        "БИРЮЗОВЫЙ": Fore.CYAN,
    }

    def __init__(self, color):
        self._color_name = color
        self._value = self._validate_color(color)

    @property
    def color_name(self):
        return self._color_name

    def _validate_color(self, color):
        if color.upper() in self.COLOR_MAPPING:
            return self.COLOR_MAPPING[color.upper()]
        elif hasattr(Fore, color.upper()):
            return getattr(Fore, color.upper())
        else:
            print(f"Предупреждение: цвет '{color}' не найден. Используется белый цвет.")
            return Fore.WHITE

    def get_value(self):
        return self._value

    def set_value(self, color):
        self._value = self._validate_color(color)
