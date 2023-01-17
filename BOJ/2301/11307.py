# https://www.acmicpc.net/problem/11307

from sys import stdin

n = int(stdin.readline().strip())
for _ in range(n):
    initial, target = stdin.readline().split()
    li = len(initial)
    lt = len(target)
    start = (li - lt) // 2
    ans = 'Bob'
    if initial == target:
        ans = 'Alice'
    elif (li - lt) % 2 == 0:
        if initial[start: start + lt] == target:
            ans = 'Alice'
        elif initial[start - 1: start - 1 + lt] == initial[start + 1: start + 1 + lt] == target:
            ans = 'Alice'
    else:
        if initial[start: start + lt] == initial[start + 1: start + lt + 1] == target:
            ans = 'Alice'
    print(ans)
