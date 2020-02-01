n,k=input().split()
k=int(k)
h=[int(x) for x in input().split()]
m=max(h)
if k>m:
    print(0)
else:
    print(abs(k-m))    

