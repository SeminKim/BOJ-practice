t = int(input())
for _ in range(t):
    s = int(input())
    n = int(input())
    for _ in range(n):
        a,b = map(int, input().split())
        s += a*b
    print(s)