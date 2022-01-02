# https://www.acmicpc.net/problem/14501
# DP

from sys import stdin

n = int(stdin.readline().strip())
seq = [(0, 0)]
for i in range(1, n + 1):
    t, p = map(int, stdin.readline().split())
    seq.append((t, p))


best = [0 for _ in range(n + 1)]

for day in range(1, n + 1):
    temp = best[day - 1]
    for back in range(day):
        prev_t, prev_p = seq[day - back]
        if day - back + prev_t - 1 <= day:
            temp = max(temp, best[day - back - 1] + prev_p)
    best[day] = temp

print(best[-1])
