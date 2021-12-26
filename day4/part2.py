class Board:
    def __init__(self, numbers):
        self.numbers = numbers
        self.rows = [0 for i in range(len(numbers))]
        self.columns = [0 for i in range(len(numbers[0]))]
        self.sum = 0
        self.won = False
        for i in range(len(self.numbers)):
            for j in range(len(self.numbers[i])):
                self.sum += self.numbers[i][j]

    def check(self, query):
        won = False
        for i in range(len(self.numbers)):
            for j in range(len(self.numbers[i])):
                if self.numbers[i][j] == query:
                    self.sum -= query
                    self.rows[i] += 1
                    self.columns[j] += 1
                    if self.rows[i] == 5 or self.columns[j] == 5:
                        won = True
        if won and not self.won:
            self.won = True
            return query * self.sum
        else:
            return -1


nums = list(map(lambda x: int(x), input().split(",")))
boards = []
while True:
    board = []
    if input() == "end":
        break
    for i in range(5):
        board.append(list(map(lambda x: int(x), input().split())))
    boards.append(Board(board))

for num in nums:
    for board in boards:
        res = board.check(num)
        if res != -1:
            print(res)
# The last number that gets printed is the answer
