# https://www.acmicpc.net/problem/11049
# Use DP.

from sys import stdin


def solve():
    n = int(stdin.readline().strip())
    sizes = []
    dp = [[2 ** 31 for _ in range(n)] for __ in range(n)]  # dp[i][j]: minimum cost of multiplying matrix i .. j
    for _ in range(n):
        a, b = map(int, stdin.readline().split())
        sizes.append((a, b))

    dp[n - 1][n - 1] = 0
    for dig in range(n - 1):
        dp[dig][dig] = 0
        dp[dig][dig + 1] = sizes[dig][0] * sizes[dig][1] * sizes[dig + 1][1]

    for add in range(2, n):
        for i in range(n):
            j = i + add
            if j > n - 1:
                break

            for k in range(add):
                foo = dp[i][i + k] + dp[i + k + 1][j] + sizes[i][0] * sizes[i + k][1] * sizes[j][1]
                dp[i][j] = min(dp[i][j], foo)

    return dp[0][n - 1]


print(solve())
