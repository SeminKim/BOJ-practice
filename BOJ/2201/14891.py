# https://www.acmicpc.net/problem/14891
# Implementation

from sys import stdin


def turn(gear, direction):  # direction 1 is CW
    return gear[-direction:] + gear[:-direction]


gears = [stdin.readline().strip() for _ in range(4)]
k = int(stdin.readline().strip())
for _ in range(k):
    n, rot = map(int, stdin.readline().split())
    temp = []
    for i in range(1, 5):
        # connectivity
        if i == n:
            temp.append(turn(gears[i - 1], rot))
        elif i + 1 == n and gears[i - 1][2] != gears[n - 1][6]:
            temp.append(turn(gears[i - 1], -rot))
        elif i + 2 == n and gears[i - 1][2] != gears[i][6] and gears[i][2] != gears[n - 1][6]:
            temp.append(turn(gears[i - 1], rot))
        elif i + 3 == n and gears[i - 1][2] != gears[i][6] and gears[i][2] != gears[i + 1][6] and gears[i + 1][2] != \
                gears[n - 1][6]:
            temp.append(turn(gears[i - 1], -rot))
        elif i - 1 == n and gears[n - 1][2] != gears[i - 1][6]:
            temp.append(turn(gears[i - 1], -rot))
        elif i - 2 == n and gears[n - 1][2] != gears[i - 2][6] and gears[i - 2][2] != gears[i - 1][6]:
            temp.append(turn(gears[i - 1], rot))
        elif i - 3 == n and gears[n - 1][2] != gears[i - 3][6] and gears[i - 3][2] != gears[i - 2][6] and gears[i - 2][
            2] != gears[i - 1][6]:
            temp.append(turn(gears[i - 1], -rot))
        else:
            temp.append(gears[i - 1])
    gears = temp

print(sum([0, 2 ** x][gears[x][0] == '1'] for x in range(4)))
