# https://www.acmicpc.net/problem/11266

from sys import stdin, setrecursionlimit


setrecursionlimit(10**6)
v, e = map(int, stdin.readline().split())
edge = [[] for _ in range(v)]
for _ in range(e):
    a, b = map(int, stdin.readline().split())
    edge[a - 1].append(b - 1)
    edge[b - 1].append(a - 1)

counter = 0
visited = [0 for _ in range(v)]
in_ans = [False for _ in range(v)]


# return the earliest reachable node number
def search(pos, is_root=False):
    global counter
    counter += 1
    visited[pos] = counter
    ret = visited[pos]
    unvisited_children = 0
    for child in edge[pos]:
        if visited[child] != 0:
            ret = min(ret, visited[child])
        else:
            unvisited_children += 1
            val = search(child)
            ret = min(ret, val)
            if (not is_root) and val >= visited[pos]:
                in_ans[pos] = True
    if is_root and unvisited_children >= 2:
        in_ans[pos] = True
    return ret


for i in range(v):
    if visited[i] == 0:
        search(i, True)

ans = []
for i in range(v):
    if in_ans[i]:
        ans.append(i + 1)
print(len(ans))
print(' '.join(map(str, ans)))
