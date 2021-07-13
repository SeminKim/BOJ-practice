# https://www.acmicpc.net/problem/16946
# Count using disjoint set.

from sys import stdin

n, m = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().strip())) for _ in range(n)]
head = [[(i, j) for j in range(m)] for i in range(n)]
rank = [[1 for _ in range(m)] for __ in range(n)]


def get_head(x, y):
    if head[x][y] == (x, y):
        return x, y
    head[x][y] = get_head(*head[x][y])
    return head[x][y]


def get_rank(x, y):
    x, y = get_head(x, y)
    return rank[x][y]


def union(x1, y1, x2, y2):
    x1, y1 = get_head(x1, y1)
    x2, y2 = get_head(x2, y2)
    if x1 == x2 and y1 == y2:  # already in same set.
        return

    if rank[x1][y1] >= rank[x2][y2]:
        head[x2][y2] = (x1, y1)
        rank[x1][y1] += rank[x2][y2]
    else:
        head[x1][y1] = (x2, y2)
        rank[x2][y2] += rank[x1][y1]


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for row in range(n):
    for col in range(m):
        if board[row][col] == 1:
            continue
        for i in range(4):
            x = row + dx[i]
            y = col + dy[i]
            if (0 <= x < n) and (0 <= y < m) and (board[x][y] == 0):
                union(row, col, x, y)

for row in range(n):
    for col in range(m):
        if board[row][col] == 0:
            print(0, end='')
        else:
            temp = 1
            counted = []
            for i in range(4):
                x = row + dx[i]
                y = col + dy[i]
                if (0 <= x < n) and (0 <= y < m) and (board[x][y] == 0):
                    foo = get_head(x, y)
                    if foo not in counted:
                        temp += get_rank(*foo)
                        counted.append(foo)
            print(temp % 10, end='')
    print()
