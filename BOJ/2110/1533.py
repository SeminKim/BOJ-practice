# https://www.acmicpc.net/problem/1533

from sys import stdin

n, s, e, t = map(int, stdin.readline().split())
graph = [[0 for _ in range(5 * n)] for _ in range(5 * n)]

for i in range(n):
    seq = list(map(int, list(stdin.readline().strip())))
    for j in range(n):
        graph[i][j] = seq[j]

for line in range(n):
    graph[line][n + 4 * line] = 1
    graph[n + 4 * line][n + 4 * line + 1] = 1
    graph[n + 4 * line + 1][n + 4 * line + 2] = 1
    graph[n + 4 * line + 2][n + 4 * line + 3] = 1
    for curr in range(n):
        element = graph[line][curr]
        if element > 1:
            graph[n + 4 * line + element - 2][curr] = 1
            graph[line][curr] = 0


def matmul(first, second=None):
    if second is None:  # square
        second = first
    temp = [[0 for _ in range(5 * n)] for _ in range(5 * n)]
    for i in range(5 * n):
        for j in range(5 * n):
            temp[i][j] = sum(first[i][x] * second[x][j] for x in range(5 * n)) % 1_000_003
    return temp


bit = bin(t)[2:][::-1]
log_t = len(bit)
subs = [graph]  # 2^ith power of graphs
for i in range(log_t):
    subs.append(matmul(subs[-1]))

res = [[0 for _ in range(5 * n)] for _ in range(5 * n)]
for i in range(5 * n):
    res[i][i] = 1

for i in range(log_t):
    if bit[i] == '1':
        res = matmul(res, subs[i])

print(res[s - 1][e - 1])
