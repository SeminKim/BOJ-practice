# https://www.acmicpc.net/problem/2623


from sys import stdin
from collections import deque


def solve():
    n, m = map(int, stdin.readline().split())
    pre = [0 for _ in range(n + 1)]
    post = [[] for _ in range(n + 1)]
    for _ in range(m):
        line = list(map(int, stdin.readline().split()))
        for i in range(1, len(line)):
            for j in range(i + 1, len(line)):
                pre[line[j]] += 1
                post[line[i]].append(line[j])

    available = deque()
    for i in range(1, n + 1):
        if pre[i] == 0:
            available.append(i)

    ans = []
    while available:
        now = available.popleft()
        ans.append(now)
        for after in post[now]:
            pre[after] -= 1
            if pre[after] == 0:
                available.append(after)
    if len(ans) < n:
        print(0)
    else:
        for foo in ans:
            print(foo)


solve()
