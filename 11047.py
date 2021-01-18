# https://www.acmicpc.net/problem/11047
n, k = map(int, input().split())
coins = []
for i in range(n):
    coins.append(int(input()))
total =0
while k > 0:
    mult = k // coins[-1]
    if mult > 0:
        total += mult
        k -= mult * coins[-1]
    else:
        del coins[-1]
print(total)