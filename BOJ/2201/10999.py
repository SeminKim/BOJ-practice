# https://www.acmicpc.net/problem/10999
# Segment tree with lazy propagation

from sys import stdin

n, m, k = map(int, stdin.readline().split())
tree = [0] * n
lazy = [0] * n
height = len(bin(n)) - 2
for _ in range(n):
    tree.append(int(stdin.readline()))

# initialize
for i in range(n - 1, -1, -1):
    tree[i] = tree[2 * i] + tree[2 * i ^ 1]


# update all parents
def build(pos):
    while pos > 1:
        pos //= 2
        tree[pos] = tree[2 * pos] + tree[2 * pos + 1] + lazy[pos]


# lazily modifying value: for leaf, do not have to be lazy.
def modify(pos, val):
    tree[pos] += val
    if pos < n:
        lazy[pos] += val


# propagate changes from root
def propagate(pos):
    for s in range(height, 0, -1):
        i = pos >> s
        if lazy[i] != 0:
            modify(2 * i, lazy[i] // 2)
            modify(2 * i + 1, lazy[i] // 2)
            lazy[i] = 0


# for update instruction
def update(left, right, delta):
    left += n - 1
    right += n - 1
    initial_left, initial_right = left, right
    while left < right:
        if left & 1 == 1:
            modify(left, delta)
            left += 1
        if right & 1 == 0:
            modify(right, delta)
            right -= 1
        left //= 2
        right //= 2
        delta *= 2

    if left == right:
        modify(left, delta)
    build(initial_left)
    build(initial_right)
    return


# for query instruction
def query(left, right):
    left += n - 1
    right += n - 1
    propagate(left)
    propagate(right)
    res = 0
    while left < right:
        if left % 2 == 1:
            res = res + tree[left]
            left += 1
        if right % 2 == 0:
            res = res + tree[right]
            right -= 1
        left //= 2
        right //= 2

    if left == right:
        res = res + tree[right]

    return res


for _ in range(m + k):
    # print(f'{tree=}\n{lazy=}')
    op = list(map(int, stdin.readline().split()))
    if op[0] == 1:
        update(op[1], op[2], op[3])
    else:
        print(query(op[1], op[2]))
# print(f'{tree=}\n{lazy=}')
