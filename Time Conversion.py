s=input()
period=s[-2:]
if period=="AM":
    if int(s[0:2])==12:
        print("00"+s[2:-2])
    else:
        print(s[0:-2])
else:
    h=s[0:2]
    if int(h)==12:
        print(s[0:-2])
    else:
        h=str((int(h)+12))
        print(h+s[2:-2])            

