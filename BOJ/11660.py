# https://www.acmicpc.net/problem/11660
# Save sum of (1,1) to (x,y) at table(x,y)

from sys import stdin

n, m = map(int, stdin.readline().split())
table = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    temp = 0
    row = [0] + list(map(int, stdin.readline().split()))
    for j in range(1, n + 1):
        temp += row[j]
        table[i][j] = temp + table[i - 1][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    print(table[x2][y2] - table[x1 - 1][y2] - table[x2][y1 - 1] + table[x1 - 1][y1 - 1])
