import math
a1,a2,a3=map(int,input().split())
x=2*a2-a1-a3
if x>=0:
    print(x)
else:
    a=math.ceil(-x/2)
    print(x+3*a)