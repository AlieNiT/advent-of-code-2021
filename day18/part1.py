def get_num(s, i):
    begin_i = i
    end_i = i
    while begin_i >= 0 and (48 <= ord(s[begin_i]) <= 57):
        begin_i -= 1
    while end_i < len(s) and (48 <= ord(s[end_i]) <= 57):
        end_i += 1
    begin_i += 1
    return begin_i, end_i, int(s[begin_i:end_i])


def explosion_index(s):
    open_brackets = 0
    for i in range(len(s)):
        if s[i] == '[':
            open_brackets += 1
        elif s[i] == ']':
            open_brackets -= 1
        if open_brackets == 5:
            return i
    return -1


def split(s):
    for i in range(len(s) - 1):
        if 48 <= ord(s[i]) <= 57 and \
                48 <= ord(s[i + 1]) <= 57:
            return i
    return -1


def reduce(s):
    i = explosion_index(s)
    if i != -1:
        end_i = i + s[i:].find("]")
        numbers = [int(x) for x in s[i + 1: end_i].split(",")]
        after_i = end_i + 1
        while after_i < len(s) and not 48 <= ord(s[after_i]) <= 57:
            after_i += 1
        if after_i < len(s):
            after_num = get_num(s, after_i)
            s = s[:after_num[0]] + str(after_num[2] + numbers[1]) + s[after_num[1]:]
        s = s[:i] + "0" + s[end_i + 1:]
        before_i = i - 1

        while before_i >= 0 and not 48 <= ord(s[before_i]) <= 57:
            before_i -= 1
        if before_i >= 0:
            before_num = get_num(s, before_i)
            s = s[:before_num[0]] + str(before_num[2] + numbers[0]) + s[before_num[1]:]
        return reduce(s)
    else:
        i = split(s)
        if i != -1:
            num = get_num(s, i)
            split_pair = "[" + str(int(num[2] // 2)) + "," + str(int(num[2] // 2 + num[2] % 2)) + "]"
            s = s[:num[0]] + split_pair + s[num[1]:]
            return reduce(s)
    return s

def mag(s):
    coefficient = 1
    res = 0
    i = 0
    while i < len(s):
        if s[i] == '[':
            coefficient *= 3
        elif s[i] == ',':
            coefficient *= 2/3
        elif s[i] == ']':
            coefficient /= 2
        else:
            num = get_num(s, i)
            res += num[2] * coefficient
            i = num[1] - 1
        i += 1
    return int(res)
res = ""
first = input()
while True:
    second = input()
    if second == "end":
        break
    res = "[" + first + "," + second + "]"
    res = reduce(res)
    first = res
# inp = input()
# print(reduce(inp))
print(res)
print(mag(res))