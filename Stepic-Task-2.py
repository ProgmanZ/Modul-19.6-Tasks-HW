filename = input('Введите имя файла: ')
all_contents = list()
contents_dict = dict()

with open(filename, 'r') as imp:
    for line in imp:
        all_contents.extend(line.lower().strip().split(' '))

contents_dict = {i: all_contents.count(i) for i in all_contents}
max_vol = max(contents_dict.values())

result = [key if vol == max_vol else None for key, vol in contents_dict.items()]

print(result[0], contents_dict[result[0]])
