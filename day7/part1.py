import math

crabs = list(map(lambda x: int(x), input().split(",")))

crabs.sort()
mode = crabs[len(crabs)//2]
res = 0
for pos in crabs:
    res += int(math.fabs(pos - mode))
print(res)