def f(n):
    x='{:08b}'.format(n)
    list1=list(x)
    y=list1.count("1")
    return y
n=eval(input("请输入一个无符号整数："))
y=f(n)
print(y)
