# https://www.acmicpc.net/problem/4225
# Convex Hull

from collections import deque
from math import atan2, ceil, sqrt
from sys import stdin


def cross(origin, fst, snd):
    foo = [fst[0] - origin[0], fst[1] - origin[1]]
    bar = [snd[0] - origin[0], snd[1] - origin[1]]
    return foo[0] * bar[1] - foo[1] * bar[0]


def ccw(origin, fst, snd):
    return cross(origin, fst, snd) > 0


output = []
while True:
    n = int(stdin.readline().strip())
    if n == 0:
        break
    points = [list(map(int, stdin.readline().split())) for _ in range(n)]
    # convex hull
    points.sort()
    start = points.pop(0)
    points.sort(key=lambda x: atan2(x[1] - start[1], x[0] - start[0]))
    stack = deque()
    stack.append(start)
    stack.append(points[0])
    for i in range(1, len(points)):
        curr = points[i]
        if ccw(stack[-2], stack[-1], curr):
            stack.append(curr)
        else:
            while len(stack) != 1 and not ccw(stack[-2], stack[-1], curr):
                stack.pop()
            stack.append(curr)
    stack.append(start)
    ans = (10 ** 20, 1)
    n = len(stack)
    for i in range(n - 1):
        j = i + 1
        temp = (0, 1)
        for k in range(n):
            if i == k or j == k:
                continue
            area = cross(stack[i], stack[j], stack[k]) * 100
            area *= area
            dist = ((stack[i][0] - stack[j][0]) ** 2 + (stack[i][1] - stack[j][1]) ** 2)
            if temp[0] * dist < temp[1] * area:
                temp = (area, dist)

        if ans[0] * temp[1] > ans[1] * temp[0]:
            ans = temp
    output.append(ceil(sqrt(ans[0] / ans[1])) / 100.0)

for i, j in enumerate(output):
    print(f"Case {i + 1}: {j:.2f}")
