# https://www.acmicpc.net/problem/13549
# Pop one position in queue, update other position related to it.

import heapq


def solve():
    n, k = map(int, input().split())
    cost = [float('inf') for _ in range(2 * k + 1)]
    pq = []

    if n >= k:
        return n - k

    def is_valid_range(t):
        return 0 <= t <= 2 * k

    heapq.heappush(pq, (0, n))
    while len(pq) != 0:
        c, pos = heapq.heappop(pq)

        if is_valid_range(2 * pos) and c < cost[pos * 2]:
            cost[pos * 2] = c
            heapq.heappush(pq, (c, pos * 2))

        if is_valid_range(pos + 1) and c + 1 < cost[pos + 1]:
            cost[pos + 1] = c + 1
            heapq.heappush(pq, (c + 1, pos + 1))

        if is_valid_range(pos - 1) and c + 1 < cost[pos - 1]:
            cost[pos - 1] = c + 1
            heapq.heappush(pq, (c + 1, pos - 1))

    return cost[k]


print(solve())

'''from collections import deque

def solve():
    n, k = map(int, input().split())
    cost = [0 for _ in range(100001)]
    q = deque()
    q.append(n)
    while len(q) != 0:
        x = q.popleft()
        if x == k:
            return cost[x]
        for next_x in [2*x, x-1, x+1]:
            if 0 <= next_x <= k+1 and not cost[next_x]:
                if next_x == 2*x and x != 0:
                    cost[next_x] = cost[x]
                    q.appendleft(next_x)
                else:
                    cost[next_x] = cost[x]+1
                    q.append(next_x)
    return cost[k]'''
