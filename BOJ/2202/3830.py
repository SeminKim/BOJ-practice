# https://www.acmicpc.net/problem/3830
# Disjoint Set

from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 5)


def union(fst, snd, delta):
    fst_head, _ = find_head(fst)
    snd_head, _ = find_head(snd)
    head[snd_head] = fst_head
    offset[snd_head] = offset[fst] - offset[snd] + delta


# find head and update offset
def find_head(num):
    if head[num] != num:
        head[num], val = find_head(head[num])
        offset[num] += val

    return head[num], offset[num]


while True:
    N, M = map(int, stdin.readline().split())
    if N == 0:
        break
    # initialize
    head = [i for i in range(N + 1)]
    offset = [0 for _ in range(N + 1)]
    # query
    for _ in range(M):
        query = stdin.readline().split()
        if query[0] == '!':
            a, b, w = map(int, query[1:])
            union(a, b, w)
        else:
            a, b = map(int, query[1:])
            if find_head(a)[0] == find_head(b)[0]:
                print(offset[b] - offset[a])
            else:
                print('UNKNOWN')
