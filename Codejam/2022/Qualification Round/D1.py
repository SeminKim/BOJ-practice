from itertools import permutations
from sys import stdin

T = int(stdin.readline().strip())
for t in range(T):
    n = int(stdin.readline().strip())
    fun = [0] + list(map(int, stdin.readline().split()))
    child = [0] + list(map(int, stdin.readline().split()))
    ans = 0
    indegree = [0 for _ in range(n + 1)]
    for i in child:
        indegree[i] += 1

    candidate = []
    for i in range(1, n + 1):
        if indegree[i] == 0:
            candidate.append(i)

    for case in permutations(candidate):
        used = [False for _ in range(n + 1)]
        used[0] = True
        ret = 0
        for initiator in case:
            temp = 0
            curr = initiator
            while not used[curr]:
                temp = max(temp, fun[curr])
                used[curr] = True
                curr = child[curr]
            ret += temp
        ans = max(ans, ret)

    print(f'Case #{t + 1}: {ans}')
