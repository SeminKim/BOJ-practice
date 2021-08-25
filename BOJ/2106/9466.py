# https://www.acmicpc.net/problem/9466
from sys import stdin


def solve():
    n = int(stdin.readline().strip())
    seq = [0] + list(map(int, stdin.readline().split()))
    visited = [0 for _ in range(n + 1)]
    ans = 0
    for i in range(1, n + 1):
        if visited[i] != 0:
            continue
        history = [i]
        now = i
        while visited[now] == 0:
            visited[now] = 1
            now = seq[now]
            history.append(now)

        idx = history.index(now)
        for node in history[:idx]:
            visited[node] = -1
            ans += 1
    print(ans)


t = int(stdin.readline().strip())
for _ in range(t):
    solve()
