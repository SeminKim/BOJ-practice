# https://www.acmicpc.net/problem/14725


from sys import stdin

n = int(stdin.readline().strip())
info = []
for _ in range(n):
    info.append(stdin.readline().split()[1:])
info.sort()

prev = info[0]
for lvl, i in enumerate(info[0]):
    print('--' * lvl + i)

for i in range(1, n):
    curr = info[i]
    j = 0
    while prev[j] == curr[j]:
        j += 1

    while j < len(curr):
        print('--' * j + curr[j])
        j += 1
    prev = curr
