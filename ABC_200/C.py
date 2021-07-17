n=int(input())
check=[0]*200
a=list(map(int,input().split()))
for i in range(n):
    check[a[i]%200]+=1
ans=0
for i in range(200):
    ans+=(check[i]*check[i]-check[i])//2
print(ans)