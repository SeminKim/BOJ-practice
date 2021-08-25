# https://www.acmicpc.net/problem/11404
# Floyd Warshall. Make adjacent matrix and update minimum cost using DP.

from sys import stdin

n = int(stdin.readline())
m = int(stdin.readline())

adj = [[float('inf') for _ in range(n)] for _ in range(n)]

for bus in range(m):
    start, end, cost = map(int, stdin.readline().split())
    adj[start - 1][end - 1] = min(adj[start - 1][end - 1], cost)

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j or j == k or k == i: continue
            adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j])

for row in adj:
    for cost in row:
        if cost == float('inf'):
            print(0, end=' ')
        else:
            print(cost, end=' ')
    print()
