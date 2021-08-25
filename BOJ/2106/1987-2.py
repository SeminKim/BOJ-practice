from sys import stdin
from collections import deque

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

r, c = map(int, stdin.readline().split())
board = []
for _ in range(r):
    board.append(list(stdin.readline().strip()))

ans = 0


def isvalid(row, col):
    return 0 <= row <= r - 1 and 0 <= col <= c - 1


temp = [[''] * c for _ in range(r)]


def solve():
    Q = deque()
    Q.append([board[0][0], 0, 0])
    global ans
    while Q:
        history, row, col = Q.popleft()
        ans = max(ans, len(history))
        for d1, d2 in delta:
            newrow = row + d1
            newcol = col + d2
            if isvalid(newrow, newcol) and (board[newrow][newcol] not in history):
                if temp[newrow][newcol] == history + board[newrow][newcol]:
                    continue
                Q.append([history + board[newrow][newcol], newrow, newcol])
                temp[newrow][newcol] = history + board[newrow][newcol]
    print(ans)


solve()
