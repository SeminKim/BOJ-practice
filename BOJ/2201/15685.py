# https://www.acmicpc.net/problem/15685
# Implementation

from collections import deque
from sys import stdin

used = [[False for _ in range(101)] for _ in range(101)]
direction = [[0, 1], [-1, 0], [0, -1], [1, 0]]


def make_dragon():
    x, y, d, g = map(int, stdin.readline().split())
    points = deque()
    points.append([y, x])
    used[y][x] = True
    points.append([y + direction[d][0], x + direction[d][1]])
    used[y + direction[d][0]][x + direction[d][1]] = True
    while g > 0:
        last_r, last_c = points[-1]
        for i in reversed(range(len(points) - 1)):
            r, c = points[i]
            new_r, new_c = last_r + c - last_c, last_c - r + last_r
            points.append([new_r, new_c])
            if 0 <= new_r <= 100 and 0 <= new_c <= 100:
                used[new_r][new_c] = True
        g -= 1
    return


n = int(stdin.readline().strip())
for _ in range(n):
    make_dragon()

ans = 0
for i in range(100):
    for j in range(100):
        ans += (used[i][j] and used[i][j + 1] and used[i + 1][j] and used[i + 1][j + 1])

print(ans)
