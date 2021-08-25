# https://www.acmicpc.net/problem/17371
# 정답인 점이 있다면 그 점을 편의시설로 옮겨도 거리는 같다.
# 만약 정답인 점이 이미 편의시설 위에 있다면 OK.
# 그렇지 않다면, 그 점은 두 편의시설을 이은 선분 안에 존재하므로 옮겨도 OK.
#   점 O가 정답인 점 중 하나이고 여기서 가장 먼 곳이 A, 가장 가까운 곳이 B라면,
#   거리 OA+OB가 전체의 minimum이다.
#   만약 O가 AB위에 없다면, 어떤 C에 대해 BC <= BO+OC <= OB+OA 이다 (A는 가장 먼곳이고, 삼각부등식을 활용)
#   OA+OB가 최소이려면 등호가 성립해야하고, 이는 OA=OC 이고 O,B,C가 직선상에 있는 경우이다.

from sys import stdin

INF = 10 ** 10


def get_dist(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


n = int(stdin.readline().strip())
points = []
adj = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(n):
    points.append(list(map(int, stdin.readline().split())))

for i in range(n):
    for j in range(i + 1, n):
        x1, y1 = points[i]
        x2, y2 = points[j]
        dist = get_dist(x1, y1, x2, y2)
        adj[i][j] = dist
        adj[j][i] = dist

best = INF
ans = None
for i in range(n):
    foo = max(adj[i])
    if foo < best:
        best = foo
        ans = points[i]

print(*ans)
