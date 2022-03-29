from sys import stdin


def solve():
    N = int(stdin.readline().strip())
    seq = [list(map(int, stdin.readline().split())) for _ in range(N)]
    ans = []
    for bit in range(1 << N):
        success = True
        for i in range(N):
            for j in range(i + 1, N):
                if ((1 << i) & bit and (1 << j) & bit) or (not (1 << i) & bit and not (1 << j) & bit):
                    s1, e1 = seq[i]
                    s2, e2 = seq[j]
                    if s1 <= s2 < e1 or s1 < e2 <= e1 or s2 <= s1 < e2 or s2 < e1 <= e2:
                        success = False
                        break
        if success:
            for digit in range(N):
                if (1 << digit) & bit:
                    ans.append('C')
                else:
                    ans.append('J')
            return ans
    else:
        return 'IMPOSSIBLE'


T = int(stdin.readline().strip())
for t in range(T):
    print(f'Case #{t + 1}:', "".join(solve()))
