# https://www.acmicpc.net/problem/1629

from sys import stdin

a, b, c = map(int, stdin.readline().split())

a = a % c


def foo(pow):  # calculate a^pow mod c
    if pow == 1:
        return a

    if pow % 2 == 0:
        return foo(pow // 2) ** 2 % c
    else:
        return (foo((pow - 1) // 2) ** 2 * a) % c


print(foo(b))
