# https://www.acmicpc.net/problem/2166

from sys import stdin

n = int(stdin.readline())
vecs = []

a, b = map(int, stdin.readline().split())

for _ in range(n - 1):
    foo = list(map(int, stdin.readline().split()))
    foo[0] -= a
    foo[1] -= b
    vecs.append(foo)


def get_area(dx1, dy1, dx2, dy2):
    return 0.5 * (dx1 * dy2 - dx2 * dy1)


ans = 0
for i in range(0, n - 2):
    dx1, dy1 = vecs[i]
    dx2, dy2 = vecs[i + 1]
    ans += get_area(dx1, dy1, dx2, dy2)

print(round(abs(ans), 1))
