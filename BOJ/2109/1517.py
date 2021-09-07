# https://www.acmicpc.net/problem/1517
# Segment tree, check in small to large order

from sys import stdin

n = int(stdin.readline().strip())
tree = [0 for _ in range(2 * n)]
seq = list(map(int, stdin.readline().split()))
Q = [i for i in range(n)]
Q.sort(key=lambda x: seq[x])


def query(start, end):  # in zero-based index
    start += n
    end += n
    res = 0
    while start < end:
        if start & 1:
            res += tree[start]
            start += 1
        if not end & 1:
            res += tree[end]
            end -= 1
        start >>= 1
        end >>= 1
    if start == end:
        res += tree[start]

    return res


def update(pos, target):  # in zero-based index
    pos += n
    tree[pos] = target
    while pos > 1:
        tree[pos >> 1] = tree[pos] + tree[pos ^ 1]
        pos >>= 1


ans = 0
for i in range(n):
    pos = Q[i]
    ans += query(pos, n - 1)
    update(pos, 1)

print(ans)
