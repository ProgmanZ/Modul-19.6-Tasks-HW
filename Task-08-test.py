# Задача 8. Угадай число

import random

number_user = int(input('Введите максимальное число: '))
riddle = random.randint(1, number_user)
flag = True
main_set_numbers = {i for i in range(1, number_user)}  # сет с числом в котором есть верное
answer_set_error = set()


def check_enter(enter_list):
    if enter_list == 'помогите':
        return -1

    elif not enter_list.isalpha():
        return {int(i) if i.isdigit() else -1 for i in enter_list.split(' ')}
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
        main_set_numbers = main_set_numbers.difference(answer_set_error)
        flag = False

    else:  # если вернулся сет

        if len(numbers_answer) == 1:
            if numbers_answer == riddle:
                print('Вы угадали! Это число:', riddle)
                flag = False
            else:
                answer_set_error.add(numbers_answer)
                continue
        else:
            if riddle in numbers_answer:
                print('Ответ Артёма: Да')
                main_set_numbers.discard(numbers_answer)
                main_set_numbers.add(riddle)
            else:
                print('Ответ Артёма: Нет')
                answer_set_error.add(numbers_answer)
print()
