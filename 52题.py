a=123456789
n=str(a)
x=n[-4:-7:-1]
y=list(x)
y.reverse()
z=''.join(y)
print(z)