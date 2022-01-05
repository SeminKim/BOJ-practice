# https://www.acmicpc.net/problem/13409
# Hackenbush! https://www.youtube.com/watch?v=ZYj4NkeGPdM&t=1640s
# evaluate each state as a number, find combination of zero sum.
# n=40, so divide to half.

from itertools import combinations
from sys import stdin

n = int(stdin.readline().strip())
nums = []
for _ in range(n):
    seq = stdin.readline().strip()
    num = 0
    curr = 0
    while curr < len(seq) and seq[curr] == seq[0]:
        curr += 1
    num += [-1, 1][seq[0] == 'B'] * curr
    level = 1
    while curr < len(seq):
        num += [-1, 1][seq[curr] == 'B'] / 2 ** level
        curr += 1
        level += 1
    nums.append((int(num * 2 ** 40), len(seq)))

left = nums[:n // 2]
right = nums[n // 2:]
l, r = len(left), len(right)

left_sums = {}
for i in range(l + 1):
    for foo in combinations(left, i):
        tmp_v, tmp_cnt = 0, 0
        for val, cnt in foo:
            tmp_v += val
            tmp_cnt += cnt
        if tmp_v in left_sums:
            left_sums[tmp_v] = max(left_sums[tmp_v], tmp_cnt)
        else:
            left_sums[tmp_v] = tmp_cnt

ans = 0
for i in range(r + 1):
    for foo in combinations(right, i):
        tmp_v, tmp_cnt = 0, 0
        for val, cnt in foo:
            tmp_v += val
            tmp_cnt += cnt
        if -tmp_v in left_sums:
            ans = max(ans, tmp_cnt + left_sums[-tmp_v])

print(ans)
