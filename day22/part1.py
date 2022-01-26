on_lights = set()
while True:
    inp = input().split()
    if inp[0] == "end":
        break
    cuboid = inp[1].split(',')
    for i in range(len(cuboid)):
        cuboid[i] = tuple(map(lambda x: int(x), cuboid[i][2:].split('..')))
    if inp[0] == "on":
        for i in range(cuboid[0][0], cuboid[0][1] + 1):
            for j in range(cuboid[1][0], cuboid[1][1] + 1):
                for k in range(cuboid[2][0], cuboid[2][1] + 1):
                    on_lights.add((i, j, k))
    if inp[0] == "off":
        for i in range(cuboid[0][0], cuboid[0][1] + 1):
            for j in range(cuboid[1][0], cuboid[1][1] + 1):
                for k in range(cuboid[2][0], cuboid[2][1] + 1):
                    if (i, j, k) in on_lights:
                        on_lights.remove((i, j, k))
    print(len(on_lights))