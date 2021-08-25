# https://www.acmicpc.net/problem/1806
# add from right, then remove from left until sum > S.

from sys import stdin
from collections import deque

Q = deque()

N, S = map(int, input().split())
seq = list(map(int, stdin.readline().split()))

current_sum = 0
ans = float('inf')
for i in range(N):
    Q.append(seq[i])
    current_sum += seq[i]
    first = Q.popleft()
    current_sum -= first
    while current_sum >= S:
        first = Q.popleft()
        current_sum -= first
    Q.appendleft(first)
    current_sum += first

    if current_sum >= S:
        ans = min(ans, len(Q))

if ans == float('inf'):
    print(0)
else:
    print(ans)
