# https://www.acmicpc.net/problem/20149
# Modified a bit from 17387

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
            print(0)
            return

        y1, y2 = sorted([y1, y2])
        y3, y4 = sorted([y3, y4])
        if y3 <= y2 <= y4 or y1 <= y4 <= y2:
            print(1)
            if y2 == y3:
                print(x2, y2)
            elif y4 == y1:
                print(x4, y4)
            return
        print(0)
        return

    if x3 == x4:
        x1, y1, x3, y3 = x3, y3, x1, y1
        x2, y2, x4, y4 = x4, y4, x2, y2

    if x1 == x2:
        x = x1
        if (x - x3) * (x - x4) > 0:
            print(0)
            return

        # m2 = (y4 - y3) / (x4 - x3)
        if y3 == y4:
            y = y3
            if (y - y1) * (y - y2) > 0:
                print(0)
                return
            print(1)
            print(x, y)
            return

        # y_substitute = (x4 - x3) * y = (y4 - y3) * (x - x3) + y3 * (x4 - x3)
        y_substitute = (y4 - y3) * (x - x3) + y3 * (x4 - x3)

        if (y_substitute - (x4 - x3) * y1) * (y_substitute - (x4 - x3) * y2) > 0:
            print(0)
            return

        print(1)
        print(x, y_substitute / (x4 - x3))
        return

    # m1 = (y2 - y1) / (x2 - x1)
    # m2 = (y4 - y3) / (x4 - x3)

    # if m1 == m2:
    if (y2 - y1) * (x4 - x3) == (x2 - x1) * (y4 - y3):
        # if m1 * (x2 - x3) == (y2 - y3):
        if (y2 - y1) * (x2 - x3) == (y2 - y3) * (x2 - x1):
            if x3 <= x2 <= x4 or x1 <= x4 <= x2:
                print(1)
                if x1 == x4:
                    print(x1, y1)
                elif x2 == x3:
                    print(x2, y2)
                return
        print(0)
        return

    # x = (m1 * x1 - m2 * x3 + y3 - y1) / (m1 - m2)
    # (m1 - m2) * x = (m1 * x1 - m2 * x3 + y3 - y1)

    # ((y2 - y1) * (x4 - x3) - (y4 - y3) * (x2 - x1)) * x =
    # ((y2 - y1) * (x4 - x3) * x1 - (y4 - y3) * x3  * (x2 - x1) + (y3 - y1)* (x4 - x3) * (x2 - x1))
    foo = (y2 - y1) * (x4 - x3) - (y4 - y3) * (x2 - x1)
    bar = ((y2 - y1) * (x4 - x3) * x1 - (y4 - y3) * x3 * (x2 - x1) + (y3 - y1) * (x4 - x3) * (x2 - x1))
    # foo * x = bar, x = bar/ foo

    if (bar - foo * x1) * (bar - foo * x2) <= 0 and (bar - foo * x3) * (bar - foo * x4) <= 0:
        print(1)
        print(bar / foo, (y2 - y1) / (x2 - x1) * (bar / foo - x1) + y1)
        return

    print(0)
    return


solve()
