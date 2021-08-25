# https://www.acmicpc.net/problem/12850
# Convert to matrix multiplication, do it fast by Divide and Conquer.

from sys import stdin

n = int(stdin.readline().strip())
# '정보과학관', '전산관', '미래관', '신양관', '한경직기념관', '진리관', '형남공학관', '학생회관'
now = [1, 0, 0, 0, 0, 0, 0, 0]
DIV = 1_000_000_007

matrix = [[0, 1, 1, 0, 0, 0, 0, 0], [1, 0, 1, 1, 0, 0, 0, 0], [1, 1, 0, 1, 1, 0, 0, 0], [0, 1, 1, 0, 1, 1, 0, 0],
          [0, 0, 1, 1, 0, 1, 1, 0], [0, 0, 0, 1, 1, 0, 0, 1], [0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 0, 1, 1, 0]]
memo = [matrix]


def mat_mult(first, second):  # assume both are 8*8 symmetric.
    res = [[0 for _ in range(8)] for _ in range(8)]
    for i in range(8):
        for j in range(8):
            for foo, bar in zip(first[i], second[j]):
                res[i][j] += foo * bar
            res[i][j] = res[i][j] % DIV
    return res


for i in range(30):
    memo.append(mat_mult(memo[-1], memo[-1]))

temp = None
for component, check in zip(memo, bin(n)[2:][::-1]):
    if check == '1':
        if temp is None:
            temp = component
        else:
            temp = mat_mult(component, temp)

print(temp[0][0])
