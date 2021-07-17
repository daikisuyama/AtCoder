from itertools import accumulate
n=int(input())
a=list(map(int,input().split()))
b=list(accumulate(a))
ans=list(accumulate(b))
now=a[0]
for i in range(n):
    now=max(now,a[i])
    ans[i]+=(now*(i+1))
for i in range(n):
    print(ans[i])