#给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。
# 如果不存在，则返回 -1。
def f(x):
    for i in range(0,len(x)):
        if x[i] not in x[i + 1:] and x[i] not in x[:i]:
            return i
    return -1


x=input("给定一个字符串：")
print(f(x))

