# https://www.acmicpc.net/problem/11689
# Find prime(sieve) -> Prime Factorization of n -> Inclusion-Exclusion
# 2*3*...*43 > 10**6, so calculating with power-set of maximum 14 elements => No TLE!.


from sys import stdin

n = int(stdin.readline().strip())
if n == 1:
    print(1)
    exit()

sqrt_n = int(n ** 0.5) + 2
factors = []
is_prime = [True for _ in range(sqrt_n)]

# Find Primes + Factorization

num = n
if is_prime[2]:
    if num % 2 == 0:
        factors.append(2)
        while num % 2 == 0:
            num //= 2
    for foo in range(2, int(num ** 0.5) + 1, 2):
        is_prime[foo] = False

factor = 3
while factor < int(num ** 0.5) + 1:
    if is_prime[factor]:
        if num % factor == 0:
            factors.append(factor)
            while num % factor == 0:
                num //= factor
        for foo in range(factor, int(num ** 0.5) + 1, factor):
            is_prime[foo] = False
    factor += 2

if num == n:  # when n is prime
    print(n - 1)
    exit()

if num != 1:
    factors.append(num)

# Inclusion-Exclusion
# ans = n
# flag = -1
# for i in range(1, len(factors) + 1):
#     for selection in combinations(factors, i):
#         foo = 1
#         for bar in selection:
#             foo *= bar
#         ans += flag * (n // foo)
#     flag *= -1

# Better approach ? ? ?
ans = n
for f in factors:
    ans //= f
    ans *= (f - 1)

print(ans)
