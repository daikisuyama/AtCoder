h,w,c=map(int,input().split())
a=[list(map(int,input().split())) for i in range(h)]
x1,x2,x3,x4=[[[0]*w for j in range(h)] for i in range(4)]
# 左上
for i in range(h):
    for j in range(w):
        if i==0 and j==0:
            x1[i][j]=a[i][j]-(i+j)*c
        elif i==0:
            x1[i][j]=min(x1[i][j-1],a[i][j]-(i+j)*c)
        elif j==0:
            x1[i][j]=min(x1[i-1][j],a[i][j]-(i+j)*c)
        else:
            x1[i][j]=min(x1[i-1][j],x1[i][j-1],a[i][j]-(i+j)*c)
# 右上
for i in range(h):
    for j in range(w-1,-1,-1):
        if i==0 and j==w-1:
            x2[i][j]=a[i][j]-(i+w-1-j)*c
        elif i==0:
            x2[i][j]=min(x2[i][j+1],a[i][j]-(i+w-1-j)*c)
        elif j==w-1:
            x2[i][j]=min(x2[i-1][j],a[i][j]-(i+w-1-j)*c)
        else:
            x2[i][j]=min(x2[i-1][j],x2[i][j+1],a[i][j]-(i+w-1-j)*c)
# 左下
for i in range(h-1,-1,-1):
    for j in range(w):
        if i==h-1 and j==0:
            x3[i][j]=a[i][j]-(h-1-i+j)*c
        elif i==h-1:
            x3[i][j]=min(x3[i][j-1],a[i][j]-(h-1-i+j)*c)
        elif j==0:
            x3[i][j]=min(x3[i+1][j],a[i][j]-(h-1-i+j)*c)
        else:
            x3[i][j]=min(x3[i+1][j],x3[i][j-1],a[i][j]-(h-1-i+j)*c)
# 右下
for i in range(h-1,-1,-1):
    for j in range(w-1,-1,-1):
        if i==h-1 and j==w-1:
            x4[i][j]=a[i][j]-(h-1-i+w-1-j)*c
        elif i==h-1:
            x4[i][j]=min(x4[i][j+1],a[i][j]-(h-1-i+w-1-j)*c)
        elif j==w-1:
            x4[i][j]=min(x4[i+1][j],a[i][j]-(h-1-i+w-1-j)*c)
        else:
            x4[i][j]=min(x4[i+1][j],x4[i][j+1],a[i][j]-(h-1-i+w-1-j)*c)
ans=10**100
for i in range(h):
    for j in range(w):
        ans_sub=[]
        if i!=0:
            ans_sub.append(x1[i-1][j]+(i+j)*c)
        if j!=w-1:
            ans_sub.append(x2[i][j+1]+(i+w-1-j)*c)
        if j!=0:
            ans_sub.append(x3[i][j-1]+(h-1-i+j)*c)
        if i!=h-1:
            ans_sub.append(x4[i+1][j]+(h-1-i+w-1-j)*c)
        ans=min(ans,min(ans_sub)+a[i][j])
print(ans)
