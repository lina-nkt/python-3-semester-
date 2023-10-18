def calculator():
    while True:
        print("Выберите операцию:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Возведение в степень")
        print("6. Остаток от деления")
        print("7. Извлечение корня заданной степени")
        print("8. Выход\n")

        choice = int(input("Введите номер операции: "))

        if choice == 8:
            print("\nРабота завершена!")
            break

        if choice in range(1, 8):
            try:
                num1 = float(input("Введите первое число: "))
                num2 = float(input("Введите второе число: "))

                if choice == 1:
                    result = num1 + num2
                elif choice == 2:
                    result = num1 - num2
                elif choice == 3:
                    result = num1 * num2
                elif choice == 4:
                    if num2 != 0:
                        result = num1 / num2
                    else:
                        print("\n!!Ошибка при делении на ноль!!\n")
                        continue
                elif choice == 5:
                    result = num1 ** num2
                elif choice == 6:
                    result = num1 % num2
                elif choice == 7:
                    result = num1 ** (1/num2)

                print("\nРезультат: ", result, "\n")
            except ValueError:
                print("\n!!Некорректные данные!!")
        else:
            print("\n!!Такой операции не существует!!")


calculator()