from sys import stdin

T = int(stdin.readline().strip())
for t in range(T):
    seq = list(map(int, stdin.readline().strip()))
    level = 0
    i = 0
    ans = []
    while i < len(seq):
        diff = seq[i] - level
        if diff > 0:
            ans.append('('*diff)
            level = seq[i]
        elif diff < 0:
            ans.append(')'*(-diff))
            level = seq[i]
        ans.append(seq[i])
        i += 1
    if level:
        ans.append(')'*level)
    print(f'Case #{t+1}:', "".join(map(str,ans)))
