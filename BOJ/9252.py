# https://www.acmicpc.net/problem/9252
# Use DP.

from sys import stdin

first = stdin.readline().strip()
second = stdin.readline().strip()

n = len(first)
m = len(second)

table = [[0 for _ in range(m+1)] for _ in range(n+1)]
ansidx = [[[] for _ in range(m+1)] for _ in range(n+1)]

for col in range(1,m+1):
    if first[0] in second[:col]:
        table[1][col] = 1
        ansidx[1][col] = [first[0]]

for row in range(1,n+1):
    if second[0] in first[:row]:
        table[row][1] = 1
        ansidx[row][1] = [second[0]]

for row in range(2,n+1):
    for col in range(2,m+1):
        table[row][col] = table[row][col - 1]
        ansidx[row][col] = ansidx[row][col - 1]

        if second[col-1] in first[:row]:
            idx = first[:row].rfind(second[col-1])
            if table[row][col] < table[idx][col-1] + 1:
                table[row][col] = table[idx][col-1] + 1
                ansidx[row][col] = ansidx[idx][col-1] + [second[col-1]]

print(table[n][m])
print(''.join(ansidx[n][m]))
