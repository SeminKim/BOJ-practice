# https://www.acmicpc.net/problem/6439

from sys import stdin


def get_line(x1, y1, x2, y2):  # in ax+by=c form
    if x1 == x2:
        return [1, 0, x1]
    if y1 == y2:
        return [0, 1, y1]
    return [y1 - y2, x2 - x1, x2 * y1 - x1 * y2]


def get_intersection(a1, b1, c1, a2, b2, c2):
    down = a1 * b2 - a2 * b1
    x_up = b2 * c1 - b1 * c2
    y_up = -a2 * c1 + a1 * c2
    return x_up / down, y_up / down


def solve():
    x_start, y_start, x_end, y_end, x1, y1, x2, y2 = map(int, stdin.readline().split())
    x1, x2 = sorted([x1, x2])
    y1, y2 = sorted([y1, y2])
    small_x, big_x = sorted([x_start, x_end])
    small_y, big_y = sorted([y_start, y_end])

    def check(x, y):
        return (y1 <= y <= y2) and (x1 <= x <= x2) and (small_x <= x <= big_x) and (small_y <= y <= big_y)

    if check(x_start, y_start) or check(x_end, y_end):
        return 'T'

    line = get_line(x_start, y_start, x_end, y_end)

    if x_start != x_end:
        # test with x=x1, x=x2
        for x in [x1, x2]:
            _, y = get_intersection(1, 0, x, *line)
            if check(x, y):
                return 'T'

    if y_start != y_end:
        # test with y=y1, y=y2
        for y in [y1, y2]:
            x, _ = get_intersection(0, 1, y, *line)
            if check(x, y):
                return 'T'
    return 'F'


t = int(stdin.readline().strip())

for _ in range(t):
    print(solve())
