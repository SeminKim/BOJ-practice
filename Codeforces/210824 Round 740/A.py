from sys import stdin


def check(arr):
    for i in range(len(arr)):
        if arr[i] != i + 1:
            return False
    return True


def solve():
    n = int(stdin.readline().strip())
    seq = list(map(int, stdin.readline().split()))
    for iter in range(1, 3 * n):
        if check(seq):
            return iter - 1

        if iter % 2 == 1:
            for i in range(0, n - 1, 2):
                if seq[i] > seq[i + 1]:
                    seq[i], seq[i + 1] = seq[i + 1], seq[i]
        else:
            for i in range(1, n - 1, 2):
                if seq[i] > seq[i + 1]:
                    seq[i], seq[i + 1] = seq[i + 1], seq[i]


t = int(stdin.readline().strip())

for _ in range(t):
    print(solve())
