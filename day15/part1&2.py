# The first and the second part are practically the same
import math
import queue

field = []

while True:
    inp = input()
    if inp == "end":
        break
    field.append([int(ch) for ch in inp])
h = len(field)
for i in range(4):
    for j in range(h):
        field.append([(x + i) % 9 + 1 for x in field[j]])
# for i in range(len(field)):
#     print(field[i])

for i in range(len(field)):
    h = len(field[i])
    for j in range(4):
        field[i] += [(field[i][k] + j) % 9 + 1 for k in range(h)]
# for i in range(len(field)):
#     print(field[i])


def settle(risks, table, pos):
    i = pos[0]
    j = pos[1]
    res = []
    next_value = risks[i][j] - table[i][j]
    if i - 1 >= 0: next_value = min(next_value, risks[i - 1][j])
    if j - 1 >= 0: next_value = min(next_value, risks[i][j - 1])
    if i + 1 < len(risks): next_value = min(next_value, risks[i + 1][j])
    if j + 1 < len(risks[0]): next_value = min(next_value, risks[i][j + 1])
    if next_value + table[i][j] < risks[i][j]:
        risks[i][j] = next_value + table[i][j]
        if i - 1 >= 0: res += [(i - 1, j)]
        if j - 1 >= 0: res += [(i, j - 1)]
        if i + 1 < len(risks): res += [(i + 1, j)]
        if j + 1 < len(risks[0]): res += [(i, j + 1)]
    return res


risks = [[math.inf for i in range(len(field[0]))] for j in range(len(field))]
risks[0][0] = 0
q = queue.Queue()
q.put((0, 1))
q.put((1, 0))
while not q.empty():
    current = q.get()
    s = settle(risks, field, current)
    for pair in s:
        q.put(pair)

print(risks[-1][-1])
