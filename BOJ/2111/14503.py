# https://www.acmicpc.net/problem/14503

from sys import stdin

dr = [-1, 0, 1, 0]  # N, E, S, W
dc = [0, 1, 0, -1]
n, m = map(int, stdin.readline().split())
r, c, d = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(n)]
ans = 0

while True:
    flag = False
    if board[r][c] == 0:
        ans += 1
        board[r][c] = 2
    for i in range(1, 5):
        nd = (d - i) % 4
        nr = r + dr[nd]
        nc = c + dc[nd]
        if board[nr][nc] == 0:
            d, r, c = nd, nr, nc
            flag = True
            break
    if not flag:
        nr = r + dr[(d - 2) % 4]
        nc = c + dc[(d - 2) % 4]
        if board[nr][nc] == 1:
            print(ans)
            exit(0)
        else:
            r, c = nr, nc
