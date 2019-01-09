f = open("D:\\数据\\data.寒假.txt",'r')
ff = open("D:\\数据\\data1.txt",'w')
fff = open("D:\\数据\\data2.txt",'w')
ffff = open("D:\\数据\\data3.txt",'w')
fffff = open("D:\\数据\\data4.txt",'w')

a = f.readlines()
b = a[0:200001]
ff.write(b)
