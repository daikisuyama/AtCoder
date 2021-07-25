from math import gcd
def lcm(x,y):
    return x*y//gcd(x,y)
def make_divisors(n):
    divisors=[]
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            divisors.append(i)
            if i!=n//i:
                divisors.append(n//i)
    #約数の小さい順にソートしたい場合
    #divisors.sort()
    #約数の大きい順にソートしたい場合
    #divisors.sort(reverse=True)
    return divisors

n=int(input())
ab=[list(map(int,input().split())) for i in range(n)]
ans=0
for i in make_divisors(ab[0][0]):
    for j in make_divisors(ab[0][1]):
        for k in range(1,n):
            if (ab[k][0]%i==0 and ab[k][1]%j==0)or(ab[k][0]%j==0 and ab[k][1]%i==0):
                pass
            else:
                break
        else:
            ans=max(ans,lcm(i,j))
print(ans)
