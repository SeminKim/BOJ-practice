# https://www.acmicpc.net/problem/1761
# calculate distance from root, then find lowest common ancestor.

from collections import deque
from sys import stdin

n = int(stdin.readline().strip())
temp = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, cost = map(int, stdin.readline().split())
    temp[a].append([b, cost])
    temp[b].append([a, cost])

distance = [0 for _ in range(n + 1)]
parent = [1 for _ in range(n + 1)]
depth = [0 for _ in range(n + 1)]
check = [False for _ in range(n + 1)]
Q = deque()
Q.append([1, 0, 0])  # node, distance to root, depth
check[1] = True
while Q:
    curr, dist, d = Q.popleft()
    for node, cost in temp[curr]:
        if check[node]:
            continue
        parent[node] = curr
        depth[node] = d + 1
        distance[node] = dist + cost
        check[node] = True
        Q.append([node, dist + cost, d + 1])


def query(a, b):
    a, b = sorted([a, b], key=lambda x: depth[x])  # b is deeper
    ans = distance[a] + distance[b]

    # make depths same
    while depth[a] != depth[b]:
        b = parent[b]

    while a != b:
        a = parent[a]
        b = parent[b]

    ans -= 2 * distance[a]
    return ans


for q in range(int(stdin.readline().strip())):
    print(query(*map(int, stdin.readline().split())))
