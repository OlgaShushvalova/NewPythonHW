class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return f'Имя животного - {self.name}'

    def get_age(self):
        return f'Возраст животного = {self.age}'

    def __str__(self):
        return f'Имя = {self.name}, Возраст = {self.age}'


class Birds(Animal):
    def __init__(self, name, age, wingspan):
        super().__init__(name, age)
        self.wingspan = wingspan

    def get_wingspan(self):
        return f'Уникальное свойство - размах крыльев {self.wingspan}см.'

    def __str__(self):
        return f'Имя - {self.name}, Возраст - {self.age}, Уникальное свойство - размах крыльев {self.wingspan}см.'


class Fish(Animal):
    def __init__(self, name, age, depth):
        super().__init__(name, age)
        self.depth = depth

    def get_depth(self):
        return f'Уникальное свойство - обитает на глубине {self.depth}м.'

    def __str__(self):
        return f'Имя - {self.name}, Возраст - {self.age}, Уникальное свойство - обитает на глубине {self.depth}м.'


class Marsupials(Animal):
    def __init__(self, name, age, length):
        super().__init__(name, age)
        self.length = length

    def get_length(self):
        return f'Уникальное свойство - прыгает в длину на {self.length}м.'

    def __str__(self):
        return f'Имя - {self.name}, Возраст - {self.age}, Уникальное свойство - прыгает в длину на {self.length}м.'


bird = Birds('Сокол', 3, 80)
# print(bird.get_name())
# print(bird.get_age())
# print(bird.get_wingspan())

fish = Fish('Рыба-дракон', 2, 600)
# print(fish.get_name())
# print(fish.get_age())
# print(fish.get_depth())

marsupial = Marsupials('Кенгуру', 10, 12)
# print(marsupial.get_name())
# print(marsupial.get_age())
# print(marsupial.get_length())


