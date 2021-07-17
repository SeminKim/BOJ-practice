# https://www.acmicpc.net/problem/10844
# Simple DP.

from sys import stdin

n = int(stdin.readline().strip())

dp = [[0 for _ in range(10)] for __ in range(n + 1)]
dp[1] = [0] + [1 for _ in range(9)]

for now in range(2, n + 1):
    for num in range(10):
        if num == 0:
            dp[now][0] = dp[now - 1][1]
        elif num == 9:
            dp[now][9] = dp[now - 1][8]
        else:
            dp[now][num] = dp[now - 1][num - 1] + dp[now - 1][num + 1]

print(sum(dp[n]) % 10 ** 9)
