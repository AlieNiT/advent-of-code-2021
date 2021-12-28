inp = input()
n = len(inp)
field = [[10 for _ in range(len(inp) + 2)]]
field.append([10] + [int(ch) for ch in inp] + [10])
while True:
    inp = input()
    if inp == "end":
        break
    field.append([10] + [int(ch) for ch in inp] + [10])
field.append([10 for _ in range(n + 2)])
res = 0
# print(field)

for i in range(len(field)):
    for j in range(len(field[0])):
        if field[i][j] == 10:
            continue
        if field[i][j - 1] > field[i][j] and\
           field[i][j + 1] > field[i][j] and\
           field[i - 1][j] > field[i][j] and\
           field[i + 1][j] > field[i][j]:
            res += field[i][j] + 1
print(res)