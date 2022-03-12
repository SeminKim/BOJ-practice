# https://www.acmicpc.net/problem/2618
# DP

from sys import stdin

INF = 10 ** 10
n = int(stdin.readline().strip())
w = int(stdin.readline().strip())
car1 = [1, 1]
car2 = [n, n]
seq = [car1, car2] + [list(map(int, stdin.readline().split())) for _ in range(w)]


def dist(fst, snd):
    return abs(fst[0] - snd[0]) + abs(fst[1] - snd[1])


# dp[i][j]: minimum when car 1 at seq[i], 2 at seq[j]
# dp[i][j] = dp[i][j-1] + dist(j-1,j) if i+1 < j
# dp[i][i+1] = min(dp[i][i-k] + dist(i-k,i+1))
dp = [[INF for _ in range(w + 2)] for _ in range(w + 2)]
prev = [[(-1, -1) for _ in range(w + 2)] for _ in range(w + 2)]
dp[0][1] = 0
for i in range(w + 2):
    if i == 1:
        continue
    for j in range(1, w + 2):
        if i == j or i + j == 1:
            continue
        elif i + 1 < j:
            dp[i][j] = dp[i][j - 1] + dist(seq[j - 1], seq[j])
            prev[i][j] = (i, j - 1)
        elif i + 1 == j and i >= 1:
            temp = INF
            best = (-1, -1)
            for k in range(1, i + 1):
                curr = dp[i][i - k] + dist(seq[i - k], seq[i + 1])
                if curr < temp:
                    best = (i, i - k)
                    temp = curr
            dp[i][i + 1] = temp
            prev[i][i + 1] = best
        elif j + 1 < i and i >= 1:
            dp[i][j] = dp[i - 1][j] + dist(seq[i - 1], seq[i])
            prev[i][j] = (i - 1, j)
        elif j + 1 == i and j >= 1:
            temp = INF
            best = (-1, -1)
            for k in range(1, i + 1):
                curr = dp[j - k][j] + dist(seq[j - k], seq[j + 1])
                if curr < temp:
                    best = (j - k, j)
                    temp = curr
            dp[j + 1][j] = temp
            prev[j + 1][j] = best

minimum = INF
best = (-1, -1)
i = w + 1
for j in range(1, w + 2):
    if dp[i][j] < minimum:
        minimum = dp[i][j]
        best = (i, j)
j = w + 1
for i in range(w + 2):
    if dp[i][j] < minimum:
        minimum = dp[i][j]
        best = (i, j)

x, y = best
print(dp[x][y])
ans = []
while prev[x][y] != (-1, -1):
    nx, ny = prev[x][y]
    if nx < x:
        ans.append('1')
        x, y = nx, ny
    else:
        ans.append('2')
        x, y = nx, ny

print('\n'.join(reversed(ans)))
