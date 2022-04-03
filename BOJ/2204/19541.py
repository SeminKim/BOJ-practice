# https://www.acmicpc.net/problem/19541

from sys import stdin

n, m = map(int, stdin.readline().split())
groups = []
for _ in range(m):
    _, *foo = map(int, stdin.readline().split())
    groups.append(foo)
result = list(map(int, stdin.readline().split()))

ans = [-1] * n
for curr in reversed(groups):
    covid = True
    for person in curr:
        if result[person - 1] == 0 or ans[person - 1] == 0:
            covid = False
            break
    if not covid:
        for person in curr:
            ans[person - 1] = 0

for i in range(n):
    if ans[i] == -1:
        ans[i] = result[i]

# check by simulation
check = ans[:]
for curr in groups:
    covid = False
    for person in curr:
        if check[person - 1] == 1:
            covid = True
            break
    if covid:
        for person in curr:
            check[person - 1] = 1
# print(ans)
if check == result:
    print("YES")
    print(" ".join(map(str, ans)))
else:
    print("NO")
