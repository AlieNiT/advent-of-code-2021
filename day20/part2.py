def advance(arr, i, j):
    res = 0
    for I in range(i - 1, i + 2):
        for J in range(j - 1, j + 2):
            res = 2 * res + arr[I][J]
    return algorithm[res]


def grow(arr, t):
    tmp = [[t % 2 for _ in range(len(arr[0]) + 4)] for _ in range(len(arr) + 4)]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            tmp[i + 2][j + 2] = arr[i][j]
    res = []
    for i in range(1, len(tmp) - 1):
        line = []
        for j in range(1, len(tmp[0]) - 1):
            line.append(advance(tmp, i, j))
        res.append(line)
    return res


algorithm = input()
algorithm = [0 if c == '.' else 1 for c in algorithm]
input()
field = []
while True:
    inp = input()
    if inp == "end":
        break
    field.append([0 if c == '.' else 1 for c in inp])

count = 50
for n in range(count):
    field = grow(field, n)
res = 0
for line in field:
    for b in line:
        res += b
print(res)
