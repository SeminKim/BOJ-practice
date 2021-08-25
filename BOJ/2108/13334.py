# https://www.acmicpc.net/problem/13334

from sys import stdin
from collections import deque

n = int(stdin.readline().strip())

start = []
end = []
for _ in range(n):
    s, e = sorted(map(int, stdin.readline().split()))
    start.append((s, e))
    end.append((e, s))
start.sort()
end.sort()
start = deque(start)
end = deque(end)

d = int(stdin.readline().strip())

ans = 0
res = 0
while start:
    left, foo = start.popleft()
    right = left + d

    while len(end) > 0 and end[0][0] <= right:
        foo_r, foo_l = end.popleft()
        if foo_l >= left:
            res += 1

    ans = max(ans, res)
    if foo <= right:
        res -= 1

    if len(end) == 0:
        break

print(ans)
