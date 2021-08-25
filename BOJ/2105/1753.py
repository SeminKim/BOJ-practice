# https://www.acmicpc.net/problem/1753
# Use Dijkstra.

from sys import stdin
import heapq

V, E = map(int, stdin.readline().split())
K = int(stdin.readline())
lines = [[] for _ in range(V + 1)]
costs = [float('inf') for _ in range(V + 1)]
for i in range(E):
    start, end, cost = map(int, stdin.readline().split())
    lines[start].append([end, cost])

costs[K] = 0
Q = []
heapq.heappush(Q, (0, K))

while len(Q) != 0:
    x = heapq.heappop(Q)[1]
    for (child, cost) in lines[x]:
        if costs[child] > costs[x] + cost:
            costs[child] = costs[x] + cost
            heapq.heappush(Q, (costs[child], child))

for i in range(1, V + 1):
    if costs[i] == float('inf'):
        print("INF")
    else:
        print(costs[i])
