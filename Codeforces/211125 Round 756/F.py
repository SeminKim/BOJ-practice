from sys import stdin

# NOT SOLVED YET

def solve():
    n, s = map(int, stdin.readline().split())
    seq = list(map(int, stdin.readline().split()))

    left = 0
    right = 0
    curr = 0
    ans = 0
    while right < n - 1:
        print(left, right)
        if curr + seq[right] >= -s:
            curr += seq[right]
            right += 1
        elif curr + seq[right] - seq[left] >= -s:
            curr += seq[right]
            left += 1
            right += 1
        else:
            ans = max(ans, right - left)
            curr = 0
            left = right + 1
            right = right + 1
    print(ans)


t = int(stdin.readline().strip())

for _ in range(t):
    solve()
