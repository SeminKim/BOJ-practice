# https://www.acmicpc.net/problem/14888
# Implementation

from sys import stdin


def helper(iterable):
    size = len(iterable)
    while True:
        yield tuple(iterable)
        for i in range(size - 2, -1, -1):
            if iterable[i] < iterable[i + 1]:
                break
        else:
            return
        for j in range(size - 1, i, -1):
            if iterable[i] < iterable[j]:
                break
        iterable[i], iterable[j] = iterable[j], iterable[i]
        iterable[i + 1:] = iterable[: i - size: -1]


n = int(stdin.readline().strip())
seq = list(map(int, stdin.readline().split()))
a, b, c, d = map(int, stdin.readline().split())
funcs = [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y, lambda x, y: int(x / y)]
func_idx = [0] * a + [1] * b + [2] * c + [3] * d

maximum = -10 ** 10
minimum = 10 ** 10
for selected in helper(func_idx):
    val = seq[0]
    i = 1
    for idx in selected:
        func = funcs[idx]
        val = func(val, seq[i])
        i += 1
    maximum = max(val, maximum)
    minimum = min(val, minimum)

print(maximum)
print(minimum)
