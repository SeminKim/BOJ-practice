from sys import stdin


def solve():
    k = 2

    seq = list(stdin.readline().strip())
    n = len(seq)

    count = {}

    exceed = 0
    for i in seq:
        if i in count.keys():
            count[i] += 1
            if count[i] > k:
                exceed += 1
        else:
            count[i] = 1

    ans = (n - exceed) // 2
    print(ans)
    return


t = int(stdin.readline().strip())

for _ in range(t):
    solve()
