#対角線をチェック
#[i,j]のi+jが等しい
#i+j=0~(h+w-2)
mod=998244353
h,w=map(int,input().split())
s=[input() for i in range(h)]
ans=1
for i_j in range(h+w-1):
    now=""
    for i in range(h):
        j=i_j-i
        if 0<=j<w:
            if s[i][j]==".":
                pass
            elif now=="":
                now=s[i][j]
            else:
                if now==s[i][j]:
                    pass
                else:
                    print(0)
                    exit()
    if now=="":
        ans*=2
        ans%=mod
    else:
        pass
print(ans)