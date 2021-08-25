# https://www.acmicpc.net/problem/1086
# DP with bitmask
import math
from collections import deque
from sys import stdin

n = int(stdin.readline().strip())
nums = []
lens = []
for _ in range(n):
    num = int(stdin.readline().strip())
    lens.append(len(str(num)))
    nums.append(num)
k = int(stdin.readline().strip())

for i in range(n):
    nums[i] %= k

dp = [[0 for _ in range(k)] for _ in range(1 << n)]  # dp[bit][mod] = num. of permutation x, s.t  x%k == mod.
Q = deque()
Q.append(0)
visited = [False for _ in range(1 << n)]
dp[0][0] = 1
visited[0] = True

while Q:
    bit = Q.popleft()
    temp = 0
    for i in range(n):
        shift = pow(10, lens[i], k)
        mod = nums[i]
        if 1 << i & bit:
            foo = 1 << i ^ bit
            for m in range(k):
                dp[bit][(shift * m + mod) % k] += dp[foo][m]

        else:
            foo = 1 << i | bit
            if not visited[foo]:
                Q.append(foo)
                visited[foo] = True

p = dp[-1][0]
q = sum(dp[-1])
div = math.gcd(p, q)

print(f'{p // div}/{q // div}')
