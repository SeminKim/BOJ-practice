from sys import stdin

T = int(stdin.readline().strip())
INF = 10 ** 20
for t in range(T):
    N, P = map(int, stdin.readline().split())
    products = [[0] * P] + [sorted(map(int, stdin.readline().split())) for _ in range(N)]
    dp = [[INF for _ in range(P)] for _ in range(N + 1)]  # nth, curr end
    dp[0] = [0 for _ in range(P)]

    for i in range(1, N + 1):
        leftmost = products[i][0]
        rightmost = products[i][-1]
        for j in range(P):
            for k in range(P):
                ret = dp[i - 1][j]
                start = products[i - 1][j]
                end = products[i][k]
                if start < end:
                    if leftmost < start:
                        ret += 2 * (start - leftmost)
                    ret += rightmost - start
                    ret += abs(rightmost - end)
                else:
                    if rightmost > start:
                        ret += 2 * (rightmost - start)
                    ret += start - leftmost
                    ret += abs(leftmost - end)
                dp[i][k] = min(dp[i][k], ret)

    ans = min(dp[-1])
    print(f'Case #{t + 1}: {ans}')
