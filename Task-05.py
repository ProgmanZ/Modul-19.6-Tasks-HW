# Задача 5. Гистограмма частоты 2

def print_dict(dict_for_prn):
    for select in sorted(dict_for_prn):
        print(f'{select}:{dict_for_prn[select]}')


user_text = input('Введите текст: ')
letter_dict = dict()

for letter in user_text:
    if letter in letter_dict.keys():
        letter_dict[letter] += 1
    else:
        letter_dict[letter] = 1

print('Оригинальный словарь частот:')
print_dict(letter_dict)

new_dict = {key: list() for key in set(letter_dict.values())}

for letter in letter_dict:
    new_dict[letter_dict[letter]].append(letter)

print('\nИнвертированный словарь частот:')
print_dict(new_dict)
