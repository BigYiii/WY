w = []
x = int(input("请你输入要比较数字总共的数量："))
for i in range(x):
    a = int(input("请输入你要比较的数字:"))
    w.append(a)
print("输入结束等待结果")
for i in range(x):
    c = max(w)
    w.remove(c)
    print(c)