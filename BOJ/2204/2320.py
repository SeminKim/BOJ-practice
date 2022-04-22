# https://www.acmicpc.net/problem/2320
# Bitmask DP

from itertools import combinations
from sys import stdin

to_num = {k: i for i, k in enumerate('AEIOU')}

n = int(stdin.readline().strip())
words = []
dp = [[0] * (1 << n) for _ in range(5)]  # best for given bitmask and ending character
for i in range(n):
    word = stdin.readline().strip()
    start = to_num[word[0]]
    end = to_num[word[-1]]
    words.append((start, end, len(word)))

for turn in range(1, n + 1):
    for indices in combinations(range(n), turn):
        base_flag = sum(1 << i for i in indices)
        for end_idx in indices:
            dp[words[end_idx][1]][base_flag] = max(dp[words[end_idx][1]][base_flag],
                                                   dp[words[end_idx][0]][base_flag ^ (1 << end_idx)] + words[end_idx][
                                                       2])

print(max(dp[i][-1] for i in range(5)))
