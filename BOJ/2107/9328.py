# https://www.acmicpc.net/problem/9328

from sys import stdin
from collections import deque

UP = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
DOWN = 'abcdefghijklmnopqrstuvwxyz'
DX = [0, 0, 1, -1]
DY = [1, -1, 0, 0]


def solve():
    h, w = map(int, stdin.readline().split())
    board = [list(stdin.readline().strip()) for _ in range(h)]
    foo = stdin.readline().strip()
    if foo == '0':
        key = set()
    else:
        key = set(foo)
    ans = 0

    # find position of doors
    door_pos = {i: [] for i in UP}
    for i in range(h):
        for j in range(w):
            if board[i][j] in UP:
                door_pos[board[i][j]].append([i, j])

    # if there is key, replace door with '.'
    for one in key:
        while door_pos[one.upper()]:
            x, y = door_pos[one.upper()].pop()
            board[x][y] = '.'

    # find entrance.
    entrance = []
    for i in range(h):
        if board[i][0] != '*':
            entrance.append([i, 0])

        if board[i][w - 1] != '*':
            entrance.append([i, w - 1])

    for i in range(1, w - 1):
        if board[0][i] != '*':
            entrance.append([0, i])

        if board[h - 1][i] != '*':
            entrance.append([h - 1, i])

    # BFS initialize (start from entrance)
    Q = deque()
    ready = {i: [] for i in UP}
    visited = [[False for _ in range(w)] for _ in range(h)]
    for enter in entrance:
        Q.append(enter)
        visited[enter[0]][enter[1]] = True

    # BFS
    while Q:
        x, y = Q.popleft()
        visited[x][y] = True

        # if blocked, stop and save to 'ready'
        if board[x][y] in UP:
            ready[board[x][y]].append([x, y])
            continue

        # found paper
        if board[x][y] == '$':
            board[x][y] = '.'
            ans += 1

        # found key
        elif board[x][y] in DOWN:
            key_found = board[x][y]
            # for every position of door open-able with this key
            for pos_x, pos_y in door_pos[key_found.upper()]:
                board[pos_x][pos_y] = '.'
            # if position is blocked before, restart search from that position
            while ready[key_found.upper()]:
                pos_x, pos_y = ready[key_found.upper()].pop()
                Q.append([pos_x, pos_y])
            board[x][y] = '.'

        # proceed search
        for dx, dy in zip(DX, DY):
            new_x, new_y = x + dx, y + dy
            if (0 <= new_x < h) and (0 <= new_y < w):
                if (not visited[new_x][new_y]) and (board[new_x][new_y] != '*'):
                    Q.append([new_x, new_y])
                    visited[new_x][new_y] = True

    print(ans)


t = int(stdin.readline().strip())

for _ in range(t):
    solve()
