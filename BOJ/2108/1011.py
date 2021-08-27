# https://www.acmicpc.net/problem/1011

from bisect import bisect_left
from sys import stdin

arr = []
for i in range(1, 46341):
    arr.append(i ** 2)
    arr.append(i * (i + 1))


def solve():
    x, y = map(int, stdin.readline().split())
    target = y - x
    idx = bisect_left(arr, target)
    return idx + 1


t = int(stdin.readline().strip())
for _ in range(t):
    print(solve())
