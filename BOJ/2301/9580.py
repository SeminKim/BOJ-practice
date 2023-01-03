# https://www.acmicpc.net/problem/9580

from sys import stdin

N, A, B = map(int, stdin.readline().split())

# Case 1
dp1 = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for n in range(1, N + 1):
    delta = N - n
    # a+b should be A + B - delta
    for x in range(delta + 1):
        y = delta - x
        a = A - x
        b = B - y
        if a < 0 or b < 0:
            dp1[n][x] = 0
        else:
            slots = 2 * a + b + 2
            dp1[n][x] = 2 / slots + 2 * a / slots * dp1[n - 1][x + 1] + b / slots * dp1[n - 1][x]

# Case 2
dp2 = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for n in range(1, N + 1):
    delta = N - n
    # a+b should be A + B - delta
    for x in range(delta + 1):
        y = delta - x
        a = A - x
        b = B - y
        if a < 0 or b < 0:
            dp2[n][x] = 0
        else:
            slots = 2 * a + b + 1
            dp2[n][x] = 1 / slots + 2 * a / slots * dp2[n - 1][x + 1] + b / slots * dp2[n - 1][x]

print(f'{dp1[-1][0]:.16f}\n{dp2[-1][0]:.16f}')
