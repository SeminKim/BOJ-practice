# https://www.acmicpc.net/problem/19236
# Implementation

from sys import stdin
from copy import deepcopy

direction = [[-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]
board = []
for i in range(4):
    line = list(map(lambda x: int(x) - 1, stdin.readline().split()))
    board.append([[line[0], line[1]], [line[2], line[3]], [line[4], line[5]], [line[6], line[7]]])

fish = [[] for _ in range(16)]
for row in range(4):
    for col in range(4):
        pos, d = board[row][col]
        fish[pos] = [row, col, d]


def dfs(shark_x, shark_y, shark_d, acc):
    # first move fish
    global fish, board
    save_fish = deepcopy(fish)
    save_board = deepcopy(board)
    for i in range(16):
        r, c, d = fish[i]
        if r == -1:  # already eaten.
            continue
        nr = r + direction[d][0]
        nc = c + direction[d][1]
        nd = d
        # maybe fish can always move??
        while not (0 <= nr < 4 and 0 <= nc < 4 and (nr, nc) != (shark_x, shark_y)):
            nd = (nd + 1) % 8
            nr = r + direction[nd][0]
            nc = c + direction[nd][1]
        # swap position
        target_num, target_d = board[nr][nc]

        fish[i] = [nr, nc, nd]
        if target_num != -1:
            fish[target_num] = r, c, target_d
        board[nr][nc] = [i, nd]
        board[r][c] = [target_num, target_d]

    # then, move shark.
    ret = acc
    for mult in range(1, 4):
        nx = shark_x + mult * direction[shark_d][0]
        ny = shark_y + mult * direction[shark_d][1]
        if not (0 <= nx < 4 and 0 <= ny < 4):
            break
        target_num, target_d = board[nx][ny]
        if target_num == -1:
            continue
        fish[target_num] = [-1, -1, -1]
        board[nx][ny] = [-1, -1]
        ret = max(ret, dfs(nx, ny, target_d, acc + target_num + 1))
        board[nx][ny] = [target_num, target_d]
        fish[target_num] = [nx, ny, target_d]
    fish = save_fish
    board = save_board
    return ret


num, d = board[0][0]
fish[num] = [-1, -1, -1]
board[0][0] = [-1, -1]

print(dfs(0, 0, d, num + 1))
