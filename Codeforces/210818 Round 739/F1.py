from sys import stdin

### TLE; Use F2 instead. ###


def solve():
    str_n, k = stdin.readline().split()
    n = int(str_n)
    L = len(str_n)

    best = '9' * L
    for i in range(9):
        foo = str(i) * L
        if foo >= str_n:
            best = min(best, foo)

    if k == '1' or n < 10:
        print(best)
        return

    first = str_n[0]
    ans = [first for _ in range(L)]
    list_n = list(str_n)
    for second in [str(i) for i in range(10)]:
        if second == first:
            continue

        for case in range(2 ** (L - 1)):
            for foo in range(L - 1):
                if case & (1 << foo):
                    ans[foo + 1] = first
                else:
                    ans[foo + 1] = second
                if ans[foo + 1] < str_n[foo + 1]:
                    break

            if ans >= list_n:
                best = min(best, ''.join(ans))

    print(best)
    return


t = int(stdin.readline().strip())

for _ in range(t):
    solve()
