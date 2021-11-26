from sys import stdin
import heapq
from collections import deque
from bisect import bisect_left


def solve():
    stdin.readline()
    n, k = map(int, stdin.readline().split())
    friends = list(map(int, stdin.readline().split()))
    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    record = [10 ** 6 for _ in range(n + 1)]

    Q = deque()
    for fr in friends:
        record[fr] = 0
        Q.append((fr, 0))

    while Q:
        pos, cost = Q.popleft()
        for node in graph[pos]:
            if record[node] > cost + 1:
                record[node] = cost + 1
                Q.append((node, cost + 1))

    Q.append((1, 0))
    best = [10 ** 6 for _ in range(n + 1)]
    while Q:
        pos, cost = Q.popleft()
        for node in graph[pos]:
            if best[node] > cost + 1:
                best[node] = cost + 1
                Q.append((node, cost + 1))

    for i in range(2, n + 1):
        if len(graph[i]) == 1 and record[i] > best[i]:
            print('YES')
            return

    print('NO')
    return


t = int(stdin.readline().strip())

for _ in range(t):
    solve()
