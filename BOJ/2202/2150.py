# https://www.acmicpc.net/problem/2150
# SCC (Tarjan's Algorithm)

from collections import deque
from sys import stdin, setrecursionlimit

setrecursionlimit(10**5)

v, e = map(int, stdin.readline().split())
graph = [[] for _ in range(v)]  # zero is not used
for _ in range(e):
    a, b = map(int, stdin.readline().split())
    graph[a - 1].append(b - 1)

visited = [0 for _ in range(v)]
counted = [False for _ in range(v)]
scc = []


# Return best approachable node number.
def dfs(curr):
    global counter
    counter += 1
    visited[curr] = counter
    ret = visited[curr]
    stack.append(curr)
    for child in graph[curr]:
        if not visited[child]:
            ret = min(ret, dfs(child))
        elif not counted[child]:
            ret = min(ret, visited[child])
    if ret == visited[curr]:
        temp = []
        while True:
            popped = stack.pop()
            counted[popped] = True
            temp.append(popped)
            if popped == curr:
                break
        temp.sort()
        scc.append(temp)
    return ret


stack = deque()
counter = 0
for i in range(v):
    if not visited[i]:
        dfs(i)

scc.sort()
print(len(scc))
for line in scc:
    for num in line:
        print(num + 1, end=' ')
    print(-1)
