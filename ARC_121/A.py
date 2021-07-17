n=int(input())
point=[[i,list(map(int,input().split()))] for i in range(n)]
if n==3:
    cand=[]
    for i in range(n):
        for j in range(i+1,n):
            cand.append(max(abs(point[i][1][0]-point[j][1][0]),abs(point[i][1][1]-point[j][1][1])))
    cand.sort(reverse=True)
    print(cand[1])
    exit()
x=sorted(point,key=lambda z:z[1][0])
y=sorted(point,key=lambda z:z[1][1])
#print(x)
#print(y)
cand=[]
check=set()
for i in range(0,2):
    for j in range(n-2,n):
        a,b=x[i][0],x[j][0]
        cand.append(max(abs(point[a][1][0]-point[b][1][0]),abs(point[a][1][1]-point[b][1][1])))
        s=sorted([x[i][0],x[j][0]])
        t=s[0]*n+s[1]
        check.add(t)
for i in range(0,2):
    for j in range(n-2,n):
        a,b=y[i][0],y[j][0]
        s=sorted([y[i][0],y[j][0]])
        t=s[0]*n+s[1]
        if t not in check:
            cand.append(max(abs(point[a][1][0]-point[b][1][0]),abs(point[a][1][1]-point[b][1][1])))
            check.add(t)
#print(cand)
cand.sort(reverse=True)
print(cand[1])
