field = []
next_field = []
while True:
    inp = input()
    if inp == "end":
        break
    field.append(list(inp))
    next_field.append(['.'] * len(inp))


def check(f1, f2):
    for i in range(len(f1)):
        for j in range(len(f1[i])):
            if f1[i][j] != f2[i][j]:
                return False
    return True


count = 0
n = len(field)
m = len(field[0])
while True:
    for i in range(n):
        for j in range(m):
            if field[i][j] == '>' and field[i][(j + 1) % m] == '.':
                next_field[i][(j + 1) % m] = '>'
            elif field[i][j] == '>':
                next_field[i][j] = '>'
    for i in range(n):
        for j in range(m):
            if field[i][j] == 'v' and next_field[(i + 1) % n][j] == '.' and field[ (i + 1) % n][j] != 'v':
                next_field[(i + 1) % n][j] = 'v'
            elif field[i][j] == 'v':
                next_field[i][j] = 'v'
    count += 1
    if check(field, next_field):
        break
    field = next_field
    next_field = [['.' for _ in range(m)] for _ in range(n)]
print(count)