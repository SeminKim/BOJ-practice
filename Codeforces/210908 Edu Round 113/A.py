from sys import stdin


def solve():
    n = int(stdin.readline().strip())
    seq = stdin.readline().strip()
    idx1 = seq.find('ab')
    idx2 = seq.find('ba')
    if idx1 == idx2 == -1:
        print(-1, -1)

    elif idx1 != -1:
        print(idx1 + 1, idx1 + 2)

    else:
        print(idx2 + 1, idx2 + 2)


t = int(stdin.readline().strip())

for _ in range(t):
    solve()
