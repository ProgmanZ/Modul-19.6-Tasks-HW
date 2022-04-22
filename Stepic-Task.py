namefile = input('Имя файла: ')


with open(namefile, 'r') as orig:
    code = orig.readline().strip()

letter = code[0]
digit = str()
count = 0
result = str()

for l in range(1, len(code)):
    if code[l].isdigit():

        digit += code[l]
    else:

        result += letter * int(digit)
        letter = code[l]
        digit = str()

result += letter * int(digit)
print(result)

with open('result.txt', 'w') as res:
    res.write(result)



