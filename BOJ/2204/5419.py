# https://www.acmicpc.net/problem/5419
# Segment Tree with Coordinate Compression

from bisect import *
from sys import stdin


def solve():
    n = int(stdin.readline().strip())
    island = [list(map(int, stdin.readline().split())) for _ in range(n)]
    y_unique = sorted(set(island[i][1] for i in range(n)))
    tree = [0 for _ in range(2 * n)]

    # coordinate compression
    def get_idx(y):
        return bisect_left(y_unique, y)

    ans = 0
    for x, y in sorted(island, key=lambda x: (-x[0], x[1])):
        y_idx = get_idx(y)
        # find sum of 0~y_idx
        left = n
        right = n + y_idx
        ret = 0
        while left < right:
            if left & 1:
                ret += tree[left]
                left += 1
            if not right & 1:
                ret += tree[right]
                right -= 1
            left >>= 1
            right >>= 1
        if left == right:
            ret += tree[left]
        ans += ret
        # update tree
        pos = n + y_idx
        while pos:
            tree[pos] += 1
            pos >>= 1

        # print(x, y, ret)

    print(ans)


T = int(stdin.readline().strip())
for _ in range(T):
    solve()
