from itertools import combinations
from math import gcd
from sys import stdin


def solve():
    n = int(stdin.readline().strip())
    seq = list(map(int, stdin.readline().split()))
    diff = set()
    for a, b in combinations(seq, 2):
        diff.add(abs(a - b))

    ans = 0
    for i in diff:
        ans = gcd(ans, i)

    if ans == 0:
        print(-1)
    else:
        print(ans)


t = int(stdin.readline().strip())

for _ in range(t):
    solve()
