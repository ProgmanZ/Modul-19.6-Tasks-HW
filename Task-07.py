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


PizzaTimeDB = dict()


def input_number_orders():
    while True:
        number_orders = input('Введите количество заказов: ')
        if number_orders.isdigit():
            return int(number_orders)
        else:
            print('Требуется ввод только числового значения.')


for order in range(1, input_number_orders() + 1):
    while True:
        order_line = input(f'{word(order).capitalize()} заказ: ').lower().split(' ')
        if not len(order_line) == 3:
            print('Некорректно ввыполнен ввод. Должны быть 3 значения через пробел.\n'
                  'Например: "Фамилия" "Название пиццы" "Кол-во"')
        else:
            break
    if order_line[0] not in PizzaTimeDB.keys():
        PizzaTimeDB[order_line[0]] = dict()
        PizzaTimeDB[order_line[0]][order_line[1]] = int(order_line[2])
    else:
        if order_line[1] in PizzaTimeDB[order_line[0]].keys():
            PizzaTimeDB[order_line[0]][order_line[1]] += int(order_line[2])
        else:
            PizzaTimeDB[order_line[0]][order_line[1]] = dict()
            print('BlockElse before = ', PizzaTimeDB[order_line[0]][order_line[1]])
            PizzaTimeDB[order_line[0]][order_line[1]] = int(order_line[2])
            print('arter = ', PizzaTimeDB[order_line[0]][order_line[1]])
    print(PizzaTimeDB)

print(PizzaTimeDB)

