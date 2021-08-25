# https://www.acmicpc.net/problem/12100

from sys import stdin
from collections import deque

n = int(stdin.readline().strip())
board = []
for _ in range(n):
    board.append(list(map(int, stdin.readline().split())))


def make_compact_up(arr):  # delete 0 between tile when moving up
    new_arr = [[0 for _ in range(n)] for __ in range(n)]
    for col in range(n):
        pointer = 0
        for row in range(n):
            if arr[row][col] != 0:
                new_arr[pointer][col] = arr[row][col]
                pointer += 1
    return new_arr


def make_compact_left(arr):  # delete 0 between tile when moving left
    new_arr = [[0 for _ in range(n)] for __ in range(n)]
    for row in range(n):
        pointer = 0
        for col in range(n):
            if arr[row][col] != 0:
                new_arr[row][pointer] = arr[row][col]
                pointer += 1
    return new_arr


def move_up(arr):  # one move to up
    arr = make_compact_up(arr)
    for row in range(1, n):
        for col in range(n):
            if arr[row - 1][col] == arr[row][col]:
                arr[row - 1][col] *= 2
                arr[row][col] = 0

    return make_compact_up(arr)


def move_down(arr):  # one move to down
    arr.reverse()
    arr = move_up(arr)
    arr.reverse()
    return arr


def move_left(arr):  # one move to left
    arr = make_compact_left(arr)
    for col in range(1, n):
        for row in range(n):
            if arr[row][col - 1] == arr[row][col]:
                arr[row][col - 1] *= 2
                arr[row][col] = 0
    return make_compact_left(arr)


def move_right(arr):  # one move to right
    for line in arr:
        line.reverse()
    arr = move_left(arr)
    for line in arr:
        line.reverse()
    return arr


def get_max(arr):
    ans = 0
    for line in arr:
        ans = max(ans, max(line))
    return ans


q = deque()
q.append(board)

for level in range(5):
    for foo in range(4 ** level):
        now = q.popleft()
        for func in [move_up, move_left, move_down, move_right]:
            q.append(func(now))

ans = 0
for curr in q:
    ans = max(get_max(curr), ans)

print(ans)
