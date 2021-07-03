# https://www.acmicpc.net/problem/2252

from sys import stdin
import heapq


def solve():
    n, m = map(int, stdin.readline().split())
    indegree = [0] + [0 for _ in range(n)]  # number of prerequisite(?)
    post = [[]] + [[] for _ in range(n)]
    ans = []

    for _ in range(m):
        first, second = map(int, stdin.readline().split())
        post[first].append(second)
        indegree[second] += 1

    available = []
    for i in range(1, n + 1):
        if indegree[i] == 0:
            available.append(i)

    while len(available) > 0:
        now = heapq.heappop(available)
        ans.append(now)
        for after in post[now]:
            indegree[after] -= 1
            if indegree[after] == 0:
                heapq.heappush(available, after)

    return " ".join(map(str, ans))


print(solve())
