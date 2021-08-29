from sys import stdin


def solve():
    n = int(stdin.readline().strip())
    seq = list(map(int, stdin.readline().split()))
    odd = []
    even = []
    for i in range(n):
        if seq[i] % 2:
            odd.append(i)
        else:
            even.append(i)

    if n % 2 == 0:
        if len(odd) != len(even):
            print(-1)
            return

        res_1 = 0
        res_2 = 0
        target = 0
        for i, j in zip(odd, even):
            res_1 += abs(i - target)
            res_2 += abs(j - target)
            target += 2
        print(min(res_1, res_2))
        return

    else:
        if len(odd) > len(even):
            if len(odd) != n // 2 + 1:
                print(-1)
                return
            # first should be odd
            target = 0
            res = 0
            for i in odd:
                res += abs(i - target)
                target += 2
            print(res)

        else:
            if len(even) != n // 2 + 1:
                print(-1)
                return
            # first should be even
            target = 0
            res = 0
            for i in even:
                res += abs(i - target)
                target += 2
            print(res)


t = int(stdin.readline().strip())

for _ in range(t):
    solve()
