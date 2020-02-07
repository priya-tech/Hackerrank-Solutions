n=int(input())
ar=[int(x) for x in input().split()]
s=set(ar)
count=0
for i in s:
    if ar.count(i)>count:
        count=ar.count(i)
        ans=i
print(ans)        

