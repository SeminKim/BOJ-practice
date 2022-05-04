# Not solved yet..

import string
from itertools import permutations
from sys import stdin


def determine(first: str, second: str):
    temp = first + second
    last_idx = {x: -2 for x in string.ascii_uppercase}
    for i in range(len(temp)):
        if last_idx[temp[i]] == -2 or last_idx[temp[i]] == i - 1:
            last_idx[temp[i]] = i
        else:
            return False
    return True


def solve():
    N = int(stdin.readline().strip())
    words = list(stdin.readline().split())
    for case in permutations(words):
        temp = ''.join(case)
        if determine(temp, ''):
            return temp
    return 'IMPOSSIBLE'


T = int(stdin.readline().strip())
for t in range(T):
    print(f'Case #{t + 1}: {solve()}')
