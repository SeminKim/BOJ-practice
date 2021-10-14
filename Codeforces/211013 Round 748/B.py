from sys import stdin


def solve():
    n = int(stdin.readline().strip())
    str_n = str(n)
    m = len(str_n)
    res = []
    # case 1 : 00
    first = str_n.rfind('0')
    second = str_n[:first].rfind('0')
    if first != -1 and second != -1:
        res.append(m - second - 2)

    # case 2: 25
    first = str_n.rfind('5')
    second = str_n[:first].rfind('2')
    if first != -1 and second != -1:
        res.append(m - second - 2)

    # case 3: 50
    first = str_n.rfind('0')
    second = str_n[:first].rfind('5')
    if first != -1 and second != -1:
        res.append(m - second - 2)

    # case 4: 75
    first = str_n.rfind('5')
    second = str_n[:first].rfind('7')
    if first != -1 and second != -1:
        res.append(m - second - 2)

    print(min(res))


t = int(stdin.readline().strip())

for _ in range(t):
    solve()
