# https://www.acmicpc.net/problem/9252
# Use DP.

from sys import stdin

first = stdin.readline().strip()
second = stdin.readline().strip()

n = len(first)
m = len(second)

table = [[0 for _ in range(m)] for _ in range(n)]

# Initial lines
for col in range(m):
    if first[0] == second[col]:
        for ncol in range(col, m):
            table[0][ncol] = 1
        break
for row in range(n):
    if second[0] == first[row]:
        for nrow in range(row, n):
            table[nrow][0] = 1
        break

# fill table
for row in range(1, n):
    for col in range(1, m):
        table[row][col] = max(table[row][col - 1], table[row - 1][col],
                              table[row - 1][col - 1] + (first[row] == second[col]))
print(table[n - 1][m - 1])  # LCS length

# find backward
row, col = n - 1, m - 1
curr = table[row][col]
ans = []
while (row, col) != (0, 0) and curr > 0:
    if row > 0 and table[row - 1][col] == curr:
        row -= 1
    elif col > 0 and table[row][col - 1] == curr:
        move = True
        col -= 1
    else:
        ans.append(first[row])
        row = max(0, row - 1)
        col = max(0, col - 1)
        curr = table[row][col]

if curr == 1:
    ans.append(first[0])

print(''.join(reversed(ans)))

# # debug
# print(" ", end='')
# for L in second:
#     print(f"  {L}", end='')
# print()
# for L, foo in zip(first, table):
#     print(L, foo)
