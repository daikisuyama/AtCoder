from collections import deque
n=int(input())
road=[[] for i in range(n)]
check=[False]*n
bef=[-1]*n
for i in range(n-1):
    a,b=map(int,input().split())
    a-=1
    b-=1
    road[a].append(b)
    road[b].append(a)
for i in range(n):
    road[i].sort()
for i in range(n):
    road[i]=deque(road[i])
ans=[0]
check[0]=True
while True:
    now=ans[-1]
    f=False
    while True:
        if len(road[now])==0:
            if now==0:
                f=True
                break
            else:
                ans.append(bef[now])
                break
        nex=road[now].popleft()
        if check[nex]:
            pass
        else:
            ans.append(nex)
            check[nex]=True
            bef[nex]=now
            break
    if f:break

print(" ".join(map(lambda x:str(x+1),ans)))