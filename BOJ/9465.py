# https://www.acmicpc.net/problem/9465
# Use DP. 2*n Table에 그 원소를 반드시 포함하는 최대 점수를 저장.
# table[1][col] = sticker값 + max(table[0][col-1], table[0][col-1])
from sys import stdin

t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    table = [[], []]
    table[0] = list(map(int, stdin.readline().split()))
    table[1] = list(map(int, stdin.readline().split()))
    if n == 1:
        print(max(table[0][0], table[1][0]))
    else:
        table[0][1] += table[1][0]
        table[1][1] += table[0][0]
        for col in range(2, n):
            for row in range(2):
                table[row][col] += max(table[1 - row][col - 1], table[1 - row][col - 2])
        print(max(table[0][n - 1], table[0][n - 2], table[1][n - 1], table[1][n - 2]))
