# https://www.acmicpc.net/problem/24397

from bisect import bisect_left
from sys import stdin

n, m, k = map(int, stdin.readline().split())
first = sorted(map(int, stdin.readline().split()))  # n elements
second = sorted(map(int, stdin.readline().split()))  # m elements

k_bin = bin(k)[2:]

ans = 0
for curr in first:
    high_bits = 0
    # all high bits than k's highest bit should be same.
    if curr > k:
        high_bits = (curr >> len(k_bin)) << len(k_bin)

    for offset in reversed(range(len(k_bin))):
        if k & (1 << offset):
            if curr & (1 << offset):
                foo = (high_bits | (1 << offset), high_bits + (1 << (offset + 1)))
                left = bisect_left(second, high_bits | (1 << offset))  # inclusive
                right = bisect_left(second, high_bits + (1 << (offset + 1)))  # exclusive
                ans += right - left
            else:
                foo = (high_bits, (high_bits | (1 << offset)))
                left = bisect_left(second, high_bits)
                right = bisect_left(second, (high_bits | (1 << offset)))
                ans += right - left
                high_bits = high_bits | (1 << offset)
        else:
            if curr & (1 << offset):
                high_bits = high_bits | (1 << offset)

print(ans)
