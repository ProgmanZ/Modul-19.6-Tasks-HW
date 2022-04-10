# Задача 8. Угадай число

import random

number_user = int(input('Введите максимальное число: '))
riddle = random.randint(1,number_user)
flag = True
set_yes = set()
set_no = set()

while flag:

    numbers_answer = input('Нужное число есть среди вот этих чисел: ')
    if numbers_answer.isdigit():
        numbers_set = set( int(i) for i in numbers_answer.split(' '))
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
    else:
         print('Неверный ввод данных. Проверьте вводимые данные. Если требуется помошь - введите "Помогите".')
    # print(numbers_set)




print()