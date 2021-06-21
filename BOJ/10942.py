# https://www.acmicpc.net/problem/10942
# Use DP

from sys import stdin

n = int(stdin.readline().strip())
seq = stdin.readline().split()
m = int(stdin.readline().strip())

dp = [[0 for _ in range(n)] for __ in range(n)]

for dig in range(n):  # diagonal
    dp[dig][dig] = 1
    if dig < n - 1 and seq[dig] == seq[dig + 1]:
        dp[dig][dig + 1] = 1

for add in range(2, n):
    for start in range(n):
        end = start + add
        if end >= n:
            break
        if seq[start] == seq[end]:
            dp[start][end] = dp[start + 1][end - 1]

for _ in range(m):
    s, e = map(int, stdin.readline().split())
    print(dp[s - 1][e - 1])
