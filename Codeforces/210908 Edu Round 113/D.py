from bisect import bisect_left
from sys import stdin
from collections import deque


### NOT SOLVED YET ###
def solve():
    n, m, k = map(int, stdin.readline().split())
    verti_line = deque(map(int, stdin.readline().split()))
    hori_line = deque(map(int, stdin.readline().split()))
    verti = []  # points in vertical line only
    hori = []
    for _ in range(k):
        x, y = map(int, stdin.readline().split())
        idx1 = bisect_left(verti_line, x)
        idx2 = bisect_left(hori_line, y)
        if verti_line[idx1] == x and hori_line[idx2] == y:
            continue

        elif verti_line[idx1] == x:
            verti.append((y, x))
        else:
            hori.append((x, y))

    verti = deque(sorted(verti))
    hori = deque(sorted(hori))

    ans = 0
    # check verti+verti case
    left = None
    right = hori_line.popleft()
    while hori_line:
        left = right
        right = hori_line.popleft()
        temp = 0
        now_y = -1
        while len(verti) > 0 and verti[0][0] < right:
            _, bar = verti.popleft()
            if now_y != bar:
                if temp > 1:
                    ans += temp * (temp - 1) // 2
                temp = 0
                now_y = bar
            temp += 1

    left = None
    right = verti_line.popleft()
    while verti_line:
        left = right
        right = verti_line.popleft()
        temp = 0
        now_x = -1
        while len(hori) > 0 and hori[0][0] < right:
            foo, _ = hori.popleft()
            if now_x != foo:
                if temp > 1:
                    ans += temp * (temp - 1) // 2
                temp = 0
                now_x = foo
            temp += 1
    print(ans)


t = int(stdin.readline().strip())

for _ in range(t):
    solve()
