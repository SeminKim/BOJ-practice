# https://www.acmicpc.net/problem/23048
# Prime

from sys import stdin

n = int(stdin.readline().strip())

# Sieve
colors = [0 for _ in range(n + 1)]
colors[1] = 1
curr = 1
for i in range(2, n + 1):
    if colors[i] == 0:
        curr += 1
        for j in range(i, n + 1, i):
            colors[j] = curr

print(curr)
print(' '.join(map(str, colors[1:])))
