# https://www.acmicpc.net/problem/2263
# Use Recursion
from sys import setrecursionlimit, stdin

setrecursionlimit(10 ** 9)

n = int(stdin.readline())
input_inorder = list(map(int, stdin.readline().split()))
input_postorder = list(map(int, stdin.readline().split()))
inorder_find = [0 for _ in range(n + 1)]
for i in range(n):
    inorder_find[input_inorder[i]] = i


def to_preorder(inorder_start, inorder_end, postorder_start, postorder_end):
    if inorder_start > inorder_end or postorder_start > postorder_end:
        return

    root = input_postorder[postorder_end]
    print(root, end=' ')

    left = inorder_find[root] - inorder_start
    right = inorder_end - inorder_find[root]
    to_preorder(inorder_start, inorder_start + left - 1, postorder_start, postorder_start + left - 1)
    to_preorder(inorder_end - right + 1, inorder_end, postorder_end - right, postorder_end - 1)
    return


to_preorder(0, n - 1, 0, n - 1)

'''
testcase

21
1 3 2 7 4 6 5 15 11 9 12 8 13 10 14 21 19 17 20 16 18
1 2 3 4 5 6 7 11 12 9 13 14 10 8 15 19 20 17 18 16 21
ANS: 21 15 7 3 1 2 6 4 5 8 9 11 12 10 13 14 16 17 19 20 18

'''
