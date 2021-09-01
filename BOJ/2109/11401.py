# https://www.acmicpc.net/problem/11401

from sys import stdin

DIV = 1_000_000_007
factorial: [int] = [1]
for i in range(1, 4_000_000 + 1):
    i %= DIV
    factorial.append((factorial[-1] * i) % DIV)

n, k = map(int, stdin.readline().split())

ans = factorial[n]
ans *= pow(factorial[k], DIV - 2, DIV)
ans %= DIV
ans *= pow(factorial[n - k], DIV - 2, DIV)
ans %= DIV

print(ans)
