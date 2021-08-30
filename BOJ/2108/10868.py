# https://www.acmicpc.net/problem/10868
# Segment Tree

from sys import stdin

INF = 10 ** 10
n, m = map(int, stdin.readline().split())
seq = [int(stdin.readline().strip()) for _ in range(n)]
tree = [0 for _ in range(n)] + seq

for i in range(n - 1, -1, -1):
    tree[i] = min(tree[i << 1], tree[i << 1 | 1])


def query(start, end):  # here, start / end is in 1-based index.
    start += n - 1
    end += n - 1
    temp = INF
    # start from even index, end with odd
    while start < end:
        if start & 1:
            temp = min(temp, tree[start])
            start += 1
        if end ^ 1:
            temp = min(temp, tree[end])
            end -= 1
        start >>= 1
        end >>= 1

    if start == end:
        temp = min(temp, tree[start])

    return temp


for _ in range(m):
    a, b = map(int, stdin.readline().split())
    print(query(a, b))
