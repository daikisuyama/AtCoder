n=int(input())
if n==3:
    print(6,10,15)
    exit()
a=[]
for i in range(1,10001):
    if i%2==0 and i%3==0:
        a.append(i)
    elif i%2==0 and i%5==0:
        a.append(i)
    elif i%3==0 and i%5==0:
        a.append(i)
    else:
        continue
print(" ".join(map(str,a[:n])))