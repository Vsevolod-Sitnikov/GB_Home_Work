def int_func(some_word):
    """
    Функция при помощи .upper делает первый символ слова заглавным, остальные символы при помощи .lower делает прописными
    :param some_word: любое слово
    :return: 
    """
    return some_word[0].upper() + some_word[1:].lower()

def int_func_1(some_word):
    """
    При помощи .capitalize первый символ становится заглавным, остальные прописными
    :param some_word: любое слово
    :return: 
    """
    return some_word.capitalize()

var_word = input("Введите любое слово или предложение в нижнем регистре: ")

#Для наглядности отображения работы функций вызываю сразу обе
for elem in var_word.split(' '):
    print(int_func(elem))
    print(int_func_1(elem))
