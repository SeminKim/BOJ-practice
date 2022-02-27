# https://www.acmicpc.net/problem/14942
# Sparse Table

from collections import deque
from sys import stdin

MAX_INT = 200000
## log2(10**5) = 16.6

n = int(stdin.readline().strip())
ants = [int(stdin.readline().strip()) for _ in range(n)]
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b, c = map(int, stdin.readline().split())
    graph[a - 1].append((b - 1, c))
    graph[b - 1].append((a - 1, c))
parent = [(-1, -1) for _ in range(n)]


# first, make tree to rooted tree.
def rooted(curr):
    for child, cost in graph[curr]:
        parent[child] = (curr, cost)
        graph[child].remove((curr, cost))
        rooted(child)
    return


parent[0] = (0, 0)
rooted(0)

warp_node = [[-1 for _ in range(17)] for _ in range(n)]
warp_cost = [[MAX_INT for _ in range(17)] for _ in range(n)]


# fill up warp information
def dfs(curr, acc):
    for idx in range(17):
        if 2 ** idx > len(history):
            break
        target_node, target_acc = history[-(2 ** idx)]
        if acc < target_acc:
            break
        warp_node[curr][idx] = target_node
        warp_cost[curr][idx] = acc - target_acc
    history.append((curr, acc))
    for child, cost in graph[curr]:
        dfs(child, acc + cost)
    history.pop()


history = deque()
dfs(0, 0)

# find the highest available node with warping
for node in range(n):
    energy = ants[node]
    pos = node
    while energy > 0 and pos > 0:
        for i in range(17):
            if warp_cost[pos][i] > energy:
                break
        i -= 1
        if i == -1:
            break
        energy -= warp_cost[pos][i]
        pos = warp_node[pos][i]
    print(pos + 1)
