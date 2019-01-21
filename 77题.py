#求0—7所能组成的奇数个数
m=0
for i in range(1,9):
    if i == 1:
        n1=4
    elif i>1:
        n=28*pow(8,i-2)
        m+=n
print(m+n1)


