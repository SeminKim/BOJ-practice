# https://www.acmicpc.net/problem/11725
# Use BFS

from sys import stdin
from collections import deque

n = int(stdin.readline())
ans = [-1 for _ in range(n + 1)]
ans[1] = 0
graph = [[] for _ in range(n + 1)]


for i in range(n - 1):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

Q = deque()
Q.append(1)
while len(Q) != 0:
    node = Q.popleft()
    for child in graph[node]:  # type:int
        if ans[child] == -1:
            ans[child] = node
            Q.append(child)


for i in range(2, n + 1):
    print(ans[i])
