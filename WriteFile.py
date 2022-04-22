with open('code.txt', 'w') as out:
    out.write('a3b4c2e10b1\n')

with open('code.txt', 'r') as inp:
    for line in inp:
        s = line.strip()

user_code = list(s)
new_string = str()
letter = str()
digit = str()

for i in user_code:
    if i not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
        letter.join(i)
    else:
        digit.join(i)
dict_l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'w',
          'v', 'x', 'y', 'z']
for i in dict_l:
    s = s.strip(__chars=i)
    print(s)
print(digit)





print(user_code)