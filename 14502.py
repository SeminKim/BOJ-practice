# https://www.acmicpc.net/problem/14502
from sys import stdin
from copy import deepcopy

n, m = map(int, stdin.readline().split())
lab = [[] for _ in range(n)]

for row in range(n):
    lab[row] = list(map(int, stdin.readline().split()))

original_lab = deepcopy(lab)

def simulate(lab_map):
    two_list = []
    visited = [[False for _ in range(m)] for _ in range(n)]
    for row in range(n):
        for col in range(m):
            if lab_map[row][col] == 2:
                two_list.append((row, col))
                visited[row][col] = True

    while len(two_list) != 0:
        x = two_list.pop(0)
        row = x[0]
        col = x[1]
        if row > 0:
            if lab_map[row - 1][col] == 0:
                lab_map[row - 1][col] = 2
                if not visited[row - 1][col]: two_list.append((row - 1, col))
        if row < n - 1:
            if lab_map[row + 1][col] == 0:
                lab_map[row + 1][col] = 2
                if not visited[row + 1][col]: two_list.append((row + 1, col))
        if col > 0:
            if lab_map[row][col - 1] == 0:
                lab_map[row][col - 1] = 2
                if not visited[row][col - 1]: two_list.append((row, col - 1))
        if col < m - 1:
            if lab_map[row][col + 1] == 0:
                lab_map[row][col + 1] = 2
                if not visited[row][col + 1]: two_list.append((row, col + 1))
    cnt = 0
    for row in range(n):
        for col in range(m):
            if lab_map[row][col] == 0: cnt += 1
    return cnt


res = 0
for i in range(n * m):
    row_i = i // m
    col_i = i % m
    for j in range(i + 1, n * m):
        row_j = j // m
        col_j = j % m
        for k in range(j + 1, n * m):
            row_k = k // m
            col_k = k % m
            a = lab[row_i][col_i]
            b = lab[row_j][col_j]
            c = lab[row_k][col_k]
            if a == 0 and b == 0 and c == 0:
                lab[row_i][col_i] = 1
                lab[row_j][col_j] = 1
                lab[row_k][col_k] = 1
                temp_res = simulate(lab)
                res = max(res, simulate(lab))
                lab = deepcopy(original_lab)
print(res)
