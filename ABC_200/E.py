n,k=map(int,input().split())

#和を決める
#now:そこまでで何個のケーキ
now=0
#m:和の値
for m in range(3,3*n+1):
    now+=((m-1)*(m-2)//2)
    if now<k:
        #もっと右にある場合
        pass
    else:
        #そこにある場合
        now-=((m-1)*(m-2)//2)
        break
#print(m)

#綺麗さを決める
#k2:和mの中で何番目か
k2=k-now
#print(k2)
#now2:そこまでで何個のケーキ
now2=0
#i:綺麗さ
for i in range(max(1,m-2*n),min(n,m-2)+1):
    #m_:おいしさ+人気度
    m_=m-i
    now2+=(m_-1)
    if now2<k2:
        pass
    else:
        now2-=(m_-1)
        break

#k3:和m-rの中で何番目か
k3=k2-now2
for j in range(1,n+1):
    if 1<=m-i-j<=n:
        k3-=1
    if k3==0:
        break

print(i,j,m-i-j)