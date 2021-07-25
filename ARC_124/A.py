# 21:50~22:00
mod=998244353
n,k=map(int,input().split())
ok=set()
# rかl
check=[0]*n
now= 0
for i in range(k):
    c,_k=input().split()
    _k=int(_k)
    ok.add(_k)
    check[_k-1]=1 if c=="R" else -1
    if c=="R":
        now+=1
if len(ok)!=k:
    print(0)
    exit()
ans=1
for i in range(n):
    if check[i]==1:
        now-=1
    elif check[i]==-1:
        now+=1
    else:
        ans*=now
        ans%=mod
print(ans)
