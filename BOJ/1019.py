# https://www.acmicpc.net/problem/1019

from sys import stdin

n = int(stdin.readline().strip())
n_str = str(n)


def helper(num_digit):  # return number of j > 1 for 00...00~99...99
    if num_digit <= 1:
        return num_digit
    return helper(num_digit-1) * 10 + 10**(num_digit-1)


def helper_zero(num_digit):
    return helper(num_digit) - int('1'*num_digit)


ans = [0 for _ in range(10)]


for idx in range(len(n_str)):
    curr = int(n_str[idx])
    lvl = len(n_str) - 1 - idx
    foo = curr * helper(lvl)
    for num in range(10):
        ans[num] += foo
        if num < curr:
            ans[num] += 10**lvl

    if lvl != 0:
        ans[curr] += int(n_str[idx+1:])

print(ans)






# curr = int(str(n)[:3])
# ans = base[curr][:]
# if n < 1000:
#     print(*ans)
#     exit()
#
#
# for digit in str(n)[3:]:
#     digit = int(digit)
#     for i in range(10):
#         ans[i] *= 10
#         ans[i] += curr
#         if i <= digit:
#             ans[i] += 1
#     curr = int(str(curr) + str(digit))
#
# print(*ans)
#
#
#
#
#
# for num in range(1, 100001):
#     for one in str(num):
#         ans[int(one)] += 1
#     if num in [2748,274,27,2]:
#         print(num, ans)
#
# ans = 0
#
# print(ans)
