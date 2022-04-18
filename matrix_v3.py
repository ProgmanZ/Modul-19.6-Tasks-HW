size = int(input('Введите размер матрицы: '))

count = 0

a_col = size - 1
b_col = -1

a_row = size - 1
b_row = 0
step = -1
i = size - 1
col = size - 1

list_col = list()
list_row = list()
all_row = 0
all_col = size - 1

while count != size:

    tmp_list = list()

    for i in range(a_col, b_col, step):
        tmp_list.append(i)
    tmp_list.reverse()
    list_col.append(tmp_list)

    b_col, a_col = a_col, i

    tmp_list = list()
    for i in range(a_row, b_row, step):
        tmp_list.append(i)
    tmp_list.reverse()
    list_row.append(tmp_list)

    step *= -1

    b_row, a_row = a_row, i
    count += 1

matrix_col = list()
for col in list_col:
    for c in col:
        matrix_col.append(c)
    tmp_list = list()
    for n in range(len(col) - 1):
        matrix_col.append(col[-1])

matrix_row = list()
tmp_list = list()

for n in range(len(list_col[0])):
    matrix_row.append(0)

for row in list_row:
    for r in row:
        matrix_row.append(r)
    tmp_list = list()
    for n in range(len(row)):
        matrix_row.append(row[-1])

matrix = list()

for i in range(size):
    tmp_list = list()
    for j in range(size):
        tmp_list.append(0)
    matrix.append(tmp_list)

for i in range(size ** 2):
    matrix[matrix_row[i]][matrix_col[i]] = i

for i in matrix:
    for j in i:
        print(j, end=' ')
    print()
