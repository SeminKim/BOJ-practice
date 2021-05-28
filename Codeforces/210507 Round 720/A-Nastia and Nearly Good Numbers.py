n = int(input())

for _ in range(n):
    a, b = map(int,input().split())
    if b == 1: print("NO")
    else:
        print("YES")
        print(a*(2*b-1), a*(2*b+1), a*b*4)
