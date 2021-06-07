from sys import stdin

letters = ' '.join('abcdefghijklmnopqrstuvwxyz').split()


def solve():
    n = int(stdin.readline().strip())
    seq = stdin.readline().strip()
    for case in letters:
        if case not in seq:
            return case

    for case1 in letters:
        for case2 in letters:
            case = case1+case2
            if case not in seq:
                return case

    for case1 in letters:
        for case2 in letters:
            for case3 in letters:
                case = case1+case2+case3
                if case not in seq:
                    return case


t = int(stdin.readline().strip())

for _ in range(t):
    print(solve())
