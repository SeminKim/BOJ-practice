# https://www.acmicpc.net/problem/21611
# Implementation
from sys import stdin

dx = [42, -1, 1, 0, 0]
dy = [42, 0, 0, -1, 1]

# get input
n, m = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(n)]
mid = n // 2
total = n * n

# make useful mappings between 1d and 2d.
to_1d = [[-1] * n for _ in range(n)]
to_2d = [(mid, mid) for _ in range(n ** 2)]
x = y = mid
to_1d[x][y] = 0
dd = [3, 2, 4, 1]
d = -1
for i in range(1, total):
    if (x + y == n - 1) or (x > n // 2 and x == y) or (x <= n // 2 and x == y + 1):
        d = (d + 1) % 4
    x += dx[dd[d]]
    y += dy[dd[d]]
    to_1d[x][y] = i
    to_2d[i] = (x, y)


def fill_empty():
    for i in range(1, total):
        x, y = to_2d[i]
        if board[x][y] == 0:
            for j in range(i + 1, total):
                jx, jy = to_2d[j]
                if board[jx][jy] != 0:
                    board[x][y] = board[jx][jy]
                    board[jx][jy] = 0
                    break
            else:
                return


# return False when explosion did not happen
def explode():
    explosion_flag = False
    last_num = -1
    last_count = -1
    for i in range(1, total):
        x, y = to_2d[i]
        if last_num == 0:
            break
        if board[x][y] == last_num:
            last_count += 1
        else:
            if last_count >= 4:
                explosion_flag = True
                ans[last_num] += last_count
                for go_back in reversed(range(i - last_count, i)):
                    bx, by = to_2d[go_back]
                    board[bx][by] = 0
            last_num = board[x][y]
            last_count = 1
    return explosion_flag


ans = [0, 0, 0, 0]  # number of exploded marble.
# do blizzard.
for _ in range(m):
    d, s = map(int, stdin.readline().split())
    # drop ice
    for mult in range(1, s + 1):
        board[mid + mult * dx[d]][mid + mult * dy[d]] = 0
    # repeat filling empty spaces and pop 4 consecutive numbers.
    fill_empty()
    while explode():
        fill_empty()
    # morph
    new_board = [[0] * n for _ in range(n)]
    current_index = 1
    last_num = board[mid][mid - 1]
    last_count = 0
    for i in range(1, total):
        x, y = to_2d[i]
        if last_num == 0 or current_index == total:
            break
        if board[x][y] == last_num:
            last_count += 1
        else:
            jx, jy = to_2d[current_index]
            new_board[jx][jy] = last_count
            jx, jy = to_2d[current_index + 1]
            new_board[jx][jy] = last_num
            current_index += 2
            last_num = board[x][y]
            last_count = 1
    board = new_board

print(1 * ans[1] + 2 * ans[2] + 3 * ans[3])
