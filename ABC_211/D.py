from collections import deque
mod=10**9+7
n,m=map(int,input().split())
path=[[] for i in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    path[a-1].append(b-1)
    path[b-1].append(a-1)
# 初めは0に、n-1へ行く
now=deque([0])
# それぞれの都市への経路数
co=[0]*n
co[0]=1
while len(now)>0:
    co_sub=[]
    nex_sub=set()
    for i in range(len(now)):
        p=now.popleft()
        for nex in path[p]:
            if co[nex]==0:
                co_sub.append([nex,co[p]])
                nex_sub.add(nex)
    for i in co_sub:
        co[i[0]]+=i[1]
        co[i[0]]%=mod
    for i in nex_sub:
        now.append(i)
print(co[n-1])
