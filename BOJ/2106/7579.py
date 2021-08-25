# https://www.acmicpc.net/problem/7579
# Use DP on cost.

from sys import stdin


def solve():
    n, m = map(int, stdin.readline().split())
    mem = list(map(int, stdin.readline().split()))
    cost = list(map(int, stdin.readline().split()))
    total = sum(cost)
    table = [0 for _ in range(total + 1)]  # table[i] 는 cost i이하로 쓰면서 확보할 수 있는 최대 메모리
    used = [set([]) for _ in range(total + 1)]  # used[i] 는 table[i]에 해당하는 사용한 후보의 index들

    for i in range(n):
        if cost[i] == 0:
            table[0] += mem[i]
            used[0].add(i)
    if m <= table[0]:
        return 0

    for nowcost in range(1, total + 1):
        foo = table[nowcost - 1]
        doge = used[nowcost - 1]
        for curr in range(n):
            before = nowcost - cost[curr]
            if before >= 0 and (curr not in used[before]):
                if table[before] + mem[curr] > foo:
                    foo = table[before] + mem[curr]
                    doge = {curr}
                    doge.update(used[before])

        table[nowcost] = foo
        used[nowcost].update(doge)
        if table[nowcost] >= m:
            return nowcost
    raise RuntimeError


print(solve())
