from sys import stdin
import heapq

#BOTH C1 and C2
n = int(stdin.readline().strip())
seq = list(map(int, stdin.readline().split()))

hp = 0
history = []
for potion in seq:
    hp = hp + potion
    heapq.heappush(history, potion)
    while hp < 0:
        vomit = heapq.heappop(history)
        hp -= vomit
print(len(history))
