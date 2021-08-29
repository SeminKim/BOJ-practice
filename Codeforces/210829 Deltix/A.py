from sys import stdin


def solve():
    c, d = map(int, stdin.readline().split())
    if c == d == 0:
        print(0)
        return

    if c == d:
        print(1)
        return

    if (c + d) % 2 == 1:
        print(-1)
        return

    print(2)
    return


t = int(stdin.readline().strip())

for _ in range(t):
    solve()
