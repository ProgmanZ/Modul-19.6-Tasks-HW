# Задача 7. Пицца

def word(number):
    words = {
        0:'',
        1:'первый',
        2:'второй',
        3:'третий',
        4:'четвертый',
        5:'пятый',
        6:'шестой',
        7:'седьмой',
        8:'восьмой',
        9:'девятый',
        10:'десятый',
        11:'одиннадцатый',
        12:'двенадцатый',
        13:'тринадцатый',
        14:'четырнадцатый',
        15:'пятнадцатый',
        16:'шестнадцатый',
        17:'семьнадцатый',
        18:'восемнадцатый',
        19:'девятнадцатый',
        20:['двадцать '],
        30:['тридцать '],
        40:['сорок '],
        50:['пятьдесят '],
        60:['шестьдесят '],
        70:['семьдесят '],
        80:['восемьдесят '],
        90:['девяносто '],
        100:['сто ']

    }

    if number <= 19:
        return words[number]
    elif number % 10 == 0:
        return words[number][0]
    else:
        return words[number // 1000] + words[number // 10 * 10][1] + words[number % 10]


def input_number_orders_check():
    while True:
        number_orders = input('Введите количество заказов: ')
        if number_orders.isdigit():
            return int(number_orders)
        else:
            print('Требуется ввод только числового значения.')


def input_order_check(num_order):
    while True:
        order = input(f'{word(num_order).capitalize()} заказ: ').split(' ')
        if not len(order) == 3:
            print('Некорректно ввыполнен ввод. Должны быть 3 значения через пробел.\n'
                  'Например: "Фамилия" "Название пиццы" "Кол-во"')
        else:
            return order


def print_item_dict(dict_db):
    for client in sorted(dict_db):
        print(client)
        for orders in sorted(dict_db[client]):
            print('\t{0}: {1}'.format(orders, dict_db[client][orders]))


PizzaTimeDB = dict()

for number_order in range(1, input_number_orders_check() + 1):

    order = input_order_check(number_order)
    if order[0] not in PizzaTimeDB.keys():
        PizzaTimeDB[order[0]] = dict()
        PizzaTimeDB[order[0]][order[1]] = int(order[2])
    else:
        if order[1] in PizzaTimeDB[order[0]].keys():
            PizzaTimeDB[order[0]][order[1]] += int(order[2])
        else:
            PizzaTimeDB[order[0]][order[1]] = dict()
            PizzaTimeDB[order[0]][order[1]] = int(order[2])

print_item_dict(PizzaTimeDB)

