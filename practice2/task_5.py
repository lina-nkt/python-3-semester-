import random

def divide_by_random_numbers():
    try:
        random_number = random.randint(0, 1)  # Генерация случайного числа (0 или 1)

        result = 10 / random_number  # Деление числа 10 на случайное число

        print(f"Результат: {result}")

    except ZeroDivisionError:
        print("Деление на 0")


divide_by_random_numbers()