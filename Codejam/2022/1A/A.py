from sys import stdin

T = int(stdin.readline().strip())
INF = 10 ** 6
for t in range(T):
    seq = stdin.readline().strip()
    pos = 0
    count = 1
    ans = []
    while pos < len(seq) - 1:
        if seq[pos] < seq[pos + 1]:
            ans.append(seq[pos] * 2 * count)
            count = 1
        elif seq[pos] == seq[pos + 1]:
            count += 1
        else:
            ans.append(seq[pos] * count)
            count = 1
        pos += 1
    ans.append(seq[-1] * count)
    print(f'Case #{t + 1}: {"".join(ans)}')
