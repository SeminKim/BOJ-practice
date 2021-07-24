from sys import stdin

ALPHA = 'abcde'


# {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0}

def solve():
    n = int(stdin.readline().strip())
    profit = {i: [] for i in ALPHA}

    for i in range(n):
        seq = stdin.readline().strip()

        for character in ALPHA:
            profit[character].append(2 * seq.count(character) - len(seq))

    best = 0
    for character in ALPHA:
        profit[character].sort(reverse=True)
        res = 0
        cnt = 0
        for num in profit[character]:
            res += num
            if res <= 0:
                break
            cnt += 1

        best = max(best, cnt)
    print(best)


t = int(stdin.readline().strip())

for _ in range(t):
    solve()
