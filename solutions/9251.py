# https://www.acmicpc.net/problem/9251
# Use DP. table[i][j]는 각 문자의 앞 i글자, 앞 j글자 끼리의 LCS 길이
# LCS(abcd,cda) = max{(LCS(abc,c) + LCS(d,da) (=1), LCS(abc,cda)}

from sys import stdin

A = stdin.readline().strip()
B = stdin.readline().strip()
n = len(A)
m = len(B)

table = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

for col in range(1, n + 1):
    if B[0] in A[:col]:
        table[1][col] = 1

for row in range(1, m + 1):
    if A[0] in B[:row]:
        table[row][1] = 1

for row in range(2, m + 1):
    for col in range(2, n + 1):
        idx = B[:row].rfind(A[col - 1])
        if idx == -1:
            table[row][col] = table[row][col - 1]
        else:
            table[row][col] = max(table[row][col - 1], table[idx][col - 1] + 1)

print(table[m][n])
