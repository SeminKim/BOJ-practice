# https://www.acmicpc.net/problem/1987
# Backtracking Search

from sys import stdin

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

r, c = map(int, stdin.readline().split())
board = []
for _ in range(r):
    board.append(list(stdin.readline().strip()))

history = set([])
ans = [0]


def isvalid(row, col):
    return 0 <= row <= r - 1 and 0 <= col <= c - 1


def search(row, col):
    history.add(board[row][col])
    if ans[0] < len(history):
        ans[0] = len(history)
    if ans[0] == 26:
        print(26)
        exit()
    for d1, d2 in delta:
        new_row = d1 + row
        new_col = d2 + col
        if isvalid(new_row, new_col) and (board[new_row][new_col] not in history):
            search(new_row, new_col)
    history.discard(board[row][col])


search(0, 0)
print(ans[0])

