# https://www.acmicpc.net/problem/20055
# Implementation

from collections import deque
from sys import stdin

n, k = map(int, stdin.readline().split())
seq = deque(map(int, stdin.readline().split()))
robots = deque(False for _ in range(n))
zero = seq.count(0)
for t in range(1, 10**10):
    seq.appendleft(seq.pop())
    robots.pop()
    robots.appendleft(False)
    robots[-1] = False
    for i in reversed(range(n - 1)):
        if robots[i] and not robots[i + 1] and seq[i + 1] > 0:
            robots[i] = False
            robots[i + 1] = True
            seq[i + 1] -= 1
            if seq[i+1] == 0:
                zero += 1
    robots[-1] = False
    if seq[0] > 0:
        robots[0] = True
        seq[0] -= 1
        if seq[0] == 0:
            zero += 1
    if zero >= k:
        print(t)
        break
