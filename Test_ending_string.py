count = 0

while count < 101:
    number = 14.93
    ending = ''

    if 2 <= (number % 10) <= 4 and not 11 < number < 15:
        ending = 'минуты'
    elif number % 10 == 1 and number != 11:
        ending = 'минута'
    else:
        ending = 'минут'

    print(f'{count} {ending}')
    count += 1
