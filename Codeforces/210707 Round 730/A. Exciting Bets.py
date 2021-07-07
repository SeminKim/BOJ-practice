from sys import stdin


def solve():
    a, b = map(int, stdin.readline().split())
    if a < b:
        a, b = b, a

    foo = a - b
    if foo == 0:
        return 0, 0

    wow = b % foo
    if wow == 0:
        return foo, 0

    bar = min(wow, foo - wow)
    return foo, bar


t = int(stdin.readline().strip())

for _ in range(t):
    print(*solve())
