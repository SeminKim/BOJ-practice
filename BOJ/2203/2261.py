# https://www.acmicpc.net/problem/2261
# Divide and Conquer: http://people.csail.mit.edu/indyk/6.838-old/handouts/lec17.pdf
import math
from bisect import *
from sys import stdin

n = int(stdin.readline().strip())
points = [list(map(int, stdin.readline().split())) for _ in range(n)]
points.sort()
INF = 10 ** 10


def dist(fst, snd):
    return (fst[0] - snd[0]) ** 2 + (fst[1] - snd[1]) ** 2


# find minimum(squared) within left <= x < right
def find_min(left, right):
    if left + 1 == right:
        return INF
    mid = (left + right) // 2
    d1 = find_min(left, mid)
    d2 = find_min(mid, right)
    d = min(d1, d2)
    # cross-subregion case
    mid_x = points[mid][0]
    left_idx = bisect_left(points, [mid_x - math.sqrt(d), -INF], lo=left, hi=mid)
    right_idx = bisect_right(points, [mid_x + math.sqrt(d), INF], lo=mid, hi=right)
    temp = points[left_idx:right_idx]
    temp.sort(key=lambda x: x[1])  # sort by y
    for i in range(len(temp) - 1):
        for j in range(i + 1, len(temp)):
            d = min(d, dist(temp[i], temp[j]))
            if (temp[j][1] - temp[i][1])**2 >= d:
                break
    return d


print(find_min(0, n))
