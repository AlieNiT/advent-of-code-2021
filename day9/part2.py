inp = input()
n = len(inp)
field = [[9 for _ in range(len(inp) + 2)]]
field.append([9] + [int(ch) for ch in inp] + [9])
while True:
    inp = input()
    if inp == "end":
        break
    field.append([9] + [int(ch) for ch in inp] + [9])
field.append([9 for _ in range(n + 2)])
res = 0


# print(field)
def basin_finder(field, i, j):
    if field[i][j] == 9 or field[i][j] == -1:
        return 0
    field[i][j] = -1
    up = basin_finder(field, i, j + 1)
    down = basin_finder(field, i, j - 1)
    right = basin_finder(field, i + 1, j)
    left = basin_finder(field, i - 1, j)
    return 1 + up + down + right + left

basins = []
for i in range(len(field)):
    for j in range(len(field[0])):
        if field[i][j] == 9 or field[i][j] == -1:
            continue
        print("here")
        basins.append(basin_finder(field, i, j))

basins.sort()
print(basins)
print(basins[-1] * basins[-2] * basins[-3])