def calculate_materials(order):
    materials = {
        'брус 50 3м': 0,
        'брус 100 6м': 0,
        'доска 25 6м': 0,
        'доска 50 6м': 0,
        'фанера 1,5x1,5 м': 0
    }

    for item in order:
        if item == 'брус 50 2м':
            materials['брус 50 3м'] += 1
        elif item == 'брус 50 1,5м':
            materials['брус 50 3м'] += 0.5
        elif item == 'брус 100 6м':
            materials['брус 100 6м'] += 1
        elif item == 'доска 25 6м':
            materials['доска 25 6м'] += 1
        elif item == 'доска 50 6м':
            materials['доска 50 6м'] += 1
        elif item == 'фанера 1,5x1,5 м':
            materials['фанера 1,5x1,5 м'] += 1

    for material, quantity in materials.items():
        if quantity > 0:
            print(f"{int(quantity)}x {material}")

order = ['брус 50 2м', 'брус 50 2м', 'брус 50 2м', 'брус 50 1,5м', 'брус 50 1,5м', 'брус 50 1,5м', 'брус 50 1,5м']
calculate_materials(order)