# https://www.acmicpc.net/problem/17837

from sys import stdin

n, k = map(int, stdin.readline().split())
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

board = [list(map(int, stdin.readline().split())) for _ in range(n)]
pieces = []
state = [[[] for _ in range(n)] for _ in range(n)]
for i in range(k):
    r, c, d = map(int, stdin.readline().split())
    pieces.append([r - 1, c - 1, d - 1])
    state[r - 1][c - 1].append(i)

t = 0
while (t := t + 1) < 1001:
    for i in range(k):
        r, c, d = pieces[i]
        nr, nc = r + dr[d], c + dc[d]
        # if blue or out of border, reverse its direction
        if (not 0 <= nr < n) or (not 0 <= nc < n) or (board[nr][nc] == 2):
            d ^= 1  # invert last digit on binary (0<->1, 2<->3)
            pieces[i][2] = d
            nr, nc = r + dr[d], c + dc[d]
            # if it is blue again or out of border, do not move and continue.
            if (not 0 <= nr < n) or (not 0 <= nc < n) or (board[nr][nc] == 2):
                continue
        # white(0) or red(1)
        idx = state[r][c].index(i)
        on_top = state[r][c][idx:]
        # if red, do in reverse order
        if board[nr][nc] == 1:
            on_top.reverse()
        for piece in on_top:
            state[nr][nc].append(piece)
            pieces[piece][0] = nr
            pieces[piece][1] = nc
        state[r][c] = state[r][c][:idx]
        if len(state[nr][nc]) >= 4:
            print(t)
            exit(0)
print(-1)
