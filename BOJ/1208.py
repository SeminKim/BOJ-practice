from sys import stdin
from itertools import combinations
from collections import defaultdict

n, s = map(int, stdin.readline().split())
seq = list(map(int, stdin.readline().split()))

left = seq[:n // 2]
right = seq[n // 2:]

left_expanded = defaultdict(int)
right_expanded = defaultdict(int)

for num in range(1, len(left) + 1):
    for selection in combinations(left, num):
        left_expanded[sum(selection)] += 1

for num in range(1, len(right) + 1):
    for selection in combinations(right, num):
        right_expanded[sum(selection)] += 1

cnt = 0
cnt += left_expanded[s]
cnt += right_expanded[s]

for a in left_expanded.keys():
    cnt += left_expanded[a] * right_expanded[s - a]

print(cnt)
