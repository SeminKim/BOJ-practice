# https://www.acmicpc.net/problem/2448

from sys import stdin

stars = [[] for _ in range(11)]
stars[0] = ['  *  ', ' * * ', '*****']

for i in range(1, 11):
    stars[i] = stars[i - 1][:]
    foo = 3 * 2 ** (i - 1)
    for idx in range(len(stars[i])):
        stars[i][idx] = ' ' * foo + stars[i][idx] + ' ' * foo

    for line in stars[i - 1]:
        stars[i].append(line + ' ' + line)

N = int(stdin.readline().strip())
foo = [3 * 2 ** i for i in range(11)]

for line in stars[foo.index(N)]:
    print(line)
