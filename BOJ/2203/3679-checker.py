### Solution Code ###
from math import atan2
from sys import stdin


def parallel(fst, snd, thd):
    dx1, dy1 = snd[0] - fst[0], snd[1] - fst[1]
    dx2, dy2 = thd[0] - snd[0], thd[1] - snd[1]
    return dx1 * dy2 == dx2 * dy1


def solve(line):
    n, *seq = map(int, line.split())
    points = [(seq[i], seq[i + 1]) for i in range(0, 2 * n, 2)]
    point_to_number = {points[i]: i for i in range(n)}
    points.sort()
    base = points.pop(0)
    points.sort(key=lambda x: (atan2(x[1] - base[1], x[0] - base[0]), x[0], x[1]))
    lasts = []
    points = [base] + points
    until = n - 1
    while until > 1 and parallel(base, points[until], points[until - 1]):
        lasts.append(points[until])
        until -= 1
    ans = points[:until] + lasts + [points[until]]
    return ans


### CHECKER ###
def check_edge(pnt1, pnt2, pnt3, pnt4):
    def ccw(origin, fst, snd):
        foo = [fst[0] - origin[0], fst[1] - origin[1]]
        bar = [snd[0] - origin[0], snd[1] - origin[1]]
        return foo[0] * bar[1] - foo[1] * bar[0]

    if pnt1 > pnt2:
        pnt1, pnt2 = pnt2, pnt1
    try:
        if pnt3 > pnt4:
            pnt3, pnt4 = pnt4, pnt3
    except:
        print(ans)
    if ccw(pnt1, pnt2, pnt3) == 0 and ccw(pnt3, pnt4, pnt1) == 0:
        if pnt1[0] == pnt2[0]:
            if pnt3[1] < pnt2[1] < pnt4[1] or pnt1[1] < pnt4[1] < pnt2[1]:
                return False
            else:
                return True
        elif pnt3[0] < pnt2[0] < pnt4[0] or pnt1[0] < pnt4[0] < pnt2[0]:
            return False
        else:
            return True
    elif ccw(pnt1, pnt2, pnt3) * ccw(pnt1, pnt2, pnt4) <= 0 and \
            ccw(pnt3, pnt4, pnt1) * ccw(pnt3, pnt4, pnt2) <= 0:
        return False
    else:
        return True


def check(ans):
    for i in range(len(ans) - 3):
        for j in range(i + 2, len(ans) - 1):
            if not check_edge(ans[i], ans[i + 1], ans[j], ans[j + 1]):
                print(ans[i], ans[i + 1], ans[j], ans[j + 1])
                return False
    return True


def draw(points):
    X = []
    Y = []
    for x, y in points:
        X.append(x)
        Y.append(y)
    plt.scatter(X, Y)
    shp = patches.Polygon(points, fill=None, edgecolor='k', ls='solid', lw=1)
    plt.gca().add_patch(shp)
    plt.axis('scaled')
    plt.show()


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches

    c = int(stdin.readline().strip())
    for i in range(c):
        print(f'TC#{i}...', end='')
        line = stdin.readline()
        ans = solve(line)
        if len(ans) != len(line.split()) // 2:
            print(f'Error!\nNumber of points do not match(expected {len(line.split()) // 2}, got {len(ans)}).')
            draw(ans)
            break
        elif not check(ans):
            print(f'Error!\nCrossing edge exists.\n{ans}')
            draw(ans)
            break
        else:
            print('OK')
