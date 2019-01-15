import math
for b in range(13,100):
    a = int(math.sqrt(b*b-168))
    if a*a==b*b - 168:
        n=b*b-268
        print(n)


