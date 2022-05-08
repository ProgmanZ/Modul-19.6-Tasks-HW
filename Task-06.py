# Задача 6. Словарь синонимов

def word(number):
    words = {
        0:'',
        1:'первая',
        2:'вторая',
        3:'третья',
        4:'четвертая',
        5:'пятая',
        6:'шестая',
        7:'седьмая',
        8:'восьмая',
        9:'девятая',
        10:'десятая',
        11:'одиннадцатая',
        12:'двенадцатая',
        13:'тринадцатая',
        14:'четырнадцатая',
        15:'пятнадцатая',
        16:'шестнадцатая',
        17:'семьнадцатая',
        18:'восемнадцатая',
        19:'девятнадцатая',
        20:['двадцатая','двадцать '],
        30:['тридцатая','тридцать '],
        40:['сороковая','сорок '],
        50:['пятидесятая','пятьдесят '],
        60:['шестидесятая','шестьдесят '],
        70:['семидесятая','семьдесят '],
        80:['восьмидесятая','восемьдесят '],
        90:['девяностая','девяносто '],
        100:['сотая']

    }

    if number <= 19:
        return words[number]
    elif number % 10 == 0:
        return words[number][0]
    else:
        return words[number // 1000] + words[number // 10 * 10][1] + words[number % 10]


n_sinonim = int(input('Введите количество пар слов: '))

user_dict = dict()
invert_user_dict = dict()

ask = list()

for numb in range(1, n_sinonim + 1):

    while len(ask) != 2:
        ask = input('{0} пара: '.format(word(numb))).lower().split('-' or '—')
        if len(ask) != 2:
            print('Ошибка ввода. Необходимо указывать только одну пару синонимов через знак тире \'-\'.')

    user_dict[ask[0].strip()] = ask[1].strip()
    user_dict[ask[1].strip()] = ask[0].strip()

    ask = list()

while True:
    ask = input('\nВведите слово: ').strip().lower()
    if not user_dict.get(ask):
        print('Такого слова в словаре нет.')
    else:
        print('Синоним: {0}'.format(user_dict[ask].capitalize()))
        break
