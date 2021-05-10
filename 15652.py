# https://www.acmicpc.net/problem/15652
from sys import stdin
from itertools import combinations_with_replacement

n, m = map(int, stdin.readline().split())

for seq in combinations_with_replacement([i for i in range(1, n+1)], m):
    for num in seq:
        print(num, end=' ')
    print()
