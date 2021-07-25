# 嘘解法です、参考にしないでください

from math import gcd
from collections import deque
def lcm(a,b):
    return a*b//gcd(a,b)
n=int(input())
x,y=map(int,input().split())
now=deque([[x,y]])
for i in range(n-1):
    a,b=map(int,input().split())
    for i in range(len(now)):
        x,y=now.popleft()
        l1=lcm(gcd(x,a),gcd(y,b))
        l2=lcm(gcd(x,b),gcd(y,a))
        if l1>l2:
            x=gcd(x,a)
            y=gcd(y,b)
            now.append([x,y])
        elif l2>l1:
            x=gcd(x,b)
            y=gcd(y,a)
            now.append([x,y])
        else:
            x=gcd(x,b)
            y=gcd(y,a)
            now.append([x,y])
            x=gcd(x,a)
            y=gcd(y,b)
            now.append([x,y])
print(max([lcm(i[0],i[1]) for i in now]))
