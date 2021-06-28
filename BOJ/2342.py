# https://www.acmicpc.net/problem/2342
# Use DP. dp[idx][i][j] is minimum cost of satisfying seq[idx] by (i, j)

from sys import stdin

seq = [0] + list(map(int, stdin.readline().split()))[:-1]
INF = 10 ** 6


def get_distance(a, b):
    if a == 0 or b == 0:
        return 2
    if a == b:
        return 1
    elif (a - b) % 2 == 0:
        return 4
    return 3


def get_paired_distance(x, y):
    if 0 in y:
        if y[0] == y[1] == 0:
            return INF
        elif y[0] == 0:
            if x[0] != 0:
                return INF
            return get_distance(x[1], y[1])
        else:
            if x[1] != 0:
                return INF
            return get_distance(x[0], y[0])

    if x[0] != y[0] and x[1] != y[1]:
        return get_distance(x[0], y[0]) + get_distance(x[1], y[1])
    elif x[0] == y[0]:
        return get_distance(x[1], y[1])
    else:
        return get_distance(x[0], y[0])


n = len(seq)

dp = [[[INF for _ in range(5)] for _ in range(5)] for _ in range(n)]
dp[0][0][0] = 0

for idx in range(1, n):
    target = seq[idx]
    for i in range(5):
        for j in range(5):
            if i == j:
                dp[idx][i][j] = INF
            elif i != target and j != target:
                dp[idx][i][j] = INF
            else:
                dp[idx][i][j] = min(
                    dp[idx - 1][x][y] + get_paired_distance([x, y], [i, j]) for x in range(5) for y in range(5))

ans = INF
for foo in dp[-1]:
    ans = min(ans, min(foo))

print(ans)
