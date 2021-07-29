# https://www.acmicpc.net/problem/2568
# LIS <=> non-crossing line

from sys import stdin
from bisect import bisect_left

n = int(stdin.readline().strip())
seq = []
for _ in range(n):
    seq.append(list(map(int, stdin.readline().split())))

seq.sort()
LIS = [seq[0][1]]
IDX = [0]

for i in range(1, n):
    if seq[i][1] > LIS[-1]:
        LIS.append(seq[i][1])
        IDX.append(len(LIS) - 1)

    else:
        idx = bisect_left(LIS, seq[i][1])
        LIS[idx] = seq[i][1]
        IDX.append(idx)

print(n - len(LIS))

res = []
goal = len(LIS) - 1
for i in range(len(IDX) - 1, -1, -1):
    if IDX[i] == goal:
        goal -= 1
    else:
        res.append(seq[i][0])

for i in reversed(res):
    print(i)
