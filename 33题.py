def f(n):
    if n==1:
        return 10
    else:
        return 2+f(n-1)
n=5
print(f(n))