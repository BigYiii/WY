a=[1,2,3,4,5,6]
n=[]
x=eval(input("请输入向右移动的位数："))
b=len(a)
for i in range(-x,b-x,1):
    n.append(a[i])
print(n)



