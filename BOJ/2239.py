# https://www.acmicpc.net/problem/2239

from sys import stdin

board = [[] for _ in range(9)]
zeros = []
for i in range(9):
    board[i] = list(map(int, stdin.readline().strip()))

for row in range(9):
    for col in range(9):
        if board[row][col] == 0:
            zeros.append([row, col])

n = len(zeros)


def dfs(i, history):
    if i == n:
        return history

    for num in range(1, 10):
        validity = True
        row, col = zeros[i]
        for r in range(9):
            if board[r][col] == num:
                validity = False
        for c in range(9):
            if board[row][c] == num:
                validity = False
        for dx in range(3):
            for dy in range(3):
                if board[3 * (row // 3) + dx][3 * (col // 3) + dy] == num:
                    validity = False

        if validity:
            board[row][col] = num
            history.append(num)
            ans = dfs(i + 1, history)
            if ans is None:
                history.pop()
                x, y = zeros[i]
                board[x][y] = 0
            else:
                return history
    return None


dfs(0, [])
for row in board:
    for col in row:
        print(col, end='')
    print()

'''
000000000
000000000
000000000
000000000
000000000
000000000
000000000
000000000
000000000
'''
