# https://www.acmicpc.net/problem/2533
# DP in tree.
# i의 자식 j라 하자.
# dp1[i]: i가 얼리어답터인 경우의 dp / dp2[i]: i가 얼리어답터가 아닌 경우의 dp
# dp1[i] = 1 + sum of min(dp1[j], dp2[j])
# dp2[i] = sum of dp1[j]
from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 8)
n = int(stdin.readline().strip())
tree = [set() for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, stdin.readline().split())
    tree[a].add(b)
    tree[b].add(a)

dp1 = [-1 for _ in range(n + 1)]
dp2 = [-1 for _ in range(n + 1)]


def case1(root: int, base: int) -> int:
    if dp1[root] != -1:
        return dp1[root]

    if len(tree[root]) == 0:
        dp1[root] = 1
        return dp1[root]

    foo = 1
    for child in tree[root]:
        if child == base:
            continue
        foo += min(case1(child, root), case2(child, root))

    dp1[root] = foo
    return dp1[root]


def case2(root: int, base: int) -> int:
    if dp2[root] != -1:
        return dp2[root]

    if len(tree[root]) == 0:
        dp2[root] = 0
        return dp2[root]

    foo = 0
    for child in tree[root]:
        if child == base:
            continue
        foo += case1(child, root)

    dp2[root] = foo
    return dp2[root]


ans = min(case1(1, 0), case2(1, 0))
print(ans)
