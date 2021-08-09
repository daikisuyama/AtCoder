h,w,n=map(int,input().split())
c,r=set(),set()
card=[]
for i in range(n):
    a,b=map(int,input().split())
    card.append([a,b])
    c.add(a)
    r.add(b)
c,r=sorted(list(c)),sorted(list(r))
checkc,checkr=dict(),dict()
for i in range(len(c)):
    checkc[c[i]]=i+1
for i in range(len(r)):
    checkr[r[i]]=i+1
ans=[]
for i,j in card:
    ans.append([checkc[i],checkr[j]])
for i,j in ans:
    print(i,j)