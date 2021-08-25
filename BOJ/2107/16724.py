# https://www.acmicpc.net/problem/16724

from sys import stdin

n, m = map(int, stdin.readline().split())
board = [list(stdin.readline().strip()) for _ in range(n)]
visited_by = [[-1 for _ in range(m)] for __ in range(n)]


def get_next(r, c):
    if board[r][c] == 'U':
        return r - 1, c
    if board[r][c] == 'D':
        return r + 1, c
    if board[r][c] == 'L':
        return r, c - 1
    return r, c + 1  # when board[r][c] == 'R'


ans = 0
for row in range(n):
    for col in range(m):
        if visited_by[row][col] != -1:
            continue

        num = row * m + col

        r, c = row, col
        while visited_by[r][c] == -1:
            visited_by[r][c] = num
            r, c = get_next(r, c)
        if visited_by[r][c] == num:
            ans += 1

print(ans)
