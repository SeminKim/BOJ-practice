from sys import stdin

T = int(stdin.readline().strip())
INF = 10 ** 6
for t in range(T):
    minimum = [INF, INF, INF, INF]
    for _ in range(3):
        line = list(map(int, stdin.readline().split()))
        for i in range(4):
            minimum[i] = min(minimum[i], line[i])

    ans = 'IMPOSSIBLE'
    if sum(minimum) >= 10 ** 6:
        left = 10 ** 6
        ret = [0] * 4
        i = 0
        while i < 4:
            if left > minimum[i]:
                left -= minimum[i]
                ret[i] = minimum[i]
            else:
                ret[i] = left
                break
            i += 1
        ans = ' '.join(map(str, ret))

    print(f'Case #{t + 1}: {ans}')
