# Задача 10. Снова палиндром

user_string = input('Введите строку: ')

len_str = len(user_string)

user_dict = {key: str(user_string.count(key)) for key in set(user_string)}

str_val = ''.join(user_dict.values())

list_val = [int(i) for i in str_val if i != '1']

if sum(list_val) % 2 == 0 and str_val.count('1') <= 1:
    print('Можно сделать палиндромом')
else:
    print('Нельзя сделать палиндромом')
