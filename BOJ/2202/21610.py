# https://www.acmicpc.net/problem/21610
# Implementation

from sys import stdin

n, m = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(n)]
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
has_cloud = [[False] * n for _ in range(n)]
has_cloud[n - 1][0] = True
has_cloud[n - 1][1] = True
has_cloud[n - 2][0] = True
has_cloud[n - 2][1] = True


def move(d, s):
    # move cloud, rain, and remove cloud.
    moved_clouds = []
    for x in range(n):
        for y in range(n):
            if has_cloud[x][y]:
                has_cloud[x][y] = False
                nx = (x + s * dx[d - 1]) % n
                ny = (y + s * dy[d - 1]) % n
                board[nx][ny] += 1
                moved_clouds.append([nx, ny])
    # water bug
    for [x, y] in moved_clouds:
        count = 0
        for direction in (1, 3, 5, 7):
            nx = x + dx[direction]
            ny = y + dy[direction]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] > 0:
                count += 1
        board[x][y] += count
    # make cloud
    for x in range(n):
        for y in range(n):
            if board[x][y] >= 2:
                board[x][y] -= 2
                has_cloud[x][y] = True
    # do not make cloud where cloud was removed.
    for [x, y] in moved_clouds:
        if has_cloud[x][y]:
            board[x][y] += 2
            has_cloud[x][y] = False


for _ in range(m):
    move(*map(int, stdin.readline().split()))

ans = 0
for i in range(n):
    for j in range(n):
        ans += board[i][j]
print(ans)
