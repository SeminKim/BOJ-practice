# https://www.acmicpc.net/problem/5373
# Naive implementation

from collections import deque
from sys import stdin


def rotate(face):  # rotate a single face in CCW
    return [face[2], face[5], face[8], face[1], face[4], face[7], face[0], face[3], face[6]]


def solve():
    _ = stdin.readline()
    seq = deque(stdin.readline().split())
    faces = {x: [y] * 9 for x, y in zip('UDFBLR', 'wyrogb')}

    while seq:
        inst = seq.popleft()
        if inst[1] == '+':
            seq.appendleft(inst[0] + '-')
            seq.appendleft(inst[0] + '-')
            seq.appendleft(inst[0] + '-')
        else:
            faces[inst[0]] = rotate(faces[inst[0]])
            if inst[0] == 'U':
                faces['L'][2], faces['L'][5], faces['L'][8], \
                faces['B'][6], faces['B'][7], faces['B'][8], \
                faces['R'][0], faces['R'][3], faces['R'][6], \
                faces['F'][0], faces['F'][1], faces['F'][2] = faces['B'][8], faces['B'][7], faces['B'][6], \
                                                              faces['R'][0], faces['R'][3], faces['R'][6], \
                                                              faces['F'][2], faces['F'][1], faces['F'][0], \
                                                              faces['L'][2], faces['L'][5], faces['L'][8]
            if inst[0] == 'D':
                faces['L'][6], faces['L'][3], faces['L'][0], \
                faces['B'][0], faces['B'][1], faces['B'][2], \
                faces['R'][2], faces['R'][5], faces['R'][8], \
                faces['F'][8], faces['F'][7], faces['F'][6] = faces['F'][8], faces['F'][7], faces['F'][6], \
                                                              faces['L'][6], faces['L'][3], faces['L'][0], \
                                                              faces['B'][0], faces['B'][1], faces['B'][2], \
                                                              faces['R'][2], faces['R'][5], faces['R'][8]
            if inst[0] == 'F':
                faces['L'][8], faces['L'][7], faces['L'][6], \
                faces['D'][0], faces['D'][1], faces['D'][2], \
                faces['R'][8], faces['R'][7], faces['R'][6], \
                faces['U'][8], faces['U'][7], faces['U'][6] = faces['U'][8], faces['U'][7], faces['U'][6], \
                                                              faces['L'][8], faces['L'][7], faces['L'][6], \
                                                              faces['D'][0], faces['D'][1], faces['D'][2], \
                                                              faces['R'][8], faces['R'][7], faces['R'][6]

            if inst[0] == 'B':
                faces['L'][0], faces['L'][1], faces['L'][2], \
                faces['U'][0], faces['U'][1], faces['U'][2], \
                faces['R'][0], faces['R'][1], faces['R'][2], \
                faces['D'][8], faces['D'][7], faces['D'][6] = faces['D'][8], faces['D'][7], faces['D'][6], \
                                                              faces['L'][0], faces['L'][1], faces['L'][2], \
                                                              faces['U'][0], faces['U'][1], faces['U'][2], \
                                                              faces['R'][0], faces['R'][1], faces['R'][2]
            if inst[0] == 'L':
                faces['B'][0], faces['B'][3], faces['B'][6], \
                faces['U'][0], faces['U'][3], faces['U'][6], \
                faces['F'][0], faces['F'][3], faces['F'][6], \
                faces['D'][0], faces['D'][3], faces['D'][6] = faces['U'][0], faces['U'][3], faces['U'][6], \
                                                              faces['F'][0], faces['F'][3], faces['F'][6], \
                                                              faces['D'][0], faces['D'][3], faces['D'][6], \
                                                              faces['B'][0], faces['B'][3], faces['B'][6]
            if inst[0] == 'R':
                faces['B'][2], faces['B'][5], faces['B'][8], \
                faces['U'][2], faces['U'][5], faces['U'][8], \
                faces['F'][2], faces['F'][5], faces['F'][8], \
                faces['D'][2], faces['D'][5], faces['D'][8] = faces['D'][2], faces['D'][5], faces['D'][8], \
                                                              faces['B'][2], faces['B'][5], faces['B'][8], \
                                                              faces['U'][2], faces['U'][5], faces['U'][8], \
                                                              faces['F'][2], faces['F'][5], faces['F'][8]
    print("%s%s%s\n%s%s%s\n%s%s%s" % tuple(faces['U']))
    return


t = int(stdin.readline().strip())
for _ in range(t):
    solve()
