from sys import stdin

DIGITS = [str(i) for i in range(10)]


def solve():
    str_n, k = stdin.readline().split()
    n = int(str_n)
    k = int(k)
    L = len(str_n)

    best = '9' * L
    for i in range(9):
        foo = str(i) * L
        if foo >= str_n:
            best = min(best, foo)

    if k == '1' or n < 10:
        print(best)
        return

    remaining = k
    ans = []
    used = {str(i): 0 for i in range(10)}
    idx = 0
    ignore = False
    while idx < L:
        digit = str_n[idx]
        if ignore:
            if remaining > 0:
                ans.append('0')
                used['0'] += 1

            else:
                minimum = '9'
                for x in DIGITS:
                    if used[x] > 0:
                        minimum = min(minimum, x)
                ans.append(minimum)

        elif used[digit]:
            ans.append(digit)
            used[digit] += 1

        elif remaining >= 1:
            used[digit] = 1
            remaining -= 1
            ans.append(digit)

        # if remaining==0 and digit was not used before
        else:
            flag = True
            for i in used.keys():
                if used[i] and digit < i:
                    flag = False  # can keep going
                    ignore = True
                    ans.append(i)
                    break

            if flag:  # should backtrack
                while ans:
                    curr = ans.pop(-1)
                    idx -= 1
                    used[curr] -= 1

                    if used[curr] == 0:
                        ignore = True
                        foo = str(int(curr) + 1)
                        ans.append(foo)
                        used[foo] += 1
                        if used[foo] > 1:
                            remaining += 1
                        break

                    for j in DIGITS:
                        if used[j] and j > curr:
                            ans.append(j)
                            used[j] += 1
                            ignore = True
                            break

                    if ignore:
                        break

        idx += 1
    print(''.join(ans))


t = int(stdin.readline().strip())

for _ in range(t):
    solve()
