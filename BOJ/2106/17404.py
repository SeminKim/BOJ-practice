# https://www.acmicpc.net/problem/17404
# Transform to linear case and DP (RGB1 in 1149)
from sys import stdin
from copy import deepcopy


def solve():
    n = int(stdin.readline().strip())
    foo = []
    for _ in range(n):
        foo.append(list(map(int, stdin.readline().split())))

    ans = 10 ** 7
    for i in range(3):
        dp = deepcopy(foo)
        dp.append([10 ** 7, 10 ** 7, 10 ** 7])
        dp[-1][i] = 0
        dp[0] = [10 ** 7, 10 ** 7, 10 ** 7]
        dp[0][i] = foo[0][i]

        for row in range(1, n + 1):
            dp[row][0] += min(dp[row - 1][1], dp[row - 1][2])
            dp[row][1] += min(dp[row - 1][2], dp[row - 1][0])
            dp[row][2] += min(dp[row - 1][0], dp[row - 1][1])

        ans = min(ans, dp[n][i])
    return ans


print(solve())
