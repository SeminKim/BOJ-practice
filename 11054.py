# https://www.acmicpc.net/problem/11054
# Similar to 11053. Use DP
# i로 끝나는 가장 긴 증가 수열, i로 시작하는 가장 긴 감소수열을 저장.

from sys import stdin

n = int(stdin.readline())
seq = list(map(int, stdin.readline().split()))
increasing = [1 for _ in range(n)]
decreasing = [1 for _ in range(n)]

for i in range(n):
    max_increase_i = 1
    for j in range(0, i):
        if seq[j] < seq[i]:
            max_increase_i = max(max_increase_i, increasing[j] + 1)
    increasing[i] = max_increase_i

for i in range(n - 1, -1, -1):
    max_decrease_i = 1
    for j in range(n - 1, i, -1):
        if seq[i] > seq[j]:
            max_decrease_i = max(max_decrease_i, decreasing[j] + 1)
    decreasing[i] = max_decrease_i

ans = 1
for i in range(n):
    ans = max(ans, increasing[i] + decreasing[i] - 1)

print(ans)
