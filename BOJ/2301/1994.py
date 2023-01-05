# https://www.acmicpc.net/problem/1994

from collections import Counter
from sys import stdin

n = int(stdin.readline().strip())
nums = [int(stdin.readline().strip()) for _ in range(n)]
# n = 2000
# nums = [i for i in range(n)]

counter = Counter(nums)
ans = max(counter.values())  # sequence with common difference zero.
nums = sorted(counter.keys())
n = len(nums)
arrows = [dict() for _ in range(n)]

for i in range(n):
    for j in range(i + 1, n):
        diff = nums[j] - nums[i]
        arrows[i][diff] = j

for i in range(n):
    for diff, after in arrows[i].items():
        temp = 2
        current = after
        while diff in arrows[current]:
            current = arrows[current][diff]
            temp += 1
        ans = max(temp, ans)

print(ans)
