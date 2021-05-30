from sys import stdin
from itertools import combinations

## Not Solved Yet!

n, m, p = map(int, stdin.readline().split())

cardi = {str(i): [] for i in range(m)}
for i, j in combinations([str(i) for i in range(m)], 2):
    cardi[i + j] = []

for idx in range(n):
    favor = stdin.readline().strip()
    for i in range(m):
        if favor[i] == '1':
            cardi[str(i)].append(idx)
            for j in range(i + 1, m):
                if favor[j] == '1':
                    cardi[str(i) + str(j)].append(idx)
