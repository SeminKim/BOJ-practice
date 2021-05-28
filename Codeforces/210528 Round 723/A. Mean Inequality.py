from sys import stdin

t = int(stdin.readline().strip())

for _ in range(t):
    n = int(stdin.readline().strip())
    ans = []
    seq = list(map(int, stdin.readline().split()))
    seq.sort()
    inc = seq[:n]
    dec = seq[n:]
    for x, y in zip(inc,dec):
        ans.append(x)
        ans.append(y)
    for i in ans:
        print(i, end=' ')
    print()


