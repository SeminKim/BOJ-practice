# https://www.acmicpc.net/problem/12865
# Knapsack problem. Use DP; table[k][w] is maximum value for using object with weight<w and total weight <k.

from sys import stdin

n, k = map(int, stdin.readline().split())
problem = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    problem[i] = list(map(int, stdin.readline().split()))  # put [weight, value]

problem.sort()

table = [[0 for col in range(n + 1)] for row in range(k + 1)]

for row in range(1, k + 1):
    for col in range(1, n + 1):
        [now_weight, now_value] = problem[col]
        if now_weight > row:
            table[row][col] = table[row][col - 1]
        else:
            table[row][col] = max(table[row][col - 1], table[row - now_weight][col - 1] + now_value)

print(table[k][n])
