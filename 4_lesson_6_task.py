from itertools import cycle, count
from random import randint

min_numb = input("Введите число, с которого начать генерацию целых положительных чисел: ")

for el in count(int(min_numb)):
    if el > 100:
        break
    print(el)

#Для большей наглядности создается список из 10 элементов, каждый элемент которого умножается на
list_new = [i * randint(-10, 10) for i in range(0, 10)]

print(list_new)

i = 0

for elem in cycle(list_new):
    print(elem)
    i += 1
    if i > 100:
        break
