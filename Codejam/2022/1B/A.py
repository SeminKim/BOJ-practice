from collections import deque
from sys import stdin

T = int(stdin.readline().strip())
for t in range(T):
    N = int(stdin.readline().strip())
    cakes = deque(map(int, stdin.readline().split()))
    best = 0
    ans = 0
    while cakes:
        if len(cakes) == 1:
            if cakes.pop() >= best:
                ans += 1
        elif cakes[0] <= cakes[-1]:
            if cakes[0] >= best:
                ans += 1
                best = cakes.popleft()
            else:
                cakes.popleft()
        else:
            if cakes[-1] >= best:
                ans += 1
                best = cakes.pop()
            else:
                cakes.pop()

    print(f'Case #{t + 1}: {ans}')
