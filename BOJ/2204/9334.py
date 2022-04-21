# https://www.acmicpc.net/problem/9334

from sys import stdin


def solve():
    n, *A = map(int, stdin.readline().split())
    # Case 1
    a = A[1] // A[0]
    for i in range(n - 1):
        if a * A[i] != A[i + 1]:
            break
    else:
        return a * A[-1]

    # Case 2
    det = A[0] * A[2] - A[1] * A[1]
    if det != 0:
        a = (A[2] * A[2] - A[1] * A[3]) // det
        b = (A[0] * A[3] - A[1] * A[2]) // det
        for i in range(n - 2):
            if a * A[i] + b * A[i + 1] != A[i + 2]:
                break
        else:
            return a * A[-2] + b * A[-1]

    # Case 3
    det = (A[0] * A[2] * A[4] + A[1] * A[3] * A[2] + A[2] * A[1] * A[3]) - (
            A[2] ** 3 + A[0] * A[3] * A[3] + A[1] * A[1] * A[4])
    a = (A[3] * (A[2] * A[4] - A[3] * A[3]) + A[4] * (A[3] * A[2] - A[1] * A[4]) + A[5] * (
            A[1] * A[3] - A[2] * A[2])) // det
    b = (A[3] * (A[2] * A[3] - A[1] * A[4]) + A[4] * (A[0] * A[4] - A[2] * A[2]) + A[5] * (
            A[1] * A[2] - A[0] * A[3])) // det
    c = (A[3] * (A[1] * A[3] - A[2] * A[2]) + A[4] * (A[1] * A[2] - A[0] * A[3]) + A[5] * (
            A[0] * A[2] - A[1] * A[1])) // det

    return a * A[-3] + b * A[-2] + c * A[-1]


t = int(stdin.readline().strip())
for _ in range(t):
    print(solve())
