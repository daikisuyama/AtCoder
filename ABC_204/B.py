n=int(input())
a=list(map(int,input().split()))
print(sum(0 if i<=10 else i-10 for i in a))