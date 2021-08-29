# https://www.acmicpc.net/problem/1036
import string
from sys import stdin

digits = string.digits + string.ascii_uppercase
profit = [0 for _ in range(36)]

n = int(stdin.readline().strip())
nums = [stdin.readline().strip() for _ in range(n)]
k = int(stdin.readline().strip())

for num in nums:
    place = 1
    for digit in reversed(num):
        profit[int(digit, 36)] += place * (int('Z', 36) - int(digit, 36))
        place *= 36

profit.sort(reverse=True)

ans = sum(map(lambda x: int(x, 36), nums)) + sum(profit[:k])

if ans == 0:
    print(0)

else:
    converted = []
    while ans:
        div, mod = divmod(ans, 36)
        converted.append(digits[mod])
        ans = div
    print(''.join(reversed(converted)))
