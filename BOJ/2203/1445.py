# https://www.acmicpc.net/problem/1445
# BFS

from collections import deque
from sys import stdin

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
INF = 10 * 10
n, m = map(int, stdin.readline().split())
board = [[0 for _ in range(m)] for _ in range(n)]
start = (-1, -1)
end = (-1, -1)
for i in range(n):
    line = stdin.readline()
    for j in range(m):
        if line[j] == 'g':
            board[i][j] = 1  # 1 denotes trash
            for d in range(4):
                ni = i + dx[d]
                nj = j + dy[d]
                if 0 <= ni < n and 0 <= nj < m and board[ni][nj] == 0:
                    board[ni][nj] = 2  # 2 denotes near-trash
        elif line[j] == 'S':
            start = (i, j)
            board[i][j] = -1  # -1 denotes special case (no-count)
        elif line[j] == 'F':
            end = (i, j)
            board[i][j] = -1

visited = [[(INF, INF) for _ in range(m)] for _ in range(n)]
Q = deque()
first = (0, 0)
if board[start[0]][start[1]] == 1:
    first = (1, 0)
elif board[start[0]][start[1]] == 2:
    first = (0, 2)
visited[start[0]][start[1]] = first
Q.append([*start, first])
while Q:
    x, y, val = Q.popleft()
    if visited[x][y] < val:
        continue
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < m:
            nval = (val[0] + (board[nx][ny] == 1), val[1] + (board[nx][ny] == 2))
            if nval < visited[nx][ny]:
                visited[nx][ny] = nval
                Q.append([nx, ny, nval])

print(*visited[end[0]][end[1]])
