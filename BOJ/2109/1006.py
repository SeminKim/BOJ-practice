# https://www.acmicpc.net/problem/1006
# DP, 3 cases for starting/ 3 cases for ending

from sys import stdin


def solve():
    n, w = map(int, stdin.readline().split())
    board = [list(map(int, stdin.readline().split())) for _ in range(2)]

    def calculate(table):
        for i in range(1, n):
            # case 0
            table[0][i] = table[2][i - 1] + 1
            if board[0][i - 1] + board[0][i] <= w:
                table[0][i] = min(table[0][i], table[1][i - 1] + 1)
            # case 1
            table[1][i] = table[2][i - 1] + 1
            if board[1][i - 1] + board[1][i] <= w:
                table[1][i] = min(table[1][i], table[0][i - 1] + 1)
            # case 2
            table[2][i] = table[2][i - 1] + 2
            if board[0][i] + board[1][i] <= w:
                table[2][i] = table[2][i - 1] + 1
            table[2][i] = min(table[2][i], table[0][i] + 1, table[1][i] + 1)
            if i < 2:
                table[2][i] = min(table[2][i],
                                  4 - (board[0][i - 1] + board[0][i] <= w)
                                  - (board[1][i - 1] + board[1][i] <= w))
            else:
                table[2][i] = min(table[2][i], table[2][i - 2] + 4
                                  - (board[0][i - 1] + board[0][i] <= w)
                                  - (board[1][i - 1] + board[1][i] <= w))
        return table

    ans = 2 * n
    # dp = [[3*n for _ in range(n)] for _ in range(3)]
    # dp[0][i] : fill both lines' 0..i-1 and fill first line's i
    # dp[1][i] : fill both lines' 0..i-1 and fill second line's i
    # dp[2][i] : fill both lines' 0..i

    # starting with no connection
    dp = [[3 * n for _ in range(n)] for _ in range(3)]
    dp[0][0] = 1
    dp[1][0] = 1
    dp[2][0] = 2
    ans = min(ans, calculate(dp)[2][n - 1])
    # print(dp)
    # print(ans, 0)

    # starting with vertical connection (1 and n+1)
    if board[0][0] + board[1][0] <= w:
        dp = [[3 * n for _ in range(n)] for _ in range(3)]
        dp[0][0] = 1
        dp[1][0] = 1
        dp[2][0] = 0
        ans = min(ans, calculate(dp)[2][n - 1] + 1)
        # print(ans, 1)

    # starting with upper horizontal connection (1 and n)
    if board[0][0] + board[0][-1] <= w:
        dp = [[3 * n for _ in range(n)] for _ in range(3)]
        dp[0][0] = 0
        dp[1][0] = 1
        dp[2][0] = 1
        ans = min(ans, calculate(dp)[1][n - 1] + 1)
        # print(ans, 2)

    # starting with lower horizontal connection (n+1 and 2n)
    if board[1][0] + board[1][-1] <= w:
        dp = [[3 * n for _ in range(n)] for _ in range(3)]
        dp[0][0] = 1
        dp[1][0] = 0
        dp[2][0] = 1
        ans = min(ans, calculate(dp)[0][n - 1] + 1)
        # print(ans, 3)

    # starting with both horizontal connection(1 and n, n+1 and 2n)
    if board[0][0] + board[0][-1] <= w and board[1][0] + board[1][-1] <= w:
        dp = [[3 * n for _ in range(n)] for _ in range(3)]
        dp[0][0] = 0
        dp[1][0] = 0
        dp[2][0] = 0
        ans = min(ans, calculate(dp)[2][n - 2] + 2)

    print(ans)


t = int(stdin.readline())
for _ in range(t):
    solve()
