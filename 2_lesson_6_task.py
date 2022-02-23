#Номер продукта в списке продуктов
count_products = 1

#Флаг для проверки необходимости повторного ввода товара
input_flag = True

#заранее заданная переменная с типом список
products = []

#цикл для заполнения списка товаров
while input_flag == True:
    name_product = input("Введите наименование товара\n")
    price_product = int(input("Введите цену товара\n"))
    count_product = int(input("Введите количество товара\n"))
    unit_products = input("Введите единицу измерения товара\n")
    products.append([count_products, {
        'Наименование': name_product,
        'цена': price_product,
        'количество': count_product,
        'ед':unit_products
    }])
    count_products += 1
    cont = input("Продолжаем вводить товар? (y/n)\n")
    if cont != 'Y' or 'y' or 'yes':
        input_flag = False

dict_analitic = {'Наименование': [], 'цена': [], 'количество': [], 'ед': []}

for elem in products:
    dict_analitic.get('Наименование').append(elem[1].get('Наименование'))
    dict_analitic.get('цена').append(elem[1].get('цена'))
    dict_analitic.get('количество').append(elem[1].get('количество'))
    dict_analitic.get('ед').append(elem[1].get('ед'))

for key, value in dict_analitic.items():
    dict_analitic[key] = list(set(value))

print(dict_analitic)
