# https://www.acmicpc.net/problem/7453
# Divide to 2 + 2 and use dictionary(n^2logn)
import collections
from sys import stdin

n = int(stdin.readline().strip())
A, B, C, D = [[0 for _ in range(n)] for _ in range(4)]
for i in range(n):
    a, b, c, d = map(int, stdin.readline().split())
    A[i] = a
    B[i] = b
    C[i] = c
    D[i] = d

first = collections.defaultdict(int)
for i in range(n):
    for j in range(n):
        first[A[i] + B[j]] += 1

ans = 0
for i in range(n):
    for j in range(n):
        if first.get(-C[i] - D[j]):
            ans += first[-C[i] - D[j]]
print(ans)
