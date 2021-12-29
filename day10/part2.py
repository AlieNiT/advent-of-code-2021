scores = []
while True:
    inp = input()
    if inp == "end":
        break
    stack = []
    corrupted = False
    for i in range(len(inp)):
        if inp[i] == '<' or \
                inp[i] == '{' or \
                inp[i] == '[' or \
                inp[i] == '(':
            stack.append(inp[i])

        elif ord(inp[i]) - ord(stack[-1]) == 2 or ord(inp[i]) - ord(stack[-1]) == 1:
            stack.pop()
        else:
            corrupted = True
            break
    if corrupted:
        continue
    n = len(stack)
    score = 0
    digit = 0
    for i in range(n):
        ch = stack.pop()
        if ch == '(': digit = 1
        if ch == '[': digit = 2
        if ch == '{': digit = 3
        if ch == '<': digit = 4
        score = score * 5 + digit
    scores.append(score)

scores.sort()
print(scores[len(scores) // 2])
