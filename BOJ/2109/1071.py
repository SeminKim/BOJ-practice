# https://www.acmicpc.net/problem/1071
# "first in dictionary order" => Greedy

from sys import stdin

n = int(stdin.readline().strip())
seq = list(map(int, stdin.readline().split()))
count = [0 for _ in range(1001)]
keys = []
for i in seq:
    if count[i] == 0:
        keys.append(i)
    count[i] += 1
keys.sort()

ans = [-42]
while len(keys) > 2:
    target = keys[0]
    if ans[-1] + 1 == target:
        target = keys[1]
    ans.append(target)
    count[target] -= 1
    if count[target] == 0:
        keys.remove(target)

if len(keys) == 2:
    num1, num2 = keys
    if num1 + 1 == num2:
        for _ in range(count[num2]):
            ans.append(num2)
        keys = [num1]
    else:
        if ans[-1] + 1 != num1:
            for _ in range(count[num1]):
                ans.append(num1)
            keys = [num2]
        else:
            ans.append(num2)
            count[num2] -= 1
            for _ in range(count[num1]):
                ans.append(num1)
            keys = [num2]

if len(keys) == 1:
    num = keys[0]
    for _ in range(count[num]):
        ans.append(num)

print(' '.join(map(str, ans[1:])))
