# https://www.acmicpc.net/problem/15591
from sys import stdin

n, q = map(int, stdin.readline().split())
tree = [[] for i in range(n+1)]

for i in range(n - 1):
    p1, p2, usa = map(int, stdin.readline().split())
    tree[p1].append((p2, usa))
    tree[p2].append((p1, usa))

for i in range(q):
    k, v = map(int, stdin.readline().split())
    cnt = 0
    boundary = [(v, float('inf'))]
    visited = [False for j in range(n+1)]
    while len(boundary) != 0:
        node = boundary.pop(0)
        now_node = node[0]
        now_usado = node[1]
        visited[now_node] = True
        for (child, usado) in tree[now_node]:
            temp = min(now_usado, usado)
            if (not visited[child]) and (temp >= k):
                cnt += 1
                boundary.append((child, temp))
                visited[child] = True
    print(cnt)
