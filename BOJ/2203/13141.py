# https://www.acmicpc.net/problem/13141

from sys import stdin

MAX_DIST = 10 ** 5
n, m = map(int, stdin.readline().split())
dist = [[MAX_DIST] * (n + 1) for _ in range(n + 1)]
lines = []
for _ in range(m):
    s, e, l = map(int, stdin.readline().split())
    lines.append([s, e, l])
    dist[s][e] = min(dist[s][e], l)
    dist[e][s] = min(dist[e][s], l)

for i in range(1, n + 1):
    dist[i][i] = 0

# Get min distance for every pair of nodes.
# V<<E so use Floyd-Warshall
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

ans = MAX_DIST
for start_node in range(1, n + 1):
    # use temp*2 to ensure integer value.
    temp = 0
    for s, e, l in lines:
        if dist[start_node][s] > dist[start_node][e]:
            s, e = e, s
        if dist[start_node][s] + l == dist[start_node][e]:
            temp = max(temp, 2 * dist[start_node][e])
        else:
            temp = max(temp, 2 * dist[start_node][e] + (l - dist[start_node][e] + dist[start_node][s]))
    ans = min(ans, temp)

print(ans / 2.0)
