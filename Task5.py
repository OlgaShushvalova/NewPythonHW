# Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.

from Task1 import create_file, gen_files
from Task2 import new_create_file, new_gen_files
from Task3 import sort_files
from Task4 import rename_files


__all__ = ['create_file', 'gen_files', 'new_create_file', 'new_gen_files', 'sort_files', 'rename_files']