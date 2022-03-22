# https://www.acmicpc.net/problem/22956
# Disjoint Set

from sys import stdin

INF = 10 ** 5
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n, m, q = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(n)]
parent = [[(r, c) for c in range(m)] for r in range(n)]
lowest = [[(INF, -1) for _ in range(m)] for _ in range(n)]


def get_parent(x, y):
    if parent[x][y] != (x, y):
        px, py = parent[x][y]
        parent[x][y] = get_parent(px, py)
    return parent[x][y]


def union(x1, y1, x2, y2):  # x1 y1 will be always the latest updated one.
    px1, py1 = get_parent(x1, y1)
    px2, py2 = get_parent(x2, y2)
    if px1 == px2 and py1 == py2:
        return
    if lowest[px1][py1] < lowest[px2][py2]:
        parent[px2][py2] = (px1, py1)
    else:
        parent[px1][py1] = (px2, py2)
    return


for counter in range(q):
    a, b, c = map(int, stdin.readline().split())
    a -= 1
    b -= 1
    board[a][b] -= c
    px, py = get_parent(a, b)
    if (board[a][b], counter) < lowest[px][py]:
        parent[a][b] = (a, b)
        parent[px][py] = (a, b)
        lowest[a][b] = (board[a][b], counter)
    for d in range(4):
        nx = a + dx[d]
        ny = b + dy[d]
        if 0 <= nx < n and 0 <= ny < m:
            if parent[nx][ny] == (nx, ny) and lowest[nx][ny][0] == INF:
                continue
            union(a, b, nx, ny)
    foo, bar = get_parent(a, b)
    print(foo + 1, bar + 1)
