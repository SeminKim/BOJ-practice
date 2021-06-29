# https://www.acmicpc.net/problem/1007
# Select n/2 points to subtract, left n/2 points are added.

from sys import stdin
from itertools import combinations


def solve():
    n = int(stdin.readline().strip())
    points = []
    sum_x = 0
    sum_y = 0
    for _ in range(n):
        x, y = map(int, stdin.readline().split())
        sum_x += x
        sum_y += y
        points.append([x, y])

    ans = 10 ** 8

    for selected in combinations(range(n), n // 2):
        current_x = sum_x
        current_y = sum_y
        for idx in selected:
            current_x -= 2 * points[idx][0]
            current_y -= 2 * points[idx][1]
        ans = min(ans, (current_x ** 2 + current_y ** 2) ** 0.5)

    print(ans)


t = int(stdin.readline().strip())

for _ in range(t):
    solve()
