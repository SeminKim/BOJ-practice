from sys import stdin

t = int(stdin.readline().strip())


def isSorted(array):
    for i in range(len(array)):
        if array[i] != i + 1:
            return False
    return True


for _ in range(t):
    n = int(stdin.readline().strip())
    seq = list(map(int, stdin.readline().split()))
    if seq[0] == n and seq[n - 1] == 1:
        print(3)
    elif isSorted(seq):
        print(0)
    elif seq[0] == 1 or seq[n - 1] == n:
        print(1)
    else:
        print(2)
