# https://www.acmicpc.net/problem/13460
# Complete search by BFS (4**10)

from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
board = [[] for _ in range(n)]
visited = [[[[False for _ in range(m)] for __ in range(n)] for ___ in range(m)] for ____ in range(n)]

red, blue, hole = [], [], []
for i in range(n):
    board[i] = list(stdin.readline().strip())
    for j in range(m):
        if board[i][j] == 'R':
            red = [i, j]
            board[i][j] = '.'
        if board[i][j] == 'B':
            blue = [i, j]
            board[i][j] = '.'
        if board[i][j] == 'O':
            hole = [i, j]


def tilt_vertical(r, b, depth, direction=1):
    # move red
    row, col = r
    while board[row + direction][col] != '#':
        row = row + direction
        if [row, col] == hole:
            break
    new_r = [row, col]

    # move blue
    row, col = b
    while board[row + direction][col] != '#':
        row = row + direction
        if [row, col] == hole:
            break
    new_b = [row, col]

    # if two ball in one col, and collide
    if r[1] == b[1] and new_r[0] == new_b[0] and new_r != hole:
        if direction == 1:
            if r[0] > b[0]:
                new_b[0] -= 1
            else:
                new_r[0] -= 1
        else:
            if r[0] < b[0]:
                new_b[0] += 1
            else:
                new_r[0] += 1

    return [new_r, new_b, depth + 1]


def tilt_horizontal(r, b, depth, direction=1):
    # move red
    row, col = r
    while board[row][col + direction] != '#':
        col = col + direction
        if [row, col] == hole:
            break
    new_r = [row, col]

    # move blue
    row, col = b
    while board[row][col + direction] != '#':
        col = col + direction
        if [row, col] == hole:
            break
    new_b = [row, col]

    # if two ball in one row, and collide
    if r[0] == b[0] and new_r[1] == new_b[1] and new_r != hole:
        if direction == 1:
            if r[1] > b[1]:
                new_b[1] -= 1
            else:
                new_r[1] -= 1
        else:
            if r[1] < b[1]:
                new_b[1] += 1
            else:
                new_r[1] += 1

    return [new_r, new_b, depth + 1]


def tilt_down(seq):
    r, b, d = seq
    return tilt_vertical(r, b, d, direction=1)


def tilt_up(seq):
    r, b, d = seq
    return tilt_vertical(r, b, d, direction=-1)


def tilt_right(seq):
    r, b, d = seq
    return tilt_horizontal(r, b, d, direction=1)


def tilt_left(seq):
    r, b, d = seq
    return tilt_horizontal(r, b, d, direction=-1)


q = deque()
q.append([red, blue, 0])
visited[red[0]][red[1]][blue[0]][blue[1]] = True

while q:
    now = q.popleft()
    for move in [tilt_down, tilt_up, tilt_left, tilt_right]:
        res = move(now)

        if res[1] == hole:
            continue

        if res[0] == hole:
            print(res[2])
            exit()

        rx, ry = res[0]
        bx, by = res[1]
        if not visited[rx][ry][bx][by] and res[2] < 10:
            visited[rx][ry][bx][by] = True
            q.append(res)

print(-1)
