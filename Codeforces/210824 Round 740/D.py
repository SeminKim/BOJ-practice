from sys import stdin

### Not Solved Yet: TLE ###

def route(i, j):
    return i // j - i // (j + 1)


n, m = map(int, stdin.readline().split())

dp = [0 for _ in range(n + 1)]
dp[1] = 1

for i in range(2, n + 1):
    temp = 0
    for j in range(1, i):
        temp += ((1 + route(i, j)) * dp[j]) % m
    dp[i] = temp % m

print(dp[-1])