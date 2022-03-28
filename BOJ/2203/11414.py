# https://www.acmicpc.net/problem/11414
# Combining Euclidean algorithm with the fact LCM = Prod / GCD.

from itertools import product
from sys import stdin

sieve = [True for _ in range(4 * 10 ** 4)]
primes = [2]
for even in range(4, 4 * 10 ** 4, 2):
    sieve[even] = False
for num in range(3, 4 * 10 ** 4, 2):
    if sieve[num]:
        primes.append(num)
        for foo in range(2 * num, 4 * 10 ** 4, num):
            sieve[foo] = False

a, b = map(int, stdin.readline().split())
if a < b:
    a, b = b, a
target = a - b
if target == 0:
    print(1)
    exit(0)

# factorize
factors = []
for prime in primes:
    if target % prime == 0:
        temp = [1]
        while target % prime == 0:
            temp.append(temp[-1] * prime)
            target //= prime
        factors.append(temp)
if target != 0:
    factors.append([1, target])

best = float('inf')
ans = -1
for case in product(*factors):
    target_gcd = 1
    for num in case:
        target_gcd *= num
    # B+N should be divisible by target_gcd, n >= 1
    n = (target_gcd - b % target_gcd)
    ret = (a * b + (a + b) * n + n * n) // target_gcd
    if ret < best:
        ans = n
        best = ret
    elif ret == best:
        ans = min(ans, n)

print(ans)
