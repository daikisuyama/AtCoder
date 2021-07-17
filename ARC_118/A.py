t,n=map(int,input().split())
check_y=set()
for y in range(100):
    check_y.add((100+t)*y//100)
check_real=[]
for y in range(100+t):
    if y not in check_y:
        check_real.append(y)
len_real=len(check_real)
if n%len_real==0:
    ans=(n//len_real-1)*(100+t)+check_real[-1]
else:
    ans=(n//len_real)*(100+t)+check_real[n%len_real-1]
print(ans)