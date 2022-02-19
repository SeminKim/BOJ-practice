from sys import stdin

T, N, D = map(int, stdin.readline().split())
MOD = 1_000_000_007


def matrix_multiplication(fst, snd):
    return [[sum(fst[i][k] * snd[k][j] for k in range(N)) % MOD for j in range(N)] for i in range(N)]


matrices = []
for _ in range(T):
    temp = [[0] * N for _ in range(N)]
    M = int(stdin.readline().strip())
    for _ in range(M):
        a, b, c = map(int, stdin.readline().split())
        temp[a - 1][b - 1] = c
    matrices.append(temp)

for i in range(1, T):
    matrices[i] = matrix_multiplication(matrices[i - 1], matrices[i])

memo = [matrices[T - 1]]
for i in range(30):
    memo.append(matrix_multiplication(memo[-1], memo[-1]))

ans = [[0] * N for _ in range(N)]
for i in range(N):
    ans[i][i] = 1

mult = D // T
for i in range(30):
    if mult & (1 << i):
        ans = matrix_multiplication(ans, memo[i])

if D % T != 0:
    ans = matrix_multiplication(ans, matrices[D % T - 1])

for line in ans:
    print(*line)
