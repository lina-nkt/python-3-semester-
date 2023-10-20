def sum_numbers(number):
    res = 0
    for _ in number:
        res += int(_)
    return res

print("Введите число: ")
input = input()
print(sum_numbers(input))