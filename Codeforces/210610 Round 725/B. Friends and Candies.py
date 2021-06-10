from sys import stdin

t = int(stdin.readline().strip())

for _ in range(t):
    n = int(stdin.readline().strip())
    seq = list(map(int, stdin.readline().split()))
    foo = sum(seq)
    if foo%n != 0:
        print(-1)
    else:
        goal = foo//n
        ans = 0
        for i in seq:
            if i > goal:
                ans += 1
        print(ans)
