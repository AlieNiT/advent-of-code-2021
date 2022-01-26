import numpy as np

situations = {}  # (pos1,pos2,score1,score2) -> (wins1, wins2)


def next_situations(pos1, pos2, score1, score2, player1):
    res = {}
    if player1:
        pos1 = (pos1 + 3) % 10
        res[(pos1, pos2, score1 + pos1 + 1, score2, not player1)] = 1
        pos1 = (pos1 + 1) % 10
        res[(pos1, pos2, score1 + pos1 + 1, score2, not player1)] = 3
        pos1 = (pos1 + 1) % 10
        res[(pos1, pos2, score1 + pos1 + 1, score2, not player1)] = 6
        pos1 = (pos1 + 1) % 10
        res[(pos1, pos2, score1 + pos1 + 1, score2, not player1)] = 7
        pos1 = (pos1 + 1) % 10
        res[(pos1, pos2, score1 + pos1 + 1, score2, not player1)] = 6
        pos1 = (pos1 + 1) % 10
        res[(pos1, pos2, score1 + pos1 + 1, score2, not player1)] = 3
        pos1 = (pos1 + 1) % 10
        res[(pos1, pos2, score1 + pos1 + 1, score2, not player1)] = 1
    else:
        pos2 = (pos2 + 3) % 10
        res[(pos1, pos2, score1, score2 + pos2 + 1, not player1)] = 1
        pos2 = (pos2 + 1) % 10
        res[(pos1, pos2, score1, score2 + pos2 + 1, not player1)] = 3
        pos2 = (pos2 + 1) % 10
        res[(pos1, pos2, score1, score2 + pos2 + 1, not player1)] = 6
        pos2 = (pos2 + 1) % 10
        res[(pos1, pos2, score1, score2 + pos2 + 1, not player1)] = 7
        pos2 = (pos2 + 1) % 10
        res[(pos1, pos2, score1, score2 + pos2 + 1, not player1)] = 6
        pos2 = (pos2 + 1) % 10
        res[(pos1, pos2, score1, score2 + pos2 + 1, not player1)] = 3
        pos2 = (pos2 + 1) % 10
        res[(pos1, pos2, score1, score2 + pos2 + 1, not player1)] = 1
    return res


def wins_calc(pos1, pos2, score1, score2, player1):
    if score1 >= 21:
        situations[(pos1, pos2, score1, score2, player1)] = (1, 0)
    if score2 >= 21:
        situations[(pos1, pos2, score1, score2, player1)] = (0, 1)
    if (pos1, pos2, score1, score2, player1) in situations:
        return
    wins1 = 0
    wins2 = 0
    next_level = next_situations(pos1, pos2, score1, score2, player1)
    for key in next_level.keys():
        if key not in situations:
            wins_calc(*key)
        wins1 += next_level[key] * situations[key][0]
        wins2 += next_level[key] * situations[key][1]

    situations[(pos1, pos2, score1, score2, player1)] = (wins1, wins2)


# print(next_situations(1, 6, 0, 0, True))
for item in next_situations(1, 6, 0, 0, True).items():
    print(item)
print(wins_calc(1, 6, 0, 0, True))
print(situations)
