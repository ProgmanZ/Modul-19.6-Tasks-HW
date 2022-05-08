# Задача 4. Товары.

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}


def counter(dict_list):
    sum_quantity = 0
    sum_price = 0
    for i in dict_list:
        sum_quantity += i['quantity']
        sum_price += i['quantity'] * i['price']
    return sum_quantity, sum_price


def word(number):
    if number % 10 == 1 and number % 100 != 11:
        return 'рубль'
    elif number % 10 in [2, 3, 4]:
        return 'рубля'
    else:
        return 'рублей'


def word_quantity(number):
    if number % 10 == 1 and number % 100 != 11:
        return 'штука'
    elif number % 10 in [2, 3, 4]:
        return 'штуки'
    else:
        return 'штук'


print('Результат работы программы:')
for item in goods:

    quontity, summ = counter(store[goods[item]])
    print(f'{item} - {quontity} {word_quantity(quontity)}, стоимость {summ} {word(summ)}.')

