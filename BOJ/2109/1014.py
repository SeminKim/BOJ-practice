# https://www.acmicpc.net/problem/1014
# Bitmask DP

from sys import stdin

INF = 1000


def solve():
    n, m = map(int, stdin.readline().split())
    board = [stdin.readline().strip() for _ in range(n)]
    dp = [[-INF for _ in range(1 << m)] for _ in range(n)]

    def is_valid(bit_upper, bit_lower, rownum):  # assume bit_upper is already valid
        if '11' in bin(bit_lower):
            return False
        for i in range(m):
            if bit_lower & (1 << i):
                if board[rownum][i] == 'x':  # board check
                    return False
                if i > 0 and bit_upper & (1 << i - 1):  # upper left diagonal
                    return False
                if i < m - 1 and bit_upper & (1 << i + 1):  # upper right diagonal
                    return False
        return True

    # first line
    for bit in range(1 << m):
        if is_valid(0, bit, 0):
            dp[0][bit] = bin(bit).count('1')

    for row in range(1, n):
        for bit1 in range(1 << m):
            if dp[row - 1][bit1] < 0:
                continue
            for bit2 in range(1 << m):
                if is_valid(bit1, bit2, row):
                    dp[row][bit2] = max(dp[row][bit2], dp[row - 1][bit1] + bin(bit2).count('1'))

    print(max(dp[-1]))


t = int(stdin.readline())
while t > 0:
    solve()
    t -= 1
