# https://www.acmicpc.net/problem/1019
# 274 = 200 + 70 + 4
# 200: [0] += 100, [1] += 100, [2] += 74
# 70: [0], [1], ... [6] += 10, [7] += 4
# 4: [0], [1], ... [4] += 1
# number starts with [0]: 111 : 0xx => 100, 0'0'x => 10, 00'0' => 1


from sys import stdin

n = int(stdin.readline().strip())
n_str = str(n)


def helper(num_digit):  # return number of j > 1 for 00...00~99...99
    if num_digit <= 1:
        return num_digit
    return helper(num_digit - 1) * 10 + 10 ** (num_digit - 1)


ans = [0 for _ in range(10)]

for idx in range(len(n_str)):
    curr = int(n_str[idx])

    if idx == len(n_str) - 1:
        for num in range(curr + 1):
            ans[num] += 1
        break

    lvl = len(n_str) - 1 - idx
    foo = curr * helper(lvl)
    for num in range(10):
        ans[num] += foo
        if num < curr:
            ans[num] += 10 ** lvl

    if lvl != 0:
        ans[curr] += int(n_str[idx + 1:]) + 1

ans[0] -= int('1' * (len(n_str)))
print(*ans)
