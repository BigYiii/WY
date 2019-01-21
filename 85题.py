#给定一个非空整数数组，除了某个元素只出现一次以外，
# 其余每个元素均出现两次。找出那个只出现了一次的元素
list=[2,34,4,56,4,2,34]
for i in range(0,len(list)):
    if list.count(list[i])==1:
        print(list[i])