inp = input()
num_of_bits = 8

num = str(bin(int(inp, 16))[2:].zfill(len(inp) * 4))


def version_summer(num, i):
    if '1' not in num[i:]:
        return 0
    print(num)
    print(num[i:i + 3])
    version = int(num[i:i + 3], 2)
    print("version:" + str(version))
    i += 3
    type = int(num[i:i + 3], 2)
    print("type:" + str(type))
    i += 3
    if type == 4:
        while num[i] == '1':
            i += 5
        i += 5
        if i >= len(num):
            return version
        else:
            return version + version_summer(num, i)
    else:
        if num[i] == '0':
            i += 1
            # l = int(num[i:i + 15], 2)
            i += 15
            return version + version_summer(num, i)
        else:
            i += 12
            return version + version_summer(num, i)

print(version_summer(num, 0))
