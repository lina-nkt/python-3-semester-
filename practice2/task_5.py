import random

def divide_by_random_numbers():
    try:
        random_number = random.randint(0, 1)

        result = 10 / random_number

        print(f"Результат: {result}")

    except ZeroDivisionError:
        print("Деление на 0")


divide_by_random_numbers()