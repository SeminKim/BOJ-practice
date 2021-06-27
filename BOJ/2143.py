# https://www.acmicpc.net/problem/2143

from sys import stdin
from bisect import *


def solve():
    t = int(stdin.readline().strip())
    n = int(stdin.readline().strip())
    A = [0] + list(map(int, stdin.readline().split()))
    m = int(stdin.readline().strip())
    B = [0] + list(map(int, stdin.readline().split()))

    for i in range(1, n + 1):
        A[i] += A[i - 1]

    for i in range(1, m + 1):
        B[i] += B[i - 1]

    temp = []
    for i in range(m + 1):
        for j in range(i + 1, m + 1):
            temp.append(B[j] - B[i])
    temp.sort()

    ans = 0
    for a1 in range(n + 1):
        for a2 in range(a1 + 1, n + 1):
            now = A[a2] - A[a1]
            target = t - now
            foo = bisect_left(temp, target)
            bar = bisect_right(temp, target)
            ans += bar - foo

    return ans


print(solve())
