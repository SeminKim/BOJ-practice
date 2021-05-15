# https://www.acmicpc.net/problem/2206
# Use BFS. Use two array A and B, each for saving cost with/without wall break.

from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
table = [[0 for _ in range(m)] for _ in range(n)]

for row in range(n):
    for col, chr in enumerate(stdin.readline()):
        if chr == '1':
            table[row][col] = 1

A = [[float('inf') for _ in range(m)] for _ in range(n)]  # Costs, without wall breaking
B = [[float('inf') for _ in range(m)] for _ in range(n)]  # Costs, with or without a wall breaking

Q = deque()

Q.append((1, True, [0, 0]))  # put tuple (cost, canBreakWall, [row,col])
ans = -1
while len(Q) != 0:
    cost, canBreakWall, (row, col) = Q.popleft()
    if row == n - 1 and col == m - 1:
        ans = cost
        break

    if row > 0:
        if canBreakWall:
            if table[row - 1][col] == 0 and cost + 1 < A[row - 1][col]:
                A[row - 1][col] = cost + 1
                Q.append((cost + 1, True, [row - 1, col]))
            elif table[row - 1][col] == 1 and cost + 1 < B[row - 1][col]:
                B[row - 1][col] = cost + 1
                Q.append((cost + 1, False, [row - 1, col]))
        else:
            if table[row - 1][col] == 0 and cost + 1 < B[row - 1][col]:
                B[row - 1][col] = cost + 1
                Q.append((cost + 1, False, [row - 1, col]))

    if col > 0:
        if canBreakWall:
            if table[row][col - 1] == 0 and cost + 1 < A[row][col - 1]:
                A[row][col - 1] = cost + 1
                Q.append((cost + 1, True, [row, col - 1]))
            elif table[row][col - 1] == 1 and cost + 1 < B[row][col - 1]:
                B[row][col - 1] = cost + 1
                Q.append((cost + 1, False, [row, col - 1]))
        else:
            if table[row][col - 1] == 0 and cost + 1 < B[row][col - 1]:
                B[row][col - 1] = cost + 1
                Q.append((cost + 1, False, [row, col - 1]))

    if row < n - 1:
        if canBreakWall:
            if table[row + 1][col] == 0 and cost + 1 < A[row + 1][col]:
                A[row + 1][col] = cost + 1
                Q.append((cost + 1, True, [row + 1, col]))
            elif table[row + 1][col] == 1 and cost + 1 < B[row + 1][col]:
                B[row + 1][col] = cost + 1
                Q.append((cost + 1, False, [row + 1, col]))
        else:
            if table[row + 1][col] == 0 and cost + 1 < B[row + 1][col]:
                B[row + 1][col] = cost + 1
                Q.append((cost + 1, False, [row + 1, col]))

    if col < m - 1:
        if canBreakWall:
            if table[row][col + 1] == 0 and cost + 1 < A[row][col + 1]:
                A[row][col + 1] = cost + 1
                Q.append((cost + 1, True, [row, col + 1]))
            elif table[row][col + 1] == 1 and cost + 1 < B[row][col + 1]:
                B[row][col + 1] = cost + 1
                Q.append((cost + 1, False, [row, col + 1]))
        else:
            if table[row][col + 1] == 0 and cost + 1 < B[row][col + 1]:
                B[row][col + 1] = cost + 1
                Q.append((cost + 1, False, [row, col + 1]))

print(ans)


