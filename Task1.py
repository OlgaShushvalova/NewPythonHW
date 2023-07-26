# 1. Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.

# 2. Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.


from string import ascii_letters
from random import randint, choices, randbytes


def create_file(extension: str, min_len_name: int = 6, max_len_name: int = 30,
                min_size_file: int = 256, max_size_file: int = 4096, amount_file: int = 42) -> None:
    for _ in range(amount_file):
        len_name = randint(min_len_name, max_len_name)
        file_name = ''.join(choices(ascii_letters, k=len_name)) + extension
        size = randint(min_size_file, max_size_file)
        with open(file_name, 'wb') as f:
            f.write(randbytes(size))


if __name__ == '__main__':
    create_file('txt', amount_file=1)


def gen_files(**kwargs) -> None:

    for extension, amount_file in kwargs.items():
        create_file(extension=extension, amount_file=amount_file)


if __name__ == '__main__':
    gen_files(bin=2, jpg=1)




