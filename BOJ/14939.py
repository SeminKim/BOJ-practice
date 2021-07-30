# https://www.acmicpc.net/problem/14939
# 2^10 case for first line, then line by line greedy.

from sys import stdin
from copy import deepcopy

dx = [1, -1, 0, 0, 0]
dy = [0, 0, 0, 1, -1]
INF = 101


def push_switch(row, col, arr):
    for i in range(5):
        x = row + dx[i]
        y = col + dy[i]
        if 0 <= x < 10 and 0 <= y < 10:
            if arr[x][y] == 'O':
                arr[x][y] = '#'
            else:
                arr[x][y] = 'O'
    return arr


foo = [list(stdin.readline().strip()) for _ in range(10)]

ans = INF
for case in range(1024):
    res = 0
    board = deepcopy(foo)
    binary = bin(case)[2:].rjust(10, '0')
    for col, bit in enumerate(binary):
        if bit == '1':
            board = push_switch(0, col, board)
            res += 1

    for row in range(1, 10):
        for col in range(10):
            if board[row - 1][col] == 'O':
                board = push_switch(row, col, board)
                res += 1

    if 'O' not in board[-1]:
        ans = min(ans, res)

if ans == INF:
    ans = -1

print(ans)
