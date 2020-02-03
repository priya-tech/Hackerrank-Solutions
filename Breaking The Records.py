n=int(input())
s=[int(x) for x in input().split()]
l=s[0]
sm=s[0]
lcount=0
scount=0
for i in range(1,n):
    if s[i]>l:
        lcount=lcount+1
        l=s[i]
    elif s[i]<sm:
        scount=scount+1
        sm=s[i]
    else:
        pass
print(lcount,scount)            
