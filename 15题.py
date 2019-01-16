for i in range(100,1000):
    a=i//100
    b=(i-a*100)//10
    c=i-100*a-10*b
    if i==a**3+b**3+c**3:
        print(i,end=" ")