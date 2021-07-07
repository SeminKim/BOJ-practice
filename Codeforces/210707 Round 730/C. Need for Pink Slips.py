from sys import stdin
from collections import deque

TO_INT = 10 ** 10  # maintain c+m+p = TO_INT
TO_FLOAT = 10 ** -10
EPSILON = 10


def solve():
    c, m, p, v = map(lambda x: int(float(x) * TO_INT), stdin.readline().split())
    q = deque()
    q.append([c, m, p, 1, 1.0])  # c, m, p, depth, multiplier
    ans = 0
    while 0 < len(q) < 10 ** 5:
        now = q.popleft()
        if now[2] < EPSILON:
            continue

        ans += now[2] * TO_FLOAT * now[3] * now[4]

        if now[0] < EPSILON and now[1] < EPSILON:
            continue

        # when x = 2
        if now[0] < EPSILON:
            if now[1] <= v + EPSILON:
                q.append([0, 0, 1 * TO_INT, now[3] + 1, now[4] * now[1] * TO_FLOAT])
            else:
                q.append([0, now[1] - v, TO_INT - now[1] + v, now[3] + 1, now[4] * now[1] * TO_FLOAT])
            continue

        if now[1] < EPSILON:
            if now[0] <= v + EPSILON:
                q.append([0, 0, 1 * TO_INT, now[3] + 1, now[4] * now[0] * TO_FLOAT])
            else:
                q.append([now[0] - v, 0, 1 * TO_INT - now[0] + v, now[3] + 1, now[4] * now[0] * TO_FLOAT])
            continue

        # select c
        if now[0] <= v + EPSILON:
            new_c = 0
            new_m = now[1] + now[0] // 2
            new_p = now[2] + now[0] // 2
            wow = new_m + new_p
            new_m = int(new_m / wow * TO_INT)
            new_p = int(new_p / wow * TO_INT)
            foo = [new_c, new_m, new_p, now[3] + 1, now[4] * now[0] * TO_FLOAT]

        else:
            new_c = now[0] - v
            new_m = now[1] + v // 2
            new_p = now[2] + v // 2
            foo = [new_c, new_m, new_p, now[3] + 1, now[4] * now[0] * TO_FLOAT]

        q.append(foo)

        # select m
        if now[1] <= v + EPSILON:
            new_c = now[0] + now[1] // 2
            new_m = 0
            new_p = now[2] + now[1] // 2
            wow = new_c + new_p
            new_c = int(new_c / wow * TO_INT)
            new_p = int(new_p / wow * TO_INT)
            foo = [new_c, new_m, new_p, now[3] + 1, now[4] * now[1] * TO_FLOAT]
        else:
            new_c = now[0] + v // 2
            new_m = now[1] - v
            new_p = now[2] + v // 2
            foo = [new_c, new_m, new_p, now[3] + 1, now[4] * now[1] * TO_FLOAT]

        q.append(foo)

    return ans


t = int(stdin.readline().strip())

for _ in range(t):
    print(solve())
