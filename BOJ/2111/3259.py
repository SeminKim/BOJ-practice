from sys import stdin

r = stdin.readline
n = int(r())
statements = [[list(map(int, r().split()))[1:], list(map(int, r().split()))[1:]] for _ in range(n)]


def test(flag):  # bit 1 indicates lie
    for man in range(n):
        lying = ((flag >> man) & 1)
        did_lie = False
        for case in range(2):
            for elem in statements[man][case]:
                if ((flag >> (elem - 1)) & 1) != case:
                    did_lie = True
        if lying != did_lie:
            return False
    return True


for bit in range(1 << n):
    if test(bit):
        for man in range(n):
            print('false' if (bit & 1 << man) else 'true')
        exit(0)
