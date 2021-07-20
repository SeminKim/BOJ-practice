# https://www.acmicpc.net/problem/2887
# Kruskal, but nearest node is easily obtained by sort.

from sys import stdin
import heapq

n = int(stdin.readline().strip())
x = []
y = []
z = []
planet = []

for i in range(n):
    a, b, c = map(int, stdin.readline().split())
    x.append((a, i))
    y.append((b, i))
    z.append((c, i))
    planet.append((a, b, c))

x.sort()
y.sort()
z.sort()

pq = []

for axis in [x, y, z]:
    for first in range(n - 1):
        pos1, idx1 = axis[first]
        pos2, idx2 = axis[first + 1]
        heapq.heappush(pq, (abs(pos1 - pos2), [idx1, idx2]))

head = [i for i in range(n)]


def get_head(num):
    if head[num] == num:
        return num
    head[num] = get_head(head[num])
    return head[num]


ans = 0
while pq:
    dist, [idx1, idx2] = heapq.heappop(pq)
    idx1 = get_head(idx1)
    idx2 = get_head(idx2)

    if idx1 == idx2:
        continue

    ans += dist
    head[idx1] = idx2

print(ans)
