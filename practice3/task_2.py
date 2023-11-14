with open('lines.txt', 'w') as file:
    i = 1
    while True:
        print(f"Введите {i} строку. Введите 'стоп', чтобы закончить: ")
        line = input()

        if line.lower() == "стоп":
            break

        file.write(line + '\n')

        i += 1

    print(f"Строки успешно записаны в файл")
