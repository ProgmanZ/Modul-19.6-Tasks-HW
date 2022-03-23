# Задача 2. География

ask_list = {1: 'Первая',
            2: 'Вторая',
            3: 'Третья',
            4: 'Четвёртая',
            5: 'Пятая',
            6: 'Шестая',
            7: 'Седьмая',
            8: 'Восьмая',
            9: 'Девятая',
            10: 'Десятая'}

ans_list = {1: 'Первый',
            2: 'Второй',
            3: 'Третий'}


def enter_country(number):
    country_list = [input(f'{ask_list[i]} страна: ').split() for i in range(1, number+1)]
    return country_list


def search_country(search_city, dict_with_city):
    flag = False
    for s_country in dict_with_city.keys():
        if search_city in dict_with_city[s_country]:
            print(f'Город {search_city} расположен в стране {s_country}.')
            return True
    return False


while True:
    numbers_countries = input('Количество стран: ')
    if not numbers_countries.isdigit() or 0 > int(numbers_countries) > 10:
        print('Ошибка ввода. Ожидается ввод цифры из диаппазона от 1 до 10 включительно.')
    else:
        numbers_countries = int(numbers_countries)
        break

country_dict = {element_list[0]: element_list[1:] for element_list in enter_country(numbers_countries)}

for i in range(1, 4):
    print()
    city = input(f'{ans_list[i]} город: ')
    if not search_country(city, country_dict):
        print(f'По городу {city} данных нет.')
