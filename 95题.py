#给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，
# 找出 0 .. n 中没有出现在序列中的那个数

x=[1,4,0,5,7,8,3,6]
for i in range(0,9):
    if i not in x:
        print(i)


