from sys import stdin


def solve(num):
    while num >= 111:
        if num % 11 == 0:
            return True
        num -= 111
    return num % 11 == 0


t = int(stdin.readline().strip())

for _ in range(t):
    n = int(stdin.readline().strip())
    if solve(n):
        print('YES')
    else:
        print('NO')
