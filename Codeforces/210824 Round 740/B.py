from sys import stdin


def solve():
    a, b = sorted(map(int, stdin.readline().split()))
    mid = (a + b) // 2
    if (a + b) % 2 == 0:
        res = []
        for i in range(mid - a, mid + a + 1, 2):
            res.append(i)
        print(len(res))
        print(' '.join(map(str, res)))

    else:
        res = []
        for i in range(mid - a, mid + a + 2):
            res.append(i)
        print(len(res))
        print(' '.join(map(str, res)))


t = int(stdin.readline().strip())

for _ in range(t):
    solve()
