#给定两个数组，编写一个函数来计算它们的交集
def f(m,n):
    a=set(m)
    b=set(n)
    x=a&b
    return list(x)
m=[1,2,3,4]
n=[5,6,2,4,6]
print(f(m,n))