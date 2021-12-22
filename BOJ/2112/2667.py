# https://www.acmicpc.net/problem/2667
# DFS

from sys import stdin

n = int(stdin.readline().strip())
board = [stdin.readline().strip() for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def valid(r, c):
    return (0 <= r < n) and (0 <= c < n)


def dfs(row, col, count):
    visited[row][col] = count
    res = 1
    for i in range(4):
        nrow = row + dx[i]
        ncol = col + dy[i]
        if (not valid(nrow, ncol)) or visited[nrow][ncol] or board[nrow][ncol] == '0':
            continue
        res += dfs(nrow, ncol, count)
    return res


ans = []
cnt = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] or board[i][j] == '0':
            continue
        temp = dfs(i, j, cnt + 1)
        if temp:
            cnt += 1
            ans.append(temp)

print(cnt)
for foo in sorted(ans):
    print(foo)
