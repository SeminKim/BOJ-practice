# https://www.acmicpc.net/problem/2467
# Use binary search

from sys import stdin

n = int(stdin.readline().strip())
seq = list(map(int, stdin.readline().split()))  # already sorted list


def find_best(start, end, target):  # find the nearest number of target
    if end == start:
        return seq[end]

    if end - start == 1:
        if abs(target - seq[start]) > abs(target - seq[end]):
            return seq[end]
        return seq[start]

    mid = (start + end) // 2

    # mid is overlapped to find 'nearest' one.
    if seq[mid] < target:
        return find_best(mid, end, target)
    if seq[mid] > target:
        return find_best(start, mid, target)

    return target


ans = float('inf')
nums = [None, None]
for i in range(n - 1):
    now = seq[i]
    foo = find_best(i + 1, n - 1, -now)

    if abs(foo + now) < ans:
        ans = abs(foo + now)
        nums[0] = now
        nums[1] = foo

print(*nums)
