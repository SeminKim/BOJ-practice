# https://www.acmicpc.net/problem/2162
# CCW + disjoint set


from sys import stdin


def ccw(x1, y1, x2, y2, x3, y3):
    return x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3


def intersect(line_one, line_two):
    x1, y1, x2, y2 = line_one
    x3, y3, x4, y4 = line_two

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
                return True
            else:
                return False
        elif x3 <= x2 <= x4 or x1 <= x4 <= x2:
            return True
        else:
            return False

    elif ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4) <= 0 and \
            ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2) <= 0:
        return True

    else:
        return False


def get_head(this):
    if head[this] == this:
        return this

    head[this] = get_head(head[this])
    return head[this]


def get_rank(this):
    this = get_head(this)
    res = rank[this]
    return res


def union(first, second):
    first = get_head(first)
    second = get_head(second)

    if first == second:
        return

    global group_count
    group_count -= 1
    if rank[first] > rank[second]:
        head[second] = first
        rank[first] += rank[second]

    else:
        head[first] = second
        rank[second] += rank[first]


n = int(stdin.readline().strip())
lines = [list(map(int, stdin.readline().split())) for _ in range(n)]
group_count = n

head = [i for i in range(n)]
rank = [1 for _ in range(n)]

for i in range(n):
    for j in range(i + 1, n):
        if intersect(lines[i], lines[j]):
            union(i, j)

print(group_count)
print(max(rank))
