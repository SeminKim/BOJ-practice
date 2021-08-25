# https://www.acmicpc.net/problem/11505
# Segment Tree

from sys import stdin

DIV = 1_000_000_007
n, m, k = map(int, stdin.readline().split())
seq = [0] + [int(stdin.readline().strip()) for _ in range(n)]
tree = [0 for _ in range(4 * n + 1)]


def init(pos=1, left=1, right=n):
    if left == right:
        tree[pos] = seq[left] % DIV
        return tree[pos]

    mid = (left + right) // 2
    tree[pos] = init(pos * 2, left, mid) * init(pos * 2 + 1, mid + 1, right) % DIV
    return tree[pos]


def query(pos, left, right, target_left, target_right):
    if left == target_left and right == target_right:
        return tree[pos]

    mid = (left + right) // 2
    if target_right <= mid:
        return query(pos * 2, left, mid, target_left, target_right)
    if target_left > mid:
        return query(pos * 2 + 1, mid + 1, right, target_left, target_right)

    foo = query(pos * 2, left, mid, target_left, mid)
    bar = query(pos * 2 + 1, mid + 1, right, mid + 1, target_right)
    return foo * bar % DIV


def update(pos, left, right, target, new):
    if pos == 1:
        seq[target] = new

    if left == right == target:
        tree[pos] = new
        return tree[pos]

    mid = (left + right) // 2

    if target <= mid:
        tree[pos] = update(pos * 2, left, mid, target, new) * tree[pos * 2 + 1] % DIV
    else:
        tree[pos] = tree[pos * 2] * update(pos * 2 + 1, mid + 1, right, target, new) % DIV
    return tree[pos]


init()
for _ in range(m + k):
    a, b, c = map(int, stdin.readline().split())
    if a == 1:
        update(1, 1, n, b, c)
    else:
        print(query(1, 1, n, b, c))
