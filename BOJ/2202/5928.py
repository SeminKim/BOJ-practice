d,h,m=map(int,input().split())
print(max((d-11)*1440+(h-11)*60+m-11,-1))