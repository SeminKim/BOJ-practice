# https://www.acmicpc.net/problem/3190
# Implementation

from collections import deque
from sys import stdin

N = int(stdin.readline().strip())
fruit = [[False for _ in range(N)] for _ in range(N)]
K = int(stdin.readline().strip())
for _ in range(K):
    r, c = map(int, stdin.readline().split())
    fruit[r - 1][c - 1] = True
L = int(stdin.readline().strip())
change = [False for _ in range(10001)]
for _ in range(L):
    X, C = stdin.readline().split()
    change[int(X)] = C

snake = deque()
snake.append((0, 0))
dr = [0, 1, 0, -1]  # E, S, W, N
dc = [1, 0, -1, 0]
heading = 0  # east
for t in range(1, 10102):
    head_r, head_c = snake[0]
    new_r = head_r + dr[heading]
    new_c = head_c + dc[heading]
    if (0 <= new_r < N) and (0 <= new_c < N) and (not (new_r, new_c) in snake):
        snake.appendleft((new_r, new_c))
        if fruit[new_r][new_c]:
            fruit[new_r][new_c] = False
        else:
            snake.pop()
        if change[t] == 'L':
            heading = (heading + 3) % 4
        if change[t] == 'D':
            heading = (heading + 1) % 4
    else:
        print(t)
        exit(0)
