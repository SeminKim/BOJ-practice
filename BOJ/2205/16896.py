# https://www.acmicpc.net/problem/16896

from sys import stdin


def solve():
    n = int(stdin.readline().strip())
    all_plus = False
    current = True
    num = n
    while num > 1:
        next_num = num // 2
        if all_plus:
            all_plus = False
            current = False
        else:
            if (num % 2 == 0 and current is False) or (num % 2 == 1 and current is True):
                all_plus = True
                current = True
            elif next_num % 2 != num % 2:
                current = not current
        num = next_num

    if current:
        print('koosaga')
    else:
        print('cubelover')
    return


t = int(stdin.readline().strip())
for _ in range(t):
    solve()
