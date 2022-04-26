
def code_func(usr_str, code_dict):
    new_text = str()
    for i in usr_str:
        if i in code_dict.keys():
            new_text += code_dict[i]
        else:
            new_text += i
    return new_text


user_string = input()
change_string = input()

db_code = dict(zip(user_string, change_string))
db_decode = dict(zip(change_string, user_string))

str_for_code = input()
str_for_decode = input()

print(code_func(str_for_code, db_code))
print(code_func(str_for_decode, db_decode))

a, b, c, d = user_string, change_string, str_for_code, str_for_decode
print(''.join(b[a.index(i)] for i in c))
print(''.join(a[b.index(i)] for i in d))