# https://www.acmicpc.net/problem/14245
# Segment Tree

from sys import stdin

n = int(stdin.readline().strip())
tree = [0 for _ in range(n)] + list(map(int, stdin.readline().split()))
m = int(stdin.readline().strip())
for _ in range(m):
    line = list(map(int, stdin.readline().split()))
    if line[0] == 1:
        _, a, b, c = line
        a += n
        b += n
        while a < b:
            if a & 1:
                tree[a] ^= c
                a += 1
            if not b & 1:
                tree[b] ^= c
                b -= 1
            a >>= 1
            b >>= 1
        if a == b:
            tree[a] ^= c
    else:
        _, num = line
        num += n
        res = 0
        while num:
            res ^= tree[num]
            num >>= 1
        print(res)
