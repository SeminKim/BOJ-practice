# 대충 크기정렬하고 자리바꾸려했는데, 순서에 따라 다르게 나옴 . . . Topologial Sort를 활용해야할 듯.
from sys import stdin

class Node:
    def __init__(self,val):
        self.next = []
        self.prev = []
        self.val = val
        self.isAvailable = True
        self.indegree = 0
        self.outdegree = 0

    def connect(self,another):
        self.next.append(another)
        another.prev.append(self)
        another.indegree += 1
        self.outdegree += 1

n, k, p = map(int, stdin.readline().split())
nodes = [Node(n-i-1) for i in range(k)]
for i in range(p):
    a, b =  map(int, stdin.readline().split())
    a, b = nodes[k-a-1], nodes[k-b-1]
    a.connect(b)

nodes.sort(key=lambda x:x.val,reverse=True)
biggest = 0
counter = 0
while counter != k:
    for node in nodes:
        if node.indegree == 0 and node.isAvailable:
            biggest += node.val*(n**(k-1-counter))
            for nextnode in node.next:
                nextnode.indegree -= 1
            node.isAvailable = False
            counter +=1
            break

nodes.sort(key=lambda x:x.val)

for node in nodes: node.isAvailable = True

smallest = 0
counter = 0
while counter != k:
    for node in nodes:
        if node.outdegree == 0 and node.isAvailable:
            smallest += (node.val - (n-k) )* (n**(counter))
            for prevnode in node.prev:
                prevnode.outdegree -= 1
            node.isAvailable = False
            counter +=1
            break

print(biggest-smallest)