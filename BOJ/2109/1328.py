# https://www.acmicpc.net/problem/1328
# DP

from sys import stdin
from math import comb
from functools import lru_cache

DIV = 1000000007
N, L, R = map(int, stdin.readline().split())
factorial = [1]
for i in range(1, N + 1):
    factorial.append(factorial[-1] * i % DIV)


# 서로 다른 n개의 수를 permutation 하여 왼쪽에서 보았을 때 k개가 보이도록 하는 경우의 수
@lru_cache(maxsize=None)
def helper(n, k):
    if n < k:
        return 0
    if n == k == 0:
        return 1
    if n == 0 or k == 0:
        return 0
    res = 0
    for i in range(1, n + 1):
        res += comb(n - 1, i - 1) * helper(i - 1, k - 1) * factorial[n - i]
        res %= DIV
    return res


# 가장 큰 빌딩위치에 따라 분할하여 생각
ans = 0
for i in range(1, N + 1):
    ans += comb(N - 1, i - 1) * helper(i - 1, L - 1) * helper(N - i, R - 1)
    ans %= DIV

print(ans)
