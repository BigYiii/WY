longstr = "Hello World"
shortstr="World"
a=len(shortstr)
b=len(longstr)

for i in range(0,b):
    if longstr[i:i+a]==shortstr:
        break
print("[%d,%d]"%(i,(i+a-1)))

















'''longstr = "Hello World"
shortstr = " "
longvar = len(longstr)
shortvar = len(shortstr)
a = 0
b = shortvar
if b==0:
    print("Error")
    exit()
while b <= len(longstr):
    if longstr[a:b] != shortstr:
        a = a + 1
        b = b + 1
    else:
        print("begin:", a, "\nend:", b-1)
        break'''
