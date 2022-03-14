# https://www.acmicpc.net/problem/3648
# 2-SAT

from collections import deque
from sys import stdin

while True:
    try:
        n, m = map(int, stdin.readline().split())
    except:
        break
    graph = [[] for _ in range(2 * n + 1)]  # zero is not used
    graph[-1] = [1]  # https://www.acmicpc.net/board/view/9155
    for _ in range(m):
        a, b = map(int, stdin.readline().split())
        graph[-a].append(b)
        graph[-b].append(a)

    # SCC
    def search(curr):
        global counter, scc_idx
        counter += 1
        visited[curr] = counter
        ret = visited[curr]
        stack.append(curr)
        for child in graph[curr]:
            if visited[child] == 0:
                ret = min(ret, search(child))
            elif scc[child] == 0:
                ret = min(ret, visited[child])

        if ret == visited[curr]:
            scc_idx += 1
            while True:
                popped = stack.pop()
                scc[popped] = scc_idx
                if popped == curr:
                    break
        return ret

    stack = deque()
    counter = scc_idx = 0
    visited = [0 for _ in range(2 * n + 1)]
    scc = [0 for _ in range(2 * n + 1)]
    for i in range(-n, n + 1):
        if visited[i] == 0 and i != 0:
            search(i)

    # check
    for i in range(1, n + 1):
        if scc[i] == scc[-i]:
            print('no')
            break
    else:
        print('yes')
