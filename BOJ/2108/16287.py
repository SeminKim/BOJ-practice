# https://www.acmicpc.net/problem/16287
# Divide into 2+2

from sys import stdin

w, n = map(int, stdin.readline().split())
seq = list(map(int, stdin.readline().split()))
MAX_NUM = 2 * 200_000

check = [0 for _ in range(MAX_NUM + 1)]
flag = False

for i in range(n):
    for j in range(i + 1, n):
        foo = seq[i] + seq[j]
        goal = w - foo
        if 0 < goal < MAX_NUM and check[goal]:
            flag = True

    for j in range(i):
        check[seq[i] + seq[j]] = 1

print('YES' if flag else 'NO')
