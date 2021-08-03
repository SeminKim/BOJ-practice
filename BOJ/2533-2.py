# https://www.acmicpc.net/problem/2533
# Kind of greedy algorithm works for this problem.
# WHY??
# let the answer of this problem for subtree with root r as f(r).
# for convenience of notation, call early adapter as good.
#
# claim 1 : for root r and its children c_1, c_2, ...,
#   root should be bad, and thus f(r) = sum of f(c_i), if all children c_i are good.
#   proof =>this is trivial, because f(c_i) is an optimal answer for sub-tree.
#           adding good node r to c_i does not change any optimal configuration decided before:
#           just because it was optimal, whether or not the root node exists.
#
# claim 2 : for root r and its children c_1, c_2, ...,
#   root should be good, and thus f(r) = 1 + sum of f(c_i), if any one child is bad.
#   proof =>the only case to be checked is bad r and good c_i (for all i).
#           but this cannot lead to smaller answer.
#           if it can, there should exist configuration with bad c_i, which results in also f(c_i). (for any i)
#           value larger than f(c_i) will lead the whole case to bigger answer then "1 + sum of f(c_i)", and
#           value smaller than f(c_i) is impossible because f(c_i) is optimal.
#           f(c_i) was obtained when c_i is bad, thus all children of c_i should be good.
#           if we change the configuration to make c_i good, at least one good node is added,
#           but c_i's children are already in optimal structure, and thus do not change (by claim 1).
#           so this result at least f(c_i) + 1.
#
# because of both claims, we can immediately calculate f(r) if all f(c_i) with good-or-bad-flag of c_i are given.
# there is no way to further optimize the answer by changing any of c_i's flag.


from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 8)
n = int(stdin.readline().strip())
tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)


def dfs(root: int, root_parent: int) -> (int, bool):  # flag: whether root is early adapter.
    res = 0
    flag = False
    for child in tree[root]:
        if child == root_parent:
            continue
        foo, bar = dfs(child, root)
        res += foo
        if not bar:
            flag = True
    if flag:
        res += 1
    # print(root, res, flag)
    return res, flag


print(dfs(1, 0)[0])
