# https://www.acmicpc.net/problem/13977
# Fermat's Little Theorem.
# a^(m-1) % m = 1 ==> a * a^(m-2) % m = 1

from sys import stdin

MOD = 1_000_000_007

factorial = [1, 1]
for i in range(2, 4 * 10 ** 6 + 1):
    factorial.append((factorial[i - 1] * i) % MOD)


def solve(n, k):
    numerator = factorial[n]
    denominator = (factorial[k] * factorial[n - k]) % MOD
    denominator = pow(denominator, MOD - 2, MOD)
    return (numerator * denominator) % MOD


m = int(stdin.readline().strip())
for _ in range(m):
    n, k = map(int, stdin.readline().split())
    print(solve(n, k))
