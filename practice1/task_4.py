import time

def timer(hours, minutes, seconds):
    total_seconds = hours * 3600 + minutes * 60 + seconds

    while total_seconds:
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60

        time_str = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
        print(time_str)

        time.sleep(1)
        total_seconds -= 1

    print("Время вышло!")


print("Введите время, на которое поставить таймер в формате чч:мм:сс")
input = input().split(":")
hours, minutes, seconds = int(input[0]), int(input[1]), int(input[2])
timer(hours, minutes, seconds)