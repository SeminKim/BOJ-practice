# https://www.acmicpc.net/problem/14500
# Implementation

from sys import stdin

n, m = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(n)]

ans = -1
for i in range(n):
    for j in range(m):
        if j + 4 <= m:
            ans = max(ans, sum(board[i][j + k] for k in range(4)))
        if i + 4 <= n:
            ans = max(ans, sum(board[i + k][j] for k in range(4)))
        if i + 2 <= n and j + 2 <= m:
            ans = max(ans, board[i][j] + board[i][j + 1] + board[i + 1][j] + board[i + 1][j + 1])
        if i + 3 <= n and j + 2 <= m:
            ans = max(ans, board[i][j] + board[i + 1][j] + board[i + 2][j] + board[i + 2][j + 1])
            ans = max(ans, board[i][j] + board[i][j + 1] + board[i + 1][j + 1] + board[i + 2][j + 1])
            ans = max(ans, board[i][j + 1] + board[i + 1][j + 1] + board[i + 2][j] + board[i + 2][j + 1])
            ans = max(ans, board[i][j] + board[i][j + 1] + board[i + 1][j] + board[i + 2][j])
            ans = max(ans, board[i][j] + board[i + 1][j] + board[i + 1][j + 1] + board[i + 2][j + 1])
            ans = max(ans, board[i][j + 1] + board[i + 1][j] + board[i + 1][j + 1] + board[i + 2][j])
            ans = max(ans, board[i][j] + board[i + 1][j] + board[i + 1][j + 1] + board[i + 2][j])
            ans = max(ans, board[i][j + 1] + board[i + 1][j] + board[i + 1][j + 1] + board[i + 2][j + 1])
        if i + 2 <= n and j + 3 <= m:
            ans = max(ans, board[i][j] + board[i + 1][j] + board[i][j + 1] + board[i][j + 2])
            ans = max(ans, board[i + 1][j] + board[i + 1][j + 1] + board[i + 1][j + 2] + board[i][j + 2])
            ans = max(ans, board[i][j] + board[i + 1][j] + board[i + 1][j + 1] + board[i + 1][j + 2])
            ans = max(ans, board[i][j] + board[i][j + 1] + board[i][j + 2] + board[i + 1][j + 2])
            ans = max(ans, board[i][j + 1] + board[i][j + 2] + board[i + 1][j] + board[i + 1][j + 1])
            ans = max(ans, board[i][j] + board[i][j + 1] + board[i + 1][j + 1] + board[i + 1][j + 2])
            ans = max(ans, board[i][j] + board[i][j + 1] + board[i][j + 2] + board[i + 1][j + 1])
            ans = max(ans, board[i][j + 1] + board[i + 1][j] + board[i + 1][j + 1] + board[i + 1][j + 2])

print(ans)
