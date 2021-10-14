from collections import deque
from sys import stdin

MAX_INT = 10 ** 6


### NOT SOVLED YET: Will upsolve later ###

def solve():
    n, k = map(int, stdin.readline().split())
    if n == 1:
        print(0)
        return

    if n == 2:
        input()
        print(0)
        return

    graph = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(int, stdin.readline().split())
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)

    initial = []
    res = [MAX_INT for _ in range(n)]

    level = 1
    lines = n - 1
    while lines > 0:
        for i in range(n):

            if len(graph[i]) == 1:
                res[i] = level
                graph[graph[i][0]].remove(i)
                graph[i].clear()
                lines -= 1
        level += 1


    ans = 0
    for i in res:
        if i > k:
            ans += 1
    print(ans)


t = int(stdin.readline().strip())

for _ in range(t):
    stdin.readline()
    solve()
