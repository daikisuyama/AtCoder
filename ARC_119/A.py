n=int(input())
ans=n+1
b=0
while 2**b<=n:
    a=n//(2**b)
    c=n-a*(2**b)
    ans=min(ans,a+b+c)
    b+=1
print(ans)
