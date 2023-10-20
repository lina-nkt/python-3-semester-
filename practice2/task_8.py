import shutil
import os

def create_file_copy(filename):
    try:
        if os.path.exists(filename):
            file_copy = filename + '.copy'
            shutil.copy2(filename, file_copy)

            print(f"Создана копия файла '{filename}' под именем '{file_copy}'")

            os.remove(filename)
            print("Удален оригинал файла")
        else:
            print(f"Файла '{filename}' нет")

    except IOError:
        print(f"Ошибка при создании копии файла '{filename}'")


create_file_copy("my_file.txt")