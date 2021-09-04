# https://www.acmicpc.net/problem/1700
# greedy

from sys import stdin

n, k = map(int, stdin.readline().split())
seq = [0] + list(map(int, stdin.readline().split()))

current = set()
ans = 0
for i in range(1, k + 1):
    # print(current)
    now = seq[i]
    if now in current:
        continue

    elif len(current) < n:
        current.add(now)

    else:
        ans += 1
        first_occur = {x: 1000 for x in current}
        for j in range(k, i, -1):
            if seq[j] in current:
                first_occur[seq[j]] = j

        to_remove = max(current, key=lambda x: first_occur[x])
        current.remove(to_remove)
        current.add(now)

print(ans)
