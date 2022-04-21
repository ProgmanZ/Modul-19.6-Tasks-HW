# Задача 9. Родословная.

# необходимо собирать имена в сет
# необходимо сделать словарь со значениями {ключ(имя): продумать значение высоты}
# каждый ввод разбивается по пробелу в список
# проверка на корректность ввода - список должен быть не более чем на 2 элемента

def word(number):
    words = {
        0: '',
        1: 'первая',
        2: 'вторая',
        3: 'третья',
        4: 'четвертая',
        5: 'пятая',
        6: 'шестая',
        7: 'седьмая',
        8: 'восьмая',
        9: 'девятая',
        10: 'десятая',
        11: 'одиннадцатая',
        12: 'двенадцатая',
        13: 'тринадцатая',
        14: 'четырнадцатая',
        15: 'пятнадцатая',
        16: 'шестнадцатая',
        17: 'семьнадцатая',
        18: 'восемнадцатая',
        19: 'девятнадцатая',
        20: ['двадцатая', 'двадцать '],
        30: ['тридцатая', 'тридцать '],
        40: ['сороковая', 'сорок '],
        50: ['пятидесятая', 'пятьдесят '],
        60: ['шестидесятая', 'шестьдесят '],
        70: ['семидесятая', 'семьдесят '],
        80: ['восьмидесятая', 'восемьдесят '],
        90: ['девяностая', 'девяносто '],
        100: ['сотая', 'сто ']

    }

    if number <= 19:
        return words[number]
    elif number % 10 == 0:
        return words[number][0]
    else:
        return words[number // 1000] + words[number // 10 * 10][1] + words[number % 10]


def enter_number():
    while True:
        user_string = input('Введите количество человек: ')
        if not user_string.isalpha():
            return int(user_string)
        else:
            print('Ошибка ввода количества. Ожидается ввод числа.')


def enter_pairs(number_pair):
    while True:
        user_list = input(f'{word(number_pair).capitalize()} пара: ').split(' ')
        if len(user_list) == 2:
            return user_list
        else:
            print('Неправильные вводные данные.')
            print('Каждая строка должна иметь вид «имя_потомка имя_родителя» (через пробел).')


people = enter_number()
try_dict = dict()

for pair in range(1, people):
    temp_list = enter_pairs(pair)
    if temp_list[1] in try_dict.keys():
        try_dict[temp_list[1]]+=1
    else:
        try_dict[temp_list[1]] = dict()
        try_dict[temp_list[1]]=(temp_list[0])

print(try_dict)

#
# for i in try_dict.keys():
#     if i in try_dict[i]:
#         try_dict[i] =
#
#
# Первая пара: Alexei Peter_I
#
# Вторая пара: Anna Peter_I
#
# Третья пара: Elizabeth Peter_I
#
# Четвёртая пара: Peter_II Alexei
#
# Пятая пара: Peter_III Anna
#
# Шестая пара: Paul_I Peter_III
#
# Седьмая пара: Alexander_I Paul_I
#
# Восьмая пара: Nicholaus_I Paul_I
