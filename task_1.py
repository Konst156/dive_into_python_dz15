# Возьмите любые 1-3 задания из прошлых домашних заданий. Добавьте к ним логирование ошибок и полезной информации.
# Также реализуйте возможность запуска из командной строки с передачей параметров

import logging
import sys


class InvalidLengthError(ValueError):
    def __init__(self, length):
        super().__init__(f"Недопустимая длина: {length}")


class InvalidWidthError(ValueError):
    def __init__(self, width):
        super().__init__(f"Недопустимая ширина: {width}")


class Rectangle:
    def __init__(self, length, width=None):
        self._length = None
        self._width = None
        self.length = length
        self.width = width if width is not None else length

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        if value < 0:
            logging.error(f"Недопустимая длина: {value}")
            raise InvalidLengthError(value)
        self._length = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value < 0:
            logging.error(f"Недопустимая ширина: {value}")
            raise InvalidWidthError(value)
        self._width = value

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width


if __name__ == "__main__":
    # Настройка логирования
    logging.basicConfig(filename="rectangle.log", level=logging.ERROR)

    try:
        # Получение параметров из командной строки
        length = float(sys.argv[1])
        width = float(sys.argv[2]) if len(sys.argv) > 2 else None

        # Создание экземпляра прямоугольника
        rectangle = Rectangle(length, width)

        # Вывод результатов
        print(f"Периметр: {rectangle.perimeter()}")
        print(f"Площадь: {rectangle.area()}")

    except (IndexError, ValueError) as e:
        logging.error(f"Ошибка ввода параметров: {e}")
        print("Ошибка ввода параметров. Проверьте правильность введенных значений.")
