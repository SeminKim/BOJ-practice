# https://www.acmicpc.net/problem/2020
# BFS; (count of 'AC' > 10) only if (count of 'A' > 10)

from collections import deque
from sys import stdin

n, m, k = map(int, stdin.readline().split())
seq = stdin.readline().strip()
str_with_pos = dict()
for i in range(n):
    if seq[i] in str_with_pos:
        str_with_pos[seq[i]].append(i)
    else:
        str_with_pos[seq[i]] = [i]

# sort
str_with_pos = {key: str_with_pos[key] for key in sorted(str_with_pos)}
Q = deque()
for word, positions in str_with_pos.items():
    if len(positions) >= m:
        Q.append((word, positions))
str_with_pos.clear()

count = 0
ans = ''
while Q:
    curr_str, positions = Q.popleft()
    count += 1
    if count == k:
        ans = curr_str
    for pos in positions:
        if pos + 1 < n:
            target = curr_str + seq[pos + 1]
            if target in str_with_pos:
                str_with_pos[target].append(pos + 1)
            else:
                str_with_pos[target] = [pos + 1]
    for word, positions in sorted(str_with_pos.items()):
        if len(positions) >= m:
            Q.append((word, positions))
    str_with_pos.clear()

print(count)
print(ans)
