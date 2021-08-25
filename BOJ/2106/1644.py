# https://www.acmicpc.net/problem/1644
# Use sieve to find primes, save partial sum and binary search among them.

from sys import stdin
from bisect import bisect_left

n = int(stdin.readline().strip())

# make partial sum list of primes <= n
check = [False, False] + [True for _ in range(2, n + 1)]

cnt = 0
partial_sum = [0]
for i in range(2, n + 1):
    if check[i]:
        cnt += i
        partial_sum.append(cnt)
        for multi in range(2 * i, n + 1, i):
            check[multi] = False

# find answer with binary search
ans = 0
for i in range(len(partial_sum)):
    target = n + partial_sum[i]
    if target > partial_sum[-1]:
        break
    idx = bisect_left(partial_sum, target, lo=i + 1)
    if target == partial_sum[idx]:
        ans += 1

print(ans)
