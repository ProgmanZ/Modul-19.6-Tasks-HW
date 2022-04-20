# чтение из файла
inf = open('file.txt', 'r')  # Открытие файла в режиме чтения
s1 = inf.readline()
inf.close()

# запись в файл
onf = open('file.txt', 'w')  # Открытие файла в режиме записи
onf.write('Some text\n')  # Запись в файл строчки
onf.write(str(25))  # Запись чисел должна быть явно преобразована в строковый формат
onf.close()  # Закрытие файла

# чтение из файла
with open('text.txt') as inf:  # открытие в такой конструкции не требует закрытия файла через ф-ю close()
    s1 = inf.readline()

# запись в файл
with open('text.txt', 'w') as onf:
    onf.write('Some text\n')
    onf.write(str(25))

# удаляет служебные символы
s = inf.readline().strip()  # удаляет служебные символы при чтении такие как \n или \t

# путь к файлу
import os

os.path.join('.', 'dirname', 'filename.txt')  # собирает путь к файлу
'./dirname/filename.txt'

# построчное чтение содержимого файла с удалением служебных символов
with open('input.txt') as inf:
    for line in inf:
        line = line.strip()
        print(line)
