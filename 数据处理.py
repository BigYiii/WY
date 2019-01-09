'''f = open("D:\\数据\\data.寒假.txt",'r')
ff = open("D:\\数据\\data3.txt",'w')
count = 0
for i in range(1080000):
    var = f.readline()
    if len(var) <= 30:
        c = var.replace(var," ")
        x = x + 1

    else:

        ff.write(var)

print(x)
f.close()
ff.close()'''
def Print(var1,var2):
    return var1 + var2

a = "Hello"
b = "World"
print(Print(a,b))



