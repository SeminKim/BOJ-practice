# https://www.acmicpc.net/problem/11281
# 2-SAT

from collections import deque
from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 5)
n, m = map(int, stdin.readline().split())
out_graph = [[] for _ in range(2 * n + 1)]  # zero is not used. 1~n and -1~-n
in_graph = [[] for _ in range(2 * n + 1)]
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    out_graph[-a].append(b)
    in_graph[b].append(a)
    if a != b:
        out_graph[-b].append(a)
        in_graph[a].append(-b)


# find SCC (Tarjan's)
def dfs(curr):
    global counter, scc_idx
    counter += 1
    visited[curr] = counter
    ret = visited[curr]
    stack.append(curr)
    for child in out_graph[curr]:
        if visited[child] == 0:
            ret = min(ret, dfs(child))
        elif is_scc[child] == 0:
            ret = min(ret, visited[child])

    if ret == visited[curr]:
        temp = []
        temp_indegree = 0
        scc_idx += 1
        while True:
            popped = stack.pop()
            is_scc[popped] = scc_idx
            temp.append(popped)
            temp_indegree += len(in_graph[popped])
            if popped == curr:
                break
        # calculation for later toposort
        for node in temp:
            node_temp_out = []
            for neighbor in out_graph[node]:
                if is_scc[neighbor] == scc_idx:
                    temp_indegree -= 1
                else:
                    node_temp_out.append(neighbor)
            out_graph[node] = node_temp_out

        scc_indegree.append(temp_indegree)
        scc.append(temp)
    return ret


visited = [0 for _ in range(2 * n + 1)]
is_scc = [0 for _ in range(2 * n + 1)]
scc = [[]]
scc_indegree = [0]
counter = scc_idx = 0
stack = deque()
for i in range(-n, n + 1):
    if visited[i] == 0 and i != 0:
        dfs(i)

# if a and -a is in same SCC: False
for i in range(1, n + 1):
    if is_scc[i] == is_scc[-i] != 0:
        print(0)
        exit(0)

print(1)
# else, do topological sort and take latter one.
Q = deque()
for i in range(-n, n + 1):
    if len(in_graph[i]) == 0 and i != 0:
        Q.append(i)

order = [0 for _ in range(2 * n + 1)]
num = 0
while Q:
    now = Q.popleft()
    num += 1
    order[now] = num
    for child in out_graph[now]:
        idx = is_scc[child]
        # if child is in scc
        if idx != 0:
            scc_indegree[idx] -= 1
            if scc_indegree[idx] != 0:
                continue
            # when scc has zero indegree
            for node in scc[idx]:
                Q.append(node)

        # normal case
        else:
            in_graph[child].remove(now)
            if len(in_graph[child]) == 0:
                Q.append(child)

# scc with indegree zero
for group in reversed(scc):
    num += 1
    for node in group:
        order[node] = num

for i in range(1, n + 1):
    if order[i] >= order[-i]:
        print(1, end=' ')
    else:
        print(0, end=' ')
