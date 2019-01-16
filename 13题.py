def f(n):
    if n == 1 or n == 2:

        return 1
    else:
        return f(n-1)+f(n-2)
n=eval(input('请输入月数：'))
print("该月的兔子总数为:",2*f(n))