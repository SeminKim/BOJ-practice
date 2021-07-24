from sys import stdin


def solve():
    n = int(stdin.readline().strip())
    c1 = n // 3
    c2 = c1
    if c1 + 2 * c2 == n:
        print(c1, c2)
    elif c1 + 2 * c2 == n - 1:
        print(c1 + 1, c2)
    else:
        print(c1, c2 + 1)


t = int(stdin.readline().strip())

for _ in range(t):
    solve()
