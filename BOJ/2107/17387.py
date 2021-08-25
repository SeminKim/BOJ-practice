# https://www.acmicpc.net/problem/17387

from sys import stdin


def solve():
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    if x1 > x2:
        x1, y1, x2, y2 = x2, y2, x1, y1

    x3, y3, x4, y4 = map(int, stdin.readline().split())
    if x3 > x4:
        x3, y3, x4, y4 = x4, y4, x3, y3

    if x1 == x2 and x3 == x4:
        if x1 != x3:
            return 0

        y1, y2 = sorted([y1, y2])
        y3, y4 = sorted([y3, y4])
        if y3 <= y2 <= y4 or y1 <= y4 <= y2:
            return 1
        return 0

    if x3 == x4:
        x1, y1, x3, y3 = x3, y3, x1, y1
        x2, y2, x4, y4 = x4, y4, x2, y2

    if x1 == x2:
        x = x1
        if (x - x3) * (x - x4) > 0:
            return 0

        # m2 = (y4 - y3) / (x4 - x3)
        if y3 == y4:
            y = y3
            if (y - y1) * (y - y2) > 0:
                return 0
            return 1

        # y_substitute = (x4 - x3) * y = (y4 - y3) * (x - x3) + y3 * (x4 - x3)

        y_substitute = (y4 - y3) * (x - x3) + y3 * (x4 - x3)

        if (y_substitute - (x4 - x3) * y1) * (y_substitute - (x4 - x3) * y2) > 0:
            return 0
        return 1

    # m1 = (y2 - y1) / (x2 - x1)
    # m2 = (y4 - y3) / (x4 - x3)

    # if m1 == m2:
    if (y2 - y1) * (x4 - x3) == (x2 - x1) * (y4 - y3):
        # if m1 * (x2 - x3) == (y2 - y3):
        if (y2 - y1) * (x2 - x3) == (y2 - y3) * (x2 - x1):
            if x3 <= x2 <= x4 or x1 <= x4 <= x2:
                return 1
        return 0

    # x = (m1 * x1 - m2 * x3 + y3 - y1) / (m1 - m2)
    # (m1 - m2) * x = (m1 * x1 - m2 * x3 + y3 - y1)

    # ((y2 - y1) * (x4 - x3) - (y4 - y3) * (x2 - x1)) * x =
    # ((y2 - y1) * (x4 - x3) * x1 - (y4 - y3) * x3  * (x2 - x1) + (y3 - y1)* (x4 - x3) * (x2 - x1))
    foo = (y2 - y1) * (x4 - x3) - (y4 - y3) * (x2 - x1)
    bar = ((y2 - y1) * (x4 - x3) * x1 - (y4 - y3) * x3 * (x2 - x1) + (y3 - y1) * (x4 - x3) * (x2 - x1))
    # foo * x = bar, x = bar/ foo

    if (bar - foo * x1) * (bar - foo * x2) <= 0 and (bar - foo * x3) * (bar - foo * x4) <= 0:
        return 1

    return 0


print(solve())
