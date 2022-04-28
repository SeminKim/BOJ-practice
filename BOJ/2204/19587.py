# https://www.acmicpc.net/problem/19587
# Matrix Multiplication, utilize symmetry

from sys import stdin


def matmul(mat1, mat2):
    [[a, b], [c, d]] = mat1
    [[e, f], [g, h]] = mat2
    return [[(a * e + b * g) % MOD, (a * f + b * h) % MOD], [(e * c + d * g) % MOD, (c * f + d * h) % MOD]]


MOD = 10 ** 9 + 7
n = int(stdin.readline().strip())
save = [[[1, 1],
         [2, 1]]]

for _ in range(60):
    save.append(matmul(save[-1], save[-1]))

ret = [[1, 0], [0, 1]]
for curr, bit in zip(save, reversed(bin(n - 1)[2:])):
    if bit == '1':
        ret = matmul(curr, ret)

[[a, b], [c, d]] = ret
ans = (a + 2 * b + c + 2 * d) % MOD

print(ans)
