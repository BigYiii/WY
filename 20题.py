n=eval(input("请输入一个大于等于1的数："))
list=[]
for i in range(1,n+1):
    if i%15 == 0:
        list.append("FizzBuzz")
    elif i%5 == 0:
        list.append("Buzz")
    elif i%3 == 0:
        list.append("Fizz")
    else:
        list.append(str(i))
m=",".join(list)
print(m)