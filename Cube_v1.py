

cube_list = list()

enter_user = input('Введите строку чисел через пробел: ').lower()
size = len(enter_user.split())
itr = 0
while itr <= size:
    if len(enter_user.split()) != size:
        print('Вы ввели количество символов больше или меньше чем', size)

    elif not enter_user.isalpha():
        line_enter = enter_user.split(' ')
        tmp_list = list()
        for i in line_enter:
            tmp_list.append(int(i))
        cube_list.append(tmp_list)
        itr += 1
    elif enter_user == 'end':
        break
    else:
        print('В строке должны присутствовать только цифры.')

    enter_user = input('Введите строку чисел через пробел: ').lower()


print(cube_list)