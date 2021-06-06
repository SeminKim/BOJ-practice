# https://www.acmicpc.net/problem/1197
# Use Kruskal's algorithm.

from sys import stdin


class Node:
    def __init__(self):
        self.parent = None
        self.rank = 1

    def find(self):
        if self.parent is None:
            return self
        return self.parent.find()

    def union(self, other):
        head1 = self.find()
        head2 = other.find()
        if head1.rank >= head2.rank:
            head2.parent = head1
            head1.rank += 1
        else:
            head1.parent = head2
            head2.rank += 1


lines = []
V, E = map(int, stdin.readline().split())
nodes = [Node() for _ in range(V)]

for line in range(E):
    start, end, cost = map(int, stdin.readline().split())
    lines.append([cost, start - 1, end - 1])

lines.sort(key=lambda x: x[0])
ans = 0

for line in lines:
    cost, start, end = line
    if nodes[start].find() != nodes[end].find():
        nodes[start].union(nodes[end])
        ans += cost

print(ans)
