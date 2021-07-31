from bisect import bisect_left
n,m=map(int,input().split())
a=list(set(list(map(int,input().split()))))
b=list(set(list(map(int,input().split()))))
n,m=len(a),len(b)
a.sort()
b.sort()
ans=10000000000000000
for i in range(n):
    x=bisect_left(b,a[i])
    if x==m:
        ans=min(ans,abs(a[i]-b[x-1]))
    elif x==0:
        ans=min(ans,abs(a[i]-b[x]))
    else:
        ans=min(ans,abs(a[i]-b[x]))
        ans=min(ans,abs(a[i]-b[x-1]))
print(ans)

