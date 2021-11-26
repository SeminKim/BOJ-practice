from sys import stdin


def solve():
    n = int(stdin.readline().strip())
    if n % 2 == 0:
        print(0)
    elif int(str(n)[0]) % 2 == 0:
        print(1)
    else:
        for i in str(n):
            if int(i) % 2 == 0:
                print(2)
                return
        print(-1)


t = int(stdin.readline().strip())

for _ in range(t):
    solve()
