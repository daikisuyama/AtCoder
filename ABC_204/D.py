n=int(input())
t=list(map(int,input().split()))
mag=100001
dp=[[0]*mag for i in range(n)]
dp[0][t[0]]=1
for i in range(1,n):
    for j in range(mag):
        if dp[i-1][j]:
            dp[i][j+t[i]]=1
            dp[i][abs(j-t[i])]=1
for i in range(mag):
    if dp[n-1][i]:
        print((sum(t)-i)//2+i)
        break