# https://www.acmicpc.net/problem/2169
# DP
from sys import stdin

INF = 10 ** 10
n, m = map(int, stdin.readline().split())
seq = [list(map(int, stdin.readline().split())) for _ in range(n)]
dp_left = [[-INF for _ in range(m)] for _ in range(n)]
dp_right = [[-INF for _ in range(m)] for _ in range(n)]
dp = [[-INF for _ in range(m)] for _ in range(n)]

for col in range(1, m):
    seq[0][col] += seq[0][col - 1]
dp_left[0] = seq[0]
dp_right[0] = seq[0]
dp[0] = seq[0]

for row in range(1, n):
    for col in range(m):
        dp_left[row][col] = max(dp_left[row][col - 1], dp[row - 1][col]) + seq[row][col]
    for col in range(-1, -m - 1, -1):
        dp_right[row][col] = max(dp_right[row][col + 1], dp[row - 1][col]) + seq[row][col]
    for col in range(m):
        dp[row][col] = max(dp_left[row][col], dp_right[row][col])

# for row in range(n):
#     print(dp[row])

print(dp[-1][-1])
