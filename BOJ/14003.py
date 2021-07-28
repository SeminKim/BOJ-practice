# https://www.acmicpc.net/problem/14003
# LIS with binary search.

from sys import stdin
from bisect import bisect_left

n = int(stdin.readline().strip())
seq = list(map(int, stdin.readline().split()))
LIS = [seq[0]]
IDX = [0]

for i in range(1, n):
    if seq[i] > LIS[-1]:
        IDX.append(len(LIS))
        LIS.append(seq[i])
    else:
        idx = bisect_left(LIS, seq[i])
        IDX.append(idx)
        LIS[idx] = seq[i]

length = len(LIS)
print(length)

counter = length - 1
pointer = n - 1
res = []
while counter >= 0:
    if IDX[pointer] == counter:
        res.append(seq[pointer])
        counter -= 1
    pointer -= 1

print(' '.join((map(str, reversed(res)))))
