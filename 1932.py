# https://www.acmicpc.net/problem/1149
# Use DP.
from sys import stdin

n = int(stdin.readline())
table = [[0 for _ in range(n)] for _ in range(n)]

for row in range(n):
    col = 0
    for num in list(map(int, stdin.readline().split())):
        table[row][col] = num + max(table[row-1][col-1], table[row-1][col]) #table[-1]은 0이라 상관 없음
        col += 1

print(max(table[n-1]))
