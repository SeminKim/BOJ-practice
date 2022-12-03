# https://www.acmicpc.net/problem/7662
# Use two priority queues and do lazy deletion to synchronize them.

import heapq
from collections import defaultdict
from sys import stdin


def solve():
    n = int(stdin.readline().strip())
    inst = [stdin.readline().split() for _ in range(n)]
    # Check if the result is empty
    cnt = 0
    cache = 0
    for i, each in enumerate(inst):
        if each[0] == 'I':
            cnt += 1
        elif each[0] == 'D' and cnt > 0:
            cnt -= 1
        if cnt == 0:
            cache = i
    if cnt == 0:
        print('EMPTY')
        return
    inst = inst[cache:]

    # Now use two priority queues, min heap and max heap.
    # When instruction D is given, save it in buffer and apply later for the other queue.
    min_q = []
    max_q = []
    min_buf = defaultdict(int)
    max_buf = defaultdict(int)
    for each in inst:
        target = int(each[1])
        if each[0] == 'I':
            heapq.heappush(min_q, target)
            heapq.heappush(max_q, -target)  # change sign to use max heap
        elif target == -1:  # Delete minimum
            while min_q:
                candidate = heapq.heappop(min_q)
                if min_buf[candidate] > 0:
                    min_buf[candidate] -= 1
                else:
                    # found valid minimum, add to max_q's buffer.
                    max_buf[candidate] += 1
                    break
        else:  # Delete maximum
            while max_q:
                candidate = -heapq.heappop(max_q)
                if max_buf[candidate] > 0:
                    max_buf[candidate] -= 1
                else:
                    min_buf[candidate] += 1
                    break

    # delete invalid number and print
    ret_min = ret_max = 0
    while min_q:
        candidate = heapq.heappop(min_q)
        if min_buf[candidate] > 0:
            min_buf[candidate] -= 1
        else:
            ret_min = candidate
            break

    while max_q:
        candidate = -heapq.heappop(max_q)
        if max_buf[candidate] > 0:
            max_buf[candidate] -= 1
        else:
            ret_max = candidate
            break

    print(ret_max, ret_min)
    return


t = int(stdin.readline().strip())
for _ in range(t):
    solve()
