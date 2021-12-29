res = 0
while True:
    inp = input()
    if inp == "end":
        break
    stack = []
    for i in range(len(inp)):
        # print(stack)
        if inp[i] == '<' or \
                inp[i] == '{' or \
                inp[i] == '[' or \
                inp[i] == '(':
            stack.append(inp[i])

        elif ord(inp[i]) - ord(stack[-1]) == 2 or ord(inp[i]) - ord(stack[-1]) == 1:
            stack.pop()
        else:
            if inp[i] == '>': res += 25137
            if inp[i] == ')': res += 3
            if inp[i] == '}': res += 1197
            if inp[i] == ']': res += 57
            break

print(res)