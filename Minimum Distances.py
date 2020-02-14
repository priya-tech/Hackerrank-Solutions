n=int(input())
a=[int(x) for x in input().split()]
l=[]
for i in range(0,n):
    for j in range(i+1,n):
        if a[i]==a[j]:
            l.append(abs(i-j))
if l:
    pass
else:
    l.append(-1)
                
print(min(l))            

