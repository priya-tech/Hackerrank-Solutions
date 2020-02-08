n,k=input().split()
ar=[int(x) for x in input().split()]
b=int(input())
n=int(n)
k=int(k)
s=0
for i in range(0,n):
    if i!=k:
        s += ar[i]
amount=s/2        
if b-amount==0:
    print("Bon Appetit")
else:
    print(int(b-amount))   
