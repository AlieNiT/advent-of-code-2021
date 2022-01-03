import math

inp = input()
num_of_bits = 8

num = str(bin(int(inp, 16))[2:].zfill(len(inp) * 4))
print(num)

def calculator(num, i):
    # if '1' not in num[i:]:
    #     return -1, -1
    res = 0
    version = int(num[i:i + 3], 2)
    i += 3
    type = int(num[i:i + 3], 2)
    print("type:" + str(type))
    i += 3
    if type == 4:
        while num[i] == '1':
            res *= 16
            res += int(num[i + 1:i + 5], 2)
            i += 5
        res *= 16
        res += int(num[i + 1:i + 5], 2)
        print(res)
        i += 5
        return res, i
    sub_packets = []
    l_type = num[i]
    if l_type == '0':
        i += 1
        l = int(num[i:i + 15], 2)
        i += 15
        end = i + l
        while i < end:
            outcome, I = calculator(num, i)
            if outcome != -1:
                sub_packets.append(outcome)
                i = I
    elif l_type == '1':
        i += 1
        l = int(num[i:i + 11], 2)
        i += 11
        while len(sub_packets) < l:
            outcome, I = calculator(num, i)
            sub_packets.append(outcome)
            i = I
    print(sub_packets)
    if type == 0:
        for j in range(len(sub_packets)):
            res += sub_packets[j]
    elif type == 1:
        res = 1
        for j in range(len(sub_packets)):
            res *= sub_packets[j]
    elif type == 2:
        res = math.inf
        for j in range(len(sub_packets)):
            if res > sub_packets[j]:
                res = sub_packets[j]
    elif type == 3:
        for j in range(len(sub_packets)):
            if res < sub_packets[j]:
                res = sub_packets[j]
    elif type == 5:
        res = int(sub_packets[0] > sub_packets[1])
    elif type == 6:
        res = int(sub_packets[0] < sub_packets[1])
    elif type == 7:
        res = int(sub_packets[0] == sub_packets[1])
    print("res:" + str(res))
    print()
    return res, i


print(calculator(num, 0)[0])
