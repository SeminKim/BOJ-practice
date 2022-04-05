from sys import stdin

T = int(stdin.readline().strip())
INF = 10 ** 6
for t in range(T):
    n = int(stdin.readline().strip())
    dice = list(map(int, stdin.readline().split()))
    dice.sort()
    left = 0
    right = 0
    curr = 1
    ans = 0
    while right < n:
        if dice[right] >= curr:
            right += 1
            curr += 1
        else:
            while dice[right] < curr:
                left += 1
                curr -= 1
        ans = max(ans, right - left)

    print(f'Case #{t + 1}: {ans}')
