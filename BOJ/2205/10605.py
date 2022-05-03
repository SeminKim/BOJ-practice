# https://www.acmicpc.net/problem/10605
# Greedy - kill dragon at start(xi>Si) or by crowd(sum(xi) > max(Ni))

from bisect import *
from collections import deque
from sys import stdin


def solve(n, m, k):
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, stdin.readline().split())
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)

    dragons = [[] for _ in range(n)]
    for _ in range(k):
        ci, si, ni = map(int, stdin.readline().split())
        dragons[ci - 1].append([ni, si])  # change order for simpler implementation

    ans = 0
    visited = [False for _ in range(n)]
    for node in range(n):
        if not visited[node]:
            # Make partial solution for connected component
            target = dragons[node]
            Q = deque([node])
            visited[node] = True
            while Q:
                curr = Q.popleft()
                for child in graph[curr]:
                    if not visited[child]:
                        visited[child] = True
                        target.extend(dragons[child])
                        Q.append(child)
            if len(target) == 0:  # no dragon in this connected component.
                continue

            target.sort()  # Ni, Si
            si_partial = [0 for _ in range(len(target) + 1)]
            acc = 0
            for i in range(len(target)):
                acc += target[i][1]
                si_partial[i + 1] = acc
            curr_ans = 0

            for hero in range(1, 10 ** 5 + 1):
                start_idx = bisect_left(target, [hero, -1])
                if start_idx == len(target):  # num of hero exceeds sum of ni
                    curr_ans = hero
                    break
                if si_partial[-1] - si_partial[start_idx] <= hero:
                    curr_ans = hero
                    break
            ans += curr_ans
    print(ans)


while True:
    n, m, k = map(int, stdin.readline().split())
    if n == m == k == 0:
        break
    else:
        solve(n, m, k)
