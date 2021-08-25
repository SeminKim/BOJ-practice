# https://www.acmicpc.net/problem/16566
# Use binary search, check by set.

from sys import stdin
from bisect import bisect_left

n, _, k = map(int, stdin.readline().split())
available = list(map(int, stdin.readline().split()))
count = [0 for _ in range(n + 1)]
for i in available:
    count[i] += 1

available = []
for i in range(n):
    for j in range(count[i]):
        available.append(i)

seq = list(map(int, stdin.readline().split()))
used = set()

res = [None for _ in range(k)]
for i in range(k):
    foo = bisect_left(available, seq[i] + 1)
    while available[foo] in used:
        foo += 1

    print(available[foo])
    used.add(available[foo])
