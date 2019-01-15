n=eval(input("楼梯阶数="))
a=1
b=2
c=3
if n==1:
    f=1
elif n==2:
    f=2
elif n==3:
    f=3
else:
    for i in range(n-3):
        a=b
        b=c
        c=a+b
        f=c
print(f)
