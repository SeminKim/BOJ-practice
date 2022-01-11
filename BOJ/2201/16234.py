# https://www.acmicpc.net/problem/16234
# Disjoint Set

from sys import stdin

n, l, r = map(int, stdin.readline().split())
world = [list(map(int, stdin.readline().split())) for _ in range(n)]


def find_head(point):
    x, y = point
    if head[x][y] != (x, y):
        head[x][y] = find_head(head[x][y])
    return head[x][y]


def union(fst, snd):
    fst, snd = sorted([find_head(fst), find_head(snd)])
    if fst == snd:
        return
    fst_n = num[fst[0]][fst[1]]
    snd_n = num[snd[0]][snd[1]]
    fst_p = population[fst[0]][fst[1]]
    snd_p = population[snd[0]][snd[1]]
    if fst_p >= snd_p:
        head[snd[0]][snd[1]] = fst
        population[fst[0]][fst[1]] = fst_p + snd_p
        population[snd[0]][snd[1]] = 0
        num[fst[0]][fst[1]] = fst_n + snd_n
    else:
        head[fst[0]][fst[1]] = snd
        population[fst[0]][fst[1]] = 0
        population[snd[0]][snd[1]] = fst_p + snd_p
        num[snd[0]][snd[1]] = fst_n + snd_n


ans = 0
flag = True
while flag:
    flag = False
    num = [[1 for _ in range(n)] for _ in range(n)]
    head = [[(i, j) for j in range(n)] for i in range(n)]
    population = [foo[:] for foo in world]
    for i in range(n):
        for j in range(n):
            for dr, dc in [[0, 1], [1, 0]]:
                ni = i + dr
                nj = j + dc
                if ni < n and nj < n and l <= abs(world[i][j] - world[ni][nj]) <= r:
                    flag = True
                    union((i, j), (ni, nj))
    for i in range(n):
        for j in range(n):
            head_i, head_j = find_head((i, j))
            world[i][j] = int(population[head_i][head_j] / num[head_i][head_j])
    ans += flag

print(ans)
