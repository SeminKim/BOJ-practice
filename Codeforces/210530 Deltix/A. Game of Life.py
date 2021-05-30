from sys import stdin


def solve():
    n, m = map(int, stdin.readline().split())
    seq = stdin.readline().strip()
    m = min(n * 2, m)
    seq = list(seq)
    next = seq[:]

    for cnt in range(m):
        for idx in range(n):
            if idx == 0 and seq[1] == '1':
                next[idx] = '1'
            elif idx == n - 1 and seq[n - 2] == '1':
                next[idx] = '1'
            elif 0 < idx < n - 1 and seq[idx] == '0':
                if seq[idx - 1] == '1' or seq[idx + 1] == '1':
                    if not (seq[idx - 1] == '1' and seq[idx + 1] == '1'):
                        next[idx] = '1'
        seq = next[:]
    return ''.join(seq)


t = int(stdin.readline().strip())
for _ in range(t):
    print(solve())
