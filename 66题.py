#编写input()和output()函数输入，输出5个学生的数据记录
list=[]
for i in range(5):
    x=input("请输入学生的数据记录：")
    list.append(x)
for j in list:
    print("输出数据记录：",j)