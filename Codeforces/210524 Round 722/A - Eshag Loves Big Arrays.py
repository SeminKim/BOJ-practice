from sys import stdin

t = int(stdin.readline().strip())

for _ in range(t):
    n = int(stdin.readline().strip())
    seq = list(map(int, stdin.readline().split()))
    foo = min(seq)
    print(n - seq.count(foo))
