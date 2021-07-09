from sys import stdin


def solve():
    n, _ = map(int, stdin.readline().split())
    print(0, flush=True)
    r = int(stdin.readline())
    if r == 1:
        return

    for i in range(1, n):
        print((i - 1) ^ i, flush=True)
        r = int(stdin.readline())
        if r == 1:
            return


t = int(stdin.readline())

for _ in range(t):
    solve()
