from sys import stdin
from math import gcd


# Not Solved Yet !!

def simplify(x: tuple):
    a, b = x[0], x[1]
    if a == 0:
        return 0, 1
    if b == 0:
        return 1, 0
    foo = gcd(a, b)
    return a // foo, b // foo


def solve():
    n = int(stdin.readline().strip())

    seq = list(stdin.readline().strip())
    partial_sum = [0 for _ in range(n)]
    ans = [1 for _ in range(n)]
    cnt = 0
    for i in range(n):
        if seq[i] == 'D':
            seq[i] = 1
            cnt += 1
        else:
            seq[i] = 0
        partial_sum[i] = cnt

    # ratio = simplify((partial_sum[n-1], n - partial_sum[n-1]))
    # unit = ratio[0] + ratio[1]

    for i in range(1, n):  # if we make first cut 0 to i
        ratio = simplify((partial_sum[i], i + 1 - partial_sum[i]))
        unit = ratio[0] + ratio[1]
        k = 1
        while 0 <= i - k * unit:
            if partial_sum[i] - partial_sum[i - unit] == ratio[0]:
                ans[i] = ans[i - unit] + 1
            k += 1
    print(*ans)


t = int(stdin.readline().strip())

for _ in range(t):
    solve()
