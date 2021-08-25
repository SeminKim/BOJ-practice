# https://www.acmicpc.net/problem/11689
# Find prime(sieve) -> Prime Factorization of n -> Multiplication Rule
# But, actually prime checking is unnecessary!

from sys import stdin

n = int(stdin.readline().strip())
if n == 1:
    print(1)
    exit()

sqrt_n = int(n ** 0.5) + 2
factors = []

# Find Prime Factorization

num = n
if num % 2 == 0:
    factors.append(2)
    while num % 2 == 0:
        num //= 2

factor = 3
while factor < int(num ** 0.5) + 1:
    if num % factor == 0:
        factors.append(factor)
        while num % factor == 0:
            num //= factor
    factor += 2

if num == n:  # when n is prime
    print(n - 1)
    exit()

if num != 1:
    factors.append(num)

# Euler phi function multiplication rule
ans = n
for f in factors:
    ans //= f
    ans *= (f - 1)

print(ans)
