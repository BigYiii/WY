'''有一组数从大到小排列
a=[30，24，19，9，3]
插入数字：15
效果：a=[30，24，19,15，9，3]'''
a=[30,24,19,9,3]
x=15
b=len(a)
for i in range(0,b+1):
    if x>a[i]:
        a.insert(i,x)
        break
print(a)




