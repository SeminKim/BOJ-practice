# https://www.acmicpc.net/problem/14553

from sys import stdin

MOD = 10 ** 9 + 9
n = int(stdin.readline().strip())
C = [0] * (n + 1)
B = [0] * (n + 1)
A = [0] * (n + 1)
A[1] = 1
B[1] = 1
C[1] = 1

for i in range(2, n + 1):
    # A[i]
    tmp = i
    for j in range(1, i):
        tmp = (tmp + B[j] + (i - j) * C[j]) % MOD
    A[i] = tmp
    # B[i]
    B[i] = (A[i - 1] + B[i - 1] + C[i - 1]) % MOD
    # C[i]
    tmp = 1
    for j in range(1, i):
        tmp = (tmp + B[j] + (i - j) * A[j]) % MOD
    C[i] = tmp

print(A[-1])
