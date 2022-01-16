from sys import stdin


def solve():
    n, m, r, c = map(int, stdin.readline().split())
    board = [stdin.readline().strip() for _ in range(n)]
    if board[r - 1][c - 1] == 'B':
        print(0)
        return
    for i in range(m):
        if board[r - 1][i] == 'B':
            print(1)
            return
    for i in range(n):
        if board[i][c - 1] == 'B':
            print(1)
            return

    for foo in board:
        if 'B' in foo:
            print(2)
            return
    print(-1)
    return


t = int(stdin.readline().strip())

for _ in range(t):
    solve()
