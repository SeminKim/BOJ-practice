# https://www.acmicpc.net/problem/11438
# sparse table

from collections import deque
from sys import stdin

n = int(stdin.readline().strip())
graph = [[] for _ in range(n + 1)]
parent = [[0 for _ in range(n + 1)] for _ in range(17)]
depth = [0 for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

Q = deque([1])
visited = [False for _ in range(n + 1)]
visited[1] = True
while Q:
    num = Q.pop()
    for child in graph[num]:
        if not visited[child]:
            depth[child] = depth[num] + 1
            parent[0][child] = num
            Q.append(child)
            visited[child] = True

for jump in range(1, 17):
    for num in range(1, n + 1):
        parent[jump][num] = parent[jump - 1][parent[jump - 1][num]]

m = int(stdin.readline().strip())
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    if depth[a] > depth[b]:  # make b always deeper
        a, b = b, a
    diff = depth[b] - depth[a]
    for i in range(16, -1, -1):
        if diff & (1 << i):
            b = parent[i][b]

    while a != b:
        for i in range(1, 17):
            if parent[i][a] == parent[i][b]:
                a = parent[i - 1][a]
                b = parent[i - 1][b]
                break

    print(a)
