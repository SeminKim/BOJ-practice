from sys import stdin


def solve():
    n = int(stdin.readline().strip())
    seq = list(map(int, stdin.readline().split()))
    while n <= 300:
        for i in range(n):
            for j in range(i + 1, n):
                seq.append(abs(seq[i] - seq[j]))
        seq = list(set(seq))
        if n == len(seq):
            print('yes')
            print(n)
            print(*seq)
            return
        n = len(seq)
    print('no')
    return


t = int(stdin.readline().strip())

for _ in range(t):
    solve()
