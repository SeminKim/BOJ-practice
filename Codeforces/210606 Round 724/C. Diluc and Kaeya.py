from sys import stdin
from math import gcd
from collections import defaultdict


# think about grid point on line.


def simplify(a, b):
    if a == 0:
        return 0, 1
    if b == 0:
        return 1, 0
    foo = gcd(a, b)
    return a // foo, b // foo


def solve():
    n = int(stdin.readline().strip())
    seq = list(stdin.readline().strip())
    save = defaultdict(int)

    num_d = 0
    num_k = 0
    for i in range(n):
        if seq[i] == 'D':
            num_d += 1
        else:
            num_k += 1
        ratio = simplify(num_d, num_k)
        save[ratio] += 1
        print(save[ratio], end=' ')
    print()


t = int(stdin.readline().strip())

for _ in range(t):
    solve()
