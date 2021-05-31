# https://www.acmicpc.net/problem/12852
# Use DP.

from sys import stdin

n = int(stdin.readline().strip())
table = [None for _ in range(n + 1)]
table[1] = 0
used = [[] for _ in range(n + 1)]
used[1] = [1]
for i in range(2, n + 1):
    options = []
    if i % 2 == 0:
        options.append((table[i // 2], used[i // 2]))
    if i % 3 == 0:
        options.append((table[i // 3], used[i // 3]))

    options.append((table[i - 1], used[i - 1]))

    op = min(options, key=lambda x: x[0])
    used[i] = op[1] + [i]
    table[i] = 1 + op[0]

used[n].reverse()
print(table[n])
print(*used[n])
