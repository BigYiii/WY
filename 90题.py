#求一个字符串的所有排列
import itertools
str=input("请输入一个字符串")
l=list(str)
n=list(itertools.permutations(l,len(str)))
print(n)
