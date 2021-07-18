# https://www.acmicpc.net/problem/1799

from sys import stdin

n = int(stdin.readline().strip())
board = [list(map(int, stdin.readline().split())) for _ in range(n)]
# board = [[1, 1, 1, 0, 1, 1, 1, 0, 1, 1] for __ in range(10)]


def search(now: int, res: int):
    global best
    if res == max_ans:
        best = 420420
        return

    if now == len(available):
        best = max(best, res)
        return

    if len(available) - now + res <= best:
        return

    r, c = available[now]
    if check_plus[r + c] and check_minus[r - c]:
        check_plus[r + c] = 0
        check_minus[r - c] = 0
        search(now + 1, res + 1)
        check_plus[r + c] = 1
        check_minus[r - c] = 1
    search(now + 1, res)
    return


ans = 0
for foo in range(2):  # divide into two: black and white
    available = []
    check_plus = {i: 0 for i in range(0, 2 * n)}
    check_minus = {i: 0 for i in range(-n + 1, n)}
    for row in range(n):
        for col in range(n):
            if board[row][col] == 1 and (row + col) % 2 == foo:
                available.append((row, col))
                check_plus[row + col] = 1
                check_minus[row - col] = 1

    max_ans = min(sum(check_plus.values()), sum(check_minus.values()), 2 * (n - 1))
    best = 0

    search(0, 0)

    if best > max_ans:
        best = max_ans
    ans += best

print(ans)
