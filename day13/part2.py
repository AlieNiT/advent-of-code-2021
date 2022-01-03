w = 1311
h = 895
field = [[0 for _ in range(h)] for i in range(w)]
while True:
    inp = input()
    if not "," in inp:
        break
    inp = list(map(lambda x: int(x), inp.split(",")))
    field[inp[0]][inp[1]] = 1


def fold(table, isX, l1, l2):
    if isX == 1:
        for i in range((l1 + 1) // 2, l1):
            for j in range(l2):
                if table[i][j] == 1:
                    table[l1 - 1 - i][j] = 1
    else:
        for i in range(l1):
            for j in range((l2 + 1) // 2, l2):
                if table[i][j] == 1:
                    table[i][l2 - 1 -j] = 1


while True:
    inp = input()
    if inp == "end":
        break
    if 'x' in inp:
        fold(field, 1, w, h)
        w = (w - 1) // 2
    else:
        fold(field, 0, w, h)
        h = (h - 1) // 2

for i in range(w):
    print(field[i][:h])