from sys import stdin

squares = [i ** 2 for i in range(4 * 10 ** 4)]


def solve():
    k = int(stdin.readline().strip())
    lvl = 0
    while squares[lvl] < k:
        lvl += 1

    if squares[lvl] - lvl + 1 <= k:
        print(lvl, squares[lvl] - k + 1)
        return

    else:
        foo = squares[lvl] - lvl + 1
        print(k - foo + lvl, lvl)
        return


t = int(stdin.readline().strip())

for _ in range(t):
    solve()
