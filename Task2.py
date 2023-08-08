# Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать.

import time


class MyString(str):
    """Класс где доступны все возможности str"""

    def __new__(cls, text: str, author: str):
        """Добавляет новые параметра = автор и время создания в класс str"""
        instance = super().__new__(cls, text)
        instance.author = author
        instance.time = time.time()
        return instance

    def __str__(self) -> str:
        return f"Экземпляр класса MyString добавляет навые параметры author и creation time в класс str"

    def __repr__(self) -> str:
        return f"MyString({self.author=})"


class Archive:
    """Класс хранит пару - число и строку."""
    _archive = None

    def __init__(self, number: int, text: str):
        """Добавляет новые параметры"""
        self.number = number
        self.text = text

    def __new__(cls, *args, **kwargs):
        """Добавляет ранее созданные параметры в архив"""
        if cls._archive is None:
            cls._archive = super().__new__(cls)
            cls._archive.num = []
            cls._archive.val = []
        else:
            cls._archive.num.append(cls._archive.number)
            cls._archive.val.append(cls._archive.text)
        return cls._archive

    def __str__(self) -> str:
        return f'Экземпляр класса Archive с переменными число {self.number} и строка {self.text}'

    def __repr__(self) -> str:
        return f'Archive ({self.number=}, {self.text=})'


class Rectangle:
    """Класс вычисляет периметр и площадь прямоугольника, а также складывает и вычитает периметры"""

    def __init__(self, side_a, side_b=None):
        """Добавляет параметр side_a и side_b, если добавляется только одит параметр,
            считаем, что side_a и side_b равны"""
        self.a = side_a
        if side_b is None:
            self.b = side_a
        else:
            self.b = side_b

    def rectangle_long(self):
        """Вычисляем периметр прямоугольника"""
        long = (self.a + self.b) * 2
        return long

    def rectangle_square(self):
        """Вычисляем площадь прямоугольника"""
        square = self.a * self.b
        return square

    def __add__(self, other):
        """Складываем периметры прямоугольников"""
        a = self.a + other.a
        b = self.b + other.b
        return Rectangle(a, b)

    def __sub__(self, other):
        """Вычитаем периметры прямоугольников"""
        if self.rectangle_long() < other.rectangle_long():
            self, other = other, self
        a = self.a - other.a
        b = self.b - other.b
        return Rectangle(a, b)

    def __str__(self) -> str:
        return f"Экземпляр класса Rectangle с переменными {self.a} и {self.b}"

    def __repr__(self) -> str:
        return f"Rectangle({self.a=},{self.b=})"


if __name__ == "__main__":
    test = MyString("text text", "aurthor author")
    print(test)
    print(f'{test = }')
    help(MyString)

    test2 = Archive(3, "text text")
    print(test2)
    print(f'{test2 = }')
    help(Archive)

    test3 = Rectangle(20, 4)
    print(test3)
    print(f'{test3 = }')
    help(Rectangle)