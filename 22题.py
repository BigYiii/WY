a=eval(input("请输入a的值:"))
n=eval(input("请输入相加次数:"))
s=a
m=a
while n>1:
    m=m*10+a
    s=s+m
    n=n-1
print(s)
