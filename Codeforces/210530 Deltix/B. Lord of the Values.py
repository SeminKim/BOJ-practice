from sys import stdin


def solve():
    n = int(stdin.readline().strip())
    _ = stdin.readline()
    print(n * 3)
    for i in range(0, n, 2):
        for _ in range(3):
            print(2, i + 1, i + 2)
            print(1, i + 1, i + 2)


t = int(stdin.readline().strip())

for _ in range(t):
    solve()
