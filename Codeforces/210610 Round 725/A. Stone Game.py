from sys import stdin

t = int(stdin.readline().strip())

for _ in range(t):
    n = int(stdin.readline().strip())
    seq = list(map(int, stdin.readline().split()))
    a = max(seq)
    b = min(seq)
    i = seq.index(a)
    j = seq.index(b)
    if i > j:
        i, j = j, i

    print(min(j + 1, n - i, n - j + i + 1))
