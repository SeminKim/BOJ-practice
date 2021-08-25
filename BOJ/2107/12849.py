# https://www.acmicpc.net/problem/12849

from sys import stdin

n = int(stdin.readline().strip())
# '정보과학관', '전산관', '미래관', '신양관', '한경직기념관', '진리관', '형남공학관', '학생회관'
now = [1, 0, 0, 0, 0, 0, 0, 0]
DIV = 1_000_000_007


def move_once(board):
    temp = [0 for _ in range(8)]
    temp[0] = (board[1] + board[2]) % DIV
    temp[1] = (board[0] + board[2] + board[3]) % DIV
    temp[2] = (board[0] + board[1] + board[3] + board[4]) % DIV
    temp[3] = (board[1] + board[2] + board[4] + board[5]) % DIV
    temp[4] = (board[2] + board[3] + board[5] + board[6]) % DIV
    temp[5] = (board[3] + board[4] + board[7]) % DIV
    temp[6] = (board[4] + board[7]) % DIV
    temp[7] = (board[5] + board[6]) % DIV
    return temp


for i in range(n):
    now = move_once(now)

print(now[0])
