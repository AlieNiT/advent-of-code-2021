scores = [0, 0]
positions = list(map(lambda x: int(x), input().split()))
dice = 1
end = False
while not end:
    for i in range(len(scores)):
        d = 3 * ((dice + 1) % 10)
        positions[i] = ((positions[i] + d - 1) % 10) + 1
        scores[i] += positions[i]
        dice += 3
        if scores[i] >= 1000:
            dice -= 1
            end = True
            break

print(dice)
print(scores)


