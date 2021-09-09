from sys import stdin

DIV = 998244353
factorial = [1]
for i in range(1, 2 * 10 ** 5 + 1):
    factorial.append(factorial[-1] * i % DIV)


def combi(first, second):
    return factorial[first] * pow(factorial[first-second], DIV-2, DIV) * pow(factorial[second], DIV-2, DIV) % DIV


def solve():
    n = int(stdin.readline().strip())
    seq = list(map(int, stdin.readline().split()))
    seq.sort()
    if seq[-1] > seq[-2] + 1:  # difference larger than 2
        print(0)

    elif seq[-1] == seq[-2]:  # two maxval.
        print(factorial[n])

    else: # one maxval, several maxval-1
        x = seq.count(seq[-2])
        res = factorial[n]
        for i in range(x+1, n+1):
            res -= combi(i-1, x) * factorial[x] * factorial[n-x-1]
            res %= DIV
        print(res)


t = int(stdin.readline().strip())

for _ in range(t):
    solve()
