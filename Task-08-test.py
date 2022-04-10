# Задача 8. Угадай число

import random

number_user = int(input('Введите максимальное число: '))
riddle = random.randint(1,number_user)
flag = True
main_set_numbers = {i for i in range(1, number_user)}     # сет с числом в котором есть верное
answer_set_error = set()


def check_enter(enter_list):
    if enter_list == 'помогите':
        return -1
    elif enter_list.isdigit():
        return {int(i) for i in enter_list.split(' ')}
    else:
        return 0


while flag:

    numbers_answer = check_enter(input('Нужное число есть среди вот этих чисел: '))

    if numbers_answer == 0:

        # неверный ввод
        print('Неверный ввод данных. Проверьте вводимые данные. Если требуется помошь - введите "Помогите".')
        continue

    elif numbers_answer == -1:

        # ответ == Помогите
        # вычисление и предоставление вариантов, которые мог загадать оппонент

        flag = False


    else:   # если вернулся сет

        # если длина сета == 1 то проверка с riddle
            # вывод ответа. Если угадал - выход из цикла по флагу, цикл продолжается

        # вычисление вариантов: "плохих ответов" и "хороших ответов"

        numbers_set = set(int(i) for i in numbers_answer.split(' '))
        if riddle in numbers_set:
            print('Ответ Артёма: Да')
            if not len(set_yes):
                set_yes.update(numbers_set)
            else:
                set_yes.add(numbers_set)
        else:
            print('Ответ Артёма: Нет')
            if not len(set_no):
                set_no.update(numbers_set)
            else:
                set_yes.discard(set_no)
    elif numbers_answer.lower() == 'помогите':
        flag = False





print()