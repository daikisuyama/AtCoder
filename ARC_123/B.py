n=int(input())
a,b,c=[sorted(list(map(int,input().split()))) for i in range(3)]
check=[-1]*n
# aとb
i,j=0,0
while True:
    if a[i]<b[j]:
        check[i]=b[j]
        i+=1
        j+=1
    else:
        j+=1
    if j==n:
        break
# checkとc
i,j=0,0
while True:
    if check[i]==-1:
        break
    elif check[i]<c[j]:
        check[i]=c[j]
        i+=1
        j+=1
    else:
        j+=1
    if j==n:
        break
print(i)