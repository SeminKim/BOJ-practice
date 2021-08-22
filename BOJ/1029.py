# https://www.acmicpc.net/problem/1029
# DP with bitmask
# https://www.acmicpc.net/source/32044568 <= this code is much faster and good.

from sys import stdin

INF = 100
n = int(stdin.readline().strip())
adj = []
for _ in range(n):
    adj.append(list(map(int, list(stdin.readline().strip()))))

dp_cost = [[[INF for _ in range(1 << n)] for _ in range(n)] for _ in range(n)]  # dp_cost[level][owner][bitmask]
dp_cost[0][0][1] = 0
ans = 0

for lvl in range(1, n):
    for owner in range(n):
        for case in range(1 << n):
            # check the owner owns picture in this case
            if case & (1 << owner) == 0:
                continue

            # desired bitmask to check
            curr = case ^ (1 << owner)

            # DP
            for before in range(n):
                # check if a possible "before" candidate owns picture in this case
                if case & (1 << before) == 0:
                    continue

                # check if "owner" can buy picture from "before"
                if dp_cost[lvl - 1][before][curr] <= adj[before][owner]:
                    dp_cost[lvl][owner][case] = min(dp_cost[lvl][owner][case], adj[before][owner])
                    ans = lvl

print(ans + 1)
