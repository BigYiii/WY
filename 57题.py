#打印出杨辉三角形
N = [1]

for i in range(10):
    print(N)
    N.append(0)
    N = [N[k] + N[k-1]for k in range(i + 2)]
    #n=[n[0]+n[-1],n[1]+n[0],…………,n[i+1]+n[i] ]