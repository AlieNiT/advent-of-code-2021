import math

hallway = ['.' for _ in range(11)]
rooms = [['D', 'D', 'D', 'B'], ['A', 'C', 'B', 'C'], ['D', 'B', 'A', 'B'], ['C', 'A', 'C', 'A']]

costs = {'A': 1,
         'B': 10,
         'C': 100,
         'D': 1000}


def show():
    print("#0123456789A#")
    print('#' + "".join(hallway) + "#0")
    print("###" + rooms[0][0] + "#" +
          rooms[1][0] + "#" +
          rooms[2][0] + "#" +
          rooms[3][0] + "###1")
    for i in range(1, len(rooms)):
        print("  #" + rooms[0][i] + "#" +
              rooms[1][i] + "#" +
              rooms[2][i] + "#" +
              rooms[3][i] + "#  " + str(i + 1))
    print("  #########")


def move(ch, source, destination):
    destination = list(map(lambda x: int(x) if x != 'A' else 10, destination.split(",")))
    source = list(map(lambda x: int(x) if x != 'A' else 10, source.split(",")))

    if (destination[0] % 2 != 0 and destination[1] > 0) or \
            (source[0] % 2 != 0 and source[1] > 0):
        print(1)
        raise Exception()
    if source[1] == 0:
        if hallway[source[0]] != ch:
            raise Exception()
        hallway[source[0]] = '.'
    else:
        if rooms[source[0] // 2 - 1][source[1] - 1] != ch:
            raise Exception()
        rooms[source[0] // 2 - 1][source[1] - 1] = '.'
    if destination[1] == 0:
        hallway[destination[0]] = ch
    else:
        rooms[destination[0] // 2 - 1][destination[1] - 1] = ch
    res = math.fabs(source[0] - destination[0]) + source[1] + destination[1]
    return res * costs[ch]


def initialize():
    print("Initialize rooms one by one")
    for i in range(len(rooms)):
        rooms[i] = list(input("room " + str(i + 1) + ": "))


def win_check():
    for i in range(len(rooms)):
        if [ord(x) for x in rooms[i]] != [65 + i for _ in range(len(rooms[i]))]:
            return False
    return True


# initialize()
cost = 0
while True:
    show()
    print("cost up to now: " + str(cost))
    if win_check():
        break

    inp = input("Enter <ch I,J i,j>:").split()
    if inp == "end":
        break
    try:
        cost += move(*inp)
    except:
        print("Wrong input")
    print()
print("YOU WON!")
