def user_info (first_name, last_name, age, city, mail, phone_number):
    """
    Функция возвращает информацию о пользователе
    :param first_name: Имя
    :param last_name: Фамилия
    :param age: возраст
    :param city: город проживания
    :param mail: электронная почта
    :param phone_number: номер телефона
    :return: строка с данными о пользователе
    """
    return str(f'Вас зовут {last_name} {first_name}. Вам {age} лет. Вы живёте в городе {city}. Ваша электронная почта {mail}. Ваш номер телефона {phone_number}')


first_name = input("Введите ваше имя: ")

last_name = input("Введите вашу фамилию: ")

age = input("Введите ваш возраст: ")

city = input("Введите город, в котором вы живёте: ")

mail = input("Введите вашу электронную почту: ")

phone_number = input("Введите ваш номер телефона: ")

print(user_info(first_name, last_name, age, city, mail, phone_number))
