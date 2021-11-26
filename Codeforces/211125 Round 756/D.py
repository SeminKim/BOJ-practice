from sys import stdin


def solve():
    n = int(stdin.readline().strip())
    parent = [0] + list(map(int, stdin.readline().split()))
    target = list(map(int, stdin.readline().split()))
    root = -1
    for i in range(1, n + 1):
        if parent[i] == i:
            root = i
            break
    dist = [-1 for _ in range(n + 1)]
    dist[root] = 0
    curr = 0
    if target[0] != root:
        print(-1)
        return

    for node in target:
        if dist[parent[node]] == -1:
            print(-1)
            return
        dist[node] = curr
        curr += 1
    for i in range(1, n + 1):
        print(dist[i] - dist[parent[i]], end=' ')
    print()
    return


t = int(stdin.readline().strip())

for _ in range(t):
    solve()

# 5
# 3 1 3 3 1
# 1 2 3 4 5
# 5
# 3 1 3 3 1
# 5 4 3 2 1
# 5
# 3 1 3 3 1
# 3 4 1 2 5
# 5
# 3 1 3 3 1
# 3 5 2 1 4
