res = 0


def similarity_check(s1, s2):
    if len(s1) != len(s2):
        return False
    for ch in s1:
        if s2.find(str(ch)) == -1:
            return False
    return True


def seven_seg_calculator(table, s):
    tmp = ""
    for i in range(len(s)):
        tmp += str(table[s[i]])
    s = tmp
    if similarity_check(s, "abcefg"): return 0
    if similarity_check(s, "cf"): return 1
    if similarity_check(s, "acdeg"): return 2
    if similarity_check(s, "acdfg"): return 3
    if similarity_check(s, "bcdf"): return 4
    if similarity_check(s, "abdfg"): return 5
    if similarity_check(s, "abdefg"): return 6
    if similarity_check(s, "acf"): return 7
    if similarity_check(s, "abcdefg"): return 8
    if similarity_check(s, "abcdfg"): return 9


def num_indicator(nums):
    table = {
        'a': [0 for i in range(6)],
        'b': [0 for i in range(6)],
        'c': [0 for i in range(6)],
        'd': [0 for i in range(6)],
        'e': [0 for i in range(6)],
        'f': [0 for i in range(6)],
        'g': [0 for i in range(6)]
    }
    for num in nums:
        l = len(num)
        if l == 7:
            continue
        for ch in num:
            table[ch][l - 2] += 1
            table[ch][-1] += 1
    for k in table.keys():
        if table[k][-1] == 3:
            table[k] = 'e'
        elif table[k][-1] == 5:
            table[k] = 'b'
        elif table[k][-1] == 8:
            table[k] = 'f'
        elif table[k][-1] == 7 and table[k][-2] == 3:
            table[k] = 'a'
        elif table[k][-1] == 7 and table[k][-2] == 2:
            table[k] = 'c'
        elif table[k][-1] == 6 and table[k][-2] == 3:
            table[k] = 'g'
        elif table[k][-1] == 6 and table[k][-2] == 2:
            table[k] = 'd'
    return table


while True:
    query = input().split()
    if query[0] == "end":
        break
    test = query[:10]
    number = query[11:]
    char_table = num_indicator(test)
    four_d_number = 0
    for i in range(len(number)):
        four_d_number *= 10
        four_d_number += seven_seg_calculator(char_table, number[i])
    res += four_d_number

print(res)