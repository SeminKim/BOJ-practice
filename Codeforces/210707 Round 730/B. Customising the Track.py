from sys import stdin


def solve():
    n = int(stdin.readline().strip())
    seq = list(map(int, stdin.readline().split()))
    foo = sum(seq) % n
    return foo * (n - foo)


t = int(stdin.readline().strip())

for _ in range(t):
    print(solve())
