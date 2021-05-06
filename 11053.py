# https://www.acmicpc.net/problem/11053
# Use DP in backward. 근데 풀고나서 보니까 그냥 앞에서부터 해도 되는건데 왜그랬지?
from sys import stdin

n = int(stdin.readline())
seq = list(map(int, stdin.readline().split()))
table = [1 for _ in range(n)]
for i in range(1, n + 1):
    temp = [1]
    for j in range(1, i):
        if seq[n - i] < seq[n - j]:
            temp.append(table[n - j] + 1)
    table[n - i] = max(temp)

print(max(table))
