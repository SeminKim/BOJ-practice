from sys import stdin

INF = 10 ** 9


def solve():
    n, k = map(int, stdin.readline().split())
    seq = list(map(int, stdin.readline().split()))
    count = {}
    colored = [0 for _ in range(k + 1)]
    colored[0] = INF

    exceed = 0
    for i in seq:
        if i in count.keys():
            count[i] += 1
            if count[i] > k:
                exceed += 1
        else:
            count[i] = 1

    exceed = (n - exceed) % k
    goal = {i: [] for i in count.keys()}

    foo = 1
    for i in count.keys():
        while count[i] > 0:
            if count[i] > k:
                count[i] = k
                continue

            if exceed > 0:
                exceed -= 1
                count[i] -= 1
                continue

            goal[i].append(foo)
            count[i] -= 1
            foo += 1
            if foo == k + 1:
                foo = 1

    # print(goal)
    for i in range(n):
        if len(goal[seq[i]]) == 0:
            print(0, end=' ')

        else:
            wow = goal[seq[i]].pop()
            print(wow, end=' ')

    print()


t = int(stdin.readline().strip())

for _ in range(t):
    solve()
