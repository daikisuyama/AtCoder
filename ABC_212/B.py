x=[int(i) for i in input()]
if len(set(x))==1:
    print("Weak")
else:
    for i in range(3):
        if (x[i+1]-x[i]+10)%10!=1:
            print("Strong")
            break
    else:
        print("Weak")
