# Задача 8. Угадай число

import random

number_user = int(input('Введите максимальное число: '))

riddle = random.randint(1, number_user)  # число, которое загадал Артур

set_say_yes = {int(i) for i in range(1, number_user + 1)}  # сет с последовательностью чисел содержащий верный элемент

set_say_no = set()  # сет с последовательностью чисел при отрицательном ответе


def check_enter(enter_list):  # проверка ввода от пользователя
    if enter_list == 'помогите':
        return -1
    elif not enter_list.isalpha():
        return {int(i) for i in enter_list.split(' ')}
    else:
        return 0


def print_numbers(set_user):
    for elem in set_user:
        print(elem, end=' ')


while True:

    user_numbers = check_enter(input('Нужное число есть среди вот этих чисел: '))

    if user_numbers == 0:
        # неверный ввод
        print('Неверный ввод данных. Проверьте вводимые данные. Если требуется помошь - введите "Помогите".')
        continue

    elif user_numbers == -1:
        # "помогите"
        print('Артём мог загадать следующие числа: ', end='')
        print_numbers(set_say_yes)
        break

    else:
        if riddle in user_numbers:
            print("Ответ Артёма: Да.")
            set_say_yes.clear()
            set_say_yes.update(user_numbers)
            if len(set_say_yes) == 1:
                print('Вы угадали число!')
                break

        else:
            print("Ответ Артёма: Нет.")
            for elem in user_numbers:
                set_say_yes.discard(elem)
                set_say_no.add(elem)
            if len(set_say_yes) == 1:
                print("Вы перебрали числа: ", end='')
                print_numbers(set_say_no)
                print("\nОсталось только одно число, которое вы не ввели. Это: ", end='')
                print_numbers(set_say_yes)
                break
