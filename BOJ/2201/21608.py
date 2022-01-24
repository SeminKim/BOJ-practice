from sys import stdin

n = int(stdin.readline().strip())
board = [[0 for _ in range(n)] for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def get_neighbor(row, col):
    ret = []
    for d in range(4):
        nx = row + dx[d]
        ny = col + dy[d]
        if 0 <= nx < n and 0 <= ny < n:
            ret.append(board[nx][ny])
    return ret


info = [list(map(int, stdin.readline().split())) for _ in range(n ** 2)]


def key(row, col, like):
    if board[row][col] != 0:
        return -1, 42, 4, 2
    neighbor = get_neighbor(row, col)
    curr_prefer = sum((num in like) for num in neighbor)
    curr_empty = sum((num == 0) for num in neighbor)
    return curr_prefer, curr_empty, -row, -col


for curr, *like in info:
    x, y = max(((i, j) for i in range(n) for j in range(n)), key=lambda pos: key(*pos, like))
    board[x][y] = curr

like = [[]] + sorted(info)

ans = 0
for i in range(n):
    for j in range(n):
        ans += int(pow(10, sum((num in like[board[i][j]]) for num in get_neighbor(i, j)) - 1))

print(ans)
