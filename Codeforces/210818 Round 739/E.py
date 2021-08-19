from sys import stdin


def solve():
    seq = stdin.readline().strip()
    n = len(seq)
    count = {}
    order = []
    for letter in reversed(seq):
        if letter not in count.keys():
            count[letter] = 1
            order.append(letter)
        else:
            count[letter] += 1
    order.reverse()
    multiplier = {order[i]: i + 1 for i in range(len(order))}
    # print(count)

    idx = 0
    while idx < n:
        count[seq[idx]] -= multiplier[seq[idx]]
        flag = True
        for val in count.values():
            if val != 0:
                flag = False
                break

        if flag:
            s = seq[:idx + 1]
            t = s
            order = ''.join(order)
            for letter in order:
                s = s.replace(letter, '')
                t += s
            if t == seq:
                print(seq[:idx + 1], order)
                return

            else:
                print(-1)
                return

        idx += 1

    print(-1)
    return


t = int(stdin.readline().strip())

for _ in range(t):
    solve()
