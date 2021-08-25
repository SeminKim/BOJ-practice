# https://www.acmicpc.net/problem/1865
# Use Bellman-Ford

from sys import stdin

MAX_INT = 10 ** 8


def solve():
    n, m, w = map(int, stdin.readline().split())

    adj = [[MAX_INT for _ in range(n + 1)] for _ in range(n + 1)]
    edges = []

    for _ in range(m):
        start, end, cost = map(int, stdin.readline().split())
        if cost < adj[start][end]:  # adj is symmetric until now
            adj[start][end] = cost
            adj[end][start] = cost

    for _ in range(w):
        start, end, cost = map(int, stdin.readline().split())
        cost *= -1
        if cost < adj[start][end]:
            adj[start][end] = cost

    for row in range(1, n + 1):
        for col in range(1, n + 1):
            if adj[row][col] < MAX_INT:
                edges.append((row, col, adj[row][col]))

    for _ in range(n - 1):  # iterate n-1 time to get shortest path value
        for edge in edges:
            for row in range(1, 2):  # is it okay to check only one point?
                if adj[row][edge[0]] + edge[2] < adj[row][edge[1]]:
                    adj[row][edge[1]] = adj[row][edge[0]] + edge[2]

    for edge in edges:  # if cost change in one additional iteration, there is negative cycle
        for row in range(1, 2):
            if adj[row][edge[0]] + edge[2] < adj[row][edge[1]]:
                return "YES"
    return "NO"


t = int(stdin.readline().strip())

for _ in range(t):
    print(solve())
