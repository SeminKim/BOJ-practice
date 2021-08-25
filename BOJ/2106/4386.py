# https://www.acmicpc.net/problem/4386
# calculate distance and use prim's algorithm
from sys import stdin
import heapq


def get_distance(pnt1, pnt2):
    return ((pnt1[0] - pnt2[0]) ** 2 + (pnt1[1] - pnt2[1]) ** 2) ** 0.5


def solve():
    n = int(stdin.readline().strip())
    stars = []
    for _ in range(n):
        x, y = map(float, stdin.readline().split())
        stars.append((x, y))

    costs = []
    selected = [False for _ in range(n)]

    selected[0] = True
    lines = 0
    ans = 0

    for i in range(1, n):
        dist = get_distance(stars[0], stars[i])
        heapq.heappush(costs, (dist, 0, i))

    while lines < n - 1:
        dist, now, another = heapq.heappop(costs)
        if selected[now] != selected[another]:
            ans += dist
            lines += 1
            toadd = now
            if selected[now]:
                toadd = another
            selected[toadd] = True
            for i in range(n):
                if i == toadd:
                    continue
                foo = get_distance(stars[toadd], stars[i])
                heapq.heappush(costs, (foo, toadd, i))
    return ans


print(solve())
