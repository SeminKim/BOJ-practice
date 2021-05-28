from sys import stdin


def solve():
    n = int(stdin.readline().strip())
    seq = list(map(int, stdin.readline().split()))
    seq.sort()
    if seq[-1] <= 0:
        return n

    for i in range(n):
        if seq[i] > 0:
            seq = seq[:i + 1]
            break

    target = seq[-1]
    n = len(seq)
    for i in range(1, n):
        d = seq[i] - seq[i - 1]
        if target > d:
            return n - 1
    return n


t = int(stdin.readline().strip())

for _ in range(t):
    print(solve())
