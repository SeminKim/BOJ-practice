from sys import stdin


def solve():
    n, m = map(int, stdin.readline().split())
    dist_count = [0] * (n + m - 1)
    for i in range(n):
        for j in range(m):
            max_dist = max(abs(i - 0) + abs(j - 0),
                           abs(i - (n - 1)) + abs(j - 0),
                           abs(i - 0) + abs(j - (m - 1)),
                           abs(i - (n - 1)) + abs(j - (m - 1)))
            dist_count[max_dist] += 1

    for d in range(n + m - 1):
        while dist_count[d] > 0:
            print(d, end=' ')
            dist_count[d] -= 1
    print()


t = int(stdin.readline().strip())

for _ in range(t):
    solve()
