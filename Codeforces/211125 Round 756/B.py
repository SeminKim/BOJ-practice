from sys import stdin


def solve():
    a, b = map(int, stdin.readline().split())
    if a > b:
        a, b = b, a
    if b > 3 * a:
        print(a)
    else:
        print((a + b) // 4)


t = int(stdin.readline().strip())

for _ in range(t):
    solve()
