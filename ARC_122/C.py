a,b=1,1
for i in range(130):
    if a>b:
        b=a+b
    else:
        a=a+b
    if a>10**18 or b>10**18:
        print(i)
        break
print(a,b)