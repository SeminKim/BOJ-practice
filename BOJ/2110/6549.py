# https://www.acmicpc.net/problem/6549
# Segment Tree and Binary Search

from bisect import *
from collections import deque
from sys import stdin

while True:
    seq = list(map(int, stdin.readline().split()))
    if seq[0] == 0:
        break
    n = seq.pop(0)
    # Segment tree with minimum
    tree = [0 for _ in range(n)] + seq
    for i in range(n - 1, 0, -1):
        tree[i] = min(tree[2 * i], tree[2 * i + 1])


    def query(left, right):
        left += n
        right += n
        res = tree[left]
        while left < right:
            if left % 2 == 1:
                res = min(res, tree[left])
                left += 1
            if right % 2 == 0:
                res = min(res, tree[right])
                right -= 1
            left >>= 1
            right >>= 1
        if left == right:
            res = min(res, tree[left])
        return res


    # for binary search
    seq = [(num, idx) for idx, num in enumerate(seq)]
    seq.sort()
    ans = 0
    Q = deque()
    Q.append((0, n - 1))

    while Q:
        start, end = Q.popleft()
        minimum = query(start, end)
        ans = max(ans, minimum * (end - start + 1))
        cuts = deque()
        idx = bisect_left(seq, (minimum, -1))
        while idx < n and seq[idx][0] == minimum:
            _, target = seq[idx]
            if start <= target <= end:
                cuts.append(target)
            idx += 1
        cuts.appendleft(start - 1)
        cuts.append(end + 1)
        for i in range(len(cuts) - 1):
            first = cuts[i]
            second = cuts[i + 1]
            if first + 2 == second:
                ans = max(ans, tree[first + n + 1])
            elif first + 2 < second:
                Q.append((first + 1, second - 1))

    print(ans)
