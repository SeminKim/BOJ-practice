# https://www.acmicpc.net/problem/2239
'''
from copy import deepcopy

class Board:
    def __init__(self, board=None):
        print('oh..')
        if board is None:
            self.board = [[[i for i in range(1, 10)] for _ in range(9)] for _ in range(9)]
        else:
            self.board = deepcopy(board)

    def update_row(self, row, col, num):
        for i in range(9):
            if i == col:
                continue
            if num in self.board[row][i]:
                self.board[row][i].remove(num)

    def update_col(self, row, col, num):
        for i in range(9):
            if i == row:
                continue
            if num in self.board[i][col]:
                self.board[i][col].remove(num)

    def update_block(self, row, col, num):
        for i in range(3):
            for j in range(3):
                pointer_1 = 3 * (row // 3) + i
                pointer_2 = 3 * (col // 3) + j
                if pointer_1 == row and pointer_2 == col:
                    continue
                if num in self.board[pointer_1][pointer_2]:
                    self.board[pointer_1][pointer_2].remove(num)

    def update(self, row, col, num):
        self.update_block(row, col, num)
        self.update_row(row, col, num)
        self.update_col(row, col, num)

    def assign(self, row, col, num):
        self.board[row][col] = [num]
        self.update(row, col, num)

    def solve(self):
        for row in range(9):
            for col in range(9):
                if len(self.board[row][col]) == 0:
                    return None
                elif len(self.board[row][col]) == 1:
                    continue
                else:
                    newboards = [Board(self.board) for _ in self.board[row][col]]
                    for foo in range(len(newboards)):
                        newboards[foo].assign(row, col, self.board[row][col][foo])
                        if newboards[foo].solve() is not None:
                            self.board = newboards[foo].board
                            return 1



    def print(self):
        for row in range(9):
            for col in range(9):
                print(self.board[row][col][0], end=' ')
            print()


my_board = Board()

for i in range(9):
    line = list(stdin.readline().strip())
    for j in range(9):
        if line[j] != '0':
            my_board.assign(i, j, int(line[j]))

my_board.solve()
my_board.print()
'''


from sys import stdin

board = [[]for _ in range(9)]
for i in range(9):
    board[i] = list(map(int,stdin.readline().strip()))



