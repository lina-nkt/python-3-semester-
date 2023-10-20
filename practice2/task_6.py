def write_to_file(text, filename):
    try:
        with open(filename, 'a') as file:
            file.write(text + '\n')

        print(f"Строка успешно записана в файл '{filename}'")

    except IOError:
        print(f"Ошибка при записи в файл '{filename}'")


write_to_file("Привет, мир!", "my_file.txt")