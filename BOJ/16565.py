# https://www.acmicpc.net/problem/16565

from sys import stdin

DIV = 10007
factorials = [1 for _ in range(52 + 1)]
for i in range(1, 52 + 1):
    factorials[i] = (factorials[i - 1] * i) % DIV


def combination(a, b):
    foo = factorials[a]
    bar = (factorials[b] * factorials[a - b]) % DIV
    return (foo * pow(bar, DIV - 2, DIV)) % DIV


n = int(stdin.readline().strip())
m = n // 4

ans = 0

for i in range(1, m + 1):
    ans += ((-1) ** (i + 1) * combination(13, i) * combination(52 - 4 * i, n - 4 * i)) % DIV

print(ans % DIV)
