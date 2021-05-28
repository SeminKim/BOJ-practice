from sys import stdin
from itertools import combinations

# NOT SOLVED YET
n = int(stdin.readline().strip())
seq = list(map(int, stdin.readline().split()))
good = []
bad = []
max_hp = 0
for idx, i in enumerate(seq):
    if i >= 0:
        good.append((i, idx))
        max_hp += i
    else:
        bad.append((i, idx))

a = len(good)
b = len(bad)

good_sorted = good[:]
good_sorted.sort()
bad_sorted = bad[:]
bad_sorted.sort()

cnt = 0
max_num = 0
for i in range(b):
    cnt += bad_sorted[b - i - 1][0]
    if max_hp + cnt < 0:
        max_num = i
        break
    if i == b - 1:
        max_num = b


def solve():
    k = 0
    while True:
        for selected_potion in combinations(bad, max_num - k):
            bad_idx = []
            for item in selected_potion:
                bad_idx.append(item[1])

            total = 0
            for i in range(n):
                if seq[i] >= 0:
                    total += seq[i]
                elif i in bad_idx:
                    total += seq[i]
                if total < 0:
                    break
                if total >= 0 and i == n-1:
                    return max_num-k + len(good)
        k -= 1


print(solve())