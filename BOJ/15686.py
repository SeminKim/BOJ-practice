# https://www.acmicpc.net/problem/15686
# Brute force, 각 치킨집과 집의 거리를 dist_table에 저장해서 다시 사용

from sys import stdin
from itertools import combinations

n, m = map(int, stdin.readline().split())
one_list = []
two_list = []
city = []


def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


for row in range(n):
    city.append(list(map(int, stdin.readline().split())))

for row in range(n):
    for col in range(n):
        if city[row][col] == 1:
            one_list.append([row, col])
        if city[row][col] == 2:
            two_list.append([row, col])

num_house = len(one_list)
num_chicken = len(two_list)
MAX_DIST = 2 * n
dist_table = [[MAX_DIST for _ in range(num_house)] for _ in range(num_chicken)]

for row in range(num_chicken):
    for col in range(num_house):
        dist_table[row][col] = distance(two_list[row], one_list[col])

ans = MAX_DIST * num_house
for selected_chicken in combinations(range(num_chicken), m):
    cost = 0
    for house_idx in range(num_house):
        nearest = MAX_DIST
        for chicken_idx in selected_chicken:
            nearest = min(nearest, dist_table[chicken_idx][house_idx])
        cost += nearest
    ans = min(ans, cost)

print(ans)
