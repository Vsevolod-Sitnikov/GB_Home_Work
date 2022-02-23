second = int(input('Введите количество секунд\n'))

hours = second // 3600

second = second - (hours * 3600)

minutes = second // 60

second = second - (minutes * 60)

if hours < 10:
    hours = "0" + str(hours)

if minutes < 10:
    minutes = "0" + str(minutes)

if second < 10:
    second = "0" + str(second)

print(f"{hours}:{minutes}:{second}")
