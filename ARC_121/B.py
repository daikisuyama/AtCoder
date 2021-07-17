n=int(input())
R,G,B=[],[],[]
for i in range(2*n):
    a,c=input().split()
    eval(c).append(int(a))
R.sort();G.sort();B.sort()
if len(R)%2==len(G)%2==len(B)%2:
    print(0)
    exit()
#R：偶数、G,B：奇数にする
#つまり、G,Bは1以上
if len(G)%2==0:
    R,G=G,R
if len(B)%2==0:
    R,B=B,R

#G,B,Rの長さ
lg,lb,lr=len(G),len(B),len(R)
#G,B間で不満最小を求める
#二分探索
from bisect import bisect_left,bisect_right
ans=10**18
for i in range(lb):
    ind1=bisect_left(G,B[i])
    ind2=bisect_right(G,B[i])-1
    if 0<=ind1<lg:
        ans=min(ans,abs(B[i]-G[ind1]))
    if 0<=ind2<lg:
        ans=min(ans,abs(B[i]-G[ind2]))
if lr==0:
    print(ans)
    exit()
#(R,G)、(R,B)間は？
xg,xb=[],[]
for i in range(lr):
    ind1=bisect_left(G,R[i])
    ind2=bisect_right(G,R[i])-1
    check=[]
    if 0<=ind1<lg:
        check.append(abs(R[i]-G[ind1]))
    if 0<=ind2<lg:
        check.append(abs(R[i]-G[ind2]))
    xg.append([i,min(check)])
    ind1=bisect_left(B,R[i])
    ind2=bisect_right(B,R[i])-1
    check=[]
    if 0<=ind1<lb:
        check.append(abs(R[i]-B[ind1]))
    if 0<=ind2<lb:
        check.append(abs(R[i]-B[ind2]))
    xb.append([i,min(check)])
xg.sort(key=lambda z:z[1])
xb.sort(key=lambda z:z[1])
if xg[0][0]!=xb[0][0]:
    print(min(ans,xg[0][1]+xb[0][1]))
else:
    if lg==1:
        print(min(ans,xg[0][1]+xb[1][1]))
    elif lb==1:
        print(min(ans,xg[1][1]+xb[0][1]))
    else:
        print(min(ans,xg[1][1]+xb[0][1],xg[0][1]+xb[1][1]))
