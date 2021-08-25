# https://www.acmicpc.net/problem/1786
# KMP

from sys import stdin

text = stdin.readline().replace('\n', '')
n = len(text)
pattern = stdin.readline().replace('\n', '')
m = len(pattern)

# preprocessing: calculate pi
pi = [0 for _ in range(m)]
j = 0
for i in range(1, m):
    while pattern[i] != pattern[j] and j > 0:
        j = pi[j - 1]

    if pattern[i] == pattern[j]:
        pi[i] = j = j + 1

# main
j = 0
pos = []
for i in range(n):
    while text[i] != pattern[j] and j > 0:
        j = pi[j - 1]

    if text[i] == pattern[j]:
        j += 1

    if j == m:
        j = pi[m - 1]
        pos.append(i - m + 2)  # i-m+1 in zero-starting index, i-m+2 in one-starting index

print(len(pos))
print(' '.join(map(str, pos)))
