x=eval(input("请输入一个十进制的数:"))
y='{:032b}'.format(x)
z=list(y)
z.reverse()
m="".join(z)
n=int(m,2)     #二进制转十进制
print(n)
