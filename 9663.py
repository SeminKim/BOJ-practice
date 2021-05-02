#https://www.acmicpc.net/problem/9663
import copy
import math

n = int(input())
empty_board = [0 for _ in range(n + 1)]
q = [[empty_board, 0]]  # 0 for step
cnt = 0


def check(board, step):
    for i in range(1, step):
        if abs(board[i] - board[step]) == (step - i): return False
    return True

while len(q) != 0:
    temp = q.pop()
    now_board = temp[0]
    step = temp[1]
    mid = math.ceil(n/2)

    if step == n:
        if now_board[1] < mid:
            cnt += 2
        elif n%2 == 0:
            cnt +=2
        else:
            cnt += 1
    else:
        step += 1
        if step == 1:
            for pos in range(1, mid + 1):
                now_board[step] = pos
                if check(now_board, step):
                    q.append([copy.deepcopy(now_board), step])
        else:
            for pos in range(1,n+1):
                if pos in now_board: continue
                now_board[step] = pos
                if check(now_board, step):
                    q.append([copy.deepcopy(now_board), step])

print(cnt)
