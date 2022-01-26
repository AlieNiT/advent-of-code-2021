import itertools


class Cuboid:
    def __init__(self, x, y, z):
        self.pos = [x, y, z]

    def contains(self, c):
        return self.pos[0][0] <= c.pos[0][0] <= c.pos[0][1] <= self.pos[0][1] and \
               self.pos[1][0] <= c.pos[1][0] <= c.pos[1][1] <= self.pos[1][1] and \
               self.pos[2][0] <= c.pos[2][0] <= c.pos[2][1] <= self.pos[2][1]

    def intersects(self, c):
        return ((self.pos[0][0] <= c.pos[0][0] < self.pos[0][1] or self.pos[0][0] < c.pos[0][1] <= self.pos[0][1] or
                 c.pos[0][0] <= self.pos[0][0] < c.pos[0][1] or c.pos[0][0] < self.pos[0][1] <= c.pos[0][1]) and
                (self.pos[1][0] <= c.pos[1][0] < self.pos[1][1] or self.pos[1][0] < c.pos[1][1] <= self.pos[1][1] or
                 c.pos[1][0] <= self.pos[1][0] < c.pos[1][1] or c.pos[1][0] < self.pos[1][1] <= c.pos[1][1]) and
                (self.pos[2][0] <= c.pos[2][0] < self.pos[2][1] or self.pos[2][0] < c.pos[2][1] <= self.pos[2][1] or
                 c.pos[2][0] <= self.pos[2][0] < c.pos[2][1] or c.pos[2][0] < self.pos[2][1] <= c.pos[2][1]))

    def split(self, c):
        contained = {}
        containing = {}
        partial = {}
        for i in range(3):
            if self.pos[i][0] <= c.pos[i][0] <= c.pos[i][1] <= self.pos[i][1]:
                containing[i] = ((self.pos[i][0], c.pos[i][0]),
                                 (c.pos[i][0], c.pos[i][1]),
                                 (c.pos[i][1], self.pos[i][1]))
            elif c.pos[i][0] <= self.pos[i][0] <= self.pos[i][1] <= c.pos[i][1]:
                contained[i] = ((c.pos[i][0], self.pos[i][0]),
                                (self.pos[i][0], self.pos[i][1]),
                                (self.pos[i][1], c.pos[i][1]))
            else:
                if self.pos[i][0] < c.pos[i][0]:
                    partial[i] = ((self.pos[i][0], c.pos[i][0]),
                                  (c.pos[i][0], self.pos[i][1]),
                                  (self.pos[i][1], c.pos[i][1]))
                else:
                    partial[i] = ((c.pos[i][1], self.pos[i][1]),
                                  (self.pos[i][0], c.pos[i][1]),
                                  (c.pos[i][0], self.pos[i][0]))
        lengths = (len(contained), len(containing), len(partial))
        if lengths == (0, 3, 0):
            cs = []
            cs.append([self.pos[0], self.pos[1], containing[2][0]])
            cs.append([self.pos[0], self.pos[1], containing[2][2]])
            cs.append([self.pos[0], containing[1][0], containing[2][1]])
            cs.append([self.pos[0], containing[1][2], containing[2][1]])
            cs.append([containing[0][0], containing[1][1], containing[2][1]])
            cs.append([containing[0][2], containing[1][1], containing[2][1]])

            return [Cuboid(*element) for element in cs]
        if lengths == (2, 1, 0):
            c1 = []
            c2 = []
            for i in range(3):
                if i in containing:
                    c1.append(containing[i][0])
                    c2.append(containing[i][2])
                else:
                    c1.append(self.pos[i])
                    c2.append(self.pos[i])
            return [Cuboid(*c1), Cuboid(*c2)]
        if lengths == (1, 2, 0):
            cs = [[] for _ in range(4)]
            tmp = True
            for i in range(3):
                if i in containing:
                    if tmp:
                        cs[0].append(self.pos[i])
                        cs[1].append(self.pos[i])
                        cs[2].append(containing[i][0])
                        cs[3].append(containing[i][2])
                        tmp = False
                    else:
                        cs[0].append(containing[i][0])
                        cs[1].append(containing[i][2])
                        cs[2].append(containing[i][1])
                        cs[3].append(containing[i][1])
                else:
                    for cu in cs:
                        cu.append(self.pos[i])
            return [Cuboid(*element) for element in cs]
        if lengths == (2, 0, 1):
            c1 = []
            for i in range(3):
                if i in partial:
                    c1.append(partial[i][0])
                else:
                    c1.append(self.pos[i])
            return [Cuboid(*c1)]
        if lengths == (0, 2, 1):
            cs = [[] for _ in range(4)]
            c5 = []
            tmp = True
            for i in range(3):
                if i in containing:
                    c5.append(self.pos[i])
                    if tmp:
                        cs[0].append(self.pos[i])
                        cs[1].append(self.pos[i])
                        cs[2].append(containing[i][0])
                        cs[3].append(containing[i][2])
                        tmp = False
                    else:
                        cs[0].append(containing[i][0])
                        cs[1].append(containing[i][2])
                        cs[2].append(containing[i][1])
                        cs[3].append(containing[i][1])
                else:
                    for cu in cs:
                        cu.append(partial[i][1])
                    c5.append(partial[i][0])
            cs.append(c5)
            return [Cuboid(*element) for element in cs]
        if lengths == (1, 1, 1):
            cs = [[] for _ in range(3)]
            for i in range(3):
                if i in contained:
                    for cu in cs:
                        cu.append(self.pos[i])
                elif i in containing:
                    cs[0].append(self.pos[i])
                    cs[1].append(containing[i][0])
                    cs[2].append(containing[i][2])
                else:
                    cs[0].append(partial[i][0])
                    cs[1].append(partial[i][1])
                    cs[2].append(partial[i][1])
            res = [Cuboid(*element) for element in cs]
            return res
        if lengths == (1, 0, 2):
            c1 = []
            c2 = []
            tmp = True
            for i in range(3):
                if i in contained:
                    c1.append(self.pos[i])
                    c2.append(self.pos[i])
                else:
                    if tmp:
                        c1.append(partial[i][1])
                        c2.append(partial[i][0])
                        tmp = False
                    else:
                        c1.append(partial[i][0])
                        c2.append(self.pos[i])
            return [Cuboid(*c1), Cuboid(*c2)]
        if lengths == (0, 1, 2):
            c1 = []
            c2 = []
            c3 = []
            c4 = []
            tmp = True
            for i in range(3):
                if i in containing:
                    c1.append(containing[i][0])
                    c2.append(containing[i][2])
                    c3.append(containing[i][1])
                    c4.append(containing[i][1])
                else:
                    c1.append(self.pos[i])
                    c2.append(self.pos[i])
                    if tmp:
                        c3.append(partial[i][1])
                        c4.append(partial[i][0])
                        tmp = False
                    else:
                        c3.append(partial[i][0])
                        c4.append(self.pos[i])
            return [Cuboid(*c1), Cuboid(*c2), Cuboid(*c3), Cuboid(*c4)]
        if lengths == (0, 0, 3):
            c1 = [self.pos[0], self.pos[1], partial[2][0]]
            c2 = [self.pos[0], partial[1][0], partial[2][1]]
            c3 = [partial[0][0], partial[1][1], partial[2][1]]
            return [Cuboid(*c1), Cuboid(*c2), Cuboid(*c3)]

    def get_volume(self):
        res = 1
        for interval in self.pos:
            res *= (interval[1] - interval[0])
        return res


cuboids = set()


def add_cuboid(c):
    removed = []
    added = []
    for cuboid in cuboids:
        if cuboid.contains(c):
            return
        if c.contains(cuboid):
            removed.append(cuboid)
            continue
        if not c.intersects(cuboid):
            continue
        added += cuboid.split(c)
        removed.append(cuboid)
    cuboids.add(c)
    for r in removed:
        cuboids.remove(r)
    cuboids.update(added)


def sub_cuboid(c):
    removed = []
    added = []
    for cuboid in cuboids:
        if c.contains(cuboid):
            removed.append(cuboid)
            continue
        if not c.intersects(cuboid):
            continue
        added += cuboid.split(c)
        removed.append(cuboid)
        if cuboid.contains(c):
            break
    for r in removed:
        cuboids.remove(r)
    cuboids.update(added)


def parse_input(cuboid_input: str):
    if cuboid_input == 'end':
        return None
    cuboid_input = cuboid_input.split()
    cuboid_sides = cuboid_input[1].split(',')
    for i in range(len(cuboid_sides)):
        cuboid_sides[i] = list(map(lambda x: int(x), cuboid_sides[i][2:].split('..')))
        cuboid_sides[i][1] += 1
    return cuboid_input[0], Cuboid(*cuboid_sides)


while True:
    cuboid = parse_input(input())
    if not cuboid:
        break
    if cuboid[0] == "on":
        add_cuboid(cuboid[1])
    else:
        sub_cuboid(cuboid[1])

print(sum([c.get_volume() for c in cuboids]))
