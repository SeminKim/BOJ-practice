# https://www.acmicpc.net/problem/12015
# LIS length in n*log(n).

from sys import stdin
import bisect

n = int(stdin.readline().strip())
seq = list(map(int, stdin.readline().split()))
foo = [seq[0]]

for i in range(1, n):
    if seq[i] > foo[-1]:
        foo.append(seq[i])
    elif seq[i] == foo[-1]:
        continue
    else:
        idx = bisect.bisect_left(foo, seq[i])
        foo[idx] = seq[i]

print(len(foo))
