list1 = []
n = int(input("请输入一个数:"))
for i in range(2,n):
    while True:
        if n%i==0:
            list1.append(str(i))
            n = n/i
        else:
            break
str="*".join(list1)
print("90=",str)

