# https://www.acmicpc.net/problem/11286

from sys import stdin
import heapq

n = int(stdin.readline().strip())
positive = []
negative = []

for _ in range(n):
    num = int(stdin.readline().strip())
    if num > 0:
        heapq.heappush(positive, num)
    elif num < 0:
        heapq.heappush(negative, -num)
    else:
        if len(positive) == len(negative) == 0:
            print(0)

        elif len(positive) == 0:
            print(-heapq.heappop(negative))

        elif len(negative) == 0:
            print(heapq.heappop(positive))

        else:
            foo = heapq.heappop(positive)
            bar = heapq.heappop(negative)

            if foo >= bar:
                print(-bar)
                heapq.heappush(positive, foo)
            else:
                print(foo)
                heapq.heappush(negative, bar)
