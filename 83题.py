#从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个 # 为止
fb = open('83.txt','w') #读取文件
n = input('输入字符串：\n')
while n!='#':

	fb.write(n)
	print(n)
	n = input('')
fb.close()
