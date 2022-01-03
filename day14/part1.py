template = [ch for ch in input()]
input()
rules = {}

while True:
    inp = input().split(" -> ")
    if inp[0] == "end":
        break
    print(inp)
    rules[(inp[0][0], inp[0][1])] = inp[1]


for i in range(30):
    tmp = [rules[(template[i], template[i + 1])] for i in range(len(template) - 1)]
    next = []
    print(i)
    for j in range(len(tmp)):
        next.append(template[j])
        next.append(tmp[j])
    next.append(template[-1])
    template = next

counts = []
count = 1
template.sort()
for i in range(1, len(template)):
    if template[i - 1] != template[i]:
        counts.append(count)
        count = 0
    count += 1
counts.sort()
print(counts[-1] - counts[0])