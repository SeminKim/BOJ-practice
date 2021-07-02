# https://www.acmicpc.net/problem/1766

from sys import stdin
import heapq


def solve():
    n, m = map(int, stdin.readline().split())
    pre = [[]] + [[] for _ in range(n)]  # pre[i] should be solved before problem i.
    post = [[]] + [[] for _ in range(n)]
    ans = []

    for _ in range(m):
        first, then = map(int, stdin.readline().split())
        post[first].append(then)
        pre[then].append(first)

    available = []
    for i in range(1, n + 1):
        if len(pre[i]) == 0:
            heapq.heappush(available, i)

    while len(ans) < n:
        now = heapq.heappop(available)
        for after in post[now]:
            pre[after].remove(now)
            if len(pre[after]) == 0:
                heapq.heappush(available, after)
        ans.append(now)

    return ' '.join(map(str, ans))


print(solve())
