from itertools import accumulate
from collections import Counter
n=int(input())
a_=list(map(int,input().split()))
a=[a_[i] if i%2 else -a_[i] for i in range(n)]
b=list(accumulate(a))
c=Counter(b)
#print(c)
ans=0
for i in c:
    ans+=(c[i]*(c[i]-1)//2)
    if i==0:ans+=c[i]
print(ans)