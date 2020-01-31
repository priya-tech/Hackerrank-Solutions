ls=[int(x) for x in input().split()]
k=0
res=[]
while (k<5):
    s=0
    for i in range(0,5):
        if k==i:
            pass
        else:
            s += ls[i]
    res.append(s)
    k+=1
print(min(res),max(res))


