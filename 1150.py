# https://www.acmicpc.net/problem/1150

from queue import PriorityQueue

class Line:
    def __init__(self,len):
        self.left = self
        self.right = self
        self.len = len
        self.isAvailable = True

    def select(self, PQ):
        self.isAvailable = False
        self.left.isAvailable = False
        self.right.isAvailable = False
        leftmost = self.left.left
        rightmost = self.right.right
        newlen = self.left.len + self.right.len - self.len
       # if newlen < MAX_INT:
        sub = Line(newlen)
        sub.left = leftmost
        sub.right = rightmost
        sub.left.right = sub
        sub.right.left = sub

        if leftmost.isAvailable and rightmost.isAvailable : PQ.put(sub)

    def __lt__(self, other):
        return self.len < other.len
    def __gt__(self, other):
        return self.len > other.len
    def __le__(self, other):
        return self.len <= other.len
    def __ge__(self, other):
        return self.len >= other.len

MAX_INT = 1000000000
n, k = map(int, input().split())
lines = [None]*(n+1)
temp = 0
for i in range(n):
    if i == 0:
        temp = int(input())
        continue
    now = int(input())
    lines[i] = Line(now - temp)
    temp = now

lines[0] = Line(MAX_INT)
lines[0].right = lines[1]
lines[n] = Line(MAX_INT)
lines[n].left = lines[n-1]
for i in range(1,n):
    lines[i].left = lines[i-1]
    lines[i].right = lines[i+1]

pq = PriorityQueue()
for line in lines:
    pq.put(line)

counter = 0
total = 0

while counter < k+1:

    temp = pq.get()

    if temp.isAvailable == True:
        temp.select(pq)
        counter += 1
        total += temp.len
        if counter == k:
            break

print(total)

