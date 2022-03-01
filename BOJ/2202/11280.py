# https://www.acmicpc.net/problem/11280
# 2-SAT

from collections import deque
from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 5)
n, m = map(int, stdin.readline().split())
graph = [[] for _ in range(2 * n + 1)]  # zero is not used. 1~n and -1~-n
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[-a].append(b)
    if a != b:
        graph[-b].append(a)


# Find SCC (Tarjan's)
def dfs(curr):
    global counter, scc_idx
    counter += 1
    visited[curr] = counter
    ret = visited[curr]
    stack.append(curr)
    for child in graph[curr]:
        if visited[child] == 0:
            ret = min(ret, dfs(child))
        elif scc[child] == 0:
            ret = min(ret, visited[child])
    if ret == visited[curr]:
        scc_idx += 1
        while True:
            popped = stack.pop()
            scc[popped] = scc_idx
            if popped == curr:
                break
    return ret


counter = scc_idx = 0
visited = [0 for _ in range(2 * n + 1)]
scc = [0 for _ in range(2 * n + 1)]
for i in range(-n, n + 1):
    if visited[i] == 0 and i != 0:
        stack = deque()
        dfs(i)

for i in range(1, n + 1):
    if scc[i] == scc[-i] != 0:
        print(0)
        exit(0)
print(1)
