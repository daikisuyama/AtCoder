ans=""
a,b,k=input().split()
k=int(k)
com=[[0]*61 for i in range(61)]
for i in range(61):
    tmp=1
    for j in range(i+1):
        if j!=0:
            tmp*=(i-j+1)
            tmp//=j
        com[i][j]=tmp
