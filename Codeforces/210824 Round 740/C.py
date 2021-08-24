from sys import stdin

INF = 10 ** 10


def solve():
    c = int(stdin.readline().strip())
    limits = []
    for _ in range(c):
        cave = list(map(int, stdin.readline().split()))
        k = cave[0]
        cave = cave[1:]
        best = cave[0]
        for i in range(len(cave)):
            best = max(best, cave[i] - i + 1)
        limits.append([best, k])

    limits.sort()

    ans = limits[0][0]
    power = limits[0][0]
    for i in range(c):
        if limits[i][0] <= power:
            power += limits[i][1]
        else:
            ans += limits[i][0] - power
            power = limits[i][0] + limits[i][1]

    print(ans)


t = int(stdin.readline().strip())

for _ in range(t):
    solve()
