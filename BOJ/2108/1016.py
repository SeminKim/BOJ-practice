# https://www.acmicpc.net/problem/1016

from sys import stdin

low, high = map(int, stdin.readline().split())
temp = [1 for _ in range(low, high + 1)]

for i in [2] + [j for j in range(3, int(high ** .5) + 1, 2)]:
    foo = i ** 2
    start = low - low % foo
    if start < low:
        start += foo

    for num in range(start, high + 1, foo):
        temp[num - low] = 0

print(sum(temp))
