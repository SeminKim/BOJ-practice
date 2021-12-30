# https://www.acmicpc.net/problem/14499
# Implementation

from sys import stdin

dr = [0, 0, 0, -1, 1]  # None, E, W, N, S
dc = [0, 1, -1, 0, 0]
n, m, x, y, k = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(n)]
seq = list(map(int, stdin.readline().split()))
dice = [0, 0, 0, 0, 0, 0]  # floor, north, east, west, south, top


def roll_south(die):
    return [die[4], die[0], die[2], die[3], die[5], die[1]]


def roll_north(die):
    return [die[1], die[5], die[2], die[3], die[0], die[4]]


def roll_east(die):
    return [die[2], die[1], die[5], die[0], die[4], die[3]]


def roll_west(die):
    return [die[3], die[1], die[0], die[5], die[4], die[2]]


for direction in seq:
    nx = x + dr[direction]
    ny = y + dc[direction]
    if 0 <= nx < n and 0 <= ny < m:
        dice = [None, roll_east, roll_west, roll_north, roll_south][direction](dice)
        if board[nx][ny] == 0:
            board[nx][ny] = dice[0]
        else:
            dice[0] = board[nx][ny]
            board[nx][ny] = 0
        print(dice[5])
        x, y = nx, ny
