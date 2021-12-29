def flash(table, i, j):
    table[i][j] = -1
    for I in range(i - 1, i + 2):
        for J in range(j - 1, j + 2):
            if not (0 <= I < 10 and 0 <= J < 10):
                continue
            if table[I][J] == -1:
                continue
            table[I][J] += 1
            if table[I][J] == 10:
                flash(table, I, J)


field = []
res = 0
size = 10
for i in range(10):
    field.append([int(ch) for ch in input()])

for i in range(100):
    for i in range(10):
        for j in range(10):
            if field[i][j] == 9:
                flash(field, i, j)
            elif field[i][j] == -1:
                continue
            else:
                field[i][j] += 1
    for i in range(10):
        for j in range(10):
            if field[i][j] == -1:
                res += 1
                field[i][j] = 0
    # for i in range(10):
    #     print(field[i])
    # print()
print(res)