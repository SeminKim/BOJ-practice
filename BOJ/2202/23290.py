from itertools import product as pd
from sys import stdin

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

M, S = map(int, stdin.readline().split())
smell = [[0] * 4 for _ in range(4)]
board = [[[0 for _ in range(8)] for _ in range(4)] for _ in range(4)]  # number of fish at board[row][col][direction]
for _ in range(M):
    x, y, d = map(int, stdin.readline().split())
    board[x - 1][y - 1][d - 1] += 1
shark_r, shark_c = map(int, stdin.readline().split())
shark_r -= 1
shark_c -= 1

# def debug(mode=0):
#     for i in range(4):
#         print(i, '|', end=' ')
#         for j in range(4):
#             print(j, ':', end='')
#             if mode == 0:
#                 for num, flag in zip(board[i][j], '←↖↑↗→↘↓↙'):
#                     print(flag * num, end='')
#             else:
#                 for num, flag in zip(new_board[i][j], '←↖↑↗→↘↓↙'):
#                     print(flag * num, end='')
#             print(' | ', end='')
#         print()


for _ in range(S):
    # make new board for copying
    new_board = [[[0 for _ in range(8)] for _ in range(4)] for _ in range(4)]
    # move fish
    for i in range(4):
        for j in range(4):
            for k in range(8):
                target = k
                while True:
                    ni = i + dx[target]
                    nj = j + dy[target]
                    if 0 <= ni < 4 and 0 <= nj < 4 and (ni, nj) != (shark_r, shark_c) and smell[ni][nj] == 0:
                        new_board[ni][nj][target] += board[i][j][k]
                        break
                    else:
                        target = (target + 7) % 8  # if not available, turn 45 CCW.
                        if target == k:
                            new_board[i][j][k] += board[i][j][k]
                            break
    # print("after move...")
    # debug(1)

    # find the best way to move shark
    best = -1
    best_move = (0, 0, 0)
    for case in pd([2, 0, 6, 4], repeat=3):
        curr = 0
        new_r, new_c = shark_r, shark_c
        visited = set()
        for move in case:
            new_r += dx[move]
            new_c += dy[move]
            if not (0 <= new_r < 4 and 0 <= new_c < 4):
                break
            if (new_r, new_c) not in visited:
                curr += sum(new_board[new_r][new_c])
                visited.add((new_r, new_c))
        else:
            if curr > best:
                best = curr
                best_move = case

    # move shark
    for move in best_move:
        shark_r += dx[move]
        shark_c += dy[move]
        for bar in range(8):
            if new_board[shark_r][shark_c][bar] != 0:
                smell[shark_r][shark_c] = 3
                new_board[shark_r][shark_c][bar] = 0
    # decrease smell
    for i in range(4):
        for j in range(4):
            smell[i][j] = max(0, smell[i][j] - 1)
    # finish copy magic
    for i in range(4):
        for j in range(4):
            for k in range(8):
                board[i][j][k] += new_board[i][j][k]
    # print("after copying...")
    # debug()

ans = 0
for i in range(4):
    for j in range(4):
        ans += sum(board[i][j])

print(ans)
