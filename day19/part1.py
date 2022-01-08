import numpy as np


def orientations():
    res = np.empty((24, 3, 3))
    count = 0
    for i in range(6):
        for j in range(6):
            if i % 3 == j:
                continue
            for k in range(6):
                if k % 3 == j or k % 3 == i:
                    continue
                candidate = np.zeros((3, 3))
                candidate[0][i % 3] = 2 * (int(i > 2) - 0.5)
                candidate[1][j % 3] = 2 * (int(j > 2) - 0.5)
                candidate[2][k % 3] = 2 * (int(k > 2) - 0.5)
                if np.linalg.det(candidate) == 1:
                    res[count] = candidate
                    count += 1
    return res


def same_counter(points1, points2):
    for point1 in points1:
        for point2 in points2:
            count = 0
            displacement = np.subtract(point2, point1)
            for p1 in points1:
                for p2 in point2:
                    tmp = displacement == np.subtract(p2, p1)
                    if tmp.all():
                        count += 1
                        break
            if count >= 12:
                return displacement
    return None


def rotator(positions1, positions2):
    rotations = orientations()
    for rotation in rotations:
        current = (rotation @ positions1.T).T
        test = same_counter(current, positions2)
        if test:
            print(test)
            for position in positions2:
                if np.subtract(position, test) not in positions1:
                    positions1 += np.subtract(position, test)
            return positions1
    return None


scanner1 = []
scanner2 = []
while True:
    inp = input().split(",")
    if inp[0] == "end":
        break
    scanner1.append([int(x) for x in inp])
while True:
    inp = input().split(",")
    if inp[0] == "end":
        break
    scanner2.append([int(x) for x in inp])

scanner1 = np.array(scanner1)
scanner2 = np.array(scanner2)
print(rotator(scanner1, scanner2))
