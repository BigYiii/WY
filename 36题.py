n=input("请输入星期英文的第一个字母（大写）：")
if n == 'S':
    print('请输入第二个字母（小写）:')
    n = input("n=")

    if n == 'a':
        print('Saturday')
    elif n == 'u':
        print('Sunday')
    else:
        print('data error')

elif n == 'F':
    print('Friday')

elif n == 'M':
    print('Monday')

elif n == 'T':
    print('请输入第二个字母（小写）')
    n = input("n=")

    if n == 'u':
        print('Tuesday')
    elif n == 'h':
        print('Thursday')
    else:
        print('data error')

elif n == 'W':
    print('Wednesday')
else:
    print('data error')