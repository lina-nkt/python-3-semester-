import random

def generate_character():
    names = ["Саша", "Даня", "Екатерина", "Мария", "Артур", "Николай"]
    name = random.choice(names)

    age = random.randint(18, 60)

    classes = ["Воин", "Маг", "Лучник", "Вор"]
    character_class = random.choice(classes)

    parameters = {
        "Сила": random.randint(1, 10),
        "Ловкость": random.randint(1, 10),
        "Интеллект": random.randint(1, 10),
        "Выносливость": random.randint(1, 10),
        "Обаяние": random.randint(1, 10),
        "Мудрость": random.randint(1, 10)
    }

    characteristics = {
        "Сила": random.randint(1, 10),
        "Восприятие": random.randint(1, 10),
        "Выносливость": random.randint(1, 10),
        "Харизма": random.randint(1, 10),
        "Интеллект": random.randint(1, 10),
        "Ловкость": random.randint(1, 10),
        "Удача": random.randint(1, 10)
    }

    skills = ["Стелс", "Взлом", "Выживание", "Магия", "Стрельба"]
    num_skills = random.randint(1, 5)
    character_skills = random.sample(skills, num_skills)

    print("Имя:", name)
    print("Возраст:", age)
    print("Класс:", character_class)
    print("Параметры:")
    for parameter, value in parameters.items():
        print("    ", parameter, ":", value)
    print("Характеристики:")
    for characteristic, value in characteristics.items():
        print("    ", characteristic, ":", value)
    print("Навыки/особенности:")
    for skill in character_skills:
        print("    ", skill)


generate_character()