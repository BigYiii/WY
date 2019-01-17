def f(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return (x * f(x-1))
print(f(5))