file_input = input('Введите имя файла: ')
file_export = input('Введите имя итогового файла: ')
print(f'Итоговый файл будет: {file_export}.txt.')

est_math = 0
est_phys = 0
est_rus_lang = 0
count = 0

with open(file_input, 'r', encoding='utf-8') as imp, open(file_export + '.txt', 'w', encoding='utf-8') as exp:
    for line in imp:
        file_line = line.strip().split(';')

        summary = 0
        count += 1
        est_math += int(file_line[1])
        est_phys += int(file_line[2])
        est_rus_lang += int(file_line[3])

        for i in range(1, len(file_line)):
            summary += int(file_line[i])

        exp.writelines(str(round(summary / (len(file_line) - 1), 9)) + '\n'
                       if (len(file_line[i]) - 1) != 0
                       else str(summary / 1) + '\n')

    exp.writelines(f'{str(round(est_math / count, 9))} '
                   f'{str(round(est_phys / count, 9))} '
                   f'{str(round(est_rus_lang / count, 9))}')
