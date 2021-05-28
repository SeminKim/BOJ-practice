# https://www.acmicpc.net/problem/11444
# F(n) = F(k+1)F(n-k) + F(k)F(n-k-1)
# F(2n) = (2F(n-1) + F(n)) * F(n)
# F(2n-1) = F(n)^2 + F(n-1)^2


from sys import setrecursionlimit

setrecursionlimit(10 ** 8)
mod = 1000000007
memo = {0: 0, 1: 1}


def fibo(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    if num == 2:
        return 1
    if num in memo.keys():
        return memo[num]

    half = num // 2
    # if num is even
    if num % 2 == 0:
        foo = ((2 * fibo(half - 1) + fibo(half)) % mod * fibo(half)) % mod
    # if num is odd
    else:
        foo = (pow(fibo(half), 2, mod) + pow(fibo(half + 1), 2, mod)) % mod

    memo[num] = foo
    return foo


n = int(input())
print(fibo(n))
