# https://www.acmicpc.net/problem/13710
# Utilize characteristic of xor, and use sum of pairwise xor in O(kn)

from sys import stdin

n = int(stdin.readline().strip())
seq = list(map(int, stdin.readline().split()))
xor_acc = [0]
for num in seq:
    xor_acc.append(xor_acc[-1] ^ num)

ans = 0
for digit in range(31):
    ones = sum((i >> digit) & 1 for i in xor_acc)
    zeroes = n + 1 - ones
    ret = ones * zeroes
    ans += (1 << digit) * ret

print(ans)

# def checker(num_list):
#     ret = num_list[0]
#     for i in range(1, len(num_list)):
#         ret ^= num_list[i]
#     return ret
#
#
# real = 0
# for i in range(n):
#     for j in range(i, n):
#         real += checker(seq[i:j + 1])
# print(real)
