# https://www.acmicpc.net/problem/16235

from sys import stdin
from collections import defaultdict

n, m, k = map(int, stdin.readline().split())
A = [list(map(int, stdin.readline().split())) for _ in range(n)]
land = [[5] * n for _ in range(n)]
trees = [[{} for _ in range(n)] for _ in range(n)]
for _ in range(m):
    r, c, a = map(int, stdin.readline().split())
    trees[r - 1][c - 1][a] = 1

for _ in range(k):
    new_trees = [[defaultdict(int) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if len(trees[i][j]) == 0:
                land[i][j] += A[i][j]
            else:
                dead = 0
                breed = 0
                for a, num in sorted(trees[i][j].items()):
                    if alive := min(num, land[i][j] // a):
                        land[i][j] -= a * alive
                        new_trees[i][j][a + 1] += alive
                    dead += (a // 2) * (num - alive)
                    if a % 5 == 4:
                        breed += alive
                if breed:
                    for dr, dc in ([-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]):
                        nr, nc = i + dr, j + dc
                        if 0 <= nr < n and 0 <= nc < n:
                            new_trees[nr][nc][1] += breed

                land[i][j] += dead + A[i][j]
    trees = new_trees

ans = 0
for i in range(n):
    for j in range(n):
        ans += sum(trees[i][j].values())
print(ans)

# 10 1 1000
# 100 100 100 100 100 100 100 100 100 100
# 100 100 100 100 100 100 100 100 100 100
# 100 100 100 100 100 100 100 100 100 100
# 100 100 100 100 100 100 100 100 100 100
# 100 100 100 100 100 100 100 100 100 100
# 100 100 100 100 100 100 100 100 100 100
# 100 100 100 100 100 100 100 100 100 100
# 100 100 100 100 100 100 100 100 100 100
# 100 100 100 100 100 100 100 100 100 100
# 100 100 100 100 100 100 100 100 100 100
# 1 1 1
