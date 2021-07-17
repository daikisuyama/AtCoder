n=int(input())
a=list(map(int,input().split()))
b=[abs(a[i]-a[i+1]) for i in range(n-1)]
s=sum(b)
