# https://www.acmicpc.net/problem/1647
# Use Kruskal

from sys import stdin


class Node:
    def __init__(self):
        self.parent = None
        self.rank = 1

    def find(self):
        if self.parent is None:
            return self
        self.parent = self.parent.find()
        return self.parent

    def union(self, other):
        head1 = self.find()
        head2 = other.find()
        if head1.rank >= head2.rank:
            head2.parent = head1
            head1.rank += 1
        else:
            head1.parent = head2
            head2.rank += 1


def solve():
    n, m = map(int, stdin.readline().split())
    lines = []
    nodes = [Node() for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, stdin.readline().split())
        lines.append((a, b, c))

    lines.sort(key=lambda x: x[2])
    ans = 0
    last = 0
    for line in lines:
        a, b, c = line
        if nodes[a].find() != nodes[b].find():
            nodes[a].union(nodes[b])
            ans += c
            last = c
    return ans - last


print(solve())
