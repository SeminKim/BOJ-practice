# https://www.acmicpc.net/problem/19237
# Implementation

from sys import stdin

dx = [-1, 1, 0, 0]  # up, down, left, right
dy = [0, 0, -1, 1]

n, m, k = map(int, stdin.readline().split())
shark = [[] for _ in range(m)]
for i in range(n):
    line = list(map(int, stdin.readline().split()))
    for j in range(n):
        if line[j] != 0:
            shark[line[j] - 1] = [i, j]

board = [[[-1, -1] for _ in range(n)] for _ in range(n)]  # initially there's no fragrance.
direction = list(map(lambda x: int(x) - 1, stdin.readline().split()))
prefer = [[list(map(lambda x: int(x) - 1, stdin.readline().split())) for _ in range(4)] for _ in range(m)]
count = m

for t in range(1, 1001):
    # first, make smell
    for i in range(m):
        row, col = shark[i]
        if row == -1:
            continue
        board[row][col] = [i, k]  # shark number, duration

    # then, move
    new_board = [[[-1, -1] for _ in range(n)] for _ in range(n)]
    for i in range(m):
        row, col = shark[i]
        if row == -1:
            continue
        d = direction[i]
        target_direction = None
        my_fragrance = None
        # first, find for no-fragrance cell
        for target in prefer[i][d]:
            nrow = row + dx[target]
            ncol = col + dy[target]
            if 0 <= nrow < n and 0 <= ncol < n:
                if board[nrow][ncol][0] == -1:  # no-fragrance
                    target_direction = target
                    break
                if board[nrow][ncol][0] == i and my_fragrance is None:  # my-fragrance
                    my_fragrance = target
        # if there was no empty cell, go to my-fragrance
        if target_direction is None:
            target_direction = my_fragrance
        # actually moving
        nrow = row + dx[target_direction]
        ncol = col + dy[target_direction]
        direction[i] = target_direction
        shark[i] = [nrow, ncol]
        # when two sharks collide
        if new_board[nrow][ncol][0] != -1:
            other = new_board[nrow][ncol][0]
            count -= 1
            # lose
            if other < i:
                shark[i] = [-1, -1]
            else:
                shark[other] = [-1, -1]
                new_board[nrow][ncol] = [i, -1]
        else:
            new_board[nrow][ncol] = [i, -1]

    # finally, decrease smell.
    for i in range(n):
        for j in range(n):
            num, dur = board[i][j]
            if num != -1 and dur > 1:
                new_board[i][j] = [num, dur - 1]

    board = new_board
    if count == 1:
        print(t)
        break

else:
    print(-1)
