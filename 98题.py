#利用内置函数chr(),ord()以及random模块写一个简单随机4位验证码
import random
list = []

num1 = random.randint(65,90)  #大写字母
str1 = chr(num1)
list.append(str1)

num2 = random.randint(97,122)  # 小写字母
str2 = chr(num2)
list.append(str2)

for i in range(2):
    num3 = random.randint(0,9)
    list.append(str(num3))
n="".join(list)
print(n)