# https://www.acmicpc.net/problem/2243
# Sqrt decomposition


from sys import stdin

n = int(stdin.readline().strip())
candy = [0 for _ in range(1_000_000)]
num_in_bucket = [0 for _ in range(1000)]


def get_nth(n):
    temp = 0
    idx = 0
    while temp < n:
        temp += num_in_bucket[idx]
        idx += 1
    idx -= 1
    temp -= num_in_bucket[idx]
    num_in_bucket[idx] -= 1
    idx *= 1000
    while temp < n:
        temp += candy[idx]
        idx += 1
    idx -= 1
    candy[idx] -= 1
    return idx + 1


for _ in range(n):
    seq = list(map(int, input().split()))
    if seq[0] == 1:
        print(get_nth(seq[1]))
    else:
        f = seq[1] - 1
        candy[f] += seq[2]
        num_in_bucket[f // 1000] += seq[2]
