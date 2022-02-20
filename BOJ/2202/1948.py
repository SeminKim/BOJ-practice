# https://www.acmicpc.net/problem/1948
# find longest distance, do bfs backward.
from collections import deque
from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 5)
n = int(stdin.readline().strip())
m = int(stdin.readline().strip())
graph = [[] for _ in range(n + 1)]
back_graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    graph[a].append([b, c])
    back_graph[b].append([a, c])

start, end = map(int, stdin.readline().split())

distances = [0 for _ in range(n + 1)]


def find_longest(curr, acc):
    for child, cost in graph[curr]:
        nacc = acc + cost
        if distances[child] < nacc:
            distances[child] = nacc
            find_longest(child, nacc)


find_longest(start, 0)
longest = distances[end]
visited = set()
ans = 0
Q = deque()
Q.append((end, distances[end]))
while Q:
    curr, acc = Q.popleft()
    for parent, cost in back_graph[curr]:
        nacc = acc - cost
        if distances[parent] == nacc:
            ans += 1
            if parent not in visited:
                visited.add(parent)
                Q.append((parent, nacc))

print(longest)
print(ans)
