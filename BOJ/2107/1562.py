# https://www.acmicpc.net/problem/1562
# Hard version of 10844.
# DP: dp[n][i][j] = length n, end with i, bit j: j is 0~2**10-1 (check visited num of 0~9)


from sys import stdin

n = int(stdin.readline().strip())
dp = [[[0 for _ in range(1024)] for __ in range(10)] for ___ in range(n + 1)]
for i in range(1, 10):
    dp[1][i][1 << i] = 1

for now in range(1, n):
    for end in range(10):
        for bit in range(1024):
            if dp[now][end][bit] > 0:
                if end != 0:
                    dp[now + 1][end - 1][bit | (1 << (end - 1))] += dp[now][end][bit]
                if end != 9:
                    dp[now + 1][end + 1][bit | (1 << (end + 1))] += dp[now][end][bit]

print(sum(dp[n][i][1023] for i in range(10)) % 10 ** 9)

# for 1~40 check
# ans = 0
# for foo in range(41):
#     ans += sum(dp[foo][i][1023] for i in range(10))
# print(ans)
#
