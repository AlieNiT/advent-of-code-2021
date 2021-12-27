res = 0
while True:
    line = input().split()
    if line[0] == "end":
        break
    for i in range(4):
        if not 7 > len(line[-(1 + i)]) > 4:
            res += 1
print(res)