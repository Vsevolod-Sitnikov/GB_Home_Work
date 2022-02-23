start_distance = int(input("Введите начальное количество километров\n"))

end_distance = int(input("Введите необходимое количество километров\n"))

days = int(1)

while start_distance < end_distance:
    start_distance *= 1.1
    days += 1

print(f"Необходимое количество дней равно {days}")
