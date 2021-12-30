# https://www.acmicpc.net/problem/13458
# Implementation

from sys import stdin

n = int(stdin.readline().strip())
seq = list(map(int, stdin.readline().split()))
b, c = map(int, stdin.readline().split())
ans = len(seq)
for i in seq:
    ans += max(0, i - b + c - 1) // c
print(ans)
