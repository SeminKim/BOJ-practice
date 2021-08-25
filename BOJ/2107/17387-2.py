# https://www.acmicpc.net/problem/17387
# Solve again with CCW algorithm.


from sys import stdin


# (x2-x1, y2-y1)  *  (x3-x1, y3-y1) => x2y3 - x2y1 -x1y3 - x3y2 + x1y2 + x3y1
def ccw(x1, y1, x2, y2, x3, y3):
    return x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3


x1, y1, x2, y2 = map(int, stdin.readline().split())
x3, y3, x4, y4 = map(int, stdin.readline().split())

if (x1, y1) > (x2, y2):
    x1, x2 = x2, x1
    y1, y2 = y2, y1

if (x3, y3) > (x4, y4):
    x3, x4 = x4, x3
    y3, y4 = y4, y3

# if two lines are parallel
if ccw(x1, y1, x2, y2, x3, y3) == 0 and ccw(x3, y3, x4, y4, x1, y1) == 0:
    if x1 == x2:  # if vertical
        if y3 <= y2 <= y4 or y1 <= y4 <= y2:
            print(1)
        else:
            print(0)
    elif x3 <= x2 <= x4 or x1 <= x4 <= x2:
        print(1)
    else:
        print(0)

elif ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4) <= 0 and \
        ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2) <= 0:
    print(1)

else:
    print(0)
