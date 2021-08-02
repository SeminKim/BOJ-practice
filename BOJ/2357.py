# https://www.acmicpc.net/problem/2357
# sqrt root decomposition


from sys import stdin

n, m = map(int, stdin.readline().split())
div_size = int(n ** 0.5)
div_num = n // div_size + 1
minimum = [10 ** 9 for _ in range(div_num)]
maximum = [0 for _ in range(div_num)]

seq = []
for i in range(n):
    foo = int(stdin.readline().strip())
    seq.append(foo)
    minimum[i // div_size] = min(minimum[i // div_size], foo)
    maximum[i // div_size] = max(maximum[i // div_size], foo)

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    a -= 1
    b -= 1
    first = a // div_size + 1
    second = b // div_size
    if first < second:
        foo = min(min(seq[a:first * div_size]), min(minimum[first:second]), min(seq[second * div_size:b + 1]))
        bar = max(max(seq[a:first * div_size]), max(maximum[first:second]), max(seq[second * div_size:b + 1]))
    else:
        foo = min(seq[a:b + 1])
        bar = max(seq[a:b + 1])

    print(foo, bar)
