# https://www.acmicpc.net/problem/9527

from sys import stdin

a, b = map(lambda x: bin(int(x))[2:], stdin.readline().split())


def zero_to_full_ones(length):
    return 2 ** (length - 1) * length


def zero_to_arbitrary(num_str):
    if len(num_str) == 1:
        return int(num_str, base=2)

    length = len(num_str)
    num = int(num_str, base=2)
    if num_str[0] == '1':
        return zero_to_full_ones(length - 1) + (num - 2 ** (length - 1) + 1) + zero_to_arbitrary(num_str[1:])

    else:
        return zero_to_arbitrary(num_str[1:])


ans = zero_to_arbitrary(b) - zero_to_arbitrary(a) + a.count('1')
print(ans)
