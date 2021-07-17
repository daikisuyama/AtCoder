n=int(input())
s=input()
t=input()
if s.count("1")!=t.count("1"):
    print(-1)
    exit()
k=0
sx,tx=[],[]
for i in range(n):
    if s[i]=="0":
        sx.append(i)
        k+=1
    if t[i]=="0":
        tx.append(i)
ans=0
for i in range(k):
    if sx[i]!=tx[i]:
        ans+=1
print(ans)