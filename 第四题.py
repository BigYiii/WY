import datetime
y=eval(input("请输入年份："))
m=eval(input("请输入月份："))
d=eval(input("请输入天数: "))
x=datetime.date(y, m, d) - datetime.date(y-1, 12, 31)
print(x)