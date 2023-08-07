# Доработаем задачи 5-6. Создайте класс-фабрику.
# ○ Класс принимает тип животного (название одного из созданных классов)
# и параметры для этого типа.
# ○ Внутри класса создайте экземпляр на основе переданного типа и
# верните его из класса-фабрики.

from Animal import Animal, Birds, Fish, Marsupials, bird, fish, marsupial


class FactoryAnimal:
    def get_animal_info(self, animal):
        return animal.__str__()


class FactoryClassAnimal:
    def __init__(self, name_class_animal):
        self.name_class_animal = name_class_animal

    def get_new_animal(self, *args):
        return self.name_class_animal(*args)


factory = FactoryAnimal()
print(factory.get_animal_info(bird))
print(factory.get_animal_info(fish))
print(factory.get_animal_info(marsupial))

print('---')


factory_bird = FactoryClassAnimal(Birds)
new_bird = factory_bird.get_new_animal('Кукушка', 5, 30)
print(type(new_bird))
print(new_bird.__str__())

factory_fish = FactoryClassAnimal(Fish)
new_fish = factory_fish.get_new_animal('Окунь', 4, 20)
print(type(new_fish))
print(new_fish.__str__())

factory_marsupial = FactoryClassAnimal(Marsupials)
new_marsupial = factory_marsupial.get_new_animal('Коала', 7, 2)
print(type(new_marsupial))
print(new_marsupial.__str__())

