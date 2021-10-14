from sys import stdin


def solve():
    seq = list(map(int, stdin.readline().split()))
    foo = max(seq)
    if seq.count(foo) == 1:
        for i in seq:
            if i == foo:
                print(0, end=' ')
            else:
                print(foo - i + 1, end=' ')
    else:
        for i in seq:
            print(foo - i + 1, end=' ')

    print()

t = int(stdin.readline().strip())

for _ in range(t):
    solve()
