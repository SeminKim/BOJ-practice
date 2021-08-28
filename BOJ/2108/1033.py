# https://www.acmicpc.net/problem/1033
from collections import deque
from sys import stdin


def factorize(num):
    res = {2: 0, 3: 0, 5: 0, 7: 0}
    for i in res.keys():
        while num % i == 0:
            num //= i
            res[i] += 1
    return res


n = int(stdin.readline().strip())

Q = deque()
for _ in range(n - 1):
    seq = list(map(int, stdin.readline().split()))
    Q.append(seq)

check = [False for _ in range(n)]
ans = [None for _ in range(n)]
ans[0] = {2: 30, 3: 20, 5: 10, 7: 10}
check[0] = True

while Q:
    a, b, p, q = Q.popleft()
    if check[a]:
        foo = factorize(p)
        bar = factorize(q)
        ans[b] = {x: ans[a][x] for x in [2, 3, 5, 7]}
        for i in [2, 3, 5, 7]:
            ans[b][i] += bar[i] - foo[i]
        check[b] = True
    elif check[b]:
        foo = factorize(p)
        bar = factorize(q)
        ans[a] = {x: ans[b][x] for x in [2, 3, 5, 7]}
        for i in [2, 3, 5, 7]:
            ans[a][i] += foo[i] - bar[i]
        check[a] = True

    else:
        Q.append([a, b, p, q])

gcd = {2: 100, 3: 100, 5: 100, 7: 100}
for i in [2, 3, 5, 7]:
    for num in range(n):
        gcd[i] = min(gcd[i], ans[num][i])

for i in range(n):
    now = ans[i]
    res = 1
    for j in [2, 3, 5, 7]:
        res *= j ** (now[j] - gcd[j])
    print(res, end=' ')
