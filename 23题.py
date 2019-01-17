for i in range(1, 1000):
    sum = 0
    for n in range(1, i):
        if i % n == 0:
            sum = sum + n
    if i == sum:
        print(i)