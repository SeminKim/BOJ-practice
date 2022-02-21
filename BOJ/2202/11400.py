# https://www.acmicpc.net/problem/11400

from sys import stdin, setrecursionlimit

setrecursionlimit(10**5)
V, E = map(int, stdin.readline().split())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0 for _ in range(V + 1)]
counter = 0


# return the earliest reachable node number, without edge (parent,pos).
def dfs(pos, parent):
    global counter
    counter += 1
    visited[pos] = counter
    ret = counter
    for child in graph[pos]:
        if child == parent:
            continue
        elif visited[child]:  # back edge
            ret = min(ret, visited[child])
        else:  # tree edge
            val = dfs(child, pos)
            if visited[pos] < val:
                ans.append(tuple(sorted([pos, child])))
            ret = min(ret, val)
    return ret


ans = []
dfs(1, 0)
print(len(ans))
for foo in sorted(ans):
    print(*foo)
