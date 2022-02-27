n=int(input())
print(['Junhee is not cute!','Junhee is cute!'][sum(int(input()) for _ in range(n))>n//2])