# https://www.acmicpc.net/problem/2042
# Segment Tree

from sys import stdin

n, m, k = map(int, stdin.readline().split())
seq = [0]

for _ in range(n):
    seq.append(int(stdin.readline().strip()))

tree = [0 for _ in range(4 * n + 1)]


def init(pos, left, right):
    if left == right:
        tree[pos] = seq[left]
        return tree[pos]

    mid = (left + right) // 2
    tree[pos] = init(pos * 2, left, mid) + init(pos * 2 + 1, mid + 1, right)

    return tree[pos]


init(1, 1, n)


def query(wanted_left, wanted_right):
    return query_helper(1, 1, n, wanted_left, wanted_right)


def query_helper(pos, left, right, wanted_left, wanted_right):
    if left == wanted_left and right == wanted_right:
        return tree[pos]

    mid = (left + right) // 2
    if wanted_right <= mid:
        return query_helper(pos * 2, left, mid, wanted_left, wanted_right)

    if mid < wanted_left:
        return query_helper(pos * 2 + 1, mid + 1, right, wanted_left, wanted_right)

    return query_helper(pos * 2, left, mid, wanted_left, mid) + \
           query_helper(pos * 2 + 1, mid + 1, right, mid + 1, wanted_right)


def update(wanted, new):
    delta = new - seq[wanted]
    if delta == 0:
        return
    seq[wanted] = new
    update_helper(1, 1, n, wanted, delta)


def update_helper(pos, left, right, wanted, delta):
    if left == right == wanted:
        tree[pos] += delta
        return

    tree[pos] += delta
    mid = (left + right) // 2
    if wanted <= mid:
        update_helper(pos * 2, left, mid, wanted, delta)
        return

    if mid < wanted:
        update_helper(pos * 2 + 1, mid + 1, right, wanted, delta)
        return


for _ in range(m + k):
    a, b, c = map(int, stdin.readline().split())
    if a == 1:
        update(b, c)
    else:
        print(query(b, c))
