def f(x):
    if x == -1:
        return ''
    else:
        return string[x] + f(x-1)
string=input("请输入5个字符：")
print (f(4))