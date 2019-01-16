n=eval(input("请输入一个整数:"))
if n == 0 :
    print("no")
elif n == 1:
    print("yes")
else:
    while n % 3 == 0:
        n =n//3
if n == 1:
    print("yes")
else:
    print("no")


