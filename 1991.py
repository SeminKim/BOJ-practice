# https://www.acmicpc.net/problem/1991

from sys import stdin

n = int(stdin.readline())
tree = {}
for _ in range(n):
    parent, left, right = stdin.readline().split()
    tree[parent] = (left, right)

PRE = []
IN = []
POST = []


def traversal(node):
    if node == '.': return
    PRE.append(node)
    traversal(tree[node][0])
    IN.append(node)
    traversal(tree[node][1])
    POST.append(node)


traversal('A')
for chr in PRE:
    print(chr, end='')
print()
for chr in IN:
    print(chr, end='')
print()
for chr in POST:
    print(chr, end='')
