from collections import deque
from sys import stdin


def solve():
    n = int(stdin.readline().strip())
    seq = [0] + list(map(int, stdin.readline().split()))
    wow = max(seq)
    if seq[1] != wow and seq[-1] != wow:
        print(-1)
        return

    ans = deque()
    left = 1
    right = n
    while left <= right:
        if seq[right] > seq[left]:
            ans.append(seq[right])
            right -= 1
        else:
            ans.appendleft(seq[left])
            left += 1

    print(' '.join(map(str, ans)))


t = int(stdin.readline().strip())

for _ in range(t):
    solve()
