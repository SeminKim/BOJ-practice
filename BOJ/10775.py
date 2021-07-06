# https://www.acmicpc.net/problem/10775
# Greedy with disjoint set

from sys import stdin

g = int(stdin.readline().strip())
p = int(stdin.readline().strip())
parent = [i for i in range(g + 1)]
ans = 0


def find(num):
    if parent[num] == num:
        return num
    else:
        parent[num] = find(parent[num])
        return parent[num]


def union(first, second):
    parent[find(first)] = find(second)


for _ in range(p):
    foo = int(stdin.readline().strip())
    goal = find(foo)
    if goal == 0:
        break
    else:
        ans += 1
        union(goal, goal - 1)

print(ans)
