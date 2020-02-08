x1,v1,x2,v2=input().split()
x1=int(x1)
v1=int(v1)
x2=int(x2)
v2=int(v2)
f=0
for n in range(10000):
    if x1==x2:
        print("YES")
        f=1
        break
    x1+=v1
    x2+=v2
if f==0:
    print("NO")

