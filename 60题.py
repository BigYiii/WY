#给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转
n="-123"
a=n[1:len(n)+1]
list1=list(a)
list1.reverse()
c="".join(list1)
print(n[0]+c)