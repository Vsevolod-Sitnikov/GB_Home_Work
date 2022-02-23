def gen(num):
    for elem in range(1, num+1):
        result = int(1)
        while elem != 0:
            result = result * elem
            elem = elem -1
        yield result


for el in gen(5):
    print(el)
