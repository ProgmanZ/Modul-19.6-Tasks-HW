# Задача 1. Песни 2.

violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.11,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

ask_list = {1: 'первой',
            2: 'второй',
            3: 'третьей',
            4: 'четвёртой',
            5: 'пятой',
            6: 'шестой',
            7: 'седьмой',
            8: 'восьмой',
            9: 'девятой',
            }


def check_song(ind):
    while True:
        name_song = input(f'Название {ask_list[ind]} песни: ')
        if name_song in violator_songs.keys():
            return name_song
        else:
            print('Такой композиции нет в коллекции.')


while True:
    tracks = input('Сколько песен выбрать? ')
    if not tracks.isdigit():
        print('Ожидается ввод только цифр.')
    elif 0 < int(tracks) < 10:
        tracks = int(tracks)
        break
    else:
        print('Ошибка в количестве треков... Имеется всего 9 пеcен.')


list_selected_tracks = [check_song(i) for i in range(1, tracks + 1)]
all_time_tracks = sum([violator_songs[name_of_single] for name_of_single in list_selected_tracks ])
all_time_tracks = round(all_time_tracks, ndigits=2)

print('\nОбщее время звучания песен:', all_time_tracks, 'минуты.')
