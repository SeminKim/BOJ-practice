# https://www.acmicpc.net/problem/3653
# Build n+m sized segment tree with zero/one flag

from sys import stdin

t = int(stdin.readline().strip())
for _ in range(t):
    n, m = map(int, stdin.readline().split())
    size = n + m
    top = size + m
    seq = list(map(int, stdin.readline().split()))
    seg_idx = [top + i for i in range(n)]
    # tree
    tree = [0 for _ in range(2 * size)]
    for i in seg_idx:
        tree[i] = 1
    for i in reversed(range(size)):
        tree[i] = tree[i << 1] + tree[i << 1 | 1]

    for selected in seq:
        selected -= 1
        idx = seg_idx[selected]

        # print partial sum, left is top
        left = top
        right = idx - 1
        res = 0
        while left < right:
            if left & 1:
                res += tree[left]
                left += 1
            if not right & 1:
                res += tree[right]
                right -= 1
            left >>= 1
            right >>= 1
        if left == right:
            res += tree[left]
        print(res, end=' ')

        # adjust flag bit.
        tree[idx] = 0
        top -= 1
        seg_idx[selected] = top
        tree[top] = 1

        # update tree
        i = idx >> 1
        while i:
            tree[i] = tree[i << 1] + tree[i << 1 | 1]
            i >>= 1
        i = top >> 1
        while i:
            tree[i] = tree[i << 1] + tree[i << 1 | 1]
            i >>= 1

    print()
