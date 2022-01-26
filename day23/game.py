import math

hallway = ['.' for _ in range(11)]
# rooms = [['.' for _ in range(2)] for _ in range(4)]
rooms = [['D', 'B'], ['A', 'C'], ['d', 'b'], ['c', 'a']]
costs = {'a': 1,
         'b': 10,
         'c': 100,
         'd': 1000}


def show():
    print("#0123456789A#")
    print('#' + "".join(hallway) + "#0")
    print("###" + rooms[0][0] + "#" +
          rooms[1][0] + "#" +
          rooms[2][0] + "#" +
          rooms[3][0] + "###1")
    print("  #" + rooms[0][1] + "#" +
          rooms[1][1] + "#" +
          rooms[2][1] + "#" +
          rooms[3][1] + "#  2")
    print("  #########")


def move(ch, destination):
    destination = list(map(lambda x: int(x) if x != 'A' else 10, destination.split(",")))
    if destination[0]%2 != 0 and destination[1] > 0:
        raise Exception()
    res = 0
    in_hallway = hallway.__contains__(ch)
    pos = None
    if in_hallway:
        pos = hallway.index(ch)
        hallway[pos] = '.'
    else:
        for i in range(len(rooms)):
            for j in range(len(rooms[i])):
                if rooms[i][j] == ch:
                    res += j + 1
                    rooms[i][j] = '.'
                    pos = 2 * i + 2
                    break
            if pos:
                break
    if destination[1] == 0:
        res += math.fabs(pos - destination[0])
        hallway[destination[0]] = ch
    else:
        res += math.fabs(pos - destination[0]) + destination[1]
        rooms[destination[0] // 2 - 1][destination[1] - 1] = ch
    return res * costs[ch.lower()]


def initialize():
    letters = set()
    print("Initialize rooms one by one")
    for i in range(len(rooms)):
        rooms[i] = list(input("room " + str(i + 1) + ": "))
    for i in range(len(rooms)):
        for j in range(len(rooms[i])):
            if rooms[i][j] in letters:
                rooms[i][j] = rooms[i][j].lower()
            else:
                letters.add(rooms[i][j])


def win_check():
    for i in range(len(rooms)):
        if [ord(x.lower()) for x in rooms[i]] != [97 + i for _ in range(len(rooms[i]))]:
            return False
    return True


# initialize()
cost = 0
while True:
    show()
    print("cost up to now: " + str(cost))
    if win_check():
        break

    inp = input("Enter <ch i,j>:").split()
    if inp == "end":
        break
    try:
        cost += move(*inp)
    except:
        print("Wrong input")
    print()
print("YOU WON!")
