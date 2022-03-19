# https://www.acmicpc.net/problem/3679
# Just sort by angle, be careful on last points.

from math import atan2
from sys import stdin


def parallel(fst, snd, thd):
    dx1, dy1 = snd[0] - fst[0], snd[1] - fst[1]
    dx2, dy2 = thd[0] - snd[0], thd[1] - snd[1]
    return dx1 * dy2 == dx2 * dy1


def solve():
    n, *seq = map(int, stdin.readline().split())
    points = [(seq[i], seq[i + 1]) for i in range(0, 2 * n, 2)]
    point_to_number = {points[i]: i for i in range(n)}
    points.sort()
    base = points.pop(0)
    points.sort(key=lambda x: (atan2(x[1] - base[1], x[0] - base[0]), x[0], x[1]))
    lasts = []
    points = [base] + points
    until = n - 1
    while until > 1 and parallel(base, points[until], points[until - 1]):
        lasts.append(points[until])
        until -= 1
    ans = points[:until] + lasts + [points[until]]

    # print(ans)
    for pnt in ans:
        print(point_to_number[pnt], end=' ')
    print()


c = int(stdin.readline().strip())
for _ in range(c):
    solve()

# 2
# 6 0 0 10 0 5 10 2 2 8 2 5 5
# 7 0 0 10 0 5 10 2 2 8 2 5 5 5 3

# 2
# 4 0 5 0 0 0 -5 1 0
# 7 1 1 0 0 5 0 3 0 7 0 2 0 9 0

# 1
# 3 -10 -10 10 -10 0 100

# 1
# 5 0 0 2 0 0 2 0 3 0 4
