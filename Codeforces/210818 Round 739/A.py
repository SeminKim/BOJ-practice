from sys import stdin

ans = [0]
for i in range(1, 10001):
    if i % 3 == 0:
        continue
    if str(i)[-1] == '3':
        continue
    ans.append(i)


def solve():
    n = int(stdin.readline().strip())
    print(ans[n])


t = int(stdin.readline().strip())

for _ in range(t):
    solve()
