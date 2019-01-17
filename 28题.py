import math
a = 2
b = 1

l = [2]
for i in range(19):
    a = a + b
    b = a - b
    c = a / b
    l.append(c)
print(sum(l))