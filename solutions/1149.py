# https://www.acmicpc.net/problem/1149
# Use DP. 1~n-1까지의 결과를 바탕으로 n번째 최소 cost를 경우를 나누어 계산
from sys import stdin

n = int(input())
table = [[0 for _ in range(4)] for _ in range(n + 1)]

for row in range(1, n + 1):
    table[row][1], table[row][2], table[row][3] = map(int, stdin.readline().split())

for row in range(2, n + 1):
    table[row][1] += min(table[row - 1][2], table[row - 1][3])
    table[row][2] += min(table[row - 1][3], table[row - 1][1])
    table[row][3] += min(table[row - 1][1], table[row - 1][2])

print(min(table[n][1:]))
