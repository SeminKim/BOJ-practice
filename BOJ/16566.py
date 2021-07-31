# https://www.acmicpc.net/problem/16566
# Use binary search, check by set.

from sys import stdin
from bisect import bisect_left

_, _, k = map(int, stdin.readline().split())
available = list(map(int, stdin.readline().split()))
available.sort()
seq = list(map(int, stdin.readline().split()))
used = set()

res = [None for _ in range(k)]
for i in range(k):
    foo = bisect_left(available, seq[i] + 1)
    while available[foo] in used:
        foo += 1

    print(available[foo])
    used.add(available[foo])
