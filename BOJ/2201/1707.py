# https://www.acmicpc.net/problem/1707
# DFS

from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)


def dfs(graph, visited, curr):
    target = - visited[curr]
    for child in graph[curr]:
        if visited[child] == 0:
            visited[child] = target
            if not dfs(graph, visited, child):
                return False
        elif visited[child] == -target:
            return False
    return True


def solve():
    v, e = map(int, stdin.readline().split())
    graph = [[] for _ in range(v)]
    for _ in range(e):
        a, b = map(int, stdin.readline().split())
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)
    visited = [0 for _ in range(v)]
    for i in range(v):
        if visited[i] == 0:
            visited[i] = 1
            if not dfs(graph, visited, i):
                print("NO")
                return
    print("YES")
    return


k = int(stdin.readline().strip())
for _ in range(k):
    solve()
