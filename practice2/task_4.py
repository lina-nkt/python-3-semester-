def create_employee_database():
    database = {}

    while True:
        fio = input("Введите ФИО работника (или введите 'q' для завершения): ")
        if fio == 'q':
            break

        age = int(input("Введите возраст работника: "))
        position = input("Введите должность работника: ")
        desk_number = input("Введите номер рабочего места работника: ")
        access_to_secret = input("Есть ли у работника доступ к тайне (да/нет): ")

        employee = {
            'возраст': age,
            'должность': position,
            'номер рабочего места': desk_number,
            'наличие доступа к тайне': access_to_secret
        }

        database[fio] = employee

    return database


employee_database = create_employee_database()

print("\nБаза данных работников:\n")
for fio, employee in employee_database.items():
    print(f"ФИО: {fio}")
    print(f"Возраст: {employee['возраст']}")
    print(f"Должность: {employee['должность']}")
    print(f"Номер рабочего места: {employee['номер рабочего места']}")
    print(f"Наличие доступа к тайне: {employee['наличие доступа к тайне']}")
    print()