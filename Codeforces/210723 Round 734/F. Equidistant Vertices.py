from sys import stdin

### NOT SOLVED YET ###


def solve():
    lines = []
    stdin.readline()
    n, k = map(int, stdin.readline().split())
    adj = [[float('inf') for _ in range(n + 1)] for _ in range(n + 1)]

    for _ in range(n-1):
        a, b = map(int, stdin.readline().split())
        adj[a][b] = 1
        adj[b][a] = 1

    for i in range(n):
        adj[i][i] = 0

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i == j or j == k or k == i: continue
                adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j])



t = int(stdin.readline().strip())

for _ in range(t):
    solve()
