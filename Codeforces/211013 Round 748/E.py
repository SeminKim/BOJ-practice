from collections import deque
from sys import stdin

MAX_INT = 10 ** 8


def solve():
    n, k = map(int, stdin.readline().split())
    if n == 1:
        if k == 0:
            print(1)
        else:
            print(0)
        return

    graph = [[] for _ in range(n)]
    degree = [0 for _ in range(n)]
    res = [-1 for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(int, stdin.readline().split())
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)
        degree[a - 1] += 1
        degree[b - 1] += 1

    Q = deque()
    for i in range(n):
        if len(graph[i]) == 1:
            res[i] = 1
            Q.append(i)

    # BFS
    while Q:
        node = Q.popleft()
        for child in graph[node]:
            degree[child] -= 1
            if degree[child] == 1:
                Q.append(child)
                res[child] = res[node] + 1

    ans = 0
    for foo in res:
        if foo > k:
            ans += 1
    print(ans)


t = int(stdin.readline().strip())

for _ in range(t):
    stdin.readline()
    solve()
