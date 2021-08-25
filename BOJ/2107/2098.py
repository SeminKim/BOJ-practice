# https://www.acmicpc.net/problem/2098
# Simple backtracking => 16! ~= 10**13; probably TLE for n=16.
# DP with bit masking => 16*16*(2^16) ~= 10**7; acceptable.


from sys import stdin

INF = 10 ** 8
n = int(stdin.readline().strip())
adj = [list(map(int, stdin.readline().split())) for _ in range(n)]
dp = [[[INF for _ in range(1 << n)] for _ in range(n)] for _ in range(n)]
dp[0][0][1] = 0

for level in range(n - 1):
    for now in range(n):
        for bit in range(1 << n):
            if dp[level][now][bit] >= INF:
                continue
            for num in range(1, n):
                if bit & (1 << num) != 0 or adj[now][num] == 0:
                    continue
                res = dp[level][now][bit] + adj[now][num]
                dp[level + 1][num][bit | (1 << num)] = min(dp[level + 1][num][bit | (1 << num)], res)

ans = INF
for foo in range(n):
    if adj[foo][0] == 0:
        continue
    bar = dp[n - 1][foo][-1] + adj[foo][0]
    ans = min(ans, bar)

print(ans)
