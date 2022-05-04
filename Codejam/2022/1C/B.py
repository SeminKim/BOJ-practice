# Not solved yet..

from sys import stdin

T = int(stdin.readline().strip())
for t in range(T):
    n, k = map(int, stdin.readline().split())
    seq = list(map(int, stdin.readline().split()))
    squared_sum = sum(i * i for i in seq)
    simple_sum = sum(seq)
    if simple_sum == 0:
        if squared_sum == 0:
            ans = 0
        else:
            ans = 'IMPOSSIBLE'
    else:
        ans = (squared_sum - simple_sum * simple_sum) // (2 * simple_sum)
        if ans < -10 ** 18 or ans > 10 ** 18:
            ans = "IMPOSSIBLE"
        elif squared_sum + ans * ans != (simple_sum + ans) ** 2:
            ans = 'IMPOSSIBLE'

    print(f'Case #{t + 1}: {ans}')
