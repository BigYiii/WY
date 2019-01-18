'''[1,2,3]    [2,3,4]
  [4,5,6]    [5,6,7]
 [7,8,9]    [8,9,0]'''
x=[]
a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[2,3,4],[5,6,7],[8,9,0]]
for i in range(3):
    m=list(a[i])
    n=list(b[i])
    print(m,n)
    for j in range(3):
        c=m[j]+n[j]
        x.append(c)

list1=x[0:3]
list2=x[3:6]
list3=x[6:9]
print(list1)
print(list2)
print(list3)


