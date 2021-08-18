from sys import stdin

targets = [2 ** i for i in range(70)]


def helper(num, target):
    Q = list(str(num))
    str_num = str(num)
    goal = str(target)
    idx = 0
    while Q:
        if Q.pop(0) == goal[idx]:
            idx += 1
        if idx == len(goal):
            break

    uncommon = len(str_num) - idx
    return uncommon + len(goal) - idx


def solve():
    n = int(stdin.readline().strip())
    best = 100
    for i in targets:
        best = min(best, helper(n, i))

    print(best)


t = int(stdin.readline().strip())

for _ in range(t):
    solve()
