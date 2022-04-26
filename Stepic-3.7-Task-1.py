db = dict()


def create_key(check_key, user_dict):
    if check_key not in user_dict.keys():
        user_dict[check_key] = [0 for _ in range(5)]
        user_dict[check_key][0] = 1
    else:
        user_dict[check_key][0] += 1


def check_result(com_a, result_a, com_b, result_b, user_dict):

    if result_a > result_b:
        user_dict[com_a][1] += 1
        user_dict[com_a][4] += 3
        user_dict[com_b][3] += 1

    elif result_b > result_a:
        user_dict[com_b][1] += 1
        user_dict[com_b][4] += 3
        user_dict[com_a][3] += 1
    else:
        user_dict[com_a][2] += 1
        user_dict[com_a][2] += 1
        user_dict[com_b][4] += 1
        user_dict[com_b][4] += 1



def print_dict(user_dict):
    for key, value in user_dict.items():
        print(f'{key}:{" ".join(str(v) for v in value)}')


for i in range(0, int(input(''))):
    line = input("").strip().split(';')
    create_key(line[0], db)
    create_key(line[2], db)

    check_result(line[0], int(line[1]), line[2], int(line[3]), db)

print_dict(db)
