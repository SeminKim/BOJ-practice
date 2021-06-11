from sys import stdin
from bisect import *


def solve():
    n, l, r = map(int, input().split())
    seq = list(map(int, stdin.readline().split()))
    seq.sort()

    ans = 0
    for i in range(n - 1):
        left = l - seq[i]
        right = r - seq[i]
        a = bisect_left(seq, left, lo=i + 1)
        b = bisect_right(seq, right, lo=i + 1)

        ans += b - a

    print(ans)


t = int(stdin.readline().strip())

for _ in range(t):
    solve()
