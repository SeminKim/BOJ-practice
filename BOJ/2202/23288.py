# https://www.acmicpc.net/problem/23288
# Disjoint set

from sys import stdin

n, m, k = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(n)]
dice = [-1, 1, 2, 3, 4, 5, 6]  # foo, top, north, east, west, south, bottom
dx = [0, 1, 0, -1]  # east, south, west, north
dy = [1, 0, -1, 0]


#  123456 -> 513462
def rotate_north(current_dice):
    return [-1, current_dice[5], current_dice[1], current_dice[3], current_dice[4], current_dice[6], current_dice[2]]


#  123456 -> 263415
def rotate_south(current_dice):
    return [-1, current_dice[2], current_dice[6], current_dice[3], current_dice[4], current_dice[1], current_dice[5]]


#  123456 -> 421653
def rotate_east(current_dice):
    return [-1, current_dice[4], current_dice[2], current_dice[1], current_dice[6], current_dice[5], current_dice[3]]


#  123456 -> 326154
def rotate_west(current_dice):
    return [-1, current_dice[3], current_dice[2], current_dice[6], current_dice[1], current_dice[5], current_dice[4]]


def rotate(current_dice, direction):
    return [rotate_east, rotate_south, rotate_west, rotate_north][direction](current_dice)


# board does not change, so calculate points with disjoint set.
head = [[(i, j) for j in range(m)] for i in range(n)]
count = [[1] * m for _ in range(n)]


def find_head(i, j):
    if head[i][j] != (i, j):
        head[i][j] = find_head(*head[i][j])
    return head[i][j]


def union(first_x, first_y, second_x, second_y):
    if find_head(first_x, first_y) == find_head(second_x, second_y):
        return
    first_x, first_y = find_head(first_x, first_y)
    second_x, second_y = find_head(second_x, second_y)
    if count[first_x][first_y] <= count[second_x][second_y]:
        first_x, first_y, second_x, second_y = second_x, second_y, first_x, first_y
    head[second_x][second_y] = (first_x, first_y)
    count[first_x][first_y] += count[second_x][second_y]
    count[second_x][second_y] = 0


def get_count(i, j):
    foo, bar = find_head(i, j)
    return count[foo][bar]


for row in range(n):
    for col in range(m):
        for d in range(4):
            nrow = row + dx[d]
            ncol = col + dy[d]
            if 0 <= nrow < n and 0 <= ncol < m and board[row][col] == board[nrow][ncol]:
                union(row, col, nrow, ncol)

ans = 0
x = y = d = 0
for _ in range(k):
    nx = x + dx[d]
    ny = y + dy[d]
    if not (0 <= nx < n and 0 <= ny < m):
        d = (d + 2) % 4
        nx = x + dx[d]
        ny = y + dy[d]
    dice = rotate(dice, d)
    x, y = nx, ny
    ans += board[nx][ny] * get_count(nx, ny)
    if dice[6] > board[nx][ny]:
        d = (d + 1) % 4
    elif dice[6] < board[nx][ny]:
        d = (d + 3) % 4
print(ans)
