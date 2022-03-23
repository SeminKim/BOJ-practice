# https://www.acmicpc.net/problem/13415
# Record inverting points

from collections import deque
from sys import stdin

n = int(stdin.readline().strip())
seq = list(map(int, stdin.readline().split()))
q = int(stdin.readline().strip())
operation = [list(map(int, stdin.readline().split())) for _ in range(q)]
equivalent = deque()
for i in range(q):
    a, b = operation[i]
    a -= 1
    b -= 1
    if a <= b:
        while len(equivalent) > 0 and abs(equivalent[-1]) <= b:
            equivalent.pop()
        equivalent.append(-b)
    else:
        while len(equivalent) > 0 and abs(equivalent[-1]) <= a:
            equivalent.pop()
        equivalent.append(a)
        equivalent.append(-b)

# print(equivalent)
ascending_right = abs(equivalent[0])
descending_left = 0
temp = sorted(seq[:ascending_right + 1]) + seq[ascending_right + 1:]
ans = [0 for _ in range(ascending_right + 1)] + seq[ascending_right + 1:]
idx = ascending_right
while equivalent:
    op = equivalent.popleft()
    if len(equivalent) == 0:
        if op > 0:  # ascending
            while idx >= 0:
                ans[idx] = temp[ascending_right]
                ascending_right -= 1
                idx -= 1
        else:  # descending
            while idx >= 0:
                ans[idx] = temp[descending_left]
                descending_left += 1
                idx -= 1

    if op > 0:  # ascending
        while equivalent and abs(equivalent[0]) < idx:
            ans[idx] = temp[ascending_right]
            ascending_right -= 1
            idx -= 1
    else:  # descending
        while equivalent and abs(equivalent[0]) < idx:
            ans[idx] = temp[descending_left]
            descending_left += 1
            idx -= 1

print(*ans)

# 7
# 1 3 5 4 2 7 0
# 5
# 1 3
# 6 4
# 2 1
# 3 1
# 1 3

# 8
# 1 7 5 4 3 2 1 9
# 6
# 1 3
# 4 1
# 5 5
# 4 3
# 2 3
# 1 1
