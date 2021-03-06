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


def merge(points1, points2, d):
    res = []
    for point1 in points1:
        res.append(point1)
    for point2 in points2:
        r_p2 = [point2[i] + d[i] for i in range(3)]
        if r_p2 not in res:
            res.append(r_p2)
    return res


def same_counter(points1, points2):
    for point1 in points1:
        for point2 in points2:
            count = 0  # counts the number of points which go on top of each other
            d = [point1[i] - point2[i] for i in range(3)]  # vector going from source 1 to 2
            for p1 in points1:
                r = [p1[i] - d[i] for i in range(3)]
                # if max(r) > 1500:
                #     break
                for p2 in points2:
                    if r == p2:
                        count += 1
                        break
                if count >= 12:
                    return count, d
    return None, None


def rotate_check(positions1, positions2):
    rotations = orientations()
    positions1 = np.array(positions1)
    for rotation in rotations:
        current = (rotation @ positions1.T).T
        current = current.tolist()
        count, d = same_counter(current, positions2)
        if count:
            print(d)
            return merge(current, positions2, d)
    return None


scanners = []
while True:
    scanner = []
    if input() == "end":
        break
    while True:
        inp = input().split(",")
        if inp[0] == "":
            scanners.append(scanner)
            break
        scanner.append([int(x) for x in inp])

while len(scanners) > 1:
    print(len(scanners))
    br = False
    for i in range(len(scanners)):
        print(i)
        for j in range(i + 1, len(scanners)):
            res = rotate_check(scanners[i], scanners[j])
            if res:
                print("index " + str(i) + " and " + str(j))
                scanners.pop(j)
                scanners.pop(i)
                scanners.append(res)
                br = True
                break
        if br:
            break
print(len(scanners[0]))