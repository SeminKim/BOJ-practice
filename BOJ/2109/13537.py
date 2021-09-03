# https://www.acmicpc.net/problem/13537
# segment tree: save sorted list, do binary search

from bisect import bisect_left
from sys import stdin

n = int(stdin.readline().strip())
seq = [[int(i)] for i in stdin.readline().split()]
tree = [[] for _ in range(n)] + seq

# initialize
for i in range(n - 1, -1, -1):
    left = tree[i << 1]
    right = tree[i << 1 | 1]
    # l, r = 0, 0
    # while l < len(left) and r < len(right):
    #     if left[l] < right[r]:
    #         tree[i].append(left[l])
    #         l += 1
    #     elif left[l] > right[r]:
    #         tree[i].append(right[r])
    #         r += 1
    #     else:
    #         tree[i].append(left[l])
    #         tree[i].append(right[r])
    #         l += 1
    #         r += 1
    # if l != len(left):
    #     tree[i] += left[l:]
    # if r != len(right):
    #     tree[i] += right[r:]
    tree[i] = sorted(left + right)  # this is faster :(


def query(start, end, target):
    start += n - 1
    end += n - 1
    target += 1
    res = 0
    while start < end:
        if start & 1:
            idx = bisect_left(tree[start], target)
            res += len(tree[start]) - idx
            start += 1
        if not end & 1:
            idx = bisect_left(tree[end], target)
            res += len(tree[end]) - idx
            end -= 1
        start >>= 1
        end >>= 1

    if start == end:
        idx = bisect_left(tree[start], target)
        res += len(tree[start]) - idx

    return res


m = int(stdin.readline().strip())
for _ in range(m):
    i, j, k = map(int, stdin.readline().split())
    print(query(i, j, k))
