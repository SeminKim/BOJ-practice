# https://www.acmicpc.net/problem/1708
# Convex Hull

from collections import deque
from sys import stdin


def get_vector(start, end):
    return [end[0] - start[0], end[1] - start[1]]


def is_cross_positive(first, second):
    return first[0] * second[1] - first[1] * second[0] > 0


INF = 200000
n = int(stdin.readline().strip())
points = [list(map(int, stdin.readline().split())) for _ in range(n)]
base = min(points)
points.sort()
points.sort(key=lambda p: INF - p[1] if p[0] == base[0] else (p[1] - base[1]) / (p[0] - base[0]))

stack = deque([base, points[0]])
for i in range(1, n):
    curr_pnt = points[i]

    while len(stack) > 1 and not is_cross_positive(get_vector(stack[-2], stack[-1]), get_vector(stack[-1], curr_pnt)):
        stack.pop()

    stack.append(curr_pnt)

print(len(stack) - 1)
