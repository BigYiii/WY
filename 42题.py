n=[[1,3,5],[8,2,0],[9,2,1]]
sum=0
for i in range(0,3):
    
    a=n[i]
    for j in range(0,3):
        b=a[j]
        if i==j:
            sum += b
print(sum)

