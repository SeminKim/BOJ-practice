from sys import stdin


def sieve(limit):
    primes = [2]
    for num in range(3, limit + 1):
        cnt = 0
        isprime = True
        while cnt < len(primes):
            if num % primes[cnt] == 0:
                isprime = False
                break
            else:
                cnt += 1
        if isprime:
            primes.append(num)
    return primes


primes = sieve(32000)


def count_prime_factors(num):
    i = 0
    ans = 0
    while primes[i] <= num:
        if num % primes[i] == 0:
            ans += 1
            num = num // primes[i]
        else:
            i += 1
        if i == len(primes):
            ans += 1
            break
    return ans


t = int(stdin.readline().strip())

for _ in range(t):
    a, b, k = map(int, stdin.readline().split())
    if a > b:
        a, b = b, a
    foo = count_prime_factors(a) + count_prime_factors(b)
    if k == 1:
        if a == b:
            print("NO")
        elif b % a == 0:
            print("YES")
        else:
            print("NO")
    else:
        if k > foo:
            print("NO")
        else:
            print("YES")
