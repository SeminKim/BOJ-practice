import math

def getRelPrime(val):
    if math.gcd(val,2) == 1: return 2
    p = 3
    while True:
        if math.gcd(val,p) == 1: return p
        else: p += 2

t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    minval = min(array)
    minidx = array.index(minval)
    p = getRelPrime(minval)
    print(n-1)
    for i in range(n):
        if i == minidx: continue
        elif (minidx - i) %2 == 0:
            print(i+1, minidx+1, minval, minval)
        else:
            print(i+1, minidx+1, minval+p, minval)