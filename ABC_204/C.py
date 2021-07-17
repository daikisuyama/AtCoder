from collections import deque
n,m=map(int,input().split())
road=[[] for i in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    road[a-1].append(b-1)
ans=0
for i in range(n):
    check=[0 for j in range(n)]
    now=deque([i])
    check[i]=1
    while len(now):
        ne=now.popleft()
        for j in road[ne]:
            if check[j]==0:
                now.append(j)
                check[j]=1
    ans+=sum(check)
print(ans)
