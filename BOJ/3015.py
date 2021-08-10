# https://www.acmicpc.net/problem/3015
# Count using stack, beware of multiplicity.


from sys import stdin
from collections import deque

n = int(stdin.readline().strip())
stack = deque()
multi = deque()

ans = 0
for _ in range(n):
    curr = int(stdin.readline().strip())
    # print(curr, stack, multi, ans)

    while len(stack) != 0 and stack[-1] < curr:
        stack.pop()
        ans += multi.pop()

    if len(stack) == 0:
        stack.append(curr)
        multi.append(1)

    elif stack[-1] > curr:
        ans += 1
        stack.append(curr)
        multi.append(1)

    else:  # stack[-1] == curr:
        ans += multi[-1]
        multi[-1] += 1
        if len(stack) > 1:
            ans += 1

print(ans)
