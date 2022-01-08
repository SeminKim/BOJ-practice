# https://www.acmicpc.net/problem/15683
# Backtracking

from sys import stdin

n, m = map(int, stdin.readline().split())
office = [list(map(int, stdin.readline().split())) for _ in range(n)]
cctvs = []
for i in range(n):
    for j in range(m):
        if 1 <= office[i][j] <= 5:
            cctvs.append([i, j])


def set_office(i, j, *args):
    changed = []
    if 'south' in args:
        move = 1
        while i + move < n and office[i + move][j] != 6:
            if office[i + move][j] == 0:
                changed.append([i + move, j])
                office[i + move][j] = 7
            move += 1
    if 'north' in args:
        move = -1
        while i + move >= 0 and office[i + move][j] != 6:
            if office[i + move][j] == 0:
                changed.append([i + move, j])
                office[i + move][j] = 7
            move -= 1
    if 'east' in args:
        move = 1
        while j + move < m and office[i][j + move] != 6:
            if office[i][j + move] == 0:
                changed.append([i, j + move])
                office[i][j + move] = 7
            move += 1
    if 'west' in args:
        move = -1
        while j + move >= 0 and office[i][j + move] != 6:
            if office[i][j + move] == 0:
                changed.append([i, j + move])
                office[i][j + move] = 7
            move -= 1
    return changed


def solve(idx):
    if idx == len(cctvs):
        ret = 0
        for r in range(n):
            for c in range(m):
                ret += (office[r][c] == 0)
        return ret

    i, j = cctvs[idx]
    tmp = []
    direction = []
    if office[i][j] == 1:
        direction = [['south'], ['north'], ['east'], ['west']]
    elif office[i][j] == 2:
        direction = [['south', 'north'], ['east', 'west']]
    elif office[i][j] == 3:
        direction = [['north', 'east'], ['east', 'south'], ['south', 'west'], ['west', 'north']]
    elif office[i][j] == 4:
        direction = [['north', 'east', 'south'], ['east', 'south', 'west'], ['south', 'west', 'north'],
                     ['west', 'north', 'east']]
    elif office[i][j] == 5:
        direction = [['south', 'north', 'east', 'west']]

    for direc in direction:
        changed = set_office(i, j, *direc)
        tmp.append(solve(idx + 1))
        for (r, c) in changed:
            office[r][c] = 0
    return min(tmp)


print(solve(0))
