from sys import stdin


#### Not Solved Yet - TLE ###


def solve():
    n, k = map(int, stdin.readline().split())
    str_n = str(n)
    if n < 10:
        print(n)
        return

    if k == 1:
        foo = str_n[0] * len(str_n)
        if int(foo) >= n:
            print(foo)
            return
        else:
            print(str(int(str_n[0]) + 1) * len(str_n))
            return

    best = 10 ** 9
    first = str_n[0]
    for second in [str(i) for i in range(10)]:
        if second == first:
            ans = first * len(str_n)
            if int(ans) > n:
                best = min(best, int(ans))
            continue

        for case in range(2 ** (len(str_n) - 1)):
            ans = first
            for foo in range(len(str_n) - 1):
                if case & (1 << foo):
                    ans += first
                else:
                    ans += second

                if ans < str_n[:len(ans)]:
                    ans = '0'
                    break

            if int(ans) >= n:
                best = min(best, int(ans))

    print(best)
    return


t = int(stdin.readline().strip())

for _ in range(t):
    solve()
