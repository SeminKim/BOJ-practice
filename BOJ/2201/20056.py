# https://www.acmicpc.net/problem/20056
# Implementation

from sys import stdin

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

N, M, K = map(int, stdin.readline().split())
board = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    row, col, mass, speed, direction = map(int, stdin.readline().split())
    board[row - 1][col - 1].append([mass, speed, direction])

for _ in range(K):
    new_board = [[[] for _ in range(N)] for _ in range(N)]
    for row in range(N):
        for col in range(N):
            for [m, s, d] in board[row][col]:
                nrow = (row + s * dx[d]) % N
                ncol = (col + s * dy[d]) % N
                new_board[nrow][ncol].append([m, s, d])
    for row in range(N):
        for col in range(N):
            if len(new_board[row][col]) > 1:
                nm = sum(foo[0] for foo in new_board[row][col]) // 5
                if nm:
                    ns = sum(foo[1] for foo in new_board[row][col]) // len(new_board[row][col])
                    direction_flag = (sum(foo[2] & 1 for foo in new_board[row][col]) % len(new_board[row][col]) == 0)
                    if direction_flag:
                        new_board[row][col] = [[nm, ns, nd] for nd in [0, 2, 4, 6]]
                    else:
                        new_board[row][col] = [[nm, ns, nd] for nd in [1, 3, 5, 7]]
                else:
                    new_board[row][col] = []
    board = new_board

ans = 0
for row in range(N):
    for col in range(N):
        for ball in board[row][col]:
            ans += ball[0]
print(ans)
