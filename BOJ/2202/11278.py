# https://www.acmicpc.net/problem/11277
# Bitmasking

from sys import stdin

n, m = map(int, stdin.readline().split())
seq = [list(map(int, stdin.readline().split())) for _ in range(m)]

for bit in range(1 << n):
    for a, b in seq:
        if a > 0:
            fst = bit & (1 << (a - 1))
        else:
            fst = not (bit & (1 << (-a - 1)))
        if b > 0:
            snd = bit & (1 << (b - 1))
        else:
            snd = not (bit & (1 << (-b - 1)))
        if not (fst or snd):
            break
    else:
        print(1)
        for digit in range(n):
            print(1 if bit & (1 << digit) else 0, end=' ')
        break
else:
    print(0)
