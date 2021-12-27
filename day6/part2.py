fish = list(map(lambda x: int(x), input().split(",")))
timings = [0 for _ in range(9)]
for n in fish:
    timings[n] += 1
for i in range(256):
    timings.append(timings.pop(0))
    timings[6] += timings[-1]

count = 0
for n in timings:
    count += n
print(count)