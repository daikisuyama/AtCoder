n=int(input())
def func():
    ans=[0]*n
    y=list(map(int,input().split()))
    for i in range(n):
        ans[y[i]-1]+=1
    return ans
a=func()
b,c=[list(map(int,input().split())) for i in range(2)]
o=0
for i in range(n):
    o+=(a[b[c[i]-1]-1])
print(o)
