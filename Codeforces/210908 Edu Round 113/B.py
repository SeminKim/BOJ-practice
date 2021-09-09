from sys import stdin


def solve():
    n = int(stdin.readline().strip())
    seq = stdin.readline().strip()
    type_1 = []
    type_2 = []
    for i in range(n):
        if seq[i] == '1':
            type_1.append(i)
        else:
            type_2.append(i)
    ans = [['=' for _ in range(n)] for _ in range(n)]
    for i in range(n):
        ans[i][i] = 'X'

    if len(type_2) > 2:
        for i in range(len(type_2) - 1):
            ans[type_2[i]][type_2[i + 1]] = '+'
            ans[type_2[i + 1]][type_2[i]] = '-'
        ans[type_2[-1]][type_2[0]] = '+'
        ans[type_2[0]][type_2[-1]] = '-'
        print('YES')
        for line in ans:
            print(''.join(line))

    elif len(type_2) == 0:
        print('YES')
        for line in ans:
            print(''.join(line))

    else:
        print('NO')


t = int(stdin.readline().strip())

for _ in range(t):
    solve()
