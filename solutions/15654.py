# https://www.acmicpc.net/problem/15654

from itertools import permutations

_, m = map(int, input().split())
nums = list(map(int,input().split()))
nums.sort()


for pair in permutations(nums, m):
    for num in pair:
        print(num, end=' ')
    print()
