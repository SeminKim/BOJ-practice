# https://www.acmicpc.net/problem/1509
# DP. dp[i] 는 seq[0]~seq[i]까지의 최소 분할.
# dp[i] = min(dp[k] + 뒷부분)
# 만약 뒷부분이 palindrome이 아니면, k를 바꾸는 것이 낫거나 같음.

from sys import stdin

seq = stdin.readline().strip()
n = len(seq)

palindrome = [[None for _ in range(n)] for _ in range(n)]


def is_palindrome(i: int, j: int):
    if palindrome[i][j] is not None:
        return palindrome[i][j]

    if i == j:
        palindrome[i][j] = True

    elif i + 1 == j:
        palindrome[i][j] = (seq[i] == seq[j])

    else:
        palindrome[i][j] = (seq[i] == seq[j]) and is_palindrome(i + 1, j - 1)

    return palindrome[i][j]


dp = [0 for _ in range(n)]

for end in range(n):
    if is_palindrome(0, end):
        dp[end] = 1
        continue

    best = 420420
    for div in range(end):
        if is_palindrome(div + 1, end):
            best = min(best, dp[div] + 1)
    dp[end] = best

print(dp[n - 1])
