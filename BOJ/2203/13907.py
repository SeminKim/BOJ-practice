# https://www.acmicpc.net/problem/13907
# Dijkstra with counting number of edges.

import heapq
from sys import stdin

INF = 10 ** 10
n, m, k = map(int, stdin.readline().split())
s, d = map(int, stdin.readline().split())
s, d = s - 1, d - 1
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b, w = map(int, stdin.readline().split())
    graph[a - 1].append([b - 1, w])
    graph[b - 1].append([a - 1, w])

# Dijkstra
Q = []
heapq.heappush(Q, (0, 0, s))  # acc dist, edge count, node
visits = [[(INF, INF)] for _ in range(n)]  # acc dist, edge count
visits[s] = [(0, 0)]
while Q:
    acc, edge, pos = heapq.heappop(Q)
    for child, cost in graph[pos]:
        nacc = acc + cost
        nedge = edge + 1
        for i in range(len(visits[child])):
            prevdist, prevcount = visits[child][i]
            if nacc >= prevdist and nedge >= prevcount:  # better case already exists.
                break
            elif nacc == prevdist or nedge == prevcount:  # change to better case.
                visits[child][i] = (nacc, nedge)
                heapq.heappush(Q, (nacc, nedge, child))
                break
            elif nacc < prevdist and nedge < prevcount:  # current is better than existing one.
                visits[child][i] = (nacc, nedge)
                heapq.heappush(Q, (nacc, nedge, child))
                break
        else:
            # add case
            visits[child].append((nacc, nedge))
            heapq.heappush(Q, (nacc, nedge, child))

candidate = dict()
for dist, count in visits[d]:
    if count in candidate:
        candidate[count] = min(candidate[count], dist)
    else:
        candidate[count] = dist

print(min(candidate.values()))
for _ in range(k):
    p = int(stdin.readline().strip())
    best = INF
    for count in candidate.keys():
        candidate[count] += count * p
        best = min(best, candidate[count])
    print(best)
