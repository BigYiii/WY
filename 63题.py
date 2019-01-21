#有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数
b_list=[]
n=8
a="11 44 23 56 74 3 8 9"
m=3
a_list=a.split(" ")
for i in range(-m,n-m,1):
    b=a_list[i]
    b_list.append(b)
print(b_list)

