from sys import stdin


def solve():
    a, b, c = map(int, stdin.readline().split())
    a, b = sorted([a, b])
    n = 2 * (b - a)
    if c > n // 2:
        ans = c - n // 2
    else:
        ans = c + n // 2

    if a <= n and b <= n and c <= n and ans <= n:
        print(ans)
    else:
        print(-1)


t = int(stdin.readline().strip())

for _ in range(t):
    solve()
