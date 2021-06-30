# https://www.acmicpc.net/problem/1202

from sys import stdin
import heapq


def solve():
    n, k = map(int, stdin.readline().split())

    jewels = [tuple(map(int, stdin.readline().split())) for _ in range(n)]
    bags = [int(stdin.readline().strip()) for _ in range(k)]

    jewels.sort(key=lambda x: x[0])
    bags.sort()

    ans = 0
    idx = 0
    available = []
    for now in range(k):
        capacity = bags[now]
        while idx < n and jewels[idx][0] <= capacity:
            heapq.heappush(available, -jewels[idx][1])
            idx += 1

        if len(available) != 0:
            ans -= heapq.heappop(available)

    return ans


print(solve())
