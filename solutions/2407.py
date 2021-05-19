# https://www.acmicpc.net/problem/2407
# Memoization, nCm = n-1Cm-1 + n-1Cm

from sys import stdin

n, m = map(int, stdin.readline().split())

table = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

for col in range(1, n + 1):
    table[1][col] = col

for row in range(2, m + 1):
    for col in range(row, n + 1):
        table[row][col] = table[row - 1][col - 1] + table[row][col - 1]

print(table[m][n])
