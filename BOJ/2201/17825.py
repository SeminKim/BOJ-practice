from sys import stdin

seq = list(map(int, stdin.readline().split()))

board = [[i for i in range(0, 41, 2)], [13, 16, 19, 25, 30, 35, 40], [22, 24, 25, 30, 35, 40],
         [28, 27, 26, 25, 30, 35, 40]]

pos = [[0, 0] for _ in range(4)]
pos[0] = [0, seq[0]]


def dfs(idx, acc):
    if idx == len(seq):
        return acc

    to_go = seq[idx]
    ret = [0]
    for curr in range(4):
        x, y = pos[curr]
        if x == y == -1:
            continue
        nacc = acc
        if x == 0 and y == 5:
            nx, ny = 1, to_go - 1
        elif x == 0 and y == 10:
            nx, ny = 2, to_go - 1
        elif x == 0 and y == 15:
            nx, ny = 3, to_go - 1
        else:
            nx, ny = x, y + to_go

        if [nx, ny] in pos:
            continue
        if (nx == 1 or nx == 3) and ny >= 3:
            if ([1, ny] in pos) or ([2, ny - 1] in pos) or ([3, ny] in pos):
                continue
            if ny == 6 and ([0, 20] in pos):
                continue
        if nx == 2 and ny >= 2:
            if ([1, ny + 1] in pos) or ([3, ny + 1] in pos):
                continue
            if ny == 5 and ([0, 20] in pos):
                continue

        if nx == 0 and ny == 20:
            if ([1, 6] in pos) or ([2, 5] in pos) or ([3, 6] in pos):
                continue

        if ny >= len(board[x]):
            pos[curr] = [-1, -1]
        else:
            nacc += board[nx][ny]
            pos[curr] = [nx, ny]

        ret.append(dfs(idx + 1, nacc))
        pos[curr] = [x, y]
    return max(ret)


print(dfs(1, board[0][seq[0]]))
