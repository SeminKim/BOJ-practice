import math
from sys import stdin

t = int(stdin.readline().strip())

for _ in range(t):
    k = int(stdin.readline().strip())
    if k == 100 or k == 0:
        print(1)
        continue
    foo = math.gcd(k, 100 - k)
    print(k // foo + (100 - k) // foo)
