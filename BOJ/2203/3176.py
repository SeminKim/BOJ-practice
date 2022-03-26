# https://www.acmicpc.net/problem/3176
# LCA (sparse table)


from collections import deque
from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 5)
INF = 10 ** 8
n = int(stdin.readline().strip())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

height = [INF for _ in range(n + 1)]
sparse = [[[-1, INF, -INF] for _ in range(n + 1)] for _ in
          range(17)]  # node, shortest, longest, zeroth is direct parent.

root = 1
Q = deque()
Q.append((root, 0))
while Q:
    curr, depth = Q.popleft()
    height[curr] = depth
    for node, cost in graph[curr]:
        if height[node] <= depth:
            continue
        sparse[0][node] = (curr, cost, cost)
        Q.append((node, depth + 1))

# Fill Sparse Table
for jump in range(1, 17):
    for node in range(1, n + 1):
        curr_node, curr_min, curr_max = sparse[jump - 1][node]
        if curr_node == -1:
            continue
        up_node, up_min, up_max = sparse[jump - 1][curr_node]
        if up_node == -1:
            continue
        sparse[jump][node] = (up_node, min(curr_min, up_min), max(curr_max, up_max))


def solve(fst, snd):
    # assume fst is always farther from root.
    if height[fst] < height[snd]:
        fst, snd = snd, fst
    minimum = INF
    maximum = -INF
    diff = height[fst] - height[snd]
    jump = 0
    while diff > 0:
        if diff & 1:
            fst, next_min, next_max = sparse[jump][fst]
            minimum = min(minimum, next_min)
            maximum = max(maximum, next_max)
        diff >>= 1
        jump += 1

    # Sparse Jump
    if fst == snd:
        return minimum, maximum
    jump = 16
    while jump >= 0:
        fst_next = sparse[jump][fst]
        snd_next = sparse[jump][snd]
        if jump == 0 or (-1 != fst_next[0] != snd_next[0] != -1):
            fst = fst_next[0]
            snd = snd_next[0]
            minimum = min(minimum, fst_next[1], snd_next[1])
            maximum = max(maximum, fst_next[2], snd_next[2])
            if jump == 0 and fst != snd:
                jump += 1
        jump -= 1
    return minimum, maximum


k = int(stdin.readline().strip())
for _ in range(k):
    a, b = map(int, stdin.readline().split())
    print(*solve(a, b))
