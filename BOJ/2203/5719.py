# https://www.acmicpc.net/problem/5719
# Dijkstra -> mark history -> Dijkstra

import heapq
from sys import stdin

INF = 10 ** 8

while True:
    n, m = map(int, stdin.readline().split())
    if n == m == 0:
        break
    s, d = map(int, stdin.readline().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v, p = map(int, stdin.readline().split())
        graph[u].append([v, p])

    # Dijkstra with history(prev)
    prev = [[] for _ in range(n)]
    dist = [INF for _ in range(n)]
    Q = [(0, s)]
    heapq.heapify(Q)
    dist[s] = 0
    while Q:
        acc, pos = heapq.heappop(Q)
        if dist[pos] < acc:
            continue

        for child, cost in graph[pos]:
            nacc = acc + cost
            if nacc < dist[child]:
                dist[child] = nacc
                prev[child] = [pos]
                heapq.heappush(Q, (nacc, child))
            elif nacc == dist[child]:
                prev[child].append(pos)

    # track history
    in_path = [[False for _ in range(n)] for _ in range(n)]
    def dfs(curr):
        for before in prev[curr]:
            if not in_path[before][curr]:
                in_path[before][curr] = True
                dfs(before)
    dfs(d)

    # Do dijkstra again
    dist = [INF for _ in range(n)]
    Q = [(0, s)]
    heapq.heapify(Q)
    dist[s] = 0
    while Q:
        acc, pos = heapq.heappop(Q)
        if dist[pos] < acc:
            continue
        for child, cost in graph[pos]:
            if in_path[pos][child]:
                continue
            nacc = acc + cost
            if nacc < dist[child]:
                dist[child] = nacc
                heapq.heappush(Q, (nacc, child))

    print(dist[d] if dist[d] < INF else -1)
