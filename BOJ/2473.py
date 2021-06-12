# https://www.acmicpc.net/problem/2473
# Use binary search => n^2 * log n
from sys import stdin
from bisect import *

n = int(stdin.readline().strip())
seq = list(map(int, stdin.readline().split()))
seq.sort()

best = 3 * 10 ** 9
ans = [-1, -1, -1]
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        target = -1 * (seq[i] + seq[j])
        foo = bisect_right(seq, target, lo=j + 1)
        if foo == n:
            cases = [n - 1]
        elif foo == j + 1:
            cases = [foo]
        else:
            cases = [foo, foo - 1]

        for idx in cases:
            if abs(seq[i] + seq[j] + seq[idx]) < best:
                ans = [seq[i], seq[j], seq[idx]]
                best = abs(seq[i] + seq[j] + seq[idx])

print(*ans)
