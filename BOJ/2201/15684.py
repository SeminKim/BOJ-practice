# https://www.acmicpc.net/problem/15684
# Brute force

from itertools import combinations
from sys import stdin

n, m, h = map(int, stdin.readline().split())
used = [[False for _ in range(n - 1)] for _ in range(h)]
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    used[a - 1][b - 1] = True

candidate = []
for i in range(h):
    for j in range(n - 1):
        if not used[i][j]:
            if (j != 0 and used[i][j - 1]) or (j != n - 2 and used[i][j + 1]):
                continue
            candidate.append([i, j])

pos = [i for i in range(n)]
for row in range(h):
    for col in range(n - 1):
        if used[row][col]:
            pos[col], pos[col + 1] = pos[col + 1], pos[col]

if sum(pos[i] != i for i in range(n)) > 6:
    print(-1)
    exit(0)


def simulate():
    pos = [i for i in range(n)]
    for row in range(h):
        for col in range(n - 1):
            if used[row][col]:
                pos[col], pos[col + 1] = pos[col + 1], pos[col]

    return pos == [i for i in range(n)]


def solve():
    if simulate():
        print(0)
        return

    for num in [1, 2, 3]:
        for selected in combinations(candidate, num):
            for (x, y) in selected:
                used[x][y] = True
                if y != 0 and used[x][y - 1]:
                    break
                if y != n - 2 and used[x][y + 1]:
                    break
            else:
                if simulate():
                    print(num)
                    return
            for (x, y) in selected:
                used[x][y] = False

    print(-1)
    return


solve()
