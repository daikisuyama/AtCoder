x,y=map(int,input().split())
s=set([0,1,2])
s.remove(x)
if y in s:
    s.remove(y)
    print(s.pop())
else:
    print(x)