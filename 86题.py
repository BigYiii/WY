#有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列),
# 输出到一个新文件C中。
f1 = open('A.txt','rt')
a = f1.read()
f1.close()

f2 = open('B.txt','rt')
b = f2.read()
f2.close()

f3 = open('C', 'w')
list = list(a + b)
list.sort()
s = "".join(list)
f3.write(s)
f3.close()