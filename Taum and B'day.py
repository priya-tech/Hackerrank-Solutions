t=int(input())
for i in range(t):
    ans=0
    b,w=input().split()
    b=int(b)
    w=int(w)
    bc,wc,z=input().split()
    bc=int(bc)
    wc=int(wc)
    z=int(z)
    if bc>wc+z:
        ans=(b+w)*wc+b*z
    elif wc>bc+z:
        ans=b*bc+w*(bc+z)
    else:
        ans=b*bc+w*wc    
    print(ans)            

