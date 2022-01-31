from functools import reduce


def mul_func(numb_1, numb_2):
    return numb_1 * numb_2


list_new = [i for i in range(100, 1001) if i % 2 == 0]


r = reduce(mul_func, list_new)
print(r)

#Либо через lambda функцию

r = reduce(lambda numb_1, numb_2: numb_1 * numb_2, list_new)

print(r)
