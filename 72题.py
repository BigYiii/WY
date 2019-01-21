#字符串排序
str="54,78,32,45,66"
list1=str.split(',')
list1.sort()
str2=",".join(list1)
print(str2)