# https://www.acmicpc.net/problem/17143

from sys import stdin

R, C, M = map(int, stdin.readline().split())
grid = [[] for _ in range(C + 1)]
sharks = []

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, 1, -1]
complement = [0, 2, 1, 4, 3]


def update(row, col, speed, direction):
    if dx[direction] != 0:
        delta = (speed * dx[direction]) % (2 * (R - 1))
        if R < row + delta < 2 * R:
            row = R - (row + delta - R)
            direction = complement[direction]
        elif row + delta >= 2 * R:
            row = 2 + row + delta - 2 * R

        elif -R + 1 < row + delta <= 0:
            row = 2 - (row + delta)
            direction = complement[direction]
        elif row + delta <= -R + 1:
            row = (row + delta) + 2 * R - 2
        else:
            row = row + delta

    else:
        delta = (speed * dy[direction]) % (2 * (C - 1))
        if C < col + delta < 2 * C:
            col = C - (col + delta - C)
            direction = complement[direction]
        elif col + delta >= 2 * C:
            col = 2 + col + delta - 2 * C

        elif -C + 1 < col + delta <= 0:
            col = 2 - (col + delta)
            direction = complement[direction]
        elif col + delta <= -C + 1:
            col = (col + delta) + 2 * C - 2
        else:
            col = col + delta
    return row, col, speed, direction


for _ in range(M):
    r, c, s, d, z = map(int, stdin.readline().split())
    grid[c].append([z, r, c, s, d])  # size comes first: [0]size, [1]row, [2]col, [3]speed, [4]direction
    sharks.append([z, r, c, s, d])

sharks.sort(reverse=True)  # large to small

ans = 0
pos = 0
while pos < C:
    pos += 1
    if len(grid[pos]) > 0:
        catch = min(grid[pos], key=lambda x: x[1])
        ans += catch[0]
    else:
        catch = None

    occupied = [[False for _ in range(C + 1)] for __ in range(R + 1)]
    new_sharks = []
    new_grid = [[] for _ in range(C + 1)]

    for shark in sharks:
        if shark == catch:
            continue

        z, r, c, s, d = shark
        r, c, s, d = update(r, c, s, d)
        if not occupied[r][c]:
            occupied[r][c] = True
            new_sharks.append([z, r, c, s, d])
            new_grid[c].append([z, r, c, s, d])
    sharks = new_sharks
    grid = new_grid

print(ans)
