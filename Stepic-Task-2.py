filename = input('Введите имя файла: ')
all_contents = list()
contents_dict = dict()

with open(filename, 'r') as imp:
    for line in imp:
        for word in line.lower().split():
            all_contents.append(word)

contents_dict = {i: all_contents.count(i) for i in all_contents}
max_vol = max(contents_dict.values())

result = [key for key, vol in contents_dict.items() if vol == max_vol]

print(result[0], contents_dict[result[0]])
