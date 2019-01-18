a=["47","46","22","65","37"]
x=len(a)
b=max(a)
c=min(a)
m=a.index(b)
n=a.index(c)
a[m]=a[0]
a[0]=b
a[n]=a[x-1]
a[x-1]=c

print(a)





