# https://www.acmicpc.net/problem/14889
# Implementation

from itertools import combinations
from sys import stdin

n = int(stdin.readline().strip())
r = n // 2
seq = [list(map(int, stdin.readline().split())) for _ in range(n)]
ans = 10 ** 8
teams = [x for x in combinations(range(n), r)]
for idx in range(len(teams) // 2):
    start = teams[idx]
    link = teams[-idx - 1]
    diff = abs(sum(seq[i][j] for i in start for j in start) - sum(seq[i][j] for i in link for j in link))
    ans = min(diff, ans)

print(ans)
