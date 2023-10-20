def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()

        if content:
            print(f"Содержимое файла '{filename}':")
            print(content)
        else:
            print(f"Файл '{filename}' пуст")

    except FileNotFoundError:
        print(f"Файла '{filename}' нет")


read_file("my_file.txt")