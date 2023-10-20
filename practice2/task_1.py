def calculate_coordinate(t, xo, v, a):
    x = xo + v * t + (a * (t ** 2)) / 2
    return x


t = float(input("Введите время (t): "))
xo = float(input("Введите начальную координату (xo): "))
v = float(input("Введите скорость (v): "))
a = float(input("Введите ускорение (a): "))
coordinate = calculate_coordinate(t=t, xo=xo, v=v, a=a)
print(coordinate)