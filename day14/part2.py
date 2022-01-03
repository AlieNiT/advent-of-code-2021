template = input()
input()
rules = {}
counts = {}
while True:
    inp = input().split(" -> ")
    if inp[0] == "end":
        break
    rules[inp[0]] = [inp[0][0] + inp[1][0],
                                     inp[1][0] + inp[0][1]]
    counts[inp[0][0] + inp[0][1]] = 0

for i in range(len(template) - 1):
    counts[template[i] + template[i + 1]] += 1

for i in range(40):
    tmp = {}
    for key in counts.keys():
        tmp[key] = 0
    for key in rules.keys():
        tmp[rules[key][0]] += counts[key]
        tmp[rules[key][1]] += counts[key]
    counts = tmp

chars = {}
for key in counts.keys():
    if key[0] not in chars: chars[key[0]] = 0
    if key[1] not in chars: chars[key[1]] = 0
    chars[key[0]] += counts[key]
    chars[key[1]] += counts[key]

values = list(chars.values())
values.sort()
print(values)
print((values[-1] + 1 - values[0])//2)