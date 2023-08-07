# Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация данных), которые
# вы уже решали. Превратите функции в методы класса, а параметры в свойства. Задачи должны решаться
# через вызов методов экземпляра.

# Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории. Результаты обхода сохраните в
# файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер
# файлов в ней с учётом всех вложенных файлов и директорий.

from working_directory import WorkingDirectory

work_in_directory = WorkingDirectory('Example_file')


work_in_directory.write_json_file('json_file', work_in_directory.file_and_folder_in_directory())
work_in_directory.write_csv_file('csv_file', work_in_directory.file_and_folder_in_directory())
work_in_directory.write_pickle_file('pickle_file', work_in_directory.file_and_folder_in_directory())