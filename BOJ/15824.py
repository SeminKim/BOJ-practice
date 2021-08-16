# https://www.acmicpc.net/problem/15824

from sys import stdin

DIV = 1_000_000_007
n = int(stdin.readline().strip())
seq = list(map(int, stdin.readline().split()))
seq.sort()

# Naive O(n^2) algorithm
# ans = 0
# for i in range(n):
#     for j in range(i + 1, n):
#         ans += (seq[j] - seq[i]) * (2 ** (j - i - 1))
# print(ans)

# Linearize
# ans = 0
# for i in range(n):
#     ans += (2 ** i - 2 ** (n - i - 1)) * seq[i]
#     ans %= DIV
# print(ans)

# Faster pow
table = [1 for _ in range(n)]
for i in range(n - 1):
    table[i + 1] = (table[i] * 2) % DIV

ans = 0
for i in range(n):
    ans += (table[i] - table[n - i - 1]) * seq[i]
    ans %= DIV

print(ans)
