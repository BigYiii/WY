#编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,
#             当输入n为奇数时，调用函数1/1+1/3+...+1/n
def f(n):
    if n<=0:
        return 0
    else:
        return (1/n)+f(n-2)
n=eval(input("请输入一个数："))
f=f(n)
print(f)
