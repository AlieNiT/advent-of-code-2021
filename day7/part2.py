import math

crabs = list(map(lambda x: int(x), input().split(",")))

crabs.sort()


def fuel_calculator(n):
    return int((n * (n + 1)) / 2)


res = math.inf
for mode in range(crabs[0], crabs[-1]):
    sum = 0
    for i in range(len(crabs)):
        sum += fuel_calculator(int(math.fabs(mode - crabs[i])))
    res = min(res, sum)
print(res)
