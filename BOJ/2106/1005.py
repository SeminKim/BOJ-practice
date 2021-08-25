from sys import stdin
import heapq


def solve():
    n, k = map(int, stdin.readline().split())
    costs = [0] + list(map(int, stdin.readline().split()))
    pre = [[] for _ in range(n + 1)]  # i번째 짓기 직전 필요한 건물
    post = [[] for _ in range(n + 1)]  # i번째를 지어야 지을 수 있는 건물

    for _ in range(k):
        a, b = map(int, stdin.readline().split())
        pre[b].append(a)
        post[a].append(b)
    goal = int(stdin.readline().strip())

    necessary = set()

    def dfs(node):
        necessary.add(node)
        for foo in pre[node]:
            if foo in necessary:
                continue
            dfs(foo)

    dfs(goal)

    pq = []  # 당장 지을수 있는 건물들
    for i in necessary:
        if len(pre[i]) == 0:
            heapq.heappush(pq, [costs[i], i])
    cost = 0
    while pq:
        nowcost, nowbuild = heapq.heappop(pq)  # 지을 수 있는 것중 가장 cost 작은것부터 생각
        cost += nowcost
        if nowbuild == goal:
            return cost

        for i in pq:
            i[0] -= nowcost

        for candi in post[nowbuild]:
            if candi not in necessary:
                continue
            pre[candi].remove(nowbuild)
            if len(pre[candi]) == 0:
                heapq.heappush(pq, [costs[candi], candi])


t = int(stdin.readline().strip())

for _ in range(t):
    print(solve())
