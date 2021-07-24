s=input()
l=len(s)
check=[[0]*8 for i in range(l)]
alp="chokudai"
mod=10**9+7
# 初期化（文字列の最初の文字）
if s[0]=="c":
    check[0][0]=1
for i in range(l-1):
    #選ぶ場合と選ばない場合
    for j in range(8):
        # 選ばない場合
        check[i+1][j]+=check[i][j]
        #選ぶ場合
        if s[i+1]==alp[j]:
            if j==0:
                check[i+1][j]+=1
            else:
                check[i+1][j]+=check[i][j-1]
        check[i+1][j]%=mod
print(check[l-1][7])