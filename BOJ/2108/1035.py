# https://www.acmicpc.net/problem/1035
# Brute force

from itertools import combinations, permutations
from sys import stdin


#  0  1  2  3  4
#  5  6  7  8  9
# 10 11 12 13 14
# 15 16 17 18 19
# 20 21 22 23 24

def check(selection):
    x = len(selection)
    connected = [False for _ in range(x)]
    connected[0] = True
    Q = [0]
    while Q:
        curr = Q.pop()
        for nxt in range(x):
            if distance(selection[curr], selection[nxt]) == 1 and not connected[nxt]:
                connected[nxt] = True
                Q.append(nxt)
    return all(connected)


def distance(first, second):
    r1, c1 = first // 5, first % 5
    r2, c2 = second // 5, second % 5
    return abs(r1 - r2) + abs(c1 - c2)


board = [stdin.readline().strip() for _ in range(5)]
initial = []
for row in range(5):
    for col in range(5):
        if board[row][col] == '*':
            initial.append(row * 5 + col)

best = 50
for selected in combinations(range(25), len(initial)):
    if check(selected):
        for ordered in permutations(selected):
            temp = 0
            for i in range(len(initial)):
                temp += distance(initial[i], ordered[i])
            best = min(best, temp)

print(best)
