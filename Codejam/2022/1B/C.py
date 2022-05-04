# Not solved yet..

from itertools import combinations
from random import randint
from sys import stdin, stdout


def io(sth):
    print(sth)
    stdout.flush()
    ret = int(stdin.readline().strip())
    if ret == -1:
        exit(0)
    return ret


def xor_ret(first, second):
    ret = int(first, 2) ^ int(second, 2)
    return bin(ret).count('1')


def solve():
    n = io('0' * 8)
    if n % 2 == 1:
        n = io('10010010')
    if n == 0:
        return
    if n > 4:
        n = io('11111111')

    if n == 0:
        return
    # now number of 1 is 2  or 4.
    if n == 2:
        pool = list(i for i in combinations(range(8), 2))
        while True:
            indices = pool[randint(0, len(pool) - 1)]
            base = [0] * 8
            for index in indices:
                base[index] = 1
            n = io(''.join(map(str, base)))
            if n == 0:
                return
            if n == 4:
                break


    pool = list(i for i in combinations(range(8), 4))
    temp = []
    for indices in pool:
        base = [0] * 8
        for index in indices:
            base[index] = 1
        temp.append(''.join(map(str, base)))
    possible = set(temp)

    while True:
        indices = pool[randint(0, len(pool) - 1)]
        base = [0] * 8
        for index in indices:
            base[index] = 1
        n = io(''.join(map(str, base)))
        new_possible = set()
        for each in possible:
            if xor_ret(each,''.join(map(str, base))) == n:
                new_possible.add(each)
        possible = new_possible

        if n == 0:
            return
        if n == 8:
            n = io('1' * 8)
            return

        else:
            for indices in combinations(range(8), 2):
                base = [0] * 8
                for index in indices:
                    base[index] = 1
                n = io(''.join(map(str, base)))
                if n == 0:
                    return
                if n == 8:
                    n = io('1' * 8)
                    return
                if n == 4:
                    break


T = int(stdin.readline().strip())
for t in range(T):
    solve()
