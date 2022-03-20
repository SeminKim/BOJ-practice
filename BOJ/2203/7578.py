# https://www.acmicpc.net/problem/7578
# Segment Tree with interval modification, single query

from sys import stdin

n = int(stdin.readline().strip())
A = list(map(int, stdin.readline().split()))
mapping = [0 for _ in range(1000001)]
for idx, num in enumerate(map(int, stdin.readline().split())):
    mapping[num] = idx

ans = 0
tree = [0 for _ in range(2 * n)]
for i in range(n):
    pos = mapping[A[i]] + n
    # query
    while pos:
        ans += tree[pos]
        pos >>= 1

    # modify: add 1
    left = n
    right = mapping[A[i]] + n - 1
    while left < right:
        if left & 1:
            tree[left] += 1
            left += 1
        if not right & 1:
            tree[right] += 1
            right -= 1
        left >>= 1
        right >>= 1
    if left == right:
        tree[left] += 1

print(ans)
