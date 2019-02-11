#两个字符串的最长公共子串，这个子串要求在原字符串中是连续的
str1="gffredop"
str2="sred"
lstr1 = len(str1)
lstr2 = len(str2)
record = [[0 for i in range(lstr2+1)] for j in range(lstr1+1)]
maxNum = 0
p = 0
for i in range(lstr1):
    for j in range(lstr2):
        if str1[i] == str2[j]:
          print(record[i+1][j+1],record[i][j] + 1)
          record[i+1][j+1] = record[i][j] + 1
          if record[i+1][j+1] > maxNum:
              maxNum = record[i+1][j+1]
              p = i + 1
print(str1[p-maxNum:p], maxNum)

