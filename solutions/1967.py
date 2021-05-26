# https://www.acmicpc.net/problem/1967
# Do BFS two times. Root's farthest node is one point of the longest path.

from sys import stdin
from collections import deque

n = int(stdin.readline().strip())
edges = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    node1, node2, dist = list(map(int, stdin.readline().split()))
    edges[node1].append((node2, dist))  # add tuple (destination, distance)
    edges[node2].append((node1, dist))  # add tuple (destination, distance)


def find_farthest(node):
    visited = [False for _ in range(n + 1)]

    q = deque()
    q.append((node, 0))
    ans_node = node
    ans_dist = 0
    while q:
        curr, total_cost = q.popleft()
        if total_cost > ans_dist:
            ans_node = curr
            ans_dist = total_cost

        visited[curr] = True
        for edge in edges[curr]:
            to, c = edge[0], edge[1]
            if not visited[to]:
                q.append((to, total_cost + c))

    return ans_node, ans_dist


foo, _ = find_farthest(1)
print(find_farthest(foo)[1])
