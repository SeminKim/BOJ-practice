# https://www.acmicpc.net/problem/14890
# Implementation

from sys import stdin

N, L = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]


def decide(line):
    installed = [False] * N
    prev = line[0]
    i = 1
    while i < N:
        curr = line[i]
        if curr > prev:
            if curr > prev + 1 or i < L or sum(installed[i - L:i]) != 0:
                return 0
            for back in range(1, L + 1):
                if line[i - back] != prev:
                    return 0
                installed[i - back] = True
        elif curr < prev:
            if curr < prev - 1 or i + L - 1 >= N:
                return 0
            for front in range(L):
                if line[i + front] != curr:
                    return 0
                installed[i + front] = True
            i += L - 1
        i += 1
        prev = curr
    # print(line)
    return 1


ans = 0
lines = board + [[board[i][j] for i in range(N)] for j in range(N)]
for line in lines:
    ans += decide(line)
print(ans)
