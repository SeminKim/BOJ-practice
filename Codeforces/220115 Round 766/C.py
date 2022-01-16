from sys import stdin


def solve():
    n = int(stdin.readline().strip())
    lines = []
    for _ in range(n - 1):
        foo, bar = map(int, stdin.readline().split())
        lines.append([foo - 1, bar - 1])
    edges_associated_with_vertex = [[] for _ in range(n)]  # edge number associated with each vertex.
    ans = [-1 for _ in range(n - 1)]
    for i in range(n - 1):
        a, b = lines[i]
        edges_associated_with_vertex[a].append(i)
        edges_associated_with_vertex[b].append(i)

    for i in range(n):
        if len(edges_associated_with_vertex[i]) > 2:
            print(-1)
            return

    ans[0] = 2  # assign 2 to edge zero.
    left = lines[0][0]  # left vertex of edge zero.
    while len(edges_associated_with_vertex[left]) == 2:
        fst, snd = edges_associated_with_vertex[left]
        if ans[fst] == -1:
            fst, snd = snd, fst
        if ans[fst] == 2:
            ans[snd] = 3
        else:
            ans[snd] = 2
        if lines[snd][0] != left:
            left = lines[snd][0]
        else:
            left = lines[snd][1]

    right = lines[0][1]  # left vertex of edge zero.
    while len(edges_associated_with_vertex[right]) == 2:
        fst, snd = edges_associated_with_vertex[right]
        if ans[fst] == -1:
            fst, snd = snd, fst
        if ans[fst] == 2:
            ans[snd] = 3
        else:
            ans[snd] = 2
        if lines[snd][0] != right:
            right = lines[snd][0]
        else:
            right = lines[snd][1]

    print(' '.join(map(str, ans)))


t = int(stdin.readline().strip())

for _ in range(t):
    solve()
