# https://www.acmicpc.net/problem/1167
# Use kind of recursion?

from sys import stdin
from collections import deque


class Node:
    def __init__(self, num):
        self.num = num
        self.child_nodes = []  # list of Node
        self.child_dist = []  # list of integer
        self.farthest_dist = None

    # Find the distance of farthest descendant.
    # Use recursion on first call. Once calculated, it is saved and reused.
    def farthest_descendant_dist(self):
        if self.farthest_dist is not None:
            return self.farthest_dist

        if len(self.child_nodes) == 0:
            self.farthest_dist = 0
            return 0

        self.farthest_dist = max(dist + node.farthest_descendant_dist()
                                 for node, dist in zip(self.child_nodes, self.child_dist))

        return self.farthest_dist


# Problem starts.
v = int(stdin.readline().strip())
edges = [[] for _ in range(v + 1)]
nodes = [Node(i) for i in range(v + 1)]
visited = [False for _ in range(v + 1)]

# Temporarily save input.
for _ in range(v):
    line = list(map(int, stdin.readline().split()))
    for idx in range(1, len(line) - 1, 2):
        edges[line[0]].append((line[idx], line[idx + 1]))  # tuple of two int (destination, cost)

# Make node 1 as a root node. Not necessarily 1.
Q = deque()
Q.append(1)
while Q:
    i = Q.popleft()
    visited[i] = True
    for e in edges[i]:
        if not visited[e[0]]:
            nodes[i].child_nodes.append(nodes[e[0]])
            nodes[i].child_dist.append(e[1])
            Q.append(e[0])


# Find the diameter of tree starting from root.
# There are two candidates for longest path: through the root or not.
def diameter(root: Node):
    if len(root.child_nodes) == 0:
        return 0

    not_through_root = max(diameter(child) for child in root.child_nodes)

    through_root = [0]
    for node, dist in zip(root.child_nodes, root.child_dist):
        through_root.append(dist + node.farthest_descendant_dist())

    dist1 = max(through_root)
    through_root.remove(dist1)
    dist2 = max(through_root)
    return max(not_through_root, dist1 + dist2)


print(diameter(nodes[1]))
