from module_7_4 import *

import os
import time

# путь к каталогу, кот. нужно обойти ("." - текущая директ.)
directory = "."

# os.walk для обхода каталога
for root, dirs, files in os.walk(directory):
    # пребираем  все файлы в тек. директ.
    for file in files:
        filepath = os.path.join(root, file) # полный путь к файлу
        filetime = os.path.getmtime(filepath) # время последнего изменения файла
        # время в удобный для чтения формат
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath) # размер файла
        parent_dir = os.path.dirname(filepath) # родит. директ. файла

        # вывод инф-и о файле
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, '
              f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')