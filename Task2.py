# Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
# (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
from os import chdir
from pathlib import Path
from string import ascii_letters
from random import randint, choices, randbytes


def new_create_file(extension: str, min_len_name: int = 6, max_len_name: int = 30,
                min_size_file: int = 256, max_size_file: int = 4096, amount_file: int = 42) -> None:
    for _ in range(amount_file):
        print(Path.cwd())
        while True:
            len_name = randint(min_len_name, max_len_name)
            file_name = ''.join(choices(ascii_letters, k=len_name)) + extension
            if not Path(f'{file_name}.{extension}').is_file():
                break
        size = randint(min_size_file, max_size_file)
        with open(f'{file_name}.{extension}', 'wb') as f:
            f.write(randbytes(size))


def new_gen_files(path: str | Path, **kwargs) -> None:
    if isinstance(path, str):
        path = Path(path)
    if not path.is_dir():
        path.mkdir(parents=True)
    chdir(path)
    for extension, amount_file in kwargs.items():
        new_create_file(extension=extension, amount_file=amount_file, min_len_name=1, max_len_name=1)


if __name__ == '__main__':
    new_gen_files('C:\MySchool\Python_New\Home Work\HW7', bin=2, jpg=1)