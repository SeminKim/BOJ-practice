from sys import stdin


def solve():
    n, k = map(int, stdin.readline().split())
    seq = list(map(int, stdin.readline().split()))
    seq.sort(reverse=True)
    temp = 0
    ans = 0
    for i in seq:
        temp += n - i
        if temp < n:
            ans += 1
        else:
            print(ans)
            return

    print(ans)


t = int(stdin.readline().strip())

for _ in range(t):
    solve()
