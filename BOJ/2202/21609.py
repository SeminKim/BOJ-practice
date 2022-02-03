# https://www.acmicpc.net/problem/21609
# Implementation

from collections import deque
from sys import stdin

n, m = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
EMPTY = 8
ans = 0


def prettyprint():
    for line in board:
        for num in line:
            print(str(num).rjust(2, " "), end=' ')
        print()


def bfs(row, col, target, get_history=False):
    Q = deque()
    Q.appendleft([row, col])
    visited = [[False] * n for _ in range(n)]
    visited[row][col] = True
    total_size = 1
    num_zero = (board[row][col] == 0)
    history = []
    representative = (row, col)
    while Q:
        x, y = Q.popleft()
        # representative block is a non-zero block with minimum (r,c)
        if board[x][y] != 0 and (x, y) < representative:
            representative = (x, y)
        if get_history:
            history.append((x, y))
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = True
                if board[nx][ny] == target:
                    total_size += 1
                    Q.append([nx, ny])
                elif board[nx][ny] == 0:
                    total_size += 1
                    num_zero += 1
                    Q.append([nx, ny])

    if get_history:
        return history
    else:
        return total_size, num_zero, representative, target


def find_biggest():
    biggest_size = 0
    biggest_groups = []
    for i in range(n):
        for j in range(n):
            # skip black and empty blocks
            if board[i][j] == -1 or board[i][j] == EMPTY:
                continue
            # colors is list of available target colors
            colors = [board[i][j]]
            if board[i][j] == 0:
                colors = [foo for foo in range(1, m + 1)]
            for color in colors:
                current_group = bfs(i, j, color)
                # size should be larger than 1 and there must be at least on common block.
                if current_group[0] < 2 or current_group[0] == current_group[1]:
                    continue
                if current_group[0] > biggest_size:
                    biggest_groups = [current_group]
                    biggest_size = current_group[0]
                elif current_group[0] == biggest_size:
                    biggest_groups.append(current_group)
    if biggest_groups:
        total, zero, [x, y], target = max(biggest_groups)
        return bfs(x, y, target, True)
    else:
        return None


while True:
    found = find_biggest()
    if found is None:
        break
    # pop and add score
    ans += len(found) ** 2
    for (x, y) in found:
        board[x][y] = EMPTY
    # gravity, rotation, gravity
    # gravity
    for i in reversed(range(n - 1)):
        for j in range(n):
            # black does not fall
            if board[i][j] != -1 and board[i + 1][j] == EMPTY:
                goal = i + 1
                while goal < n and board[goal][j] == EMPTY:
                    goal += 1
                goal -= 1
                board[goal][j] = board[i][j]
                board[i][j] = EMPTY
    # rotation
    new_board = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_board[n - 1 - j][i] = board[i][j]
    board = new_board
    # gravity
    for i in reversed(range(n - 1)):
        for j in range(n):
            # black does not fall
            if board[i][j] != -1 and board[i + 1][j] == EMPTY:
                goal = i + 1
                while goal < n and board[goal][j] == EMPTY:
                    goal += 1
                goal -= 1
                board[goal][j] = board[i][j]
                board[i][j] = EMPTY
print(ans)
