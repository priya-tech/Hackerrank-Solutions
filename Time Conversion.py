s=input()
h=s[0:2]
m=s[3:5]
se=s[6:8]
f=s[8:]
if f=="PM":
    if int(h)==12:
        print(h+":"+m+":"+se)
    else:
        g=str((int(h)+12))
        print(g+":"+m+":"+se)
else:
    if int(h)==12:
        print("00"+":"+m+":"+se)
    else:
        print(h+":"+m+":"+se)

