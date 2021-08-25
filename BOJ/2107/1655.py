# https://www.acmicpc.net/problem/1655

from sys import stdin
import heapq

n = int(stdin.readline().strip())
smaller = []
larger = []
med = int(stdin.readline().strip())
print(med)

for i in range(1, n):
    # print(smaller, med, larger)
    num = int(stdin.readline().strip())

    if num <= med:
        if len(smaller) < len(larger):
            heapq.heappush(smaller, -num)
            heapq.heappush(smaller, -med)
            med = -heapq.heappop(smaller)

        else:  # len(smaller) == len(larger):
            heapq.heappush(smaller, -num)
            heapq.heappush(larger, med)
            med = -heapq.heappop(smaller)

    else:
        if len(smaller) < len(larger):
            heapq.heappush(smaller, -med)
            heapq.heappush(larger, num)
            med = heapq.heappop(larger)

        else:  # len(smaller) == len(larger):
            heapq.heappush(larger, num)
    print(med)
