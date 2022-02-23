proceed = int(input("Введите выручку\n"))

costs = int(input("Введите издержки\n"))

if proceed > costs:
    print("выручка больше издержек")
    profit = proceed / costs
    print(f"Прибыль равна {profit}")
    number_of_workers = int(input("Введите количество работников\n"))
    average_profit = proceed / number_of_workers
    print(f'Средняя выручка на сотрудника равна {average_profit}')
elif proceed == costs:
    print("выручка равна издержкам")
else:
    print("выручка меньше издержек")
