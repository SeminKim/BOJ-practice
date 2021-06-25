# https://www.acmicpc.net/problem/20040
# Disjoint set

from sys import stdin


class Node:
    def __init__(self, name):
        self.name = name
        self.parent = self
        self.rank = 0

    def find_parent(self):
        if self.parent is self:
            return self

        self.parent = self.parent.find_parent()
        return self.parent

    def union(self, other):
        foo = self.find_parent()
        bar = other.find_parent()

        if foo.rank >= bar.rank:
            bar.parent = foo
            foo.rank += 1
        else:
            foo.parent = bar
            bar.rank += 1


def solve():
    n, m = map(int, stdin.readline().split())
    nodes = [Node(i) for i in range(n)]
    for i in range(1, m + 1):
        a, b = map(int, stdin.readline().split())

        if nodes[a].find_parent() == nodes[b].find_parent():
            return i
        nodes[a].union(nodes[b])
    return 0


print(solve())
